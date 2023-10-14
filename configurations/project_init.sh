#!/bin/bash

SCRIPT_DIR="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

PROJECT_DIR=${SCRIPT_DIR%/*}

RELATIVE_GITS_PATH="code/gits.py"

GITS_EXEC_PATH="${PROJECT_DIR}/${RELATIVE_GITS_PATH}"

BASHRC=~/.bashrc
if [ -f "$BASHRC" ]; then
    echo "$BASHRC exists, appending gits commandline tool alias"
    echo "alias gits=\"python3 \"$GITS_EXEC_PATH\"\"" >> $BASHRC
else
    echo "$BASHRC does not exist, creating a new file and adding gits commandline tool alias"
    echo "alias gits=\"python3 \"$GITS_EXEC_PATH\"\"" >> $BASHRC
fi

echo "Initialising gits directory in user home directory"

GITS=~/.gits
GITS_LOG=~/.gits/logs

mkdir -p $GITS $GITS_LOG
