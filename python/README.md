# Python3

## Start

Since the requirements are installed as root project needed, so not necessary to install again.

Simply, 
**change daily in [daily.json](../daily-problems.json)** `Note: the json file is under root with your problem folder, named 'daily-${folder}.json'` and try:
```shell
.venv/bin/python python/test.py
```

or if you want to run more than one questions,
**change plans in [daily.json](../daily-problems.json)** `Note: the json file is under root with your problem folder, named 'daily-${folder}.json'` and try:
```shell
.venv/bin/python python/tests.py
```

If the virtualenv is unavailable, substitute `python3`. `make` targets prefer
`.venv/bin/python` when it exists; override with `make test PYTHON=/path/to/python`.

## EXTRA

If you are using vscode and python root gets wrong,
add this line into your .env

```env
PYTHONPATH=.
```