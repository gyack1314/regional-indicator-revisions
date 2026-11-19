import json
from pathlib import Path
import unittest

FIXTURE = Path(__file__).parents[1] / 'fixtures' / 'scenario.json'

class FixtureContractTests(unittest.TestCase):
    def test_synthetic_records_match_declared_fields(self):
        payload = json.loads(FIXTURE.read_text(encoding='utf-8'))
        self.assertIs(payload['synthetic'], True)
        self.assertGreaterEqual(len(payload['records']), 4)
        self.assertEqual(len(payload['fields']), len(set(payload['fields'])))
        for record in payload['records']:
            self.assertEqual(set(record), set(payload['fields']))
            self.assertTrue(all(isinstance(value, str) for value in record.values()))

if __name__ == '__main__':
    unittest.main()
