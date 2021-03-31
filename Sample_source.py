from __future__ import print_function
import json
import hashlib
import requests
import pymysql
from datetime import datetime
from virus_total_apis import PrivateApi as VirusTotalPrivateApi

### Sample Sourcing ### source latest sample ###
timestamp=datetime.now()
cur_day_format = timestamp.strftime("%Y-%m-%d")
val1 ="C:\\virustotal\Sample_sha256_"
val2 ='fs:'+cur_day_format
url = 'https://www.virustotal.com/vtapi/v2/file/search'
params = {'apikey': '<apikey>', 'query': val2+'+'' positives: 5+ positives:10- nod32:infected'}
response = requests.get(url, params=params)
data = response.json()
with open(val1+cur_day_format+'.json', 'w', encoding='utf-8') as outfile:
  json.dump(data, outfile, ensure_ascii=False)

### file read ###
with open(val1+cur_day_format+".json", "rb") as myfile:
  data1 = myfile.read() 
obj = json.loads(data1)

### full report generate ###
API_KEY = '<apikey>'
vt = VirusTotalPrivateApi(API_KEY)

resobj = []
if 'hashes' in obj:
    sha256_hash = obj['hashes']
    for x in sha256_hash:
      response = vt.get_file_report(x)
      resobj.append(response)
    with open("data_"+cur_day_format+".json", "w", encoding='utf-8') as write_file:
        json.dump(resobj, write_file, ensure_ascii=False)