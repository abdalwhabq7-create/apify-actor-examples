"""Run one catalog Actor using only Python's standard library."""
import argparse
import json
import math
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def request(path, token, body=None, **params):
    url = 'https://api.apify.com/v2/' + path
    if params:
        url += '?' + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, data=None if body is None else json.dumps(body).encode(),
                                 headers={'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=75) as response:
            data = json.load(response)
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f'Apify HTTP {exc.code}. Check your token, input and Actor listing; inspect Console before retrying.') from None
    return data.get('data', data) if isinstance(data, dict) else data

def run(name, inp, token, max_charge):
    if not token:
        raise ValueError('Set APIFY_TOKEN to your own Apify token.')
    if not math.isfinite(max_charge) or max_charge <= 0:
        raise ValueError('max-charge must be a finite positive number.')
    names={a['name'] for a in json.loads((ROOT/'catalog.json').read_text(encoding='utf-8'))}
    if name not in names or not isinstance(inp, dict):
        raise ValueError('Choose a catalog Actor and a JSON object as input.')
    # Never retry this POST: a lost response could still have started a billed run.
    try:
        result=request('acts/abdulwhab95~'+name+'/runs',token,inp,
                       timeout=180,maxTotalChargeUsd=max_charge,waitForFinish=60)
        run_id=result['id']
    except (OSError,ValueError,KeyError) as exc:
        raise RuntimeError('Start response unavailable. A paid run may already be active. '
                           'Check Apify Console before running again.') from None
    print('Run:',run_id,flush=True)
    deadline=time.monotonic()+300
    while result['status'] in ('READY','RUNNING','TIMING-OUT','ABORTING'):
        if time.monotonic()>=deadline:
            raise RuntimeError(f'Client wait ended. Check run {run_id} in Apify Console; it was not aborted.')
        result=request('actor-runs/'+run_id,token,waitForFinish=60)
        if result['status']=='READY':time.sleep(1)
    if result['status']!='SUCCEEDED':
        raise RuntimeError(f"Run {run_id} ended with {result['status']}; inspect its log in Apify Console.")
    rows=request('datasets/'+result['defaultDatasetId']+'/items',token,limit=1000,clean='true')
    return result,rows

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('actor')
    parser.add_argument('--input',type=Path)
    parser.add_argument('--max-charge',type=float,default=0.10)
    args=parser.parse_args()
    names={a['name'] for a in json.loads((ROOT/'catalog.json').read_text(encoding='utf-8'))}
    if args.actor not in names:parser.error('Actor not in catalog; see README.md.')
    path=args.input or ROOT/'actors'/args.actor/'input.json'
    inp=json.loads(path.read_text(encoding='utf-8-sig'))
    result,rows=run(args.actor,inp,os.environ.get('APIFY_TOKEN',''),args.max_charge)
    folder=ROOT/'results';folder.mkdir(exist_ok=True)
    output=folder/(args.actor+'-'+result['id']+'.json')
    output.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'Saved {len(rows)} rows (up to 1,000; export larger datasets in Console) to {output}')

if __name__=='__main__':
    try:main()
    except (ValueError,OSError,RuntimeError,KeyError) as exc:
        print(str(exc),file=sys.stderr)
        sys.exit(1)
