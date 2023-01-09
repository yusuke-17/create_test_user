import textwrap
import datetime
import json
from faker import Faker

def main():
    createJsonFile()
    insertSQL()

def getFakerData():
    fake = Faker('jp-JP')
    first_name = fake.first_name()
    last_name = fake.last_name()
    login_email = fake.email()
    password = fake.password()
    return first_name, last_name, login_email, password

def createJsonFile():
    f_name, l_name, mail, password = getFakerData()
    json_dict = {'first_name': f_name, 'last_name': l_name, 'login_email': mail, 'password': password}
    dt_now = datetime.datetime.now()
    with open('./test_data/test_data_' + dt_now.strftime('%Y%m%d_%H%M%S') + '.json', 'w') as f:
        json.dump(json_dict, f, ensure_ascii=False)

def insertSQL():
    f_name, l_name, mail, password = getFakerData()
    dt_now = datetime.datetime.now()
    s = "INSERT INTO 'receipts' VALUE ('{}', '{}')".format(f_name, l_name)
    with open('./test_data/test_sql_' + dt_now.strftime('%Y%m%d_%H%M%S') + '.sql', 'w') as f:
        f.write(s)

if __name__ == '__main__':
    main()