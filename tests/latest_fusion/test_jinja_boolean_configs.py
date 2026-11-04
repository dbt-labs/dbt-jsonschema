import json
import unittest
from pathlib import Path

from jsonschema import Draft7Validator

SCHEMA_PATH = (
    Path(__file__).resolve().parents[2]
    / "schemas/latest_fusion/dbt_project-latest-fusion.json"
)

BOOLEAN_CONFIGS = {
    "+enabled", "+bind", "+copy_grants", "+full_refresh",
    "+quote_columns", "+secure", "+store_failures", "+transient",
}


class TestJinjaBooleanConfigs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads(SCHEMA_PATH.read_text())
        Draft7Validator.check_schema(cls.schema)

    def test_boolean_configs_accept_jinja(self):
        checked = 0

        for definition_name, definition in self.schema["definitions"].items():
            if not isinstance(definition, dict):
                continue

            for property_name, property_schema in definition.get(
                "properties", {}
            ).items():
                if property_name not in BOOLEAN_CONFIGS:
                    continue

                if not isinstance(property_schema, dict):
                    continue

                if "anyOf" not in property_schema:
                    continue

                validator = Draft7Validator({
                    "$schema": self.schema["$schema"],
                    "definitions": self.schema["definitions"],
                    **property_schema,
                })

                with self.subTest(
                    definition=definition_name,
                    property=property_name,
                ):
                    for value in (
                        True,
                        False,
                        None,
                        "{{ target.name != 'prod' }}",
                    ):
                        self.assertTrue(validator.is_valid(value), value)

                    for value in ("invalid", "true", 123):
                        self.assertFalse(validator.is_valid(value), value)

                checked += 1

        self.assertEqual(checked, 42)


if __name__ == "__main__":
    unittest.main()
