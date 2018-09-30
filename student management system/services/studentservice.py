from javax.swing import JOptionPane
import domain
import util

def showStudentChoiceCourse(course):
    try:
        instituteId = domain.Institute.instId  # Logined insitute id
        sql = "select teacherName from teacher where instituteId ='"+str(instituteId)+"' AND teacherCourse ='"+str(course)+"'" 
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchall() # it return in list of list
        return rows
    except:
        return False
    
def studentLogin(loginId, password):
    try:
        sql = " Select * from student where studentLoginId='jayesh@gmail' AND  studentPassword ='jaguu'"
        print sql
        cursor=util.getCursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        print row
        if(row == None):
            JOptionPane.showMessageDialog(None,"No Student of that loginId or password ")
            return False 
        
        else:
           # now admin login so we have to store its id in static variable to do more task ans store lsit of details
            domain.Student.studentId=row[0]
            domain.Student.instId=row[1]
            domain.Student.studentObj=row 
           
            
            stObj= domain.Student()
            setattr(stObj,'studentId',row[0])
            setattr(stObj,'instituteId',row[1])
            setattr(stObj,'studentName',row[2].encode('ascii'))
            setattr(stObj,'studentPhone',row[3].encode('ascii'))
            setattr(stObj,'studentEmail',row[4].encode('ascii'))
            setattr(stObj,'studentAddress',row[5].encode('ascii'))
            setattr(stObj,'studentAssignTeacher',row[10].encode('ascii'))
            setattr(stObj,'courseName',row[6].encode('ascii'))
            setattr(stObj,'courseFee',row[7])
           
            JOptionPane.showMessageDialog(None,row[2].encode('ascii')+"  is logined successfully")
            return stObj
    except:
        JOptionPane.showMessageDialog(None,"Failed to student login")
        return False

        
def addStudentService(stObj):   
    con = util.getCon()
    try:
        instituteId = domain.Institute.instId # act as foreignKey. domain is package in which Institute is class andwe get static variable instId 
        studentName = getattr(stObj,'studentName')
        studentPhone = getattr(stObj,'studentPhone')
        studentEmail = getattr(stObj,'studentEmail')
        studentAddress = getattr(stObj,'studentAddress')
        courseName = getattr(stObj,'courseName')
        courseFee = getattr(stObj,'courseFee')
        studentAssignTeacher = getattr(stObj,'studentAssignTeacher')
        studentLoginId = getattr(stObj,'studentLoginId')
        studentPassword = getattr(stObj,'studentPassword')
        
        
        sql = "insert into student (instituteId,studentName,studentPhone,studentEmail,studentAddress,courseName,courseFee,studentAssignTeacher,studentLoginId,studentPassword) values ('" + str(instituteId) + "','" + str(studentName) + "','" + str(studentPhone) + "','" + str(studentEmail) +"','"+str(studentAddress)+"','"+str(courseName)+"','"+str(courseFee)+"','"+str(studentAssignTeacher)+"','"+str(studentLoginId)+"','"+str(studentPassword)+"')"
        print sql
        cursor = util.getCursor()
        cursor.execute(sql)
        con.commit()
        JOptionPane.showMessageDialog(None,"Successfully student has been added")
        return True
    except:
        con.rollback()
        JOptionPane.showMessageDialog(None,"Failed to add the student ")
        return False   

def updateStudentService(stObj):   
    con = util.getCon()
    try:
        studentId = getattr(stObj,'studentId')
        studentName = getattr(stObj,'studentName')
        studentPhone = getattr(stObj,'studentPhone')
        studentEmail = getattr(stObj,'studentEmail')
        studentAddress = getattr(stObj,'studentAddress')
        studentAssignTeacher = getattr(stObj,'studentAssignTeacher')
        studentLoginId = getattr(stObj,'studentLoginId')
        
        sql =" update student set studentName='"+str(studentName)+"' , studentPhone = '"+str(studentPhone)+"', studentEmail='"+str(studentEmail)+"', studentAddress='"+str(studentAddress)+"', studentAssignTeacher='"+str(studentAssignTeacher)+"', studentLoginId='"+str(studentLoginId)+"'  where studentId='"+str(studentId)+"'"
        print sql
        cursor = util.getCursor()
        cursor.execute(sql)
        con.commit()
        JOptionPane.showMessageDialog(None,"Successfully student has been updated")
        return True
    except:
        con.rollback()
        JOptionPane.showMessageDialog(None,"Failed to update the student ")
        return False   


def showAllStudentList():
    try:
        instituteId = domain.Institute.instId  # Logined insitute id
        sql = "select * from student where instituteId ='"+str(instituteId)+"'" 
        print sql
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchall() # it return in list of list
        return rows
    except:
        return False
  
