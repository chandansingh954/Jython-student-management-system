import domain
import util

def getTodayStudentAttendence(todayDate,studentIds):
    try:
        instituteId = domain.Teacher.instId  # Logined insitute id
        sql = "select studentId,studentName,date,present from studentattendence where instituteId ='"+str(instituteId)+"' And date='"+str(todayDate)+"' AND studentId IN ("
        for id in studentIds:
            sql = sql+str(id)+","
        sql=sql[:-1]
        sql=sql+" )"
        
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchall() # it return in list of list
        return rows
    except:
        return False
    
def saveStudentAttendence(sa):
    con = util.getCon()
    try:
        instituteId = domain.Teacher.instId # act as foreignKey. domain is package in which Institute is class andwe get static variable instId 
        studentId = getattr(sa, 'studentId')
        studentName = getattr(sa, 'studentName')
        date = getattr(sa, 'date')
        present = getattr(sa, 'present')
        
        
        sql = "insert into studentattendence (studentId,instituteId,studentName,date,present) values ('" + str(studentId) + "','" + str(instituteId) + "','" + str(studentName) + "','"+str(date)+"','"+ str(present) +"')"
        print sql
        cursor = util.getCursor()
        cursor.execute(sql)
        con.commit()
        return True
    except:
        con.rollback()
        return False
 
def updateStudentAttendence(studentId,date,present):
    con = util.getCon()
    try:
        instituteId = domain.Teacher.instId # act as foreignKey. domain is package in which Institute is class andwe get static variable instId 

        sql = "Update studentattendence set present='"+str(present)+"' where instituteId='"+str(instituteId)+"' AND studentId = '"+str(studentId)+"' AND date ='"+str(date)+"'"
        print sql
        cursor = util.getCursor()
        cursor.execute(sql)
        con.commit()
        return True
    except:
        con.rollback()
        return False
 

def getStudentsAttendenceByStudentId(studentIds):
    try:
        instituteId = domain.Institute.instId  # Logined insitute id
        sql = "select studentId,studentName,date,present from studentattendence where instituteId ='"+str(instituteId)+"' And studentId IN ( "
        for id in studentIds:
            sql =sql+str(id)+","
        sql =sql[:-1]
        sql =sql+" )"
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchall() # it return in list of list
        return rows
    except:
        return False

def getStudentsAttendenceByStudentIdInMonth(studentIds,month,year):
    try:
        sql = "select studentId,studentName,date,present from studentattendence where MONTH(date)='"+str(month)+"' AND YEAR(date)='"+str(year)+"'  AND  studentId IN ("
        for id in studentIds:
            sql =sql+str(id)+","
        sql =sql[:-1]
        sql =sql+" )"
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchall() # it return in list of list
        return rows
    except:
        return False
def getAllStudentAttendenceStatisticsInMonth(month,year):
    try:
        instituteId = domain.Institute.instId  # Logined insitute id
        sql =" select t1.studentId,t1.studentName,t1.totaldays,IFNULL(t2.NoOfPresent,0)as NoOfPresent,IFNULL(t3.NoOfAbsent,0) as NoOfAbsent from (select studentId,studentName,count(date) as totaldays from studentattendence  where instituteId='"+str(instituteId)+"' AND MONTH(date) ='"+str(month)+"' AND YEAR(date)='"+str(year)+"' group by studentId,studentName ) as t1 left outer join (select studentId ,count(present) as NoOfPresent  from studentattendence where instituteId='"+str(instituteId)+"' And MONTH(date) ='"+str(month)+"' AND YEAR(date) ='"+str(year)+"' AND present='P' group  by studentId) as t2 on t1.studentId=t2.studentId left outer join (select studentId,count(present) as NoOfAbsent from studentattendence where instituteId ='"+str(instituteId)+"' AND MONTH(date)='"+str(month)+"' AND YEAR(date)='"+str(year)+"' AND present='A' group by studentId ) as t3 on t1.studentId=t3.studentId"
        print sql
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchall() # it return in list of list
        return rows
    except:
        return False
def getStudentsAttendenceStatisticsByStudentIdInMonth(studentIds,month,year): 
    try:
        sql =" select t1.studentId,t1.studentName,t1.totaldays,IFNULL(t2.NoOfPresent,0)as NoOfPresent,IFNULL(t3.NoOfAbsent,0) as NoOfAbsent from (select studentId,studentName,count(date) as totaldays from studentattendence  where  MONTH(date) ='"+str(month)+"' AND YEAR(date)='"+str(year)+"' AND studentId IN ("
        for id in studentIds:
            sql =sql+str(id)+","
        sql =sql[:-1]
        sql =sql+" ) group by studentId,studentName ) as t1 left outer join (select studentId ,count(present) as NoOfPresent  from studentattendence where  MONTH(date) ='"+str(month)+"' AND YEAR(date) ='"+str(year)+"' AND present='P' AND studentId IN ("
        for id in studentIds:
            sql =sql+str(id)+","
        sql =sql[:-1]
        sql =sql+" ) group  by studentId) as t2 on t1.studentId=t2.studentId left outer join (select studentId,count(present) as NoOfAbsent from studentattendence where  MONTH(date)='"+str(month)+"' AND YEAR(date)='"+str(year)+"' AND present='A' AND studentId IN ("
        for id in studentIds:
            sql =sql+str(id)+","
        sql =sql[:-1]
        sql =sql+" ) group by studentId ) as t3 on t1.studentId=t3.studentId"
        print sql
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchall() # it return in list of list
        return rows
    except:
        return False

    
def getSpecificStudentAttendenceInMonth(instituteId,studentName,month,year):
    try:
        sql = "select studentId,studentName,date,present from studentattendence where instituteId ='"+str(instituteId)+"' And MONTH(date)='"+str(month)+"' AND YEAR(date)='"+str(year)+"'  AND  studentName ='"+str(studentName)+"'"
        print sql
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchall() # it return in list of list
        return rows
    except:
        return False
    
def getSpecificStudentAttendenceByStudentId():
    try:
        studentId = domain.Student.studentId  # Logined insitute id
        sql = "select studentId,studentName,date,present from studentattendence where studentId ='"+str(studentId)+"'"
        print sql
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchall() # it return in list of list
        return rows
    except:
        return False
    
def getSpecificStudentAttendencInMonthByStudentId(month,year):    
    try:
        studentId = domain.Student.studentId  # Logined insitute id
        sql = "select studentId,studentName,date,present from studentattendence where studentId ='"+str(studentId)+"' And MONTH(date)='"+str(month)+"' AND YEAR(date)='"+str(year)+"'"
        print sql
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchall() # it return in list of list
        return rows
    except:
        return False