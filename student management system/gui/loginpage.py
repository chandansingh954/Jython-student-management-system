from javax.swing import JFrame,JButton,JLabel,JTextField,JPanel,JRadioButton,ButtonGroup,ImageIcon
from java.awt import Color
from adminform import *
from teacherlogined import *
from studentform import *

from instRegForm import * # we haveto call the method available in that module so we have to import it . __init__.py is for when we import thr module in __init__.py (all methods)  and call the method by package name

import services as srv
heading = None
rbAdmin = None
rbTeacher = None
rbStudent = None

frame =None

tfLoginId = None
tfPassword =None
  
    
def loginPage():
    global heading 
    global rbAdmin
    global rbTeacher
    global rbStudent
    global frame
    global tfLoginId
    global tfPassword
    
    frame = JFrame("Login Form ")
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setSize(500,500)
    frame.setLocation(200,200)
    frame.setLayout(None)
    frame.setVisible(True)
    
    panel = JPanel()
    panel.setSize(500,500)
    panel.setLocation(0,0)
    panel.setLayout(None)
    
    panel.setBackground(Color.BLUE)
    
    heading = JLabel("Admin Login")
    heading.setBounds(200,50,150,30)
    
    
    rbAdmin = JRadioButton("Admin",actionPerformed=clickRadio)
    rbTeacher=JRadioButton("Teacher",actionPerformed=clickRadio)
    rbStudent=JRadioButton("Student",actionPerformed=clickRadio)
    
    rbAdmin.setBounds(100,150,100,20)
    rbTeacher.setBounds(200,150,100,20)
    rbStudent.setBounds(300,150,100,20)
    
    btnGroup = ButtonGroup()
    btnGroup.add(rbAdmin)
    btnGroup.add(rbTeacher)
    btnGroup.add(rbStudent)
    
    lbLoginId=JLabel("LoginId")
    lbPassword = JLabel("Password")
    
    lbLoginId.setBounds(100,230,150,30)
    lbPassword.setBounds(100,300,150,30)
    
    tfLoginId = JTextField()
    tfPassword = JTextField()
    
    tfLoginId.setBounds(250,230,150,30)
    tfPassword.setBounds(250,300,150,30)
    
    btnLogin = JButton("Login",actionPerformed=clickLogin)
    btnLogin.setBounds(350,350,100,30)
    
    btnReg = JButton("New Institute Registration",actionPerformed=clickReg)
    btnReg.setBounds(350,400,100,30)
    
    
        
    panel.add(heading)
    panel.add(rbAdmin)
    panel.add(rbTeacher)
    panel.add(rbStudent)
    panel.add(lbLoginId)
    panel.add(lbPassword)
    panel.add(tfLoginId)
    panel.add(tfPassword)
    panel.add(btnLogin)
    panel.add(btnReg)
    
    panel.setVisible(True)
    
    frame.add(panel)
    
    
def clickRadio(event):
    global heading
    global rbAdmin
    global rbTeacher
    global rbStudent
    
    if(rbAdmin.isSelected()):
        heading.setText("Admin Login")
    elif(rbTeacher.isSelected()):
        heading.setText("Teacher Login") 
    elif(rbStudent.isSelected()):
        heading.setText("Student Login")      
    

def clickLogin(event):
    global rbAdmin
    global rbTeacher
    global rbStudent
    global tfLoginId
    global tfPassword
    
    
    loginId = tfLoginId.getText()
    password = tfPassword.getText()
    
    if(rbAdmin.isSelected()):
        InloginObj = srv.instituteLogin(loginId, password)
        if(InloginObj != False):
            frame.dispose()
            adminLogined(InloginObj)
            
    elif(rbTeacher.isSelected()):
        TeloginObj = srv.teacherLogin(loginId, password)
        if(TeloginObj != False):
            frame.dispose()
            teacherLogined(TeloginObj)   
    elif(rbStudent.isSelected()):
        StloginObj = srv.studentLogin(loginId, password)
        if(StloginObj != False):
            frame.dispose()
            studentLogined(StloginObj)  
    
def clickReg(event):
    # new registration for institute 
    frame.dispose()
    instReg() # this method is is available as  same package and in different module so we have to import all methods of that module
    