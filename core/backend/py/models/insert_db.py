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