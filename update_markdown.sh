#!/bin/bash

if [ -z "$SECRET_SCANNING_TOOLS_PATH" ]; then
  export SECRET_SCANNING_TOOLS_PATH="${HOME}"/secret-scanning-tools
  echo "Defaulting to SECRET_SCANNING_TOOLS_PATH=${SECRET_SCANNING_TOOLS_PATH}"
fi

CUSTOM_PATTERNS_PATH=$PWD "${SECRET_SCANNING_TOOLS_PATH}"/examples/update_custom_patterns_readme.sh
