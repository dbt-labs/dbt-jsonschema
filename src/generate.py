import json
import os

from latest.dbt_cloud import DbtCloud
from latest.dbt_project import DbtProject
from latest.dbt_yml_files import DbtYmlFiles
from latest.dependencies import Dependencies, Packages
from latest.selectors import Selectors

if __name__ == "__main__":
    files = {
        "dbt_yml_files": DbtYmlFiles, 
        "dependencies": Dependencies, 
        "packages": Packages,
        "selectors": Selectors,
        "dbt_project": DbtProject,
        "dbt_cloud": DbtCloud,

    }
    output_directory = os.path.join(
        os.path.dirname(__file__), "../", f"schemas/latest-generated"
    )
    for file_name, model in files.items():
        file_path = os.path.join(
            output_directory, f"{file_name}-latest-generated.json"
        )
        schema = model.model_json_schema(mode="validation")
        with open(file_path, "w") as file:
            json.dump(schema, file, indent=2)
