import json
import unittest
from unittest.mock import patch
import run

class RunnerTests(unittest.TestCase):
    def test_successful_run_polls_and_downloads_without_restarting(self):
        responses=[{'id':'test','status':'RUNNING'}, {'id':'test','status':'SUCCEEDED','defaultDatasetId':'data'}, [{'price':12}]]
        with patch.object(run,'request',side_effect=responses) as api:
            result,rows=run.run('salla-catalog-scraper',{},'test-token',.10)
        self.assertEqual(rows,[{'price':12}])
        self.assertEqual(api.call_count,3)
        self.assertEqual(api.call_args_list[0].kwargs['maxTotalChargeUsd'],.10)
        self.assertEqual(api.call_args_list[0].kwargs['timeout'],180)
        self.assertEqual(api.call_args_list[1].args[0],'actor-runs/test')

    def test_failed_run_never_downloads_results(self):
        with patch.object(run,'request',return_value={'id':'test','status':'FAILED'}) as api:
            with self.assertRaisesRegex(RuntimeError,'FAILED'):
                run.run('salla-catalog-scraper',{},'test-token',.10)
        self.assertEqual(api.call_count,1)

    def test_uncertain_submission_is_not_retried(self):
        with patch.object(run,'request',side_effect=OSError('connection lost')) as api:
            with self.assertRaisesRegex(RuntimeError,'paid run may already be active'):
                run.run('salla-catalog-scraper',{},'test-token',.10)
        self.assertEqual(api.call_count,1)

    def test_bad_credentials_or_spend_limit_fail_before_network(self):
        with patch.object(run,'request') as api:
            for budget in (0,-1,float('nan'),float('inf')):
                with self.assertRaises(ValueError):run.run('salla-catalog-scraper',{},'test-token',budget)
            with self.assertRaises(ValueError):run.run('salla-catalog-scraper',{},'',.1)
            with self.assertRaises(ValueError):run.run('../private',{},'test-token',.1)
        api.assert_not_called()

if __name__=='__main__':unittest.main()
