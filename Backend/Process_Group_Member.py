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
    
    path_of_the_directory = r'C:\Users\Selina\Desktop\tracking_tool_import_data\.csv\Engagement_v2'
    for filename in os.listdir(path_of_the_directory): #process multiple csv files in the same folder
        file = os.path.join(path_of_the_directory, filename)
        if os.path.isfile(file):
            with open(file, 'r') as csv_file:
                reader = csv.reader(csv_file, delimiter=',')

                #skip the first few lines
                for i in range(2):
                    next(reader)

                for row in reader:
                    
                    if((check_member_id(row[2]) != False) and (row[3].find("TAM") == -1)):

                        gp_id = get_group_id(row)
                        eng_id = gp_id.split("-")[1]

                        # if(row[1].find("Generic") != -1):
                        #     member_id_query = 0
                        # else:
                        #     member_id_query = row[2]

                        if(gp_id[-1] != '0'):
                            phase_name_query = "MS" + gp_id[-1]
                        else:
                            phase_name_query = row[13]

                        input_planned_hr = float(row[8])
                        expect_hr = round(input_planned_hr)

                        if(row[10] != ""):
                            input_actual_hr = float(row[10])
                            actual_hr = round(input_actual_hr)
                        
                        else:
                            actual_hr = 0

                        group_member = GroupMember(
                            engagement_id=eng_id.strip(),
                            group_id=gp_id,
                            member_id=row[2],
                            phase_name=phase_name_query,
                            expect_hours=expect_hr,
                            actual_hours=actual_hr
                        )
                        s.add(group_member)


                csv_file.close()

            s.commit()

            s.close()
    
            
