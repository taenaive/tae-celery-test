from fastapi import FastAPI
from pydantic import BaseModel
from client import  runClient

class ProjectReq(BaseModel):
    projectid: str
    test: str | None = None

fast_api_app = FastAPI()

@fast_api_app.get("/")
async def root():
    return {"msg": "Hola"}

@fast_api_app.post("/ner/")
async def ner(prj: ProjectReq):
    await runClient()
    return prj

@fast_api_app.get("/ner/{project_id}")
async def nerget(project_id: int):
    result = await runClient()
    return result