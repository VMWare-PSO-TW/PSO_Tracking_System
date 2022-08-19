import csv
import datetime #temp import
from sys import setprofile, setrecursionlimit
from unicodedata import name
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import db_host, db_name, db_pass, db_user
from Model.phase import Phase
from Get_Info import get_engagement_id, get_phase_id, get_csv_file


#Get engagement id by passing engagement name
def get_start_date(engagement_name):

    with open(r'C:\Users\Selina\Desktop\tracking_tool_import_data\.csv\Engagements2.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)
        next(reader)

        for row in reader:
            eng_name = row[0].strip()
            if(eng_name == engagement_name.strip()):
                return row[3]
    
        csv_file.close()
    return ""



def Read_Phase():

    #connect to database
    engine = create_engine(f'postgresql://{db_user}:{db_pass}@{db_host}/{db_name}')

    Session = sessionmaker(bind=engine)

    s = Session()

    #truncate table before reading data into db to avoid duplicate primary keys
    s.execute('TRUNCATE TABLE "Phase"')
    s.commit()
    
    #Read from the member CSV file and write the data into database
    with open(r'C:\Users\Selina\Desktop\tracking_tool_import_data\.csv\TaskDistribution.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')

        next(reader)

        line_num = 1
        eng_id = 0
        eng_name = ""
        phase_counter = 1

        for row in reader:
            
            line_num += 1

            if line_num == 2: #temp 
                eng_id = get_engagement_id(row[0]) #temp
                eng_name = row[0]
                continue

            if line_num == 3 or line_num == 4:  #temp
                continue  #temp
            
            if(int(row[0][3]) == phase_counter):
                

                input_planned_hr = float(row[2])
                planned_hr = round(input_planned_hr)

                input_actual_hr = float(row[4])
                actual_hr = round(input_actual_hr)

                p_id = get_phase_id(eng_id, row)

                phase = Phase (
                    phase_id=p_id,
                    engagement_id=eng_id,
                    group_id= "G-" + p_id,
                    name=row[0],
                    step=row[0][3],
                    expect_hours=planned_hr,
                    actual_hours=actual_hr
                )
                s.add(phase)
                phase_counter += 1

        csv_file.close()

    s.commit()

    s.close()
    
