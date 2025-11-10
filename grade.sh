#!/bin/bash

if [[ -z "$1" ]]; then
  echo "Must enter task to grade."
  exit 1
fi

TASK="$1"
[[ $TASK = "strassen" ]] && FILE="matrix-multiplication.py"
[[ $TASK = "dictionary" ]] && FILE="lookup.py"
[[ $TASK = "phonebook" ]] && FILE="sort.py"


RED=$'\e[31m'
GREEN=$'\e[32m'
RESET=$'\e[0m'

cd $TASK
for i in {1..2}; do
  if diff <(cat "sample${i}.in" | python "$FILE") "sample${i}.out" >/dev/null 2>&1; then
    echo -e "Sample $i: ${GREEN}CORRECT${RESET}"
  else
    echo -e "Sample $i: ${RED}WRONG${RESET}"
  fi
done