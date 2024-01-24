import json 
from jsondiff import diff

PROJECT_SCHEMA_FILES = [
    "./schemas/dbt_project.json",
    "./schemas/1.5/dbt_project-1.5.json",
    "./schemas/1.6/dbt_project-1.6.json",
    "./schemas/1.7/dbt_project-1.7.json",
    "./schemas/latest/dbt_project-latest.json"
]

def check_equivalency(key, node_type, node_properties):
    if not key.startswith("+"):
        counterpart_key = "+" + key
    else:
        counterpart_key = key[1:]

    if counterpart_key not in node_properties.keys():
        raise Exception(f"{key} doesn't have an equivalent {counterpart_key} defined")
    key_properties = node_properties[key]
    counterpart_properties = node_properties[counterpart_key]
    match = key_properties == counterpart_properties
    if not match:
        difference = diff(key_properties, counterpart_properties)
        raise Exception(f"{key} and {counterpart_key} both exist in {node_type}, but are different: {difference}")

node_types = ['model_configs', 'seed_configs', 'snapshot_configs', 'source_configs', 'test_configs', 'unit_test_configs']
for filepath in PROJECT_SCHEMA_FILES:
    with open(filepath, "r") as f:
        data = json.load(f)
        for node_type in node_types:
            node_properties = data["$defs"].get(node_type, {}).get("properties", {})
            for key in node_properties.keys():
                check_equivalency(key, node_type, node_properties)


