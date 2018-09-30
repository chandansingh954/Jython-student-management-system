from javax.swing import JOptionPane
import domain
import util
def getTodayAttendence(todayDate):
    try:
        instituteId = domain.Institute.instId  # Logined insitute id
        sql = "select teacherId,teacherName,date,present from teacherattendence where instituteId ='"+str(instituteId)+"' And date='"+str(todayDate)+"'" 
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchall() # it return in list of list
        return rows
    except:
        return False
    
def saveTeacherAttendence(ta):
    con = util.getCon()
    try:
        instituteId = domain.Institute.instId # act as foreignKey. domain is package in which Institute is class andwe get static variable instId 
        teacherId = getattr(ta, 'teacherId')
        teacherName = getattr(ta, 'teacherName')
        date = getattr(ta, 'date')
        present = getattr(ta, 'present')
        
        
        sql = "insert into teacherattendence (teacherId,instituteId,teacherName,date,present) values ('" + str(teacherId) + "','" + str(instituteId) + "','" + str(teacherName) + "','"+str(date)+"','"+ str(present) +"')"
        print sql
        cursor = util.getCursor()
        cursor.execute(sql)
        con.commit()
        return True
    except:
        con.rollback()
        return False
 
def updateTeacherAttendence(teacherId,date,present):
    con = util.getCon()
    try:
        instituteId = domain.Institute.instId # act as foreignKey. domain is package in which Institute is class andwe get static variable instId 

        sql = "Update teacherattendence set present='"+str(present)+"' where instituteId='"+str(instituteId)+"' AND teacherId = '"+str(teacherId)+"' AND date ='"+str(date)+"'"
        print sql
        cursor = util.getCursor()
        cursor.execute(sql)
        con.commit()
        return True
    except:
        con.rollback()
        return False
 
def getSpecificTeacherAttendence(teacherName):
    try:
        instituteId = domain.Institute.instId  # Logined insitute id
        sql = "select teacherId,teacherName,date,present from teacherattendence where instituteId ='"+str(instituteId)+"' And teacherName='"+str(teacherName)+"'" 
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchall() # it return in list of list
        return rows
    except:
        return False
    
def getAllTeacherAttendenceInMonth(month,year):
    try:
        instituteId = domain.Institute.instId  # Logined insitute id
        sql = "select teacherId,teacherName,date,present from teacherattendence where instituteId ='"+str(instituteId)+"' And MONTH(date)='"+str(month)+"' AND  YEAR(date)='"+str(year)+"'" 
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchall() # it return in list of list
        return rows
    except:
        return False
    
    
def getSpecificTeacherAttendenceInMonth(teacherName,month,year):    
    try:
        instituteId = domain.Institute.instId  # Logined insitute id
        sql = "select teacherId,teacherName,date,present from teacherattendence where instituteId ='"+str(instituteId)+"' And teacherName='"+str(teacherName)+"' AND MONTH(date)='"+str(month)+"' AND  YEAR(date)='"+str(year)+"'" 
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchall() # it return in list of list
        return rows
    except:
        return False
    
def getAllTeacherAttendenceStatisticsInMonth(month,year):
    try:
        instituteId = domain.Institute.instId  # Logined insitute id
        sql =" select t1.teacherId,t1.teacherName,t1.totaldays,IFNULL(t2.NoOfPresent,0)as NoOfPresent,IFNULL(t3.NoOfAbsent,0) as NoOfAbsent from (select teacherId,teacherName,count(date) as totaldays from teacherattendence  where instituteId='"+str(instituteId)+"' AND MONTH(date) ='"+str(month)+"' AND YEAR(date)='"+str(year)+"' group by teacherId,teacherName ) as t1 left outer join (select teacherId ,count(present) as NoOfPresent  from teacherattendence where instituteId='"+str(instituteId)+"' And MONTH(date) ='"+str(month)+"' AND YEAR(date) ='"+str(year)+"' AND present='P' group  by teacherId) as t2 on t1.teacherId=t2.teacherId left outer join (select teacherId,count(present) as NoOfAbsent from teacherattendence where instituteId ='"+str(instituteId)+"' AND MONTH(date)='"+str(month)+"' AND YEAR(date)='"+str(year)+"' AND present='A' group by teacherId ) as t3 on t1.teacherId=t3.teacherId"
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchall() # it return in list of list
        return rows
    except:
        return False

def getSpecificTeacherAttendenceByTeacherId():    
    try:
        instituteId = domain.Teacher.instId  # Logined insitute id
        teacherId = domain.Teacher.teacherId  # Logined insitute id
        sql = "select teacherId,teacherName,date,present from teacherattendence where instituteId ='"+str(instituteId)+"' And teacherId='"+str(teacherId)+"'" 
        print sql
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchall() # it return in list of list
        return rows
    except:
        return False
def getSpecificTeacherAttendenceByTeacherIdInMonth(month,year):
    try:
        instituteId = domain.Teacher.instId  # Logined insitute id
        teacherId = domain.Teacher.teacherId  # Logined insitute id
        sql = "select teacherId,teacherName,date,present from teacherattendence where instituteId ='"+str(instituteId)+"' And teacherId='"+str(teacherId)+"' AND MONTH(date) ='"+str(month)+"' AND YEAR(date)='"+str(year)+"'" 
        print sql
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchall() # it return in list of list
        return rows
    except:
        return False