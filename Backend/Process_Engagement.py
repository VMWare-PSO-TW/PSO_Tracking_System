import csv
import datetime #temp import
from sys import setrecursionlimit
from xmlrpc.client import DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import db_host, db_name, db_pass, db_user
from Model.engagement import Engagement
from Get_Info import get_csv_file

def Read_Engagement():
    #connect to database
    engine = create_engine(f'postgresql://{db_user}:{db_pass}@{db_host}/{db_name}')

    Session = sessionmaker(bind=engine)

    s = Session()

    #truncate table before reading data into db to avoid duplicate primary keys
    s.execute('TRUNCATE TABLE "Engagement"')
    s.commit()


    #Read from the member CSV file and write the data into database
    with open(r'C:\Users\Selina\Desktop\tracking_tool_import_data\.csv\Engagements2.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)
        next(reader)

        for row in reader:

            input_budgeted_hr = float(row[2])
            budgeted_hr = round(input_budgeted_hr)

            input_planned_hr = float(row[3])
            planned_hr = round(input_planned_hr)

            input_actual_hr = float(row[10])
            actual_hr = round(input_actual_hr)

            input_internal_hr = float(row[7])
            internal_hr = round(input_internal_hr)

            input_subb_hr = float(row[8])
            subb_hr = round(input_subb_hr)

            current_qtr_planned_hr = row[5]
            if(current_qtr_planned_hr == ""):
                current_qtr_planned_hr = 0

            forecast_hr_this_qt = row[6]
            if(forecast_hr_this_qt == ""):
                forecast_hr_this_qt = 0
            else:
                forecast_hr_this_qt = round(float(forecast_hr_this_qt))

            input_hr_balance = float(row[11])
            hr_balance = round(input_hr_balance)

            input_inactive_days = float(row[12])
            inactive_d = round(input_inactive_days)

            last_entry_dt = row[9]
            if(last_entry_dt == ''):
                last_entry_dt = None

            engagement = Engagement(
                engagement_id=row[1],
                name=row[0],
                budgeted_hours=budgeted_hr,
                expect_hours=planned_hr,
                actual_hours=actual_hr,
                internal_hours=internal_hr,
                subb_hours=subb_hr,
                current_qtr_planned_hours=current_qtr_planned_hr,
                forecast_hours_this_qtr=forecast_hr_this_qt,
                start_date=row[4],
                last_entry_date=last_entry_dt,
                hours_balance=hr_balance,
                inactive_days=inactive_d
            )
            s.add(engagement)

        csv_file.close()

    s.commit()
    s.close()

