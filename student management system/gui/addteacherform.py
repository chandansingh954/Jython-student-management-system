from javax.swing import JFrame,JButton,JLabel,JTextField,JPanel,JTextArea
from java.awt import Color
import services as srv
import domain
import extra as ex
heading = None
tfTeacherName = None
tfTeacherPhone = None
taTeacherAddress = None
tfTeacherEmail = None
tfTeacherCourse = None
tfTeacherPayment = None
frame = None
btnEnter = None
teacherId  = None

def addTeacher():
    
    global heading
    global tfTeacherName
    global tfTeacherPhone
    global taTeacherAddress
    global tfTeacherEmail
    global tfTeacherCourse
    global tfTeacherPayment
    global frame
    global btnEnter
    
    frame = JFrame("Add Teacher ")
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setSize(500,600)
    frame.setLocation(200,200)
    frame.setLayout(None)
    frame.setVisible(True)
    
    panel = JPanel()
    panel.setSize(500,600)
    panel.setLocation(0,0)
    panel.setLayout(None)
    panel.setVisible(True)
    panel.setBackground(Color.LIGHT_GRAY)
    
    heading = JLabel("ADD TEACHER")
    heading.setBounds(200,30,150,40)

    lbTeacherName = JLabel("Teacher Name ")
    lbTeacherPhone = JLabel("Phone")
    lbTeacherEmail = JLabel("Email")
    lbTeacherAddress = JLabel("Address")
    lbTeacherCourse = JLabel("Teacher Course ")
    lbTeacherPayment = JLabel("Teacher Payment")
    
    tfTeacherName = JTextField()
    tfTeacherPhone = JTextField()
    taTeacherAddress = JTextArea()
    tfTeacherEmail = JTextField()
    tfTeacherCourse = JTextField()
    tfTeacherPayment = JTextField()
    
    lbTeacherName.setBounds(70,100,130,30)
    lbTeacherPhone.setBounds(70,150,130,30)
    lbTeacherEmail.setBounds(70,200,130,30)
    lbTeacherAddress.setBounds(70,250,130,30)
    lbTeacherCourse.setBounds(70,350,130,30)
    lbTeacherPayment.setBounds(70,400,130,30)
    
    tfTeacherName.setBounds(220,100,130,30)
    tfTeacherPhone.setBounds(220,150,130,30)
    tfTeacherEmail.setBounds(220,200,130,30)
    taTeacherAddress.setBounds(220,250,130,80)
    tfTeacherCourse.setBounds(220,350,130,30)
    tfTeacherPayment.setBounds(220,400,130,30)
    
    btnEnter = JButton("ADD",actionPerformed=clickAddTeacher)
    btnEnter.setBounds(350,450,100,40)
    
    panel.add(heading)
    panel.add(lbTeacherName)
    panel.add(lbTeacherPhone)
    panel.add(lbTeacherEmail)
    panel.add(lbTeacherAddress)
    panel.add(lbTeacherCourse)
    panel.add(lbTeacherPayment)
    panel.add(tfTeacherName)
    panel.add(tfTeacherPhone)
    panel.add(tfTeacherEmail)
    panel.add(taTeacherAddress)
    panel.add(tfTeacherCourse)
    panel.add(tfTeacherPayment)
    panel.add(btnEnter)
    
    
    
    frame.add(panel)
  
def clickAddTeacher(event):
    global tfTeacherName
    global tfTeacherPhone
    global tfTeacherAddress
    global tfTeacherCourse
    global tfTeacherPayment
    global tfTeacherLoginId
    global tfTeacherPassword
    global frame
    global teacherId
    global btnEnter
    
    tr = domain.Teacher()
    setattr(tr,'teacherName',tfTeacherName.getText())
    setattr(tr,'teacherPhone',tfTeacherPhone.getText())
    setattr(tr,'teacherEmail',tfTeacherEmail.getText())
    setattr(tr,'teacherAddress',taTeacherAddress.getText())
    setattr(tr,'teacherCourse',tfTeacherCourse.getText())
    setattr(tr,'teacherPayment',tfTeacherPayment.getText())
    setattr(tr,'teacherLoginId',tfTeacherEmail.getText())
    
    if(btnEnter.getText()=="ADD"):
        password = ex.generatePassword(8)
        setattr(tr,'teacherPassword',password)
        check = srv.addTeacherService(tr)
        print check
    elif(btnEnter.getText() == "Update"):
        setattr(tr,'teacherId',teacherId)
        check= srv.updateTeacherService(tr)
    if(check == True):
        # successfully addes then close the frame 
        frame.dispose()
        
def updateTeacher(trObj):
    global tfTeacherName
    global tfTeacherPhone
    global taTeacherAddress
    global tfTeacherEmail
    global tfTeacherCourse
    global tfTeacherPayment
    global heading
    global btnEnter
    global teacherId
    
    addTeacher()
    
    teacherId = getattr(trObj,'teacherId') # it is set in global
    teacherName = getattr(trObj, 'teacherName')
    teacherPhone = getattr(trObj, 'teacherPhone')
    teacherEmail = getattr(trObj, 'teacherEmail')
    teacherAddress = getattr(trObj, 'teacherAddress')
    teacherCourse = getattr(trObj, 'teacherCourse')
    teacherPayment = getattr(trObj, 'teacherPayment')
    
    tfTeacherName.setText(teacherName)
    tfTeacherPhone.setText(teacherPhone)
    tfTeacherEmail.setText(teacherEmail)
    taTeacherAddress.setText(teacherAddress)
    tfTeacherCourse.setText(teacherCourse)
    tfTeacherPayment.setText(str(teacherPayment))
    
    heading.setText("Update Teacher")
    tfTeacherCourse.setEditable(False)
    
    btnEnter.setText("Update")
    