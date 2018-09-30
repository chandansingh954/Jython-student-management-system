from javax.swing import JOptionPane
import domain
import util
def addCourseService(courseObj):
    con = util.getCon()
    try:
        instituteId = domain.Institute.instId # act as foreignKey. domain is package in which Institute is class andwe get static variable instId 
        courseName = getattr(courseObj, 'courseName')
        courseId = getattr(courseObj, 'courseId')
        courseFee = getattr(courseObj, 'courseFee')
        sql = sql+"insert into course" 
        sql=sql+"(instituteId,courseName,courseId,courseFee) values ('" + str(instituteId) + "','" + str(courseName) + "','" + str(courseId) + "','" + str(courseFee) +"')"
        cursor = util.getCursor()
        cursor.execute(sql)
        con.commit()
        JOptionPane.showMessageDialog(None,"Successfully course has been added")
        return True
    except:
        con.rollback()
        JOptionPane.showMessageDialog(None,"Failed to add the course ")
        return False
    
def updateCourse(courseObj):
    con = util.getCon()
    try:
        sno = getattr(courseObj,'sno')
        print sno
        instituteId = domain.Institute.instId # act as foreignKey. domain is package in which Institute is class andwe get static variable instId 
        courseName = getattr(courseObj, 'courseName')
        courseId = getattr(courseObj, 'courseId')
        courseFee = getattr(courseObj, 'courseFee')
        sql = ""
        sql =sql+" update course set courseName='"+str(courseName)+"' , courseId = '"+str(courseId)+"', courseFee='"+str(courseFee)+"' where sno='"+str(sno)+"'"
        print sql
        cursor = util.getCursor()
        cursor.execute(sql)
        con.commit()
        JOptionPane.showMessageDialog(None,"Successfully course has been updated")
        return True
    except:
        con.rollback()
        JOptionPane.showMessageDialog(None,"Failed to the update the course ")
        return False
 
 
def showCourseList():
    try:
        instituteId = domain.Institute.instId  # Logined insitute id
        sql = "select * from course where instituteId ="+str(instituteId) 
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchall() # it return in list of list
        return rows
    except:
        return False
    
def getFee(courseName):
    try:
        instituteId = domain.Institute.instId  # Logined insitute id
        sql = "select courseFee from course where instituteId ='"+str(instituteId)+"' AND courseName ='"+str(courseName)+"'" 
        cursor = util.getCursor()
        cursor.execute(sql)
        row = cursor.fetchone() # it return in list of list
        return row
    except:
        return False 
    
        
def getCoursePrimaryKey(courseObj):
    try:
        instituteId = domain.Institute.instId  # Logined insitute id
        courseName = getattr(courseObj,'courseName')
        courseId = getattr(courseObj,'courseId')
        courseFee = getattr(courseObj,'courseFee')
        
        sql = "select sno from course where instituteId ='"+str(instituteId)+"' AND courseName ='"+str(courseName)+"' ANd courseId='"+str(courseId)+"' AND courseFee='"+str(courseFee)+"'"
        cursor = util.getCursor()
        cursor.execute(sql)
        row = cursor.fetchone() # it return in list of list
        return row
    except:
        return False
        