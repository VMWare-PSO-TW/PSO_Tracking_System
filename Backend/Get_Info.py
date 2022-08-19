import csv
import pandas as pd

def get_csv_file(excel_filename):
    read_file = pd.read_excel(excel_filename)
    new_filename = excel_filename[:-4] + "csv"
    read_file.to_csv(new_filename, header=0, index=0)
    return new_filename

#Get engagement id by passing engagement name
def get_engagement_id(engagement_name):

    with open(r'C:\Users\Selina\Desktop\tracking_tool_import_data\.csv\Engagements2.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)
        next(reader)

        for row in reader:
            eng_name = row[0].strip()
            if(eng_name == engagement_name.strip()):
                csv_file.close()
                return row[1]
    
    return ""

def get_group_id(task_line):

    with open(r'C:\Users\Selina\Desktop\tracking_tool_import_data\.csv\TaskDistribution.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)

        for row in reader:
            eng_name = row[0]
            break

        csv_file.close()

    eng_id = get_engagement_id(eng_name)
    return "G-" + get_phase_id(eng_id, task_line)


#Get phase id by passing a line of task from an engagement file
def get_phase_id(engagement_id, task_line):

    phase_num = task_line[0][3]

    phase_id = engagement_id + "-0" + phase_num

    return phase_id


def get_member_id(member_name):

    exist_id = {}

    #Read from the member CSV file and write the data into database
    with open(r'C:\Users\Selina\Desktop\tracking_tool_import_data\.csv\My-Team-Sampling.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)
        next(reader)

        for row in reader:
            exist_id[row[0]] = row[1]

        csv_file.close()

        return exist_id[member_name]