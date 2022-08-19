import csv
import datetime #temp import
from sys import setprofile, setrecursionlimit
from unicodedata import name
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import db_host, db_name, db_pass, db_user
from Model.group_member import GroupMember
from Get_Info import get_group_id, get_member_id, get_engagement_id


def Read_Group_Member():
    #connect to database
    engine = create_engine(f'postgresql://{db_user}:{db_pass}@{db_host}/{db_name}')

    Session = sessionmaker(bind=engine)

    s = Session()

    #truncate table before reading data into db to avoid duplicate primary keys
    s.execute('TRUNCATE TABLE "GroupMember"')
    s.commit()
    
    with open(r'C:\Users\Selina\Desktop\tracking_tool_import_data\.csv\TaskDistribution.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')

        #skip the first few lines
        for i in range(4):
            next(reader)

        for row in reader:

            gp_id = get_group_id(row)
            eng_id = gp_id.split("-")[1]


            group_member = GroupMember(
                engagement_id=eng_id,
                group_id=gp_id,
                member_id=get_member_id(row[1]),
                expect_hours=row[2],
                actual_hours=row[4]
            )
            s.add(group_member)
            
        csv_file.close()

    s.commit()

    s.close()
                
            

            

            
