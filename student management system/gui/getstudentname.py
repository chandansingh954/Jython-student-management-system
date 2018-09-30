from javax.swing import JButton,JLabel,JTextField,JPanel,JFrame
from java.awt import Color

import adminform as af
import  teacherloginedstudentattendence as tlsa
import studentattendenceform as saf

frame= None
tfStudentNameChoice = None
value = None

def getStudentName(check):    
    global frame
    global tfStudentNameChoice
    global value
    
    value = check
    frame = JFrame("Student  Name ")
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setSize(500,250)
    frame.setLocation(200,200)
    frame.setLayout(None)
    frame.setVisible(True)
    
    panel = JPanel()
    panel.setSize(500,250)
    panel.setLocation(0,0)
    panel.setLayout(None)
    panel.setVisible(True)
    panel.setBackground(Color.LIGHT_GRAY)
    
    heading = JLabel("Student Name")
    heading.setBounds(200,30,150,40)
    
    lbStudentNameChoice = JLabel("Get Student Name")
    tfStudentNameChoice = JTextField()
    
    lbStudentNameChoice.setBounds(50,70,150,30)
    tfStudentNameChoice.setBounds(220,70,150,30)
    
    btnEnter = JButton("Enter",actionPerformed=clickStudentNameChoice)
    btnCancel = JButton("Cancel",actionPerformed=clickBtnCancel)
    
    btnEnter.setBounds(350,150,100,30)
    btnCancel.setBounds(50,150,100,30)
    
    panel.add(heading)
    panel.add(lbStudentNameChoice)
    panel.add(tfStudentNameChoice)
    panel.add(btnEnter)
    panel.add(btnCancel)
    frame.add(panel)

def clickBtnCancel(event):
    global frame
    frame.dispose()

def clickStudentNameChoice(event):
    # call the method in admin form with course name in textfield
    global tfStudentNameChoice
    global frame
    global value
    
    studentName = tfStudentNameChoice.getText()
    frame.dispose()
    if(value == "for student id password"):
        af.takeStudentName(studentName)  
    elif(value == " get student name for specific student attendence in month"):
        saf.takeStudentNameForSpecificStudentAttendenceInMonth(studentName)
    elif(value =="pay student fee"):
        af.takeStudentNameForPaidFee(studentName)
    elif(value =="for teacher logined show specific student attendence in month"):
        tlsa.takeStudentNameForStudentAttendenceInTeacherLogined(studentName)