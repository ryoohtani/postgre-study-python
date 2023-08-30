from setting import session
from create_db import DbTbl

Session = session()

deltbl = DbTbl

delcode = Session.query(deltbl).filter_by(EMPLOYEE_CODE = "s005").delete()

Session.commit()
Session.close()