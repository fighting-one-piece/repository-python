# -*- coding:utf-8 -*-
'''
@author: wulin
'''

import sys
import xlwt
import datetime
from pymongo import MongoClient

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    print sys.getdefaultencoding()
    reload(sys)
    #sys.setdefaultencoding(default_encoding)
    

if __name__=='__main__':  
    startTime = datetime.datetime.now()
    
    #conn = pymongo.Connection("123.57.0.218", 27017)
    mongoClient = MongoClient("123.57.0.218", 27017)
    #连接库
    db = mongoClient.ganji_house 
    #用户认证
    db.authenticate("dhy","8826377a9e7525586dc1f4b9c0379ac9")
    
    print db.caigou.count()
    
    workbook = xlwt.Workbook(encoding='utf-8')  
    
    #datas = db.caigou.find()
    datas = db.caigou.find()[0:100]

    EXCEL_ROWS = 65535
    EXCEL_COLS = 256
    nrows, total_rows, sheet_num = 0, 0, 0
    
    for data in datas:
        if (nrows % EXCEL_ROWS == 0):
            wsheet = workbook.add_sheet('sheet' + str(sheet_num), cell_overwrite_ok = True)
            nrows = 0
            sheet_num = sheet_num + 1
        keys = data.keys()
        cols_num = EXCEL_COLS if len(keys) > EXCEL_COLS else len(keys)
        for ncol in xrange(cols_num):
            value = data[keys[ncol]]
            wsheet.write(nrows, ncol, value)
        nrows = nrows + 1
        total_rows = total_rows + 1
    
    workbook.save("F:\\a.xls")
    endTime = datetime.datetime.now()
    print "import xls success ! spend time %s seconds" %((endTime - startTime).seconds)
           
