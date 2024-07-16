# Celery FastAPI Test Play

This project shows you how to do celery and FastAPI in python

## Installation

Use the package manager to install redis

```bash
 sudo apt update
 sudo apt install redis
 ``` 

 ## python installation

 ```bash
  python3.11 -m venv .venv
  source .venv/bin/activate

  pip install celery redis ...etc
  #or just
  pip install -r requirements.txt
  pip install ../tae-celery-package/dist/tae_celery_pac-0.0.1-py3-none-any.whl --force-reinstall
  ```

## Run on another terminal to test

```bash
#from new terminal
uvicorn server:fast_api_app --reload
#and from another terminal
pytest -v -s
```
## Celery with Flower (Optional)

```bash
pip install flower

celery -A main flower --loglevel=INFO
# --OR--
celery --broker="redis://localhost:6379" flower --loglevel=INFO
```
*refer to this page [flower docs](https://flower.readthedocs.io/en/latest/install.html#usage)
