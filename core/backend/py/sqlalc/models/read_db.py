from setting import session
from create_db import DbTbl
from create_db import DbTbl2

Session = session()

records = Session.query(DbTbl).all()
for record in records:
    print(record.EMPLOYEE_CODE, record.POSITION_NO, record.GENDER, record.BASE_SALARY, record.DATE_OF_HIRE)


records2 = Session.query(DbTbl2).all()
for record2 in records2:
    print(record2.EMPLOYEE_CODE, record2.EMPLOYEE_NAME, record2.COUNTRY, record2.COUNTRY_NO, record2.ENROLLMENT_ID)


dbtbl_joins = Session.query(DbTbl, DbTbl2).join(DbTbl2, DbTbl.EMPLOYEE_CODE == DbTbl2.EMPLOYEE_CODE).all()
for record, record2 in dbtbl_joins:
    print(record.EMPLOYEE_CODE, record.GENDER, record2.EMPLOYEE_NAME, record2.COUNTRY)

Session.close()