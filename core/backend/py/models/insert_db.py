class DbInsert(object):
    def __init__(self, basic_data):
        self.basic_data = basic_data

    def insert_data(self):
        insert_employee_code = ['s001', 's002', 's003', 's004']

        delete_employee = """
            delete from learning_table where EMPLOYEE_CODE = %s
        """

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

        for in_employee_code in insert_employee_code:
            self.basic_data.cursor.execute(delete_employee, (in_employee_code,))
            self.basic_data.psyconnect.commit()

        for in_employee_info in employee_info:
            self.basic_data.cursor.execute(insert_employee, in_employee_info)
            self.basic_data.psyconnect.commit()

    def insert_subdata(self):
        subid_employee_code = ['s001', 's002', 's003', 's004']

        delet_subemployee = """
            delete from subid_table where EMPLOYEE_CODE = %s
        """

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
        for employee_code in subid_employee_code:
            self.basic_data.cursor.execute(delet_subemployee, (employee_code,))
            self.basic_data.psyconnect.commit()
        
        for subemployee in subemployee_info:
            self.basic_data.cursor.execute(insert_subemployee, subemployee)
            self.basic_data.psyconnect.commit()