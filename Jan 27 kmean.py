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
            END as OverallGrade,
            TrainingCompetency.Name as CompetencyName,
            /*TrainingCompetencyAssessment.Grade as CompetencyGrade,   */
            CASE
                WHEN ass.Grade='1' THEN 1
                WHEN ass.Grade='2' THEN 2
                WHEN ass.Grade='3' THEN 3
                WHEN ass.Grade='4' THEN 4
                ELSE null
            END as CompetencyGrade,
            AssessmentCrewMember.TrainingRecommended as RemedialTrainingRec,
            TeachingPoint.TeachingPointId,
            TeachingPointDefinition.Name as TeachingPointName,
            TrainingEventDefinition.TrainingEventDefinitionId,
            TrainingEventDefinition.Name as TrainingEventName,
            CASE
                WHEN TeachingPoint.Grade='1' THEN 1
                WHEN TeachingPoint.Grade='2' THEN 2
                WHEN TeachingPoint.Grade='3' or TeachingPoint.Grade='PERF' or TeachingPoint.Grade='NPERF' THEN 3
                WHEN TeachingPoint.Grade='4' THEN 4
                ELSE null
            END as InstructorGrade,

            TeachingPoint.Comment as TeachingPointComment,
          
            TC.Name as FlaggedCompetencyName,
            TrainingCompetencyIndicator.Name as FlaggedBehaviorIndicatorName,
                                    TeachingPointCompetencyIndicatorAssessment.Comment as FlaggedBehaviorIndicatorComment,
          
            Scorecard.ScorecardId,
            Scorecard.TrainingEventStart,
            Scorecard.TrainingEventStop,
            Scorecard.SuggestedGrade as OAGrade,
            ScorecardBelowStandardCriteria.Grade as ReasonGrade,
            BelowStandardCriteriaReason.Reason,
          
            SentinelAircraftType.Model,
            SentinelTrainingDevice.DeviceKey,
          
            Person.Email as TrainingInstructorEmail,
            Customer.Name as CustomerName
        FROM
            TeachingPoint
            /* Training Event Definition */
            LEFT JOIN TeachingPointDefinition ON TeachingPoint.TeachingPointDefinitionId = TeachingPointDefinition.TeachingPointDefinitionId
            LEFT JOIN TrainingEventDefinition ON TeachingPointDefinition.EventDefinitionId = TrainingEventDefinition.TrainingEventDefinitionId
      
            /* Scorecards */
            LEFT JOIN AssessmentCrewMember ON TeachingPoint.AssessmentCrewMemberId = AssessmentCrewMember.AssessmentCrewMemberId
            LEFT JOIN Scorecard       ON (AssessmentCrewMember.AssessmentCrewMemberId = Scorecard.AssessmentCrewMemberId
                                     AND TrainingEventDefinition.TrainingEventDefinitionId=Scorecard.TrainingEventDefinitionId)
          
                   
            /* Assessment Role */
            LEFT JOIN AssessmentRole       ON AssessmentRole.AssessmentRoleId = AssessmentCrewMember.AssessmentRoleId
      
            /* Training Device */
            left JOIN Assessment                ON AssessmentCrewMember.AssessmentId = Assessment.AssessmentId
            left JOIN TrainingSession           ON TrainingSession.TrainingSessionId = Assessment.TrainingSessionId
            left JOIN TrainingSessionInstructor ON TrainingSession.TrainingSessionId = TrainingSessionInstructor.TrainingSessionId
            left JOIN PairingSession            ON PairingSession.PairingSessionId = TrainingSessionInstructor.PairingSessionId
            left JOIN SentinelTrainingDevice    ON SentinelTrainingDevice.TrainingDeviceId =  PairingSession.TrainingDeviceId
            left JOIN SentinelAircraftType      ON SentinelAircraftType.AircraftTypeId =  SentinelTrainingDevice.AircraftTypeId

            /* Customer */
            left JOIN AssessmentDefinition ON Assessment.AssessmentDefinitionId = AssessmentDefinition.AssessmentDefinitionId
            left JOIN Customer             ON AssessmentDefinition.CustomerId   = Customer.CustomerId
          
            /* Instructor */
            left JOIN Person                    ON TrainingSessionInstructor.InstructorId = Person.PersonId
          
            /* Competency */   
            LEFT JOIN TrainingCompetencyAssessment ON AssessmentCrewMember.AssessmentCrewMemberId = TrainingCompetencyAssessment.AssessmentCrewMemberId
            LEFT JOIN TrainingCompetency ON TrainingCompetencyAssessment.TrainingCompetencyId = TrainingCompetency.TrainingCompetencyId
            LEFT JOIN TeachingPointCompetencyIndicatorAssessment ON TeachingPoint.TeachingPointId =TeachingPointCompetencyIndicatorAssessment.TeachingPointId
            LEFT JOIN TrainingCompetencyIndicator ON    TeachingPointCompetencyIndicatorAssessment.TrainingCompetencyIndicatorId =     TrainingCompetencyIndicator.TrainingCompetencyIndicatorId
            LEFT JOIN TrainingCompetency TC ON TrainingCompetencyIndicator.TrainingCompetencyId = TC.TrainingCompetencyId

          
            /* Reasons below criteria */
            LEFT JOIN ScorecardBelowStandardCriteria ON Scorecard.ScorecardId                                        = ScorecardBelowStandardCriteria.ScorecardId
            LEFT JOIN BelowStandardCriteriaReason    ON ScorecardBelowStandardCriteria.BelowStandardCriteriaReasonId = BelowStandardCriteriaReason.BelowStandardCriteriaReasonId
                 
        WHERE
            TrainingSession.StartTime >= CONVERT(DATETIME,'2019-07-01')
            AND TrainingSession.EndTime <= CONVERT(DATETIME,'2019-12-31')
            AND AssessmentDefinition.Name like '%AirAsia REC%'
            and AssessmentDefinition.Name like '%Jul%'
            and (AssessmentRole.AssessmentRoleId = '2' OR AssessmentRole.AssessmentRoleId = '3')
            and TeachingPoint.Grade is not null
            and Person.Email like '%airasia%'
            and Customer.name like '%Air Asia%' or Customer.name like '%AirAsia%'
   

'''.format(startDate, endDate, 'Jul')
#%%

cursor1 = conn.cursor()
dftest = cursor1.execute(query_session)
with open(r'C:\Users\jejia\Desktop\DataScience\1 data pilots\Chaojin.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([x[0] for x in cursor1.description])  # column headers
    for row in dftest:
#conn.setencoding(cursor, conn)
#for row in cursor:
        writer.writerow(row)
        
        
#df = pd.read_sql(query_session, conn)
#conn.setencoding(query_session, conn)

#df.to_csv(r'C:\Users\jejia\Desktop\DataScience\1 data pilots\Chaojin.csv')


