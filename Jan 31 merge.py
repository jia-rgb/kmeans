# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 12:00:46 2020

@author: jejia
"""

import pandas as pd  
  

dsc = pd.read_csv(r'C:\Users\jejia\Desktop\DataScience\1 data pilots\data_pilots.csv')
 

grade = pd.read_csv(r'C:\Users\jejia\Desktop\DataScience\1 data pilots\Chaojin5 - spyder.csv')

#grade2 = pd.read_csv(r'C:\Users\jejia\Desktop\DataScience\1 data pilots\air asia - sql.csv')
#合并sc表与student表，把sc的sid列与student的index进行关联  

#sc1 = am.join(dsc,on='ID',how='inner')
dsc=dsc.rename(columns={'Id':'CrewMemberId'})

sc1 = pd.merge(grade, dsc, how = 'outer', on=['CrewMemberId']) 
#print (sc1)
sctest = sc1[:10]
#%% 1 221 266 rows some grades don't have  pilots

sc2 = pd.merge(grade, dsc, how = 'left', on=['CrewMemberId']) 

export_csv = sc2.to_csv (r'C:\Users\jejia\Desktop\DataScience\1 data pilots\merge left join.csv', index = None, header=True)

#%% 741 609 rows pilots and grades match   

sc3 = pd.merge(grade, dsc, how = 'inner', on=['CrewMemberId']) 

#%% 741 652 rows - some pilots don't have grade  

sc4 = pd.merge(grade, dsc, how = 'right', on=['CrewMemberId']) 

