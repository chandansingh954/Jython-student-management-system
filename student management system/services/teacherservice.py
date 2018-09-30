from javax.swing import JOptionPane
import domain
import util
def teacherLogin(loginId, password):
    try:
        sql = " Select * from teacher where teacherLoginId='"+loginId+"' AND  teacherPassword ='"+password+"'"
        print sql
        cursor=util.getCursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        print row
        if(row == None):
            JOptionPane.showMessageDialog(None,"No Teacher of that loginId or password ")
            return False 
        
        else:
            # now admin login so we have to store its id in static variable to do more task ans store lsit of details
            domain.Teacher.teacherId=row[0]
            domain.Teacher.instId=row[1]
            domain.Teacher.teacherObj=row 


            teObj= domain.Teacher()
            setattr(teObj,'teacherId',row[0])
            setattr(teObj,'instituteId',row[1])
            setattr(teObj,'teacherName',row[2].encode('ascii'))
            setattr(teObj,'teacherPhone',row[3].encode('ascii'))
            setattr(teObj,'teacherEmail',row[9].encode('ascii'))
            setattr(teObj,'teacherAddress',row[4].encode('ascii'))
            setattr(teObj,'teacherCourse',row[5].encode('ascii'))
            setattr(teObj,'teacherPayment',row[6])

            JOptionPane.showMessageDialog(None,row[2].encode('ascii')+"  is logined successfully")
            return teObj
    except:
        JOptionPane.showMessageDialog(None,"Failed to teacher login")
        return False

def addTeacherService(trObj):
    con = util.getCon()
    try:
        instituteId = domain.Institute.instId # act as foreignKey. domain is package in which Institute is class andwe get static variable instId 
        teacherName = getattr(trObj, 'teacherName')
        teacherPhone = getattr(trObj, 'teacherPhone')
        teacherEmail = getattr(trObj, 'teacherEmail')
        teacherAddress = getattr(trObj, 'teacherAddress')
        teacherCourse = getattr(trObj, 'teacherCourse')
        teacherPayment = getattr(trObj, 'teacherPayment')
        teacherLoginId = getattr(trObj, 'teacherLoginId')
        teacherPassword= getattr(trObj, 'teacherPassword')
        print "hello"
        
        sql = "insert into teacher (instituteId,teacherName,teacherPhone,teacherEmail,teacherAddress,teacherCourse,teacherPayment,teacherLoginId,teacherPassword) values ('" + str(instituteId) + "','" + str(teacherName) + "','" + str(teacherPhone) + "','"+str(teacherEmail)+"','"+ str(teacherAddress) +"','"+str(teacherCourse)+"','"+str(teacherPayment)+"','"+str(teacherLoginId)+"','"+str(teacherPassword)+"')"
        print sql
        cursor = util.getCursor()
        cursor.execute(sql)
        con.commit()
        JOptionPane.showMessageDialog(None,"Successfully teacher has been added")
        return True
    except:
        con.rollback()
        JOptionPane.showMessageDialog(None,"Failed to add the teacher ")
        return False
 
def updateTeacherService(trObj):
    con = util.getCon()
    try:
        teacherId = getattr(trObj, 'teacherId')
        teacherName = getattr(trObj, 'teacherName')
        teacherPhone = getattr(trObj, 'teacherPhone')
        teacherEmail = getattr(trObj, 'teacherEmail')
        teacherAddress = getattr(trObj, 'teacherAddress')
        teacherCourse = getattr(trObj, 'teacherCourse')
        teacherPayment = getattr(trObj, 'teacherPayment')
        teacherLoginId = getattr(trObj, 'teacherLoginId')
    
        sql =" update teacher set teacherName='"+str(teacherName)+"' , teacherPhone = '"+str(teacherPhone)+"', teacherEmail='"+str(teacherEmail)+"', teacherAddress='"+str(teacherAddress)+"', teacherCourse='"+str(teacherCourse)+"', teacherPayment='"+str(teacherPayment)+"',teacherLoginId='"+str(teacherLoginId)+"'  where teacherId='"+str(teacherId)+"'"
        print sql
        cursor = util.getCursor()
        cursor.execute(sql)
        con.commit()
        JOptionPane.showMessageDialog(None,"Successfully teacher has been Updated")
        return True
    except:
        con.rollback()
        JOptionPane.showMessageDialog(None,"Failed to update the teacher ")
        return False    

def showTeacherList():
    try:
        instituteId = domain.Institute.instId  # Logined insitute id
        sql = "select * from teacher where instituteId ="+str(instituteId) 
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchall() # it return in list of list
        return rows
    except:
        return False
    
def getTeacherDetails():
    try:
        instituteId = domain.Institute.instId  # Logined insitute id
        sql = "select teacherId,teacherName from teacher where instituteId ="+str(instituteId) 
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchall() # it return in list of list
        return rows
    except:
        return False
    
def getTeacherPrimaryKey(teacherObj):
    try:
        instituteId = domain.Institute.instId  # Logined insitute id
        teacherName = getattr(teacherObj,'teacherName') 
        teacherEmail = getattr(teacherObj,'teacherEmail') 
        teacherPhone = getattr(teacherObj,'teacherPhone') 
        teacherAddress = getattr(teacherObj,'teacherAddress') 
        teacherCourse = getattr(teacherObj,'teacherCourse') 
        teacherPayment = getattr(teacherObj,'teacherPayment') 
        
        sql = "select teacherId from teacher where instituteId ='"+str(instituteId)+"' AND teacherName ='"+str(teacherName)+"' AND teacherEmail ='"+str(teacherEmail)+"' AND teacherPhone='"+str(teacherPhone)+"' AND  teacherAddress ='"+str(teacherAddress)+"' AND teacherCourse ='"+str(teacherCourse)+"' AND teacherPayment='"+str(teacherPayment)+"'"   
        print sql
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchone() # it return in tuple
        return rows
    except:
        return False

def getTeacherIdPassword(teacherName):
    try:
        instituteId = domain.Institute.instId  # Logined insitute id
        sql = "select teacherloginId,teacherPassword from teacher where instituteId ='"+str(instituteId)+"' AND teacherName ='"+str(teacherName)+"'"
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchone() # it return in list of list
        return rows
    except:
        return False

def getTeacherPassword(teacherId):
    try:
        print teacherId
        sql = "select teacherPassword from teacher where  teacherId ='"+str(teacherId)+"'"
        print sql
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchone() # it return in list of list
        return rows
    except:
        return False

def updateTeacherPassword(password):
    con = util.getCon()
    try:
        teacherId = domain.Teacher.teacherId
        
        sql =" update teacher set teacherPassword='"+str(password)+"'  where teacherId='"+str(teacherId)+"'"
        print sql
        cursor = util.getCursor()
        cursor.execute(sql)
        con.commit()
        return True
    except:
        con.rollback()
        return False    
def getTeacherInfo():
    try:
        teacherId = domain.Teacher.teacherId  # Logined insitute id
        sql = "select teacherName,teacherPhone,teacherEmail,teacherAddress,teacherCourse,teacherPayment from teacher where teacherId ='"+str(teacherId)+"'"
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchone() # it return in list of list
        return rows
    except:
        return False
