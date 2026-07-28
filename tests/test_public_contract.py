import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PublicContractTests(unittest.TestCase):
    def load(self, relative_path):
        with (ROOT / relative_path).open(encoding="utf-8") as handle:
            return json.load(handle)

    def test_latest_changes_required_fields_remain_available(self):
        payload = self.load("data/latest_changes.json")
        required = {
            "build_hash",
            "extractor_version",
            "new_experiments",
            "deleted_experiments",
            "modified_experiments",
            "new_api_endpoints",
            "deleted_api_endpoints",
            "modified_api_endpoints",
            "string_changes",
            "timestamp",
        }

        self.assertTrue(required.issubset(payload))
        self.assertEqual(set(payload["string_changes"]), {"en", "ko"})

    def test_web_contract_types_remain_stable(self):
        meta = self.load("data/web/meta.json")
        self.assertIsInstance(meta["schema_version"], int)
        self.assertIsInstance(meta["counts"], dict)
        for filename in (
            "experiments.json",
            "experiment-details.json",
            "apis.json",
            "strings.en.json",
            "strings.ko.json",
        ):
            self.assertIsInstance(self.load(f"data/web/{filename}"), list)


if __name__ == "__main__":
    unittest.main()