def showSpecificStudentsByCourse(courseName):
    try:
        instituteId = domain.Institute.instId  # Logined insitute id
        sql = "select * from student where instituteId ='"+str(instituteId) +"' And courseName ='"+str(courseName)+"'"
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchall() # it return in list of list
        return rows
    except:
        return False
    
def showSpecificStudentsByTeacher(teacherName):
    try:
        instituteId = domain.Institute.instId  # Logined insitute id
        sql = "select * from student where instituteId ='"+str(instituteId) +"' And studentAssignTeacher ='"+str(teacherName)+"'"
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchall() # it return in list of list
        return rows
    except:
        return False
    
def getStudentPrimaryKey(stObj):  
    try:
        instituteId = domain.Institute.instId  # Logined insitute id
        studentName = getattr(stObj,'studentName')
        studentPhone = getattr(stObj,'studentPhone')
        studentEmail= getattr(stObj,'studentEmail')
        studentAddress = getattr(stObj,'studentAddress')
        studentCourse = getattr(stObj,'courseName')
        studentAssignTeacher = getattr(stObj,'studentAssignTeacher')

        sql = "select studentId from student where instituteId ='"+str(instituteId) +"' And studentName='"+str(studentName)+"' AND studentPhone ='"+str(studentPhone)+"' AND studentEmail='"+str(studentEmail)+"'AND studentAddress= '"+str(studentAddress)+"'AND courseName='"+str(studentCourse)+"'  AND studentAssignTeacher='"+str(studentAssignTeacher)+"'"
        print sql
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchone() # it return in list of list
        return rows
    except:
        return False
    
def getStudentIdPassword(studentName,courseName):
    try:
        instituteId = domain.Institute.instId  # Logined insitute id
        sql = "select studentLoginId,studentPassword from student where instituteId ='"+str(instituteId) +"' And courseName ='"+str(courseName)+"' AND studentName='"+str(studentName)+"'"
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchone() # it return in list of list
        return rows
    except:
        return False
    
def getStudentIdsOfSpecificTeacher(teacherName):
    try:
        sql = "select studentId from student where studentAssignTeacher ='"+str(teacherName)+"'"
        print sql
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchall() # it return in list of list
        print rows
        return rows
    except:
        return False

def getStudentIdsOfSpecificCourse(courseName):
    try:
        instituteId = domain.Institute.instId  # Logined insitute id
        sql = "select studentId from student where instituteId ='"+str(instituteId) +"' And courseName ='"+str(courseName)+"'"
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchall() # it return in list of list
        return rows
    except:
        return False
        
def getStudentDetailsByStudentName(studentName):
    try:
        instituteId = domain.Institute.instId  # Logined insitute id
        sql = "select studentId,studentName,studentPhone,studentEmail,studentAddress,courseName from student where instituteId ='"+str(instituteId) +"' AND studentName ='"+str(studentName)+"'"
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchall() # it return in list of list
        return rows
    except:
        return False
def getStudentIdAndNameByTeacherName(teacherName):    
    try:
        instituteId = domain.Teacher.instId  # Logined insitute id
        sql = "select studentId,studentName from student where instituteId ='"+str(instituteId) +"' AND studentAssignTeacher ='"+str(teacherName)+"'"
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchall() # it return in list of list
        return rows
    except:
        return False
def getStudentDeatailsByStudentIds(studentIds):
    try:
        sql = "select studentId,studentName,studentPhone,studentEmail,studentAddress,courseName from student where  studentId  IN ("
        for id in studentIds:
            sql =sql+str(id)+","
        sql =sql[:-1]
        sql=sql+" )"
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchall() # it return in list of list
        return rows
    except:
        return False
    
def getStudentPassword(studentId):
    try:
        instituteId = domain.Student.instId  # Logined insitute id
        sql = "select studentPassword from student where instituteId ='"+str(instituteId)+"' AND studentId ='"+str(studentId)+"'"
        print sql
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchone() # it return in list of list
        return rows
    except:
        return False
    
def updateStudentPassword(password):
    con = util.getCon()
    try:
        studentId = domain.Student.studentId
        sql =" update student set studentPassword='"+str(password)+"'  where studentId='"+str(studentId)+"'"
        print sql
        cursor = util.getCursor()
        cursor.execute(sql)
        con.commit()
        return True
    except:
        con.rollback()
        return False    
 
def getStudentInfo():
    try:
        studentId = domain.Student.studentId  # Logined insitute id
        sql = "select studentName,studentPhone,studentEmail,studentAddress,courseName,courseFee,studentAssignTeacher from student where studentId ='"+str(studentId)+"'"
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchone() # it return in list of list
        return rows
    except:
        return False
    