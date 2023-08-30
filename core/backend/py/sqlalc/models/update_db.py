from setting import session
from create_db import DbTbl

Session = session()

dbup = Session.query(DbTbl).all()

if len(dbup) >= 4:
    dbup_to_update = dbup[3]
    dbup_to_update.EMPLOYEE_CODE = "s005"


Session.commit()
Session.close()