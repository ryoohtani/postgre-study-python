class DbSelect(object):
    def __init__(self, basic_data):
        self.basic_data = basic_data
    
    def select_data(self):
        select_learning_table = """
            select * from learning_table
        """
        self.basic_data.cursor.execute(select_learning_table)
        select_learning = self.basic_data.cursor.fetchall()
        for select_cli in select_learning:
            print(select_cli) 
        
    def select_data2(self):
        select_subid_table = """
            select * from subid_table
        """
        self.basic_data.cursor.execute(select_subid_table)
        select_subid = self.basic_data.cursor.fetchall()
        for select_cli2 in select_subid:
            print(select_cli2)

    def select_data_join(self):
        select_join_table = """
            select lt.GENDER, st.EMPLOYEE_NAME, st.COUNTRY 
            from learning_table as lt 
            join subid_table as st on lt.EMPLOYEE_CODE = st.EMPLOYEE_CODE 
            where lt.EMPLOYEE_CODE in ('s001', 's002');
        """
        self.basic_data.cursor.execute(select_join_table)
        select_join = self.basic_data.cursor.fetchall()
        for select_cli3 in select_join:
            print(select_cli3)