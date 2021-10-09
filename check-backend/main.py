import os
import json

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import db


app = FastAPI(docs_url=None, redoc_url=None)
def get_checked_list():
    checked = db.DBBase().query_all('SELECT event_id FROM need_checked_events')
    checked_list = []
    for i in checked:
        checked_list.append(i['event_id'])
    return checked_list

origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/', status_code=200, description='首页')
async def homepage():
    resp = {'code':0, 'success':'success'}
    return resp

@app.get('/details', status_code=200, description='查看当前支持校验的埋点')
async def details():
    homepage_json = {}
    checked_list = get_checked_list()
    if checked_list is not None:
        for i in range(len(checked_list)):
            homepage_json[i] = checked_list[i]
        return homepage_json
    else:
        raise HTTPException(status_code=500)

class Item(BaseModel):
    date: str
    equip_id: str

@app.post('/check-is-missed', status_code=200, description='校验埋点上报是否丢失')
async def check_is_missed(item:Item):
    checked_list = get_checked_list()
    date = item.date
    equip_id = item.equip_id
    results = db.DBBase().query_all(f'SELECT event_id, count(*) as c FROM events_tracking_log_{date} '
                                    f'WHERE equip_id = "{equip_id}" GROUP BY event_id')
    result_dict = {} # save database event_id -> count json
    result_event_id_list = []
    if type(results) == list:
        for result in results:
            select_event_id = result['event_id']
            select_event_count = result['c']
            result_dict[select_event_id] = select_event_count
            result_event_id_list.append(select_event_id)
        resp_dict = {}
        for check_event in checked_list:
            resp_dict[check_event] = 0
        for check_event in checked_list:
            if check_event in result_event_id_list:
                resp_dict[check_event] = result_dict[check_event]
        return resp_dict
    else:
        raise HTTPException(status_code=500)



if __name__ == '__main__':
    uvicorn.run(app='main:app', host = '127.0.0.1', port = 1234, reload=True, debug=True)
