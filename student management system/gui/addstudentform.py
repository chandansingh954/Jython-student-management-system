from javax.swing import JFrame,JButton,JLabel,JTextField,JTextArea,JScrollPane,JPanel,JComboBox
from java.util import Vector
from java.awt import Color
import services as srv
import domain
import extra as ex


frame1 = None
tfStudentChoice = None

tfStudentName= None
tfStudentPhone = None
tfStudentEmail = None
taStudentAddress  = None
tfCourseName = None
tfCourseFee  = None
cbStudentAssignTeacher = None
frame= None

def selectTeacher():
    
    global frame1
    global tfStudentChoice
    
    frame1 = JFrame("Add Student ")
    frame1.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame1.setSize(500,250)
    frame1.setLocation(200,200)
    frame1.setLayout(None)
    frame1.setVisible(True)
    
    panel = JPanel()
    panel.setSize(500,250)
    panel.setLocation(0,0)
    panel.setLayout(None)
    panel.setVisible(True)
    panel.setBackground(Color.LIGHT_GRAY)
    
    heading = JLabel("ADD STUDENT")
    heading.setBounds(200,30,150,40)
    
    lbStudentChoice = JLabel("Student course name")
    tfStudentChoice = JTextField()
    
    lbStudentChoice.setBounds(50,70,150,30)
    tfStudentChoice.setBounds(220,70,150,30)
    
    btnEnter = JButton("Enter",actionPerformed=clickStudentChoice)
    btnCancel = JButton("Cancel",actionPerformed=clickBtnCancel)
    
    btnEnter.setBounds(350,150,100,30)
    btnCancel.setBounds(50,150,100,30)
    
    panel.add(heading)
    panel.add(lbStudentChoice)
    panel.add(tfStudentChoice)
    panel.add(btnEnter)
    panel.add(btnCancel)
    frame1.add(panel)

def clickBtnCancel(event):
    global frame1
    frame1.dispose()

def clickStudentChoice(event):
    global tfStudentChoice
    global frame1

    courseName =tfStudentChoice.getText()
    frame1.dispose()
    check  =srv.showStudentChoiceCourse(courseName)
    if(check == False):
        JOtionPane.showMessageDialog(None," Failed to get the teacher of that course")
    elif(check == None):
        JOtionPane.showMessageDialog(None," No any Teacher of that course")
    elif(len(check) != 0):
        # means some data
        print check;
        v = Vector()
        for d in check: # now check treat as datas , check is in list of tuple
            v.add(d[0].encode('ascii')) #teachers are added in vector
            
        fee = srv.getFee(courseName) # only one value in list
        if(len(fee) != 0): # means we get fee
            print fee[0]
            addStudent(courseName,fee[0],v) #  v is vector in which list of teacher in that instiute that teach specific course
        
def addStudent(courseName,courseFee,v):
    
    global tfStudentName
    global tfStudentPhone
    global tfStudentEmail
    global taStudentAddress
    global tfCourseName
    global tfCourseFee
    global cbStudentAssignTeacher
    global frame
    
    frame = JFrame("Add Student ")
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
    
    heading = JLabel("ADD STUDENT")
    heading.setBounds(200,30,150,40)

    lbCourseName = JLabel(" Course name")
    lbCourseFee = JLabel(" Course Fee")
    lbStudentName = JLabel("Student name ")
    lbStudentPhone = JLabel("Phone")
    lbStudentEmail = JLabel("Email Id")
    lbStudentAddress = JLabel("Address")
    lbStudentAssignTeacher = JLabel("Student Assign teacher  ")
    
    tfCourseName = JTextField(courseName)
    tfCourseFee = JTextField(str(courseFee))
    tfStudentName = JTextField()
    tfStudentPhone = JTextField()
    tfStudentEmail = JTextField()
    taStudentAddress = JTextArea()
    cbStudentAssignTeacher = JComboBox(v)
    
    tfCourseName.setEditable(False)
    tfCourseFee.setEditable(False)
    
    lbCourseName.setBounds(70,100,130,30)
    lbCourseFee.setBounds(70,150,130,30)
    lbStudentName.setBounds(70,200,130,30)
    lbStudentPhone.setBounds(70,250,130,30)
    lbStudentEmail.setBounds(70,300,130,30)
    lbStudentAddress.setBounds(70,350,130,80)
    lbStudentAssignTeacher.setBounds(70,450,130,30)
    
    tfCourseName.setBounds(220,100,130,30)
    tfCourseFee.setBounds(220,150,130,30)
    tfStudentName.setBounds(220,200,130,30)
    tfStudentPhone.setBounds(220,250,130,30)
    tfStudentEmail.setBounds(220,300,130,30)
    taStudentAddress.setBounds(220,350,130,80)
    cbStudentAssignTeacher.setBounds(220,450,130,30)
    
    btnEnter = JButton("ADD",actionPerformed=clickAddStudent)
    btnEnter.setBounds(350,510,100,40)
    
    btnCancel = JButton("Cancel",actionPerformed=clickbtnCancelForm)
    btnCancel.setBounds(50,510,100,40)
    
    panel.add(heading)
    panel.add(lbCourseName)
    panel.add(lbCourseFee)
    panel.add(lbStudentName)
    panel.add(lbStudentPhone)
    panel.add(lbStudentEmail)
    panel.add(lbStudentAddress)
    panel.add(lbStudentAssignTeacher)
    panel.add(tfCourseName)
    panel.add(tfCourseFee)
    panel.add(tfStudentName)
    panel.add(tfStudentPhone)
    panel.add(tfStudentEmail)
    panel.add(taStudentAddress)
    panel.add(cbStudentAssignTeacher)
    panel.add(btnEnter)
    panel.add(btnCancel)
    
    frame.add(panel)
def clickbtnCancelForm(event):
    global frame
    frame.dispose()

def clickAddStudent(event):
    global tfStudentName
    global tfStudentPhone
    global tfStudentEmail
    global taStudentAddress
    global tfCourseName
    global tfCourseFee
    global cbStudentAssignTeacher
    
    global frame
    
    password = ex.generatePassword(8)
    
    stObj = domain.Student()
    setattr(stObj,'studentName',tfStudentName.getText())
    setattr(stObj,'studentPhone',tfStudentPhone.getText())
    setattr(stObj,'studentEmail',tfStudentEmail.getText())
    setattr(stObj,'studentAddress',taStudentAddress.getText())
    setattr(stObj,'courseName',tfCourseName.getText())
    setattr(stObj,'courseFee',tfCourseFee.getText())
    setattr(stObj,'studentAssignTeacher',cbStudentAssignTeacher.getSelectedItem())
    setattr(stObj,'studentLoginId',tfStudentEmail.getText())
    setattr(stObj,'studentPassword',password)
    
    
    check = srv.addStudentService(stObj)
    if(check == True):
        studentId = srv.getStudentPrimaryKey(stObj)
        print studentId
        stFeeObj = domain.StudentFee()
        setattr(stFeeObj,'studentId',studentId[0]) #  the value in studentid ia in tuple so we have to get the value inside the tuple
        setattr(stFeeObj,'studentName',tfStudentName.getText())
        setattr(stFeeObj,'totalAmount',tfCourseFee.getText())
        setattr(stFeeObj,'paidAmount','0')
        setattr(stFeeObj,'remainingAmount',tfCourseFee.getText())

        srv.addStudentFeeService(stFeeObj)
        
        frame.dispose()