from javax.swing import JButton,JLabel,JTextField,JPanel,JFrame
from java.awt import Color
import services as srv
import domain
import adminform as af
import teacherattendenceform as taf
import studentattendenceform as saf

frame= None
tfTeacherNameChoice = None
value = None

def getTeacherName(check):    
    global frame
    global tfTeacherNameChoice
    global value
    
    value = check
    frame = JFrame("Teacher  Name ")
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
    
    heading = JLabel("Teacher Name")
    heading.setBounds(200,30,150,40)
    
    lbTeacherNameChoice = JLabel("Get Teacher Name")
    tfTeacherNameChoice = JTextField()
    
    lbTeacherNameChoice.setBounds(50,70,150,30)
    tfTeacherNameChoice.setBounds(220,70,150,30)
    
    btnEnter = JButton("Enter",actionPerformed=clickTeacherNameChoice)
    btnCancel = JButton("Cancel",actionPerformed=clickBtnCancel)
    
    btnEnter.setBounds(350,150,100,30)
    btnCancel.setBounds(50,150,100,30)
    
    panel.add(heading)
    panel.add(lbTeacherNameChoice)
    panel.add(tfTeacherNameChoice)
    panel.add(btnEnter)
    panel.add(btnCancel)
    frame.add(panel)

def clickBtnCancel(event):
    global frame
    frame.dispose()

def clickTeacherNameChoice(event):
    # call the method in admin form with course name in textfield
    global tfTeacherNameChoice
    global frame
    global value
    
    teacherName = tfTeacherNameChoice.getText()
    frame.dispose()
    if(value == "for admin"):
        af.takeTeacherName(teacherName)   # af is admin form and call the method that send the course name
    elif(value == "for teacher attendence"):
        taf.takeTeacherName(teacherName)
    elif(value == "for specific teacher attendence in month"):
        taf.takeTeacherNameSpecificMonth(teacherName)
    elif(value == "fot teacher Id password"):
        af.takeTeacherNameForIdPassword(teacherName)
    elif(value == "for student attendence"):
        saf.takeTeacherNameForAllStudent(teacherName)
    elif(value =="for specific teacher Student attendence in month"):
        saf.takeTeacherNameForStudentAttendenceInMonth(teacherName)
    elif(value =="for specific teacher Student attendence statistics in month"):
        saf.takeTeacherNameForStudentAttendenceStatisticsInMonth(teacherName)
        