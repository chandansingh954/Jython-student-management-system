from javax.swing import JFrame,JPanel,JButton,JLabel,JTextField,JOptionPane
from java.awt import Color 

import teacherattendenceform as taf
import studentattendenceform as saf
import teacherlogined as tl
import teacherloginedstudentattendence as tlsa
import studentform as sf

frame = None
tfMonth = None
tfYear  = None
value = None

def createMonthYearForm(check):
    
    global frame
    global tfMonth
    global tfYear
    global value
    
    value = check
    frame = JFrame("Date Frame ")
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setSize(500,300)
    frame.setLocation(200,200)
    frame.setLayout(None)
    frame.setVisible(True)
    
    panel = JPanel()
    panel.setSize(500,300)
    panel.setLocation(0,0)
    panel.setLayout(None)
    panel.setVisible(True)
    panel.setBackground(Color.WHITE)
    
    heading = JLabel("Get MonthYear")
    heading.setBounds(200,20,100,30)

    lbMonth = JLabel("Month")
    lbYear = JLabel("Year")
    
    tfMonth = JTextField()
    tfYear = JTextField()
    
    lbMonth.setBounds(70,90,100,30)
    lbYear.setBounds(70,150,100,30)
    
    tfMonth.setBounds(200,90,100,30)
    tfYear.setBounds(200,150,100,30)
    
    
    btnEnter = JButton("Enter",actionPerformed = clickEnter)
    btnCancel = JButton("Cancel",actionPerformed = clickCancel)
    
    btnEnter.setBounds(350,230,100,40)
    btnCancel.setBounds(70,230,100,40)

    panel.add(heading)
    panel.add(lbMonth)
    panel.add(lbYear)
    panel.add(tfMonth)
    panel.add(tfYear)
    panel.add(btnEnter)
    panel.add(btnCancel)
    
    frame.add(panel)
    
    
def clickEnter(event):
    global tfMonth
    global tfYear
    global frame
    global value
    
    
    month =tfMonth.getText()
    year =tfYear.getText()
    
    frame.dispose()
    if(value == "show all teacher attendence in month"):
        taf.takeMonthYear(month,year)
    elif(value ==  "for specific teacher attendence in month"):
        taf.takeMonthYearSpecificTeacher(month,year)
    elif( value == "show all  teacher attendence statistics in month"):
        taf.takeMonthYearAllTeacherAttendenceStatistics(month,year)
    elif(value == "show student attendence for specific teacher in month"):
        saf.takeMonthYearForSpecificTeacherStudentsAttendence(month,year)
    elif(value =="show student attendence for specific course in month"):
        saf.takeMonthYearForSpecificCourseStudentsAttendence(month,year)
    elif(value=="show all student attendence statistics in month"):
        saf.takeMonthYearForAllStudentStatisticsInMonth(month,year)
    elif(value =="show student attendence statistics for specific teacher in month"):    
        saf.takeMonthYearForSpecificTeacherStudentsAttendenceStatistics(month,year)
    elif(value == "show student attendence statistics for specific course in month"):
        saf.takeMonthYearForSpecificCourseStudentsAttendenceStatistics(month,year)
    elif(value =="for specific student attendence in month"):
        saf.takeMonthYearForSpecificStudentAttendenceInMonth(month,year)
    elif(value == "for specific teacher attendence in month for teacher logined"):
        tl.takeMonthYearForSpecificTeacherInMonth(month,year)
    elif(value =="for teacher logined show student attendence in month"):
        tlsa.takeMonthYearForTeacherLoginedStudentAttendenceInMonth(month,year)
    elif(value =="for teacher logined show specific student attendence in month"):
        tlsa.takeMonthYearForTeacherLoginedSpecificStudentAttendenceInMonth(month,year)
    elif(value =="for teacher logined show student attendence statistics in month"):
        tlsa.takeMonthYearForTeacherLoginedStudentAttendenceStatisticsInMonth(month,year)
    elif(value == "for student logined get month year for attendence"):
        sf.takeMonthYearForStudentLoginedAttendence(month,year)
def clickCancel(event):
    global frame
    frame.dispose()