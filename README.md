# Proof of concept: dbt YAML validator for VSCode

This code is a proof of concept to demonstrate how a valid JSON Schema and the right extensions in VSCode can provide immediate error checking during the development of a dbt project.

To get the proof of concept working:
1. Clone this repo locally, and open it VSCode
2. VSCode should prompt you to install the [VSCode-YAML extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml) (see [extensions.json](/.vscode/extensions.json))
3. Open one of the examples and write some YAML, it should get automatically error-checked.
