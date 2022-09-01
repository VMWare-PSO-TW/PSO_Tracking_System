from cmath import phase
import csv
import datetime #temp import
from sys import setprofile, setrecursionlimit
from unicodedata import name
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import db_host, db_name, db_pass, db_user
from Model.phase import Phase
from Get_Info import get_engagement_id, get_phase_id, get_csv_file


def Read_Phase():

    #connect to database
    engine = create_engine(f'postgresql://{db_user}:{db_pass}@{db_host}/{db_name}')

    Session = sessionmaker(bind=engine)

    s = Session()

    #truncate table before reading data into db to avoid duplicate primary keys
    s.execute('TRUNCATE TABLE "Phase"')
    s.commit()
    
    #Read from the member CSV file and write the data into database
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
            if row[item_index['Engagement Number']] not in exist_eng_id:

                exist_eng_id.add(row[item_index['Engagement Number']])

                original_task_name = row[item_index['Task']]
                
                phase_counter = 1

                #if the engagement contains phases
                if 'MS' in row[item_index['Task']].replace(" ", ""):
                    
                    while phase_counter <= 4:

                        phase_detail = get_phase_details(row[item_index['Engagement Number']], phase_counter, item_index)

                        phase = Phase (
                            phase_id=phase_detail['phase_id'],
                            engagement_id=phase_detail['engagement_id'],
                            group_id= phase_detail['group_id'],
                            name=phase_detail['name'],
                            step=phase_detail['step'],
                            expect_hours=phase_detail['expect_hours'],
                            actual_hours=phase_detail['actual_hours']
                        )
                        s.add(phase)
                        phase_counter += 1

                #if the engagement is short-term
                else:

                    eng_details = get_short_term_engagement_details(row[item_index['Engagement Number']], item_index)
                    phase = Phase (
                            phase_id=eng_details['phase_id'],
                            engagement_id=eng_details['engagement_id'],
                            group_id=eng_details['group_id'],
                            name=eng_details['name'],
                            step=eng_details['step'],
                            expect_hours=eng_details['expect_hours'],
                            actual_hours=eng_details['actual_hours']
                        )
                    s.add(phase)

        csv_file.close()

    s.commit()

    s.close()
    

def get_phase_details(engagement_number, phase_number, item_index):

    phase_details = dict.fromkeys(['phase_id', 'engagement_id', 'group_id', 'name', 'step', 'expect_hours', 'actual_hours'])

    phase_details['phase_id'] = engagement_number + "-0" + str(phase_number)
    phase_details['group_id'] = "G-" + engagement_number + "-0" + str(phase_number)
    phase_details['engagement_id'] = engagement_number
    phase_details['step'] = phase_number
    phase_details['expect_hours'] = 0
    phase_details['actual_hours'] = 0
    phase_details['name'] = ''

    
    with open(r'C:\Users\Selina\Desktop\tracking_tool_import_data\.csv\Phase_v2.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')

        for row in reader:

            if(row[0] == "Time - Planned Vs Actual for Active Engmt" or row[0] == None or row[0] == "Workgroup"):
                continue
            
            task_name = row[item_index['Task']]

            if(row[item_index['Engagement Number']] == engagement_number):
                
                get_phase_index = row[item_index['Task']].replace(' ', '').lower().find("phase")
                get_phase = row[item_index['Task']].replace(' ', '').lower()[get_phase_index + 5]
                pound_sign_index = row[item_index['Task']].replace(' ', '').find("#")

                #when the engagement contains phases
                if(get_phase != "-1" and (get_phase == str(phase_number) or row[item_index['Task']].replace(' ', '')[pound_sign_index + 1] == str(phase_number))):

                    if(phase_details['name'] == ''):
                        phase_details['name'] = "MS" + str(phase_number)  
                    
                    #process expected hours
                    if(row[item_index['PlannedHours']] == ''):
                        phase_details['expect_hours'] += 0
                    else:    
                        planned_hr = float(row[item_index['PlannedHours']].replace(',', ''))
                        phase_details['expect_hours'] += round(planned_hr)
                
                    #process actual hours
                    if(row[item_index['ActualHours']] == ''):
                        phase_details['actual_hours'] += 0
                    else:    
                        actual_hr = round(float(row[item_index['ActualHours']].replace(',', '')))
                        phase_details['actual_hours'] += actual_hr


        csv_file.close()
                    

    return phase_details
            

def get_short_term_engagement_details(engagement_number, item_index):

    eng_details = dict.fromkeys(['phase_id', 'engagement_id', 'group_id', 'name', 'step', 'expect_hours', 'actual_hours'])

    eng_details['phase_id'] = engagement_number + "-00"
    eng_details['group_id'] = "G-" + engagement_number + "-00"
    eng_details['engagement_id'] = engagement_number
    eng_details['step'] = 0
    eng_details['expect_hours'] = 0
    eng_details['actual_hours'] = 0
    eng_details['name'] = ''

    with open(r'C:\Users\Selina\Desktop\tracking_tool_import_data\.csv\Phase_v2.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')

        for row in reader:

            if(row[0] == "Time - Planned Vs Actual for Active Engmt" or row[0] == None or row[0] == "Workgroup"):
                continue
            
            if(row[item_index['Engagement Number']] == engagement_number):

                if(eng_details['name'] == ''):
                    eng_details['name'] = row[item_index['Engagement Name']]
                
                #process expected hours
                if(row[item_index['PlannedHours']] == ''):
                    eng_details['expect_hours'] += 0
                else:    
                    planned_hr = float(row[item_index['PlannedHours']].replace(',', ''))
                    eng_details['expect_hours'] += round(planned_hr)
                
                #process actual hours
                if(row[item_index['ActualHours']] == ''):
                    eng_details['actual_hours'] += 0
                else:    
                    actual_hr = round(float(row[item_index['ActualHours']].replace(',', '')))
                    eng_details['actual_hours'] += actual_hr


        csv_file.close()
    
    return eng_details

        # line_num += 1

        # if line_num == 2: #temp 
        #     eng_id = get_engagement_id(row[0]) #temp
        #     eng_name = row[0]
        #     continue

        # if line_num == 3 or line_num == 4:  #temp
        #     continue  #temp
        
        # if(int(row[0][3]) == phase_counter):
            

        #     input_planned_hr = float(row[2])
        #     planned_hr = round(input_planned_hr)

        #     input_actual_hr = float(row[4])
        #     actual_hr = round(input_actual_hr)

        #     p_id = get_phase_id(eng_id, row)

        #     phase = Phase (
        #         phase_id=p_id,
        #         engagement_id=eng_id,
        #         group_id= "G-" + p_id,
        #         name=row[0],
        #         step=row[0][3],
        #         expect_hours=planned_hr,
        #         actual_hours=actual_hr
        #     )
        #     s.add(phase)
        #     phase_counter += 1