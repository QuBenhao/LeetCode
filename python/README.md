# Python3

## Start

Since the requirements are installed as root project needed, so not necessary to install again.

Simply, 
**change daily in [daily.json](../daily-problems.json)** `Note: the json file is under root with your problem folder, named 'daily-${folder}.json'` and try:
```shell
python3 python/test.py
```

or if you want to run more than one questions,
**change plans in [daily.json](../daily-problems.json)** `Note: the json file is under root with your problem folder, named 'daily-${folder}.json'` and try:
```shell
python3 python/tests.py
```

## EXTRA

If you are using vscode and python root gets wrong,
add this line into your .env

```env
PYTHONPATH=.
```