import json
import pymysql
import os
from datetime import datetime

## Json parser may useful for push queried data to mysqldb ##

timestamp=datetime.now()
cur_day_format = timestamp.strftime("%Y-%m-%d")
val1="C:\\VT_Query_Automation\\"

# # read file
with open(val1+"data_"+cur_day_format+".json", "rb") as myfile:
  data=myfile.read()
  
# parse file
obj = json.loads(data)

tags0 = ""
tags1 = ""
for data in obj:
      if 'results' in data:
        dataobj = data['results']
        rescode = dataobj['response_code']
        vhash = dataobj['vhash']
        subname = dataobj['submission_names']
        sdate = dataobj['scan_date']
        ls = dataobj['last_seen']
        tsub = dataobj['times_submitted']
        fsize = dataobj['size']
        tags = dataobj['tags']
        sha256_hash = dataobj['sha256']
        print('Sha256:',sha256_hash)
        fs = dataobj['first_seen']
        print('First_seen:',fs)
        md5_hash = dataobj['md5']
        sha1_hash = dataobj['sha1']
        ssdeep = dataobj['ssdeep']
        vtscore = dataobj['positives']
        print('No of detection:',vtscore)
        print('\n')
      else:
        dataobj = ""
      if tags is None:     
         tags0 = ftype
         tags1 = ""
      else:
         result = tags
         legth = len(result)
         if legth == 2:
           tags0 = result[0]
           tags1 = result[1]
         else:
           tags0 = ""
           tags1 = ""       
      if('additional_info') in dataobj:
        addinfo = dataobj['additional_info']
        if 'pe-imphash' in addinfo:
          imphash = addinfo['pe-imphash']  
        else:
          imphash =""
        if 'execution_parents' in addinfo:
          parent_sha256 = addinfo['execution_parents']
        else:
          parent_sha256 =""
        if 'sigcheck' in addinfo:
          sigcheck = addinfo['sigcheck']
        else:
          sigcheck=""
        if('exiftool') in addinfo:
          exiftool = addinfo['exiftool']
          if 'FileTypeExtension' in exiftool:
            ftype = exiftool['FileTypeExtension']
          else:
            ftype =""
          if 'OriginalFileName' in exiftool:
            filename = exiftool['OriginalFileName']
          else:
            filename =""
          if 'MIMEType' in exiftool:
            fmimetype = exiftool['MIMEType']
          else:
            fmimetype =""
      if('scans') in dataobj:
        dataobjo = dataobj['scans']
        if 'ESET-NOD32' in dataobjo:
          esetobj = dataobjo['ESET-NOD32']
          esetdet = esetobj['result']  
        else:
          esetdet =""
        if 'Symantec' in dataobjo:
          symobj = dataobjo['Symantec']
          symdet = symobj['result']
        else:
          symdet =""
        if 'Kaspersky' in dataobjo:
          ksobj = dataobjo['Kaspersky']
          ksdet = ksobj['result']
        else:
          ksdet =""
      
        if'Cyren' in dataobjo:
          cyobj = dataobjo['Cyren']
          cydet = cyobj['result']
        else:
          cydet =""

        if'Fortinet' in dataobjo:
          fortobj = dataobjo['Fortinet']
          fordet = fortobj['result']
        else:
          fordet =""
      source = "VirusTotal"
      reporter ="Vishnu-reverser"
      sourceLink ="https://www.virustotal.com/gui/home/search"
