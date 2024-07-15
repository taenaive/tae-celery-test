from tae_celery_pac.tasks.taskBasic import where_am_i

# from tae_celery_pac.tae_server import cel_client


from asyncio import run, sleep
from celery.result import AsyncResult
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from tae_celery_pac.tae_server import TaskQueue, app

async def runClient():
        result = TaskQueue.delay("Hola Task for Celery!")
        # print( dir(result))
        #print(f"${result.status} > {result.id}")
        while  result.status == 'PENDING':
                await sleep(1)
                print(f"${result.status} > {result.result} > {result.task_id}")
                # print( vars(result))
        res = AsyncResult(result.id,app=app)
        print(f"$${res.state} > {res.get()} > {res.id}")
run(runClient())