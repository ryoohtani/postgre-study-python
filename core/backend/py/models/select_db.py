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