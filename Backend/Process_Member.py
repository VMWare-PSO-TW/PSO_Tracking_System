from os import truncate
import pandas as pd
#import pyodbc
import csv
from sys import setrecursionlimit
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import db_host, db_name, db_pass, db_user
from Model.member import Member

def Read_Member():
    #connect to database
    engine = create_engine(f'postgresql://{db_user}:{db_pass}@{db_host}/{db_name}')

    Session = sessionmaker(bind=engine)

    s = Session()

    #truncate table before reading data into db to avoid duplicate primary keys
    s.execute('TRUNCATE TABLE "Member"')
    s.commit()

    #Read from the member CSV file and write the data into database
    with open(r'C:\Users\Selina\Desktop\tracking_tool_import_data\.csv\Phase_v2.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        
        item_index = {}
        exist_member_id = set()

        for row in reader:
            
            if(row[0] == "Time - Planned Vs Actual for Active Engmt"):
                continue
            #store each column's index in the dictionary
            if(row[0] == "Workgroup"):
                for i in range(len(row)):
                    item_index[row[i]] = i
                continue

            if row[item_index['Resource Id']] not in exist_member_id and "Generic" not in row[item_index['Resource']] and row[item_index['Resource Id']] != '':
                exist_member_id.add(row[item_index['Resource Id']])

                role_name = ""
                check_role = row[item_index['Workgroup']]

                #process member roles
                if(check_role.lower().find("consultants") != -1):

                    role_name = "Consultant"
                
                elif(check_role.lower().find("architects") != -1):

                    role_name = "Architect"

                elif(check_role.lower().find("pmo") != -1):

                    role_name = "Project Manager"
                
                elif(check_role.lower().find("managers") != -1):

                    role_name = "Manager"
                
                else:
                    role_name = "Outside of Taiwan"
                

                #process names
                name = row[item_index['Resource']].split(" ")

                if(len(name) > 2):

                    for i in range(len(name) - 1):
                        get_first_name += name[i]
                    
                    get_last_name = name[len(name) - 1]

                else:
                    get_first_name = name[0]
                    get_last_name = name[1]

                member = Member(
                    member_id = row[item_index['Resource Id']],
                    first_name=get_first_name,
                    last_name=get_last_name,
                    role=role_name,
                    employee=True
                )
                s.add(member)

            
    
        csv_file.close()

    s.commit()

    s.close()
    
