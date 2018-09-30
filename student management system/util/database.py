from com.ziclix.python.sql import zxJDBC
import os
import sys
from java.util import Properties
sys.path.append('/root/Desktop/mysql-connector-java-5.1.42.jar')
import com.mysql.jdbc.Driver as Driver
props =Properties()
props.put('user','root')
props.put('password','avinash')
mysqlCon =zxJDBC.connect(Driver().connect('jdbc:mysql://localhost/inst_mang',props))
def getCon():
    return mysqlCon
cursor = mysqlCon.cursor()
def getCursor():
	return cursor
