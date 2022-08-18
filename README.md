# dbt YAML validator using JSON Schema

[JSON Schema](https://json-schema.org/) is a way to define the expected shape of JSON (or YAML) documents, which enable live checking of your files, as well as Intellisense/autocomplete as you type:

<div style="position: relative; padding-bottom: 66.84856753069577%; height: 0;"><iframe src="https://www.loom.com/embed/7dd4dfc67765441b80ff454942f59b63" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

This repository contains schemata for:
- Project definition files (`dbt_project.yml`)
- Package files (`packages.yml`)
- Selectors files (`selectors.yml`)
- Property files (`models/whatever.yml`)

## Installation in VS Code

1. Clone this repo locally
2. Install the [VSCode-YAML extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml)
3. Inside of your dbt project's directory, create a `.vscode/settings.json` file containing the following data. This is what tells the extension which schema to associate with each file. 
```json
//If you are checking the file into source control, you should make PATH_TO_THIS_REPO a relative link so that your colleagues get it too.
{    
    "yaml.schemas": {
        "PATH_TO_THIS_REPO/schemas/dbt_yml_files.json": [
            "/*.yml",
            "!profiles.yml",
            "!dbt_project.yml",
            "!packages.yml",
            "!selectors.yml",
            "!profile_template.yml"
        ],
        "PATH_TO_THIS_REPO/schemas/dbt_project.json": [
            "dbt_project.yml"
        ],
        "PATH_TO_THIS_REPO/schemas/selectors.json": [
            "selectors.yml"
        ],
        "PATH_TO_THIS_REPO/schemas/packages.json": [
            "packages.yml"
        ]
    },
}
```
4. To prompt other users to install the YAML extension, create a `.vscode/extensions.json` file containing the following data inside of your dbt project's directory:
```json
{
    "recommendations": [
        "redhat.vscode-yaml"
    ]
}
```

_Do you use a different IDE which also supports JSON Schema? Please open a PR with setup instructions and links to any extensions!_

## Contributing 
PRs that improve these schemata are welcome! 

Please ensure that JSON keys are sorted by [vscode-sort-json](https://marketplace.visualstudio.com/items?itemName=richie5um2.vscode-sort-json) according to the rules in `.vscode/settings`. 