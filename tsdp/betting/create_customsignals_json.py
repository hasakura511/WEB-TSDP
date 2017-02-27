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

dataPath='/Users/hidemiasakura/Dropbox/ML-TSDP/data/csidata/v4futures4/'
lookbacks=[1,2,5,20]
columns = ['Date', 'Open','High','Low','Close','Volume','OpenInterest',
           'Contract','Seasonality']
def getBackendDB():
    dbPath = 'futures.sqlite3'
    readConn = sqlite3.connect(dbPath)
    return readConn

def getChartDB():
    dbPath = 'db_charts.sqlite3'
    readConn = sqlite3.connect(dbPath)
    return readConn

readConn=getBackendDB()
readPriceConn=getChartDB()



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
df=pd.DataFrame(data=dict(Group=futuresDF.group.values,\
                          Markets=desc_hyperlink,
                            Default=futuresDF.Custom.values),
                            index=futuresDF.index)

filename='custom_signals_data.json'
if isfile(filename):
    with open(filename, 'r') as f:
        custom_signals_data = json.load(f)
    custom_signals_data=custom_signals_data[custom_signals_data.keys()[0]]
    df['signals']=pd.Series(custom_signals_data)
else:
    custom_dict={'Default':df.sort_values(by=['Group'])['Default']\
                                                 .transpose().to_dict()}
    with open(filename, 'w') as f:
        json.dump(custom_dict,f)
    df['signals']=df['Default'].copy()
    
df=df[['Markets','Group','signals','Default']]
df['Anti-Default']=np.where(df.Default>0,-1,1)

for sym in df.index:
    filename=dataPath+futuresDict.Filename.ix[sym]+'_B.CSV'
    print sym, isfile(filename)
    if isfile(filename):
        data=pd.read_csv(filename)
        data.columns = columns
        tablename = 'pricedata_'+sym
        data.to_sql(name=tablename,con=readPriceConn, index=False,
                    if_exists='replace')
        print 'Wrote', tablename,'to db_charts.sqlite3'
        data2=data[-max(lookbacks)-1:]
        print data2.shape
        for lookback in lookbacks:
            col_name=str(lookback)+'-Day %Chg'
            pctchg=data2.Close.pct_change(periods=lookback).values[-1]
            signal=1 if pctchg>0 else -1
            df.set_value(sym, col_name, signal)
            df.set_value(sym, 'Anti-'+col_name, -signal)
            print col_name, pctchg, signal

customsignals=df.sort_values(by=['Group']).transpose().to_json()





'''
#from vol_adjsize
filename='./web/tsdp/custom_signals_data.json'
if isfile(filename):
    with open(filename, 'r') as f:
        custom_signals_data = json.load(f)
        
for sym in custom_signals_data:
    #print c2contractSpec[sym], custom_signals_data[sym]['signals']
    c2contractSpec[sym][5]=int(custom_signals_data[sym]['signals'])
print 'loaded and updated custom signals from', filename
'''
