# dbt YAML validator using JSON Schema

[JSON Schema](https://json-schema.org/) is a way to define the expected shape of JSON (or YAML) documents. This enables live checking of your files, as well as Intellisense/autocomplete as you type. 

## 60 second demo video:
<a href="https://www.loom.com/share/7dd4dfc67765441b80ff454942f59b63?autoplay=1"><img src="https://user-images.githubusercontent.com/7335046/185288526-7dda607f-b406-4e79-ad9f-bf96f654ead0.gif"/></a>

## What does it do?
This repository contains schemata for:
- Project definition files (`dbt_project.yml`)
- Package files (`packages.yml`)
- Selectors files (`selectors.yml`)
- Property files (`models/whatever.yml`)

## Installation in VS Code

1. Install the [VSCode-YAML extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml)
2. Inside of your dbt project's directory, create a `.vscode/settings.json` file containing the following data. This is what tells the extension which schema to associate with each file. 
```json
{    
    "yaml.schemas": {
        "https://raw.githubusercontent.com/dbt-labs/dbt-jsonschema/main/schemas/latest/dbt_yml_files.json": [
            "/**/*.yml",
            "!profiles.yml",
            "!dbt_project.yml",
            "!packages.yml",
            "!selectors.yml",
            "!profile_template.yml"
        ],
        "https://raw.githubusercontent.com/dbt-labs/dbt-jsonschema/main/schemas/latest/dbt_project.json": [
            "dbt_project.yml"
        ],
        "https://raw.githubusercontent.com/dbt-labs/dbt-jsonschema/main/schemas/latest/selectors.json": [
            "selectors.yml"
        ],
        "https://raw.githubusercontent.com/dbt-labs/dbt-jsonschema/main/schemas/latest/packages.json": [
            "packages.yml"
        ]
    },
}
```
3. To prompt other users to install the YAML extension, create a `.vscode/extensions.json` file containing the following data inside of your dbt project's directory:
```json
{
    "recommendations": [
        "redhat.vscode-yaml"
    ]
}
```

## Installation in Vim

1. Install the [coc.nvim](https://github.com/neoclide/coc.nvim) plugin
2. Install [coc-yaml](https://github.com/neoclide/coc-yaml): `:CocInstall coc-yaml`
3. Add JSON Schema (there might be a better way to do this, but adding directly to `coc-settings.json` using `:CocConfig` works):
```json
{    
    "yaml.schemas": {
        "https://raw.githubusercontent.com/dbt-labs/dbt-jsonschema/main/schemas/latest/dbt_yml_files.json": [
            "/**/*.yml",
            "!profiles.yml",
            "!dbt_project.yml",
            "!packages.yml",
            "!selectors.yml",
            "!profile_template.yml"
        ],
        "https://raw.githubusercontent.com/dbt-labs/dbt-jsonschema/main/schemas/latest/dbt_project.json": [
            "dbt_project.yml"
        ],
        "https://raw.githubusercontent.com/dbt-labs/dbt-jsonschema/main/schemas/latest/selectors.json": [
            "selectors.yml"
        ],
        "https://raw.githubusercontent.com/dbt-labs/dbt-jsonschema/main/schemas/latest/packages.json": [
            "packages.yml"
        ]
    },
}
```

## Installation in JetBrains

IDEs by JetBrains like PyCharm and IntelliJ enable us to use the JSON Schema, using [the JSON schema mapping feature](https://www.jetbrains.com/help/idea/json.html#ws_json_schema_add_custom).

1. Open the preferences of JSON schema mapping in JetBrains
2. Add custom schema mappings

There is no way to add the preferences with a configuration file like VS Code.
As we have to manually configure them one by one, we just describe values of the configurations below.
If you want to know the details, the [dbt YAML validator in JetBrains article](https://yu-ishikawa.medium.com/dbt-yaml-validator-in-jetbrains-b5ef25e9253e) describes how to configure the JSON schema mapping in details.

- Project definition files
    - URL: `https://raw.githubusercontent.com/dbt-labs/dbt-jsonschema/main/schemas/latest/dbt_project.json`
    - Schema version: JSON schema version 7
    - Mapping: `dbt_project.yml`
- Package files
    - URL: `https://raw.githubusercontent.com/dbt-labs/dbt-jsonschema/main/schemas/latest/packages.json`
    - Schema version: JSON schema version 7
    - Mapping: `packages.yml`
- Selectors files
    - URL: `https://raw.githubusercontent.com/dbt-labs/dbt-jsonschema/main/schemas/latest/selectors.json`
    - Schema version: JSON schema version 7
    - Mapping: `selectors.yml`
- Property files
    - URL: `https://raw.githubusercontent.com/dbt-labs/dbt-jsonschema/main/schemas/latest/dbt_yml_files.json`
    - Schema version: JSON schema version 7
    - Mapping: `models/**/*.yml`, `analysis/**/*.yml`, `snapshots/**/*.yml`

![A screenshot of a JetBrains Preferences panel showing the correct mapping of the dbt_yml_files JSON Schema](/jetbrains-config.png)

_Do you use a different IDE which also supports JSON Schema? Please open a PR with setup instructions and links to any extensions!_

## Contributing 
PRs that improve these schemata are welcome! 

Please ensure that JSON keys are sorted by [vscode-sort-json](https://marketplace.visualstudio.com/items?itemName=richie5um2.vscode-sort-json) according to the rules in `.vscode/settings`. 
