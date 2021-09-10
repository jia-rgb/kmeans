# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 09:37:59 2020

@author: jejia
"""
    #open database connection = database
import csv
import pyodbc
import pandas as pd
    #loop through all drivers we have acces to
#for driver in pyodbc.drivers():
#    print (driver)
#%%
conn = pyodbc.connect(
            'DRIVER={SQL Server};\
            SERVER=server.database.windows.net;DATABASE=database;\
            UID=xxx;PWD=xx')
#test with single table
#cursor = conn.cursor()
#dftest = cursor.execute('SELECT*FROM database.dbo.tablename')
#with open(r'C:\Users\jejia\Desktop\DataScience\1.csv', 'w', newline='') as csvfile:
#    writer = csv.writer(csvfile)
#    writer.writerow([x[0] for x in cursor.description])  # column headers
#    for row in dftest:

#        writer.writerow(row)

#conn.setencoding(cursor, conn)
#for row in cursor:

#cursor.to_csv(r'C:\Users\jejia\Desktop\DataScience\11.csv')
    
#%%

startDate = 'dateformat'
endDate = 'dateformat' 
query_session ='''
SELECT distinct
         
            tablename.columnname,
            tablename.column2 as name,
            
                WHEN table.name='P' or x.x='PP' THEN 'P'
                WHEN table.name='F' THEN 'F'
                ELSE null
            END as OvlGrd,
            Table.Name as nName,
            /*table.Grade as nGrade,   */
            CASE
                WHEN ass.Grade='1' THEN 1
                WHEN ass.Grade='2' THEN 2
                WHEN ass.Grade='3' THEN 3
                WHEN ass.Grade='4' THEN 4
                ELSE null
            END as nGrade,
            table.column as name,
            
            CASE
                WHEN name.grd='1' THEN 1
                WHEN name.grd='2' THEN 2
                WHEN name.grd='3' or name.grd='xx' or name.grd='xxx' THEN 3
                WHEN name.grd='4' THEN 4
                ELSE null
            END as nmegrd,

           
        FROM
            tptable
            /* Training Event Definition */
            LEFT JOIN tpdtable ON tptable.tpdId = tpdtable.tpdId
            LEFT JOIN teftable ON tpdtable.edId = tedtable.tedId
      
          /* FILTER */
        WHERE
            TSTABLE.stcolm >= CONVERT(DATETIME,'dateformate1')
            AND  TSTABLE.stcolm <= CONVERT(DATETIME,'dateformate2')
            AND adtable.Name like '%text%'
           
            and (artable.arId = 'xxx1' OR artable.arId = 'xxx2')
            and tptable.Grade is not null
            and table.Email like '%domain%'
        
   

'''.format(startDate, endDate, 'Jul')
#%%

cursor1 = conn.cursor()
dftest = cursor1.execute(query_session)
with open(r'C:\Users\jejia\Desktop\DataScience\n.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([x[0] for x in cursor1.description])  # column headers
    for row in dftest:
#conn.setencoding(cursor, conn)
#for row in cursor:
        writer.writerow(row)
        
        
#df = pd.read_sql(query_session, conn)
#conn.setencoding(query_session, conn)

#df.to_csv(r'C:\Users\jejia\Desktop\DataScience\1n.csv')


