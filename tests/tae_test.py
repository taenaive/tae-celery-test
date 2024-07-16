import pytest 
import asyncio 
from tae_celery_pac import tae_server

pytest_plugins = ('pytest_asyncio',) 
 
@pytest.mark.asyncio 
async def test_celery_worker_spawn(): 

    print("making available to celery.... TaskQueue and add") 
    try: 
        task = asyncio.create_task(tae_server.app.worker_main(argv = ['worker', '--loglevel=info'])) 
        task.cancel() 
        await task 
    except asyncio.CancelledError: 
        print("Task Cancelled already") 
    except Exception:
        print("General Exception")

 

 