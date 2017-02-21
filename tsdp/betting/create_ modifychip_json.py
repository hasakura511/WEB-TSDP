from django import forms
import json
import time
import math
import datetime
from datetime import datetime as dt
from pytz import timezone
from tzlocal import get_localzone
import sqlite3
import pandas as pd
#from .models import MetaData, AccountData, UserSelection
import calendar
import numpy as np
import re
from os.path import isfile, join
from os import listdir

def getBackendDB():
    dbPath = 'futures.sqlite3'
    readConn = sqlite3.connect(dbPath)
    return readConn

readConn=getBackendDB()
futuresDict = pd.read_sql('select * from Dictionary', con=readConn,\
                          index_col='CSIsym')
feeddata = pd.read_sql('select * from feeddata', con=readConn,\
                          index_col='CSIsym')
lastdate= pd.read_sql('select distinct Date from futuresATRhist',\
                      con=readConn).Date.tolist()[-1]
futuresDF=pd.read_sql('select * from (select * from futuresATRhist\
                                      where Date=%s\
                order by timestamp ASC) group by CSIsym'%lastdate,\
                    con=readConn,  index_col='CSIsym')

accountInfo=pd.read_sql('select * from accountInfo where timestamp=\
                (select max(timestamp) from accountInfo)',\
                con=readConn,  index_col='index').drop(['timestamp','Date'],axis=1)
ai_dict=accountInfo.to_dict()
for account in ai_dict:
    ai_dict[account]['offline']=[x for x in\
                                   eval(accountInfo[account].offline)\
                                   if x in feeddata.index]
    
images=listdir('./betting/static/public/images/')
chip_images=filter(lambda x: 'chip_' in x, images)


'''
lastdate= pd.read_sql('select distinct Date from futuresATRhist',\
                      con=readConn).Date.tolist()[-1]
futuresDF=pd.read_sql('select * from (select * from futuresATRhist\
                                      where Date=%s\
                order by timestamp ASC) group by CSIsym'%lastdate,\
                    con=readConn,  index_col='CSIsym')

futuresDict = pd.read_sql('select * from Dictionary', con=readConn,\
                          index_col='CSIsym')

desc_list = futuresDict.ix[futuresDF.index].Desc.values
desc_hyperlink = [re.sub(r'\(.*?\)', '', desc) for desc in desc_list]
desc_hyperlink = ['<a href="/static/images/v4_' + [futuresDict.index[i]\
                       for i, desc in enumerate(futuresDict.Desc) \
              if re.sub(r'-[^-]*$', '', x) in desc][0] + \
            '_BRANK.png" target="_blank">' + x + '</a>' \
            for x in desc_hyperlink]
df=pd.DataFrame(data=dict(signals=futuresDF.Custom.values,\
                          group=futuresDF.group.values,\
                          desc=desc_hyperlink), index=futuresDF.index)

df.sort_values(by=['group']).transpose().to_json('custom_signals_data.json')

filename='custom_signals_data.json'
if isfile(filename):
    with open(filename, 'r') as f:
        custom_signals_data = json.load(f)
'''