import json
from subprocess import CompletedProcess, run

async def arun(text:str) -> CompletedProcess:

    res =  run(args=text, shell=True, capture_output=True)

    return json.dumps(obj=res,default=str)
