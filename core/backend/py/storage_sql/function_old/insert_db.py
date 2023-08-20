# 複数同時にデータの挿入をexecutemanyで行う。データを消さないと再度挿入できないコードの記載なので注意
class DbInsert(object):
    def __init__(self, basic_data):
        self.basic_data = basic_data

    def insert_data(self):

        insert_employee = """
            insert into learning_table (
                EMPLOYEE_CODE, POSITION_NO, GENDER, BASE_SALARY, DATE_OF_HIRE
            ) values (%s, %s, %s, %s, %s)
        """

        employee_info = [
            ('s001', '1', '男', '210000', '2023-8-01'),
            ('s002', '2', '女', '220000', '2023-8-10'),
            ('s003', '3', '男', '230000', '2023-8-15'),
            ('s004', '4', '男', '240000', '2023-8-20')
        ]
        self.basic_data.cursor.executemany(insert_employee, employee_info)
        self.basic_data.psyconnect.commit()

    def insert_subdata(self):
        insert_subemployee = """
            insert into subid_table (
                EMPLOYEE_CODE, EMPLOYEE_NAME, COUNTRY, COUNTRY_NO, ENROLLMENT_ID
            ) values (%s, %s, %s, %s, %s)
        """

        subemployee_info = [
            ('s001', '井上尚弥', 'JP', '21', '134'),
            ('s002', '朝倉カンナ', 'JP', '21', '123'),
            ('s003', 'グレゴリアン', 'ARM', '10', '200'),
            ('s004', 'マクレガー', 'IRL', '2', '300')
        ]
        self.basic_data.cursor.executemany(insert_subemployee, subemployee_info)
        self.basic_data.psyconnect.commit()