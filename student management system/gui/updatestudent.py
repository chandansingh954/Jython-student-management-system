from javax.swing import JFrame,JButton,JLabel,JTextField,JTextArea,JScrollPane,JPanel,JComboBox
from java.util import Vector
from java.awt import Color
import services as srv
import domain
import extra as ex

studentId = None
tfStudentName= None
tfStudentPhone = None
tfStudentEmail = None
taStudentAddress  = None
tfCourseName = None
cbStudentAssignTeacher = None
frame= None
        
def updateStudent(stObj):
    global studentId
    global tfStudentName
    global tfStudentPhone
    global tfStudentEmail
    global taStudentAddress
    global tfCourseName
    global cbStudentAssignTeacher
    global frame
    
    frame = JFrame("Update student ")
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setSize(500,500)
    frame.setLocation(200,200)
    frame.setLayout(None)
    frame.setVisible(True)
    
    panel = JPanel()
    panel.setSize(500,500)
    panel.setLocation(0,0)
    panel.setLayout(None)
    panel.setVisible(True)
    panel.setBackground(Color.LIGHT_GRAY)
    
    studentId = getattr(stObj,'studentId')
    studentName= getattr(stObj,'studentName')
    studentPhone = getattr(stObj,'studentPhone')
    studentEmail = getattr(stObj,'studentEmail')
    studentAddress = getattr(stObj,'studentAddress')
    studentCourse = getattr(stObj,'courseName')
    
    teachersName =  srv.showStudentChoiceCourse(studentCourse)
    v = Vector()
    for d in teachersName: 
            v.add(d[0].encode('ascii')) 
    
    
    heading = JLabel("Update  TEACHER")
    heading.setBounds(200,30,150,40)

    lbStudentName = JLabel("Student name ")
    lbStudentPhone = JLabel("Phone")
    lbStudentEmail = JLabel("Email Id")
    lbStudentAddress = JLabel("Address")
    lbStudentAssignTeacher = JLabel("Student Assign teacher  ")
    
    tfStudentName = JTextField(studentName)
    tfStudentPhone = JTextField(studentPhone)
    tfStudentEmail = JTextField(studentEmail)
    taStudentAddress = JTextArea(studentAddress)
    cbStudentAssignTeacher = JComboBox(v)
    
    
    lbStudentName.setBounds(70,100,130,30)
    lbStudentPhone.setBounds(70,150,130,30)
    lbStudentEmail.setBounds(70,200,130,30)
    lbStudentAddress.setBounds(70,250,130,30)
    lbStudentAssignTeacher.setBounds(70,350,130,30)
    
    tfStudentName.setBounds(220,100,130,30)
    tfStudentPhone.setBounds(220,150,130,30)
    tfStudentEmail.setBounds(220,200,130,30)
    taStudentAddress.setBounds(220,250,130,80)
    cbStudentAssignTeacher.setBounds(220,350,130,30)
    
    
    btnEnter = JButton("Update",actionPerformed=clickUpdateStudent)
    btnEnter.setBounds(350,420,100,40)
    
    btnCancel = JButton("Cancel",actionPerformed=clickbtnCancel)
    btnCancel.setBounds(50,420,100,40)
    
    panel.add(heading)
    panel.add(lbStudentName)
    panel.add(lbStudentPhone)
    panel.add(lbStudentEmail)
    panel.add(lbStudentAddress)
    panel.add(lbStudentAssignTeacher)
    panel.add(tfStudentName)
    panel.add(tfStudentPhone)
    panel.add(tfStudentEmail)
    panel.add(taStudentAddress)
    panel.add(cbStudentAssignTeacher)
    panel.add(btnEnter)
    panel.add(btnCancel)
    
    frame.add(panel)
def clickbtnCancel(event):
    global frame
    frame.dispose()

def clickUpdateStudent(event):
    global studentId
    global tfStudentName
    global tfStudentPhone
    global tfStudentEmail
    global taStudentAddress
    global tfCourseName
    global cbStudentAssignTeacher
    global frame

    stObj = domain.Student()
    
    setattr(stObj,'studentId',studentId)
    setattr(stObj,'studentName',tfStudentName.getText())
    setattr(stObj,'studentPhone',tfStudentPhone.getText())
    setattr(stObj,'studentEmail',tfStudentEmail.getText())
    setattr(stObj,'studentAddress',taStudentAddress.getText())
    setattr(stObj,'studentAssignTeacher',cbStudentAssignTeacher.getSelectedItem())
    setattr(stObj,'studentLoginId',tfStudentEmail.getText())
    
    check = srv.updateStudentService(stObj)
    if(check == True):
        frame.dispose()