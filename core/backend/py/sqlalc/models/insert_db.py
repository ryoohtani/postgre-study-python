from setting import session
from create_db import DbTbl

Session = session()

Session.add(DbTbl(EMPLOYEE_CODE = "s001", POSITION_NO = "1", GENDER = "男", BASE_SALARY = "210000", DATE_OF_HIRE = "2023-8-01"))
Session.add(DbTbl(EMPLOYEE_CODE = "s002", POSITION_NO = "2", GENDER = "女", BASE_SALARY = "220000", DATE_OF_HIRE = "2023-8-10"))
Session.add(DbTbl(EMPLOYEE_CODE = "s003", POSITION_NO = "3", GENDER = "男", BASE_SALARY = "230000", DATE_OF_HIRE = "2023-8-15"))
Session.add(DbTbl(EMPLOYEE_CODE = "s004", POSITION_NO = "4", GENDER = "男", BASE_SALARY = "240000", DATE_OF_HIRE = "2023-8-20"))

Session.commit()
Session.close()