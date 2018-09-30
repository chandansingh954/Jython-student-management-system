from javax.swing import JButton,JLabel,JTextField,JPanel,JFrame
from java.awt import Color
import services as srv
import domain
import adminform as af
import studentattendenceform as  saf

value = None
frame= None
tfStudentCourseChoice=None

def getCourseName(check):    
    global frame
    global tfStudentCourseChoice
    global value

    value = check
    
    frame = JFrame("Course Name ")
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
    
    heading = JLabel("Get Course Name")
    heading.setBounds(200,30,150,40)
    
    lbStudentCourseChoice = JLabel("Student course name")
    tfStudentCourseChoice = JTextField()
    
    lbStudentCourseChoice.setBounds(50,70,150,30)
    tfStudentCourseChoice.setBounds(220,70,150,30)
    
    btnEnter = JButton("Enter",actionPerformed=clickStudentCourseChoice)
    btnCancel = JButton("Cancel",actionPerformed=clickBtnCancel)
    
    btnEnter.setBounds(350,150,100,30)
    btnCancel.setBounds(50,150,100,30)
    
    panel.add(heading)
    panel.add(lbStudentCourseChoice)
    panel.add(tfStudentCourseChoice)
    panel.add(btnEnter)
    panel.add(btnCancel)
    frame.add(panel)

def clickBtnCancel(event):
    global frame
    frame.dispose()

def clickStudentCourseChoice(event):
    # call the method in admin form with course name in textfield
    global tfStudentCourseChoice
    global frame 
    courseName = tfStudentCourseChoice.getText()
    frame.dispose()
    if(value == "for show syudent by course"):
        af.takeStudentCourse(courseName)   # af is admin form and call the method that send the course name
    elif(value =="for student id password"):
        af.takeStudentCourseForIdPassword(courseName)
    elif(value =="for specfic course student attendence"):
        saf.takeCourseNameForAllStudent(courseName)
    elif(value == "for specific course Student attendence in month"):
        saf.takeCourseNameForAllStudentsInMonth(courseName)
    elif(value =="for specific course Student attendence statistics in month"):
        saf.takeCourseNameForAllStudentsStatisticsInMonth(courseName)
    elif(value  == "for show student fee list"):
        af.takeCourseNameForShowStudentFeeList(courseName)