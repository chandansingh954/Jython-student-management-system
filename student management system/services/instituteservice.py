# wehave to get the domain class in that module
import util
import domain 
from javax.swing import JOptionPane
 
dObj = domain.Institute() # here we make the object of class Institute by package name

def instituteLogin(loginId, password):
    try:
        sql = " Select * from institute where adminLoginId='"+loginId+"' AND  adminPassword ='"+password+"'"
        print sql
        cursor=util.getCursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        print row
        if(row == None):
            JOptionPane.showMessageDialog(None,"No Admin of that loginId or password ")
            return False 
        
        else:
            # now admin login so we have to store its id in static variable to do more task ans store lsit of details
            domain.Institute.instId=row[0]
            domain.Institute.instObj=row 


            instObj= domain.Institute()
            setattr(instObj,'instituteId',row[0])
            setattr(instObj,'name',row[1].encode('ascii'))
            setattr(instObj,'phone',row[2].encode('ascii'))
            setattr(instObj,'address',row[3].encode('ascii'))

            JOptionPane.showMessageDialog(None,row[1].encode('ascii')+"  is logined successfully")
            return instObj
    except:
        JOptionPane.showMessageDialog(None,"Failed to login ")
        return False
def  instituteRegistration(inst):
    con = util.getCon()
    try:
        name = getattr(inst, 'name')
        phone = getattr(inst, 'phone')
        address = getattr(inst, 'address')
        adminLoginId = getattr(inst, 'adminLoginId')
        adminPassword = getattr(inst, 'adminPassword')
        sql = "insert into institute (name,phone,address,adminLoginId,adminPassword) values('" + name + "','" + phone + "','" + address + "','" + adminLoginId + "','" + adminPassword + "')"
        print sql
        cursor = util.getCursor()
        cursor.execute(sql)
        con.commit()
        JOptionPane.showMessageDialog(None,"Institute Registered successfully.Go to Login Page")
        return True
    except:
        JOptionPane.showMessageDialog(None,"Failed in Registration,Recheck the enterd Data")
        con.rollback()
        return False
    