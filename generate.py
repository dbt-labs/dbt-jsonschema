import json
from pathlib import Path

from src.latest.dbt_cloud import DbtCloud
from src.latest.dbt_project import DbtProject
from src.latest.dbt_yml_files import DbtYmlFiles
from src.latest.dependencies import Dependencies, Packages
from src.latest.selectors import Selectors

if __name__ == "__main__":
    files = {
        "dbt_yml_files": DbtYmlFiles, 
        "dependencies": Dependencies, 
        "packages": Packages,
        "selectors": Selectors,
        "dbt_project": DbtProject,
        "dbt_cloud": DbtCloud,

    }
    output_directory = Path("schemas/latest")
    for file_name, model in files.items():
        schema_file = output_directory /  f"{file_name}-latest.json"
        schema_file.parent.mkdir(parents=True, exist_ok=True)
        schema = model.model_json_schema(mode="validation")
        schema_file.write_text(json.dumps(schema, indent=2))
