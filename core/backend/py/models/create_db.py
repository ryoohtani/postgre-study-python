# from models.connector_db import DbConnecotor

class DbCreate(object):
    def __init__(self, basic_data):
        self.basic_data = basic_data

    def learning_table(self):
        cleate_learning_table = """
            CREATE TABLE IF NOT EXISTS learning_table(
                EMPLOYEE_CODE varchar(10) NOT NULL,
                POSITION_NO varchar(5) NOT NULL,
                GENDER varchar(1),
                BASE_SALARY int,
                DATE_OF_HIRE date,
                PRIMARY KEY(EMPLOYEE_CODE)
            )
        """
        self.basic_data.cursor.execute(cleate_learning_table)
        self.basic_data.psyconnect.commit()