import json
from pathlib import Path
from typing import Any, Dict

from src.latest.dbt_cloud import DbtCloud
from src.latest.dbt_yml_files import DbtYmlFiles
from src.latest.dependencies import Dependencies, Packages
from src.latest.selectors import Selectors
from pydantic.json_schema import GenerateJsonSchema


class RemoveNullsGenerateJsonSchema(GenerateJsonSchema):
    """A GenerateJsonSchema which removes nullability from types.

    We do not want to include optional values in the json schema because
    that would inhibit code completion and validation.

    Certain properties (such as freshness overrides) need to be nullable,
    which can be achieved by setting the $comment value below.
    """

    def _remove_null(self, json_schema: Dict[str, Any]):
        if "$comment" in json_schema and json_schema["$comment"] == "truly_nullable":
            return
        if "anyOf" in json_schema:
            json_schema["anyOf"] = [
                item for item in json_schema["anyOf"] if item != {"type": "null"}
            ]
        for v in json_schema.values():
            if isinstance(v, dict):
                self._remove_null(v)

    def generate(self, schema, mode="validation"):
        json_schema = super().generate(schema, mode=mode)
        json_schema["schema"] = "http://json-schema.org/draft-07/schema#"
        self._remove_null(json_schema)
        return json_schema


if __name__ == "__main__":
    files = {
        "dbt_yml_files": DbtYmlFiles,
        "dependencies": Dependencies,
        "packages": Packages,
        "selectors": Selectors,
        "dbt_cloud": DbtCloud,
    }
    output_directory = Path("schemas/latest")
    for file_name, model in files.items():
        schema_file = output_directory / f"{file_name}-latest.json"
        schema_file.parent.mkdir(parents=True, exist_ok=True)
        schema = model.model_json_schema(
            mode="validation", schema_generator=RemoveNullsGenerateJsonSchema
        )
        print("Generating", schema_file)
        schema_file.write_text(json.dumps(schema, indent=2))
