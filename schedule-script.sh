#!/usr/bin/env bash
set -e

DIR_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
exec >> "${DIR_PATH}/output.log" 2>&1

print_statement()
{
  echo -e "$1"
}

print_statement "\n\n\n$(date)\n"

print_statement "Starting Script\n"
print_statement "Directory Path: ${DIR_PATH}\n"

print_statement "Changing directory\n"
cd "$DIR_PATH"

print_statement "Activating Virtual Environment\n"
source .venv/bin/activate

print_statement "Executing Script \n"
python -B manage.py