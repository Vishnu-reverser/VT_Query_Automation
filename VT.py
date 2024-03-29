from __future__ import print_function
import json
import hashlib
import pymysql
from virus_total_apis import PublicApi as VirusTotalPublicApi
from datetime import datetime

API_KEY = 'APIKEY'

vt = VirusTotalPublicApi(API_KEY)
resobj = []

with open ('sha256.txt', 'r', encoding='utf-8') as istr:
    for line in istr:
        mysha = line
        print(line)
        response = vt.get_file_report(mysha)
        resobj.append(response)
        timestamp=datetime.now()
        variable="C:\\VT_Query_Automation\\haslist"
        cur_day_format = timestamp.strftime("%Y-%m-%d_%H")
        with open(variable+cur_day_format+".json", "w", encoding='utf-8') as write_file:
            json.dump(resobj, write_file, ensure_ascii=False)
