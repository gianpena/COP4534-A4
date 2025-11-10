#!/bin/bash

RED=$'\e[31m'
GREEN=$'\e[32m'
RESET=$'\e[0m'

for i in {1..2}; do
  if diff <(cat "sample${i}.in" | python matrix-multiplication.py) "sample${i}.out" >/dev/null 2>&1; then
    echo -e "Sample $i: ${GREEN}CORRECT${RESET}"
  else
    echo -e "Sample $i: ${RED}WRONG${RESET}"
  fi
done