# Diigging: A Python Script for Interacting with the Diigo API

## How To Use
You'll need to rename example.env to .env and fill in the values for it's three variables before using the script.

This script currently includes three functions: `query_basic()`, `query_multiple_pages()`, and `query_all_pages()`.

At the bottom of the script are calls to each of the three functions. Two are commented by default, one uncommented. If you want to run a different query uncomment the desired function call and comment the unneeded function call.

## Requests
This script relies on the Requests Library to do the heavy lifting. If you are unfamiliar with Requests, see below article:
[https://realpython.com/python-requests/]

## Visual Studio Code
This project includes a .devcontainer folder which has a definition of a container that can be consumed by VSC to quickly spinup a dev environment.

In addition, there is a .vscode folder which contains a settings.json file that overrides VSC's default settings. You'll need to update the pythonPath. Easiest way to accomplish this is: View --> Command Palette -> Python: Select Interpreter.