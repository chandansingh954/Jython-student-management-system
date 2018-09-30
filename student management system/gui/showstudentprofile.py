from javax.swing import JFrame,JButton,JLabel,JTextField,JPanel,JTextArea
from java.awt import Color
import services as srv
import domain

heading = None
tfStudentName = None
tfStudentPhone = None
taStudentAddress = None
tfStudentEmail = None
tfCourseName = None
tfCourseFee = None
tfStudentAssignTeacher = None

frame = None
btnEnter = None

def studentProfileForm(data):
    
    global heading
    global tfStudentName
    global tfStudentPhone
    global taStudentAddress
    global tfStudentEmail
    global tfCourseName
    global tfCourseFee
    global tfStudentAssignTeacher
    global frame
    global btnEnter
    
    frame = JFrame(" Student ")
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setSize(500,620)
    frame.setLocation(200,200)
    frame.setLayout(None)
    frame.setVisible(True)
    
    panel = JPanel()
    panel.setSize(500,620)
    panel.setLocation(0,0)
    panel.setLayout(None)
    panel.setVisible(True)
    panel.setBackground(Color.LIGHT_GRAY)
    
    heading = JLabel(" STUDENT PROFILE")
    heading.setBounds(200,30,150,40)

    lbStudentName = JLabel("Student Name ")
    lbStudentPhone = JLabel("Phone")
    lbStudentEmail = JLabel("Email")
    lbStudentAddress = JLabel("Address")
    lbCourseName = JLabel("Course Name ")
    lbCourseFee = JLabel("Course Fee")
    lbStudentAssignTeacher = JLabel("Teacher")
    
    studentName = data[0].encode('ascii')
    studentPhone = data[1].encode('ascii')
    studentEmail = data[2].encode('ascii')
    studentAddress = data[3].encode('ascii')
    courseName = data[4].encode('ascii')
    courseFee = data[5]
    studentAssignTeacher = data[6].encode('ascii')
    
    tfStudentName = JTextField(studentName)
    tfStudentPhone = JTextField(studentPhone)
    taStudentAddress = JTextArea(studentAddress)
    tfStudentEmail = JTextField(studentEmail)
    tfCourseName = JTextField(courseName)
    tfCourseFee = JTextField(str(courseFee))
    tfStudentAssignTeacher = JTextField(studentAssignTeacher)
    
    tfCourseName.setEditable(False)
    tfCourseFee.setEditable(False)
    tfStudentAssignTeacher.setEditable(False)
    tfStudentName.setEditable(False)
    
    lbStudentName.setBounds(70,100,130,30)
    lbStudentPhone.setBounds(70,150,130,30)
    lbStudentEmail.setBounds(70,200,130,30)
    lbStudentAddress.setBounds(70,250,130,30)
    lbCourseName.setBounds(70,350,130,30)
    lbCourseFee.setBounds(70,400,130,30)
    lbStudentAssignTeacher.setBounds(70,450,130,30)
    
    tfStudentName.setBounds(220,100,130,30)
    tfStudentPhone.setBounds(220,150,130,30)
    tfStudentEmail.setBounds(220,200,130,30)
    taStudentAddress.setBounds(220,250,130,80)
    tfCourseName.setBounds(220,350,130,30)
    tfCourseFee.setBounds(220,400,130,30)
    tfStudentAssignTeacher.setBounds(220,450,130,30)
    
    btnEnter = JButton("Update",actionPerformed=clickUpdateStudent)
    btnEnter.setBounds(350,530,100,40)
    
    btnCancel = JButton("Cancel",actionPerformed=clickCancel)
    btnCancel.setBounds(100,530,100,40)
    
    panel.add(heading)
    panel.add(lbStudentName)
    panel.add(lbStudentPhone)
    panel.add(lbStudentEmail)
    panel.add(lbStudentAddress)
    panel.add(lbCourseName)
    panel.add(lbCourseFee)
    panel.add(lbStudentAssignTeacher)
    panel.add(tfStudentName)
    panel.add(tfStudentPhone)
    panel.add(tfStudentEmail)
    panel.add(taStudentAddress)
    panel.add(tfCourseName)
    panel.add(tfCourseFee)
    panel.add(tfStudentAssignTeacher)
    panel.add(btnEnter)
    panel.add(btnCancel)
    
    
    
    frame.add(panel)
  
def clickUpdateStudent(event):
    global tfStudentName
    global tfStudentPhone
    global tfStudentEmail
    global taStudentAddress
    global tfCourseName
    global tfCourseFee
    global tfStudentAssignTeacher
    global frame
    
    studentId = domain.Student.studentId
    
    st = domain.Student()
    setattr(st,'studentName',tfStudentName.getText())
    setattr(st,'studentPhone',tfStudentPhone.getText())
    setattr(st,'studentEmail',tfStudentEmail.getText())
    setattr(st,'studentAddress',taStudentAddress.getText())
    setattr(st,'courseName',tfCourseName.getText())
    setattr(st,'courseFee',tfCourseFee.getText())
    setattr(st,'studentAssignTeacher',tfStudentAssignTeacher.getText())
    setattr(st,'studentLoginId',tfStudentEmail.getText())
    setattr(st,'studentId',studentId)
    
    check = srv.updateStudentService(st)
    if(check == True):
        # successfully addes then close the frame 
        frame.dispose()
        
def clickCancel(event):
    global frame
    frame.dispose()