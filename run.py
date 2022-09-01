import json
import requests
from pydantic import BaseModel
import os


class MyLog(BaseModel):
    job_id: str
    level: str
    event: str
    timestamp: str


params_service = {"query": '{container_name="angry_greider"}'}
url = os.getenv("LOKI_URL")
response = requests.get(url=url, params=params_service)
data = response.json()["data"]["result"]
print("==== Get all rows ====")
# params_service
for row in data:
    dt = row["values"]
    for item in dt:
        nest = item[1]
        j_data = json.loads(nest)
        print(MyLog(**j_data))
print("==================")
print("\n")
print("==== Get all rows based by job_id ====")
# params_logs
params_logs = {
    "query": '{container_name="angry_greider"} |= `` | json | job_id = `HEJhej`'
}
response = requests.get(url=url, params=params_logs)
data = response.json()["data"]["result"]
for row in data:
    dt = row["stream"]
    print(MyLog(**dt))
print("==================")
