import json
import os

from latest.dbt_yml_files import DbtYmlFiles

if __name__ == "__main__":
    versions = ["latest"]
    files = {"dbt_yml_files": DbtYmlFiles}
    for v in versions:
        output_directory = os.path.join(
            os.path.dirname(__file__), "../", f"schemas/{v}-generated"
        )
        for file_name, model in files.items():
            file_path = os.path.join(
                output_directory, f"{file_name}-{v}-generated.json"
            )
            schema = model.model_json_schema(mode="validation")
            with open(file_path, "w") as file:
                json.dump(schema, file, indent=2)
