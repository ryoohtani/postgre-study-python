from setting import session
from create_db import DbTbl
from create_db import DbTbl2

Session = session()

learning_date = [
    ("s001", "1", "男", "210000", "2023-8-01"),
    ("s002", "2", "女", "220000", "2023-8-10"),
    ("s003", "3", "男", "230000", "2023-8-15"),
    ("s004", "4", "男", "240000", "2023-8-20")
]

for enployee, position, gender, base, dateof in learning_date:
    dbtbl = Session.query(DbTbl).filter_by(EMPLOYEE_CODE = enployee).first()
    if dbtbl is None:
        dbtbl1 = DbTbl()
        dbtbl1.EMPLOYEE_CODE = enployee
        dbtbl1.POSITION_NO = position
        dbtbl1.GENDER = gender
        dbtbl1.BASE_SALARY = int(base)
        dbtbl1.DATE_OF_HIRE = dateof
        Session.add(dbtbl1)


subid_date = [
    ("s001", "井上尚弥", "JP", "21", "134"),
    ("s002", "朝倉カンナ", "JP", "21", "123"),
    ("s003", "グレゴリアン", "ARM", "10", "200"),
    ("s004", "マクレガー", "IRL", "2", "300")
]

for enployee2, empname, country, countryno, enid in subid_date:
    dbtbl2 = Session.query(DbTbl2).filter_by(EMPLOYEE_CODE = enployee2).first()
    if dbtbl2 is None:
        dbtbl2 = DbTbl2()
        dbtbl2.EMPLOYEE_CODE = enployee2
        dbtbl2.EMPLOYEE_NAME = empname
        dbtbl2.COUNTRY = country
        dbtbl2.COUNTRY_NO = int(countryno)
        dbtbl2.ENROLLMENT_ID = int(enid)
        Session.add(dbtbl2)

Session.commit()
Session.close()