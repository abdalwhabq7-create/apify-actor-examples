import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CatalogTests(unittest.TestCase):
    def test_thirty_distinct_public_tools_have_readme_and_valid_object_input(self):
        rows = json.loads((ROOT / 'catalog.json').read_text(encoding='utf-8'))
        self.assertEqual(len(rows), 30)
        self.assertEqual(len({r['name'] for r in rows}), 30)
        for row in rows:
            folder = ROOT / 'actors' / row['name']
            self.assertTrue((folder / 'README.md').is_file(), row['name'])
            self.assertIsInstance(json.loads((folder / 'input.json').read_text(encoding='utf-8')), dict)
            self.assertEqual(row['url'], 'https://apify.com/abdulwhab95/' + row['name'])

    def test_five_new_examples_have_synthetic_samples(self):
        names = ['sitemap-snapshot-change-feed', 'http-security-header-presence-audit', 'openapi-structural-change-checker', 'csv-json-deduplicate-normalize', 'static-html-tables-to-json']
        for name in names:
            folder = ROOT / 'actors' / name
            self.assertIn('payload', json.loads((folder / 'input.json').read_text(encoding='utf-8')))
            self.assertIsInstance(json.loads((folder / 'sample-output.json').read_text(encoding='utf-8')), list)
            self.assertIn('synthetic', (folder / 'README.md').read_text(encoding='utf-8'))


if __name__ == '__main__': unittest.main()
