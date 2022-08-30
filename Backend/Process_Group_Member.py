import csv
import os
from sys import setprofile, setrecursionlimit
from unicodedata import name
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import db_host, db_name, db_pass, db_user
from Model.group_member import GroupMember
from Get_Info import get_group_id, check_member_id, get_engagement_id


def Read_Group_Member():
    #connect to database
    engine = create_engine(f'postgresql://{db_user}:{db_pass}@{db_host}/{db_name}')

    Session = sessionmaker(bind=engine)

    s = Session()

    #truncate table before reading data into db to avoid duplicating primary keys
    s.execute('TRUNCATE TABLE "GroupMember"')
    s.commit()
    
    with open(r'C:\Users\Selina\Desktop\tracking_tool_import_data\.csv\Phase_v2.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')

        item_index = {}
        exist_eng_id = set()

        for row in reader:
            if(row[0] == "Time - Planned Vs Actual for Active Engmt" or row[0] == None):
                continue
            #store each column's index in the dictionary
            if(row[0] == "Workgroup"):
                for i in range(len(row)):
                    item_index[row[i]] = i
                continue

            #Check to avoid processing the same id again
            if(row[item_index['Engagement Number']] not in exist_eng_id):

                exist_eng_id.add(row[item_index['Engagement Number']])

                original_task_name = row[item_index['Task']]

                #if the engagement contains phases
                if ('MS' in row[item_index['Task']]):

                    group_rows = get_engagement_rows(row[item_index['Engagement Number']], item_index)

                    for i in group_rows:
                        #process expected hours
                        if(i[item_index['PlannedHours']] == ''):
                            expect_hr = 0
                        else:    
                            planned_hr = float(i[item_index['PlannedHours']].replace(',', ''))
                            expect_hr = round(planned_hr)
                    
                        #process actual hours
                        if(i[item_index['ActualHours']] == ''):
                            actual_hr = 0
                        else:    
                            actual_hr = round(float(i[item_index['ActualHours']].replace(',', '')))
                        
                        get_phase_index = i[item_index['Task']].replace(' ', '').lower().find("phase")
                        get_phase = i[item_index['Task']].replace(' ', '').lower()[get_phase_index + 5]
                        pound_sign_index = i[item_index['Task']].replace(' ', '').find("#")
                        
                        phase_count = 0

                        if(get_phase_index != -1):
                            phase_count = get_phase
                        else:
                            phase_count = row[item_index['Task']].replace(' ', '')[pound_sign_index + 1]

                        groupMember = GroupMember (
                            group_id="G-" + i[item_index['Engagement Number']] + "-0" + phase_count,
                            member_id=i[item_index['Resource Id']],
                            expect_hours=planned_hr,
                            actual_hours=actual_hr,
                            engagement_id=i[item_index['Engagement Number']],
                            phase_name="MS" + phase_count
                        )
                        s.add(groupMember)

                #if the engagement is short-term
                else:

                    short_group_rows = get_engagement_rows(row[item_index['Engagement Number']], item_index)
                    
                    for k in short_group_rows:
                        
                        #process expected hours
                        if(k[item_index['PlannedHours']] == ''):
                            expect_hr = 0
                        else:    
                            planned_hr = float(k[item_index['PlannedHours']].replace(',', ''))
                            expect_hr = round(planned_hr)
                    
                        #process actual hours
                        if(k[item_index['ActualHours']] == ''):
                            actual_hr = 0
                        else:    
                            actual_hr = round(float(k[item_index['ActualHours']].replace(',', '')))

                        groupMember = GroupMember (
                            group_id="G-" + k[item_index['Engagement Number']] + "-00",
                            member_id=k[item_index['Resource Id']],
                            expect_hours=expect_hr,
                            actual_hours=actual_hr,
                            engagement_id=k[item_index['Engagement Number']],
                            phase_name=k[item_index['Task']]
                        )
                        s.add(groupMember)                

        csv_file.close()

    s.commit()

    s.close()


def get_engagement_rows(engagement_number, item_index):

    result_list = []

    with open(r'C:\Users\Selina\Desktop\tracking_tool_import_data\.csv\Phase_v2.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')

        for row in reader:

            if(row[0] == "Time - Planned Vs Actual for Active Engmt" or row[0] == None or row[0] == "Workgroup"):
                continue

            if((row[item_index['Engagement Number']] == engagement_number) and (row[item_index['Resource Id']] != '') and (row[item_index['Resource Id']] != None)):
                result_list.append(row)
        
        csv_file.close()
    
    return result_list





#skip the first few lines
                # for i in range(2):
                #     next(reader)

                # for row in reader:
                    
                #     if((check_member_id(row[2]) != False) and (row[3].find("TAM") == -1)):

                #         gp_id = get_group_id(row)
                #         eng_id = gp_id.split("-")[1]

                #         # if(row[1].find("Generic") != -1):
                #         #     member_id_query = 0
                #         # else:
                #         #     member_id_query = row[2]

                #         if(gp_id[-1] != '0'):
                #             phase_name_query = "MS" + gp_id[-1]
                #         else:
                #             phase_name_query = row[13]

                #         input_planned_hr = float(row[8])
                #         expect_hr = round(input_planned_hr)

                #         if(row[10] != ""):
                #             input_actual_hr = float(row[10])
                #             actual_hr = round(input_actual_hr)
                        
                #         else:
                #             actual_hr = 0

                #         group_member = GroupMember(
                #             engagement_id=eng_id.strip(),
                #             group_id=gp_id,
                #             member_id=row[2],
                #             phase_name=phase_name_query,
                #             expect_hours=expect_hr,
                #             actual_hours=actual_hr
                #         )
                #         s.add(group_member)
