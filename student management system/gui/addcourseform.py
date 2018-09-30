from javax.swing import JFrame,JButton,JLabel,JTextField,JPanel
from java.awt import Color
import services as srv
import domain

tfCourseName = None
tfCourseId = None
tfCourseFee = None
btnEnter = None
frame =None
sno = None

def addCourse():
    global tfCourseName
    global tfCourseId
    global tfCourseFee
    global frame
    global btnEnter
    
    frame = JFrame("Add Course ")
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setSize(450,450)
    frame.setLocation(200,200)
    frame.setLayout(None)
    frame.setVisible(True)
    
    panel = JPanel()
    panel.setSize(450,450)
    panel.setLocation(0,0)
    panel.setLayout(None)
    panel.setVisible(True)
    panel.setBackground(Color.LIGHT_GRAY)
    
    heading = JLabel("ADD COURSE")
    heading.setBounds(200,30,150,40)

    lbCourseName = JLabel("Course Name ")
    lbCourseId = JLabel("Course Id")
    lbCourseFee = JLabel(" Course Fee")
    
    tfCourseName = JTextField()
    tfCourseId = JTextField()
    tfCourseFee = JTextField()
    
    lbCourseName.setBounds(70,120,130,30)
    lbCourseId.setBounds(70,170,130,30)
    lbCourseFee.setBounds(70,220,130,30)
    
    tfCourseName.setBounds(220,120,150,30)
    tfCourseId.setBounds(220,170,150,30)
    tfCourseFee.setBounds(220,220,150,30)
    
    btnEnter = JButton("Enter",actionPerformed=clickAddCourseFee)
    btnEnter.setBounds(300,300,100,40)
    
    btnCancel = JButton("Cancel",actionPerformed=clickCancel)
    btnCancel.setBounds(70,300,100,40)
    
    panel.add(heading)
    panel.add(lbCourseName)
    panel.add(lbCourseId)
    panel.add(lbCourseFee)
    panel.add(tfCourseFee)
    panel.add(tfCourseName)
    panel.add(tfCourseId)
    panel.add(tfCourseFee)
    panel.add(btnEnter)
    panel.add(btnCancel)
    
    
    
    frame.add(panel)
    
def clickAddCourseFee(event):
    global tfCourseName
    global tfCourseId
    global tfCourseFee
    global frame
    global btnEnter
    global sno
    
    courseObj = domain.Course()
    setattr(courseObj,'courseName',tfCourseName.getText())
    setattr(courseObj,'courseId',tfCourseId.getText())
    setattr(courseObj,'courseFee',tfCourseFee.getText())
    
    if(btnEnter.getText() =="Enter"):
        check = srv.addCourseService(courseObj)
    elif(btnEnter.getText() == "Update"):
        setattr(courseObj,'sno',sno)
        check = srv.updateCourse(courseObj)
    if(check == True):
        frame.dispose() # If cource will added then we check as true and dispose the addcource form
    
def clickCancel(event):
    global frame 
    frame.dispose()
    
def updateCourse(courseObj):    
    global tfCourseName
    global tfCourseId
    global tfCourseFee
    global btnEnter
    global sno
    
    addCourse()
    
    sno = getattr(courseObj,'sno')
    courseName = getattr(courseObj,'courseName')
    courseId = getattr(courseObj,'courseId')
    courseFee = getattr(courseObj,'courseFee')
    
    
    tfCourseName.setText(str(courseName))
    tfCourseId.setText(str(courseId))
    tfCourseFee.setText(str(courseFee))
    btnEnter.setText("Update")
    