import csv
import os
from datetime import datetime
from sys import setrecursionlimit
from xmlrpc.client import DateTime
from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import db_host, db_name, db_pass, db_user
from Model.engagement import Engagement
from Model.member import Member
from Get_Info import get_csv_file, sort_csv

def Read_Engagement():

    #connect to database
    engine = create_engine(f'postgresql://{db_user}:{db_pass}@{db_host}/{db_name}')

    Session = sessionmaker(bind=engine)

    s = Session()

    #truncate table before reading data into db to avoid duplicate primary keys
    s.execute('TRUNCATE TABLE "Engagement"')
    s.commit()

    #Read from the member CSV file and write the data into database
    with open(r'C:\Users\Selina\Desktop\tracking_tool_import_data\.csv\Engagement_v3.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')

        item_index = {}

        for row in reader:

            #skip the title
            if not ''.join(row).strip():
                print("here")
                continue
            #store each column's index in the dictionary
            if(row[0] == "Engagement Name"):
                for i in range(len(row)):
                    item_index[row[i]] = i
                continue    
                    
                # for k, v in item_index.items():
                #     print(k, v)
            
            remaining_info = Get_Remaining_Engagement_Info(row[item_index["Engagement Id"]])
            
            input_budgeted_hr = float(row[item_index['Budgeted Hours Total']]) 
            budgeted_hr = round(input_budgeted_hr)

            input_planned_hr = float(row[item_index['Planned Hours Total']])
            planned_hr = round(input_planned_hr)

            hr_balance = planned_hr - remaining_info['ActualHours']

            if(row[item_index['Last Time Entry Date']] == ''):
                last_entry_dt = None
                inactive_d = None
            else:    
                last_entry_dt = datetime.strptime(row[item_index['Last Time Entry Date']], '%m/%d/%Y').date()
                delta = date.today() - last_entry_dt
                inactive_d = delta.days

            

            engagement = Engagement(
                engagement_id=row[item_index['Engagement Id']],
                name=row[item_index['Engagement Name']],
                budgeted_hours=budgeted_hr,
                expect_hours=planned_hr,
                actual_hours=remaining_info['ActualHours'], #TBD
                start_date=remaining_info['PlannedStart'], #TBD
                finish_date=remaining_info['PlannedFinish'], #TBD
                last_entry_date=last_entry_dt, 
                hours_balance=hr_balance, #TBD
                inactive_days=inactive_d
            )
            s.add(engagement)

        csv_file.close()

    s.commit()
    s.close()


def Get_Remaining_Engagement_Info(Engagement_Id):

    info_dict = dict.fromkeys(['ActualHours', 'PlannedStart', 'PlannedFinish'])
    info_dict['ActualHours'] = 0
    info_dict['PlannedStart'] = date.today()
    info_dict['PlannedFinish'] = date.today()

    with open(r'C:\Users\Selina\Desktop\tracking_tool_import_data\.csv\Phase_v2.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')

        item_index = {}

        for row in reader:
            
            if(row[0] == "Time - Planned Vs Actual for Active Engmt"):
                continue
            #store each column's index in the dictionary
            if(row[0] == "Workgroup"):
                for i in range(len(row)):
                    item_index[row[i]] = i
                    continue
            
            if(row[item_index['Engagement Number']] == Engagement_Id):
                
                if(row[item_index['ActualHours']] == ''):
                    actual_hr = 0
                else:    
                    input_actual_hr = float(row[item_index['ActualHours']])
                    actual_hr = round(input_actual_hr)

                info_dict['ActualHours'] += actual_hr

                if(info_dict['PlannedStart'] == date.today()) :
                    info_dict['PlannedStart'] = row[item_index['PlannedStart']]
                    info_dict['PlannedFinish'] = row[item_index['PlannedFinish']]

        csv_file.close()
    
    return info_dict
    



# def Read_Engagement():
#     #connect to database
#     engine = create_engine(f'postgresql://{db_user}:{db_pass}@{db_host}/{db_name}')

#     Session = sessionmaker(bind=engine)

#     s = Session()

#     #truncate table before reading data into db to avoid duplicate primary keys
#     s.execute('TRUNCATE TABLE "Engagement"')
#     s.commit()

#     path_of_the_directory = r'C:\Users\Selina\Desktop\tracking_tool_import_data\.csv\Engagement_v2'
#     for filename in os.listdir(path_of_the_directory): #process multiple csv files in the same folder
#         file = "r" + os.path.join(path_of_the_directory, filename)
#         if os.path.isfile(file):
#             sort_csv(file, r'C:\Users\Selina\Desktop\tracking_tool_import_data\.csv\output.csv', ["Engagement Number"])
#             with open(r'C:\Users\Selina\Desktop\tracking_tool_import_data\.csv\output.csv', 'r') as csv_file:
#                 reader = csv.reader(csv_file, delimiter=',')

#                 exist_eng_id = set()
#                 item_index = {}

#                 planned_hr = 0
#                 actual_hr = 0

#                 eng_name = ""
#                 eng_id = 0
#                 planned_start_date = datetime.date.today()
#                 planned_finish_date = datetime.date.today()

#                 for row in reader:
#                     #skip the title
#                     if(row[0] == "Time - Planned Vs Actual for Active Engmt"):
#                         continue
#                     #store each column's index in the dictionary
#                     if(row[0] == "Workgroup"):
#                         for i in range(len(row)):
#                             item_index[row[i]] = i

#                     if 'TAM' not in row[item_index['Engagement Name']]:

#                         #get the engagement id of current row
#                         eng_id = row[item_index['Engagement Number']]

#                         if eng_id not in exist_eng_id:
#                             #add the engagement id into existing_eng_id set if haven't already
#                             exist_eng_id.add(eng_id)

#                             if(eng_name != ""):

#                                 hr_balance = planned_hr - actual_hr

#                                 engagement = Engagement(
#                                     engagement_id=eng_id,
#                                     name=eng_name,
#                                     budgeted_hours=planned_hr,
#                                     expect_hours=planned_hr,
#                                     actual_hours=actual_hr,
#                                     start_date=planned_start_date,
#                                     finish_date=planned_finish_date,
#                                     #last_entry_date=last_entry_dt,
#                                     hours_balance=hr_balance,
#                                     #inactive_days=inactive_d
#                                 )

#                                 s.add(engagement)

#                                 #store the new engagement info if the loop starts processing a new engagement
#                                 eng_name = row[item_index['Engagement Name']]

#                                 input_planned_hr = float(row[item_index['PlannedHours']])
#                                 planned_hr = round(input_planned_hr)

#                                 if(row[item_index['ActualHours']] == ''):
#                                     actual_hr = 0
#                                 else:
#                                     input_actual_hr = float(row[item_index['ActualHours']])
#                                     actual_hr = round(input_actual_hr)

#                                 planned_start_date = row[item_index['PlannedStart']]
#                                 planned_finish_date = row[item_index['PlannedFinish']]
                        
#                         else:
#                             #keep updating the planned and actual hours for existing engagement
#                             input_planned_hr = float(row[item_index['PlannedHours']])
#                             planned_hr += round(input_planned_hr)

#                             if(row[item_index['ActualHours']] == ''):
#                                 actual_hr += 0
#                             else:    
#                                 input_actual_hr = float(row[item_index['ActualHours']])
#                                 actual_hr += round(input_actual_hr)
                    
#                 csv_file.close()

#     s.commit()
#     s.close()

                    


   