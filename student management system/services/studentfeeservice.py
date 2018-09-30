from javax.swing import JOptionPane
import domain
import util

def addStudentFeeService(stFeeObj):   
    con = util.getCon()
    try:
        studentId = getattr(stFeeObj,'studentId')
        studentName  = getattr(stFeeObj,'studentName')
        totalAmount = getattr(stFeeObj,'totalAmount')
        paidAmount = getattr(stFeeObj,'paidAmount')
        remainingAmount = getattr(stFeeObj,'remainingAmount')
        
        sql = "insert into studentfee (studentId,studentName,totalAmount,paidAmount,remainingAmount) values ('" + str(studentId) + "','" + str(studentName) + "','" + str(totalAmount) + "','" + str(paidAmount) +"','"+str(remainingAmount)+"')"
        print sql
        cursor = util.getCursor()
        cursor.execute(sql)
        con.commit()
        JOptionPane.showMessageDialog(None,"Successfully student fee has been added")
        return True
    except:
        con.rollback()
        JOptionPane.showMessageDialog(None,"Failed to add the student fee details ")
        return False   

def getStudentFeeDetailsByStudentId(studentId):
    try:
        sql = "select studentId,studentName,totalAmount,paidAmount,remainingAmount from studentfee where studentId ='"+str(studentId)+"'" 
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchone() # it return in list of list
        return rows
    except:
        return False
    
def updateStudentFee(remainingAmount,studentId):    
    con = util.getCon()
    try:
        sql =" update studentfee set remainingAmount='"+str(remainingAmount)+"'  where studentId='"+str(studentId)+"'"
        print sql
        cursor = util.getCursor()
        cursor.execute(sql)
        con.commit()
        JOptionPane.showMessageDialog(None,"Successfully student fee has been paid")
        return True
    except:
        con.rollback()
        JOptionPane.showMessageDialog(None,"Failed to pay the student fee ")
        return False   
def getStudentsFeeListByStudentId(studentIds):
    try:
        sql = ""
        sql = sql+"select studentId,studentName,totalAmount,paidAmount,remainingAmount from studentfee where studentId IN ("
        for id in studentIds:
            sql=sql+str(id)+","
        sql=sql[:-1]
        sql=sql+")"
        print sql
        cursor = util.getCursor()
        cursor.execute(sql)
        rows = cursor.fetchall() # it return in list of list
        return rows
    except:
        return False
    
