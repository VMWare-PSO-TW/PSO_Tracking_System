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
    with open(r'C:\Users\Selina\Desktop\tracking_tool_import_data\.csv\My-Team-Sampling.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)
        next(reader)

        for row in reader:

            member = Member(
                member_id = row[1],
                first_name=row[0].split(" ")[0],
                last_name=row[0].split(" ")[1],
                role=row[2],
                employee=True
            )
            s.add(member)
    
        csv_file.close()

    s.commit()

    s.close()
    
