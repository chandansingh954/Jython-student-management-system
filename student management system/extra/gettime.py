from java.util import Date
d = Date()
from java.sql import Date
def getDate():
    sqlDate = Date(d.getYear(),d.getMonth(),d.getDate())
    return sqlDate