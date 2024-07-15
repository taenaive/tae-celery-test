# Celery Test Play

This project shows you how to do celery in python

## Installation

Use the package manager to install redis

```bash
 sudo apt update
 sudo apt install redis
 ``` 

 ## python installation

 ```bash
  python3.11 -m venv .venv
  pip install celery redis
  ```

  ## How to run

  ```bash
  export PYTHONPATH=$PYTHONPATH:$(pwd)/src
  celery -A main worker --loglevel=INFO
  ```

## Run on another terminal to test

```bash
>>> from main import add
>>> result1 = add(100,100)
>>> result1
200
>>> result1 = add.delay(100,100)
>>> result1
<AsyncResult: 421b3df7-6811-48fd-8540-27fef8a2a841>
>>> result1.status
'PENDING'
>>> 
```
## Celery with Flower (Optional)

```bash
pip install flower

celery -A main flower --loglevel=INFO
# --OR--
celery --broker="redis://localhost:6379" flower --loglevel=INFO
```
*refer to this page [flower docs](https://flower.readthedocs.io/en/latest/install.html#usage)

## distribution

```bash
pip install build
# source distribution.
python -m build -s -v
#
```