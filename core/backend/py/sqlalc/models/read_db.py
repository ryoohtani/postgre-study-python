from setting import session
from create_db import DbTbl

Session = session()

records = Session.query(DbTbl).all()

for record in records:
    print(record.EMPLOYEE_CODE, record.POSITION_NO, record.GENDER, record.BASE_SALARY, record.DATE_OF_HIRE)

Session.close()