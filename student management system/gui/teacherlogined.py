from javax.swing import JFrame,JButton,JLabel,JTextField,JPanel,JRadioButton,ButtonGroup,JMenuBar,JMenu,JMenuItem,JTable,JScrollPane,ScrollPaneConstants,JOptionPane
from java.awt import Color
from showtable import * # it means we import all class and method of showtable and we can make the object of that class
from studentattendenceform import *
from showteacherprofile import *
from teacherloginedstudentattendence import *


from changepasswordform import *
import services as srv
import monthyear as my
import loginpage as lp

heading  = None
frame = None
panel = None
table = None

def teacherLogined(teObj): # teacherObject is object of teacher
    global panel
    global table
    global heading
    global frame
    
    frame = JFrame("Teacher  Page ")
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setSize(500,600)
    frame.setLocation(200,200)
    frame.setLayout(None)
    
    
    panel = JPanel()
    panel.setSize(500,580)
    panel.setLocation(0,20)
    panel.setLayout(None)
    panel.setVisible(True)
    panel.setBackground(Color.WHITE)
    
    heading = JLabel()
    heading.setBounds(210,10,200,30)
    
    table = JTable()
    table.setBounds(0,50,500,470)
    sp=  JScrollPane(table,ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS,ScrollPaneConstants.HORIZONTAL_SCROLLBAR_ALWAYS)
    
    
    bar = JMenuBar()
    
    profile = JMenu("Profile")
    showProfile = JMenuItem("Show Profile",actionPerformed=clickShowProfile)
    changePassword = JMenuItem("Change Password",actionPerformed=clickChangePassword)
    showStudents = JMenuItem("Show students",actionPerformed=clickShowStudents)
    profile.add(showProfile)
    profile.add(changePassword)
    profile.add(showStudents)
    bar.add(profile)
    
    attendence = JMenu("Attendence")
    showAllAttendence = JMenuItem("Show All Attendence",actionPerformed=clickAllAttendence)
    showAttendenceInMonth = JMenuItem("show attendence in month",actionPerformed=clickAttendenceInMonth)
    attendence.add(showAllAttendence)
    attendence.add(showAttendenceInMonth)
    bar.add(attendence)
    
    studentAttendence = JMenu("Student Attendence")
    takeStudentAttendence = JMenuItem("Take Student Attendence",actionPerformed=clickTakeStudentAttendence)
    showStudentAttendenceInMonth = JMenuItem("show all student attendence in month",actionPerformed=clickShowAllStudentAttendenceInMonth)
    showStudentAttendenceStatisticsInMonth = JMenuItem("show  student attendence statistics in month",actionPerformed=clickShowStudentAttendenceStatisticsInMonth)
    showSpecificStudentAttendenceInMonth = JMenuItem("show specific student attendence in month",actionPerformed=clickShowSpecificStudentAttendenceInMonth)
    studentAttendence.add(takeStudentAttendence)
    studentAttendence.add(showStudentAttendenceInMonth)
    studentAttendence.add(showSpecificStudentAttendenceInMonth)
    studentAttendence.add(showStudentAttendenceStatisticsInMonth)
    bar.add(studentAttendence)
    
    logout =JMenuItem("logout",actionPerformed=clickLogout)
    bar.add(logout)
    
    
    
    panel.add(table)
    
    
    frame.setJMenuBar(bar)
    frame.add(panel)
    
    frame.setVisible(True)

def clickShowProfile(event):
    datas = srv.getTeacherInfo()
    if(datas ==False):
        JOptionPane.showMessageDialog(None,"Failed to get the teacher information")
    elif(len(datas ) != 0):
        updateTeacherForm(datas)
 
def clickChangePassword(event):
    value ="change password for teacher"
    changePasswordForm(value)
    
def clickShowStudents(event):
    global table
    global heading
    
    studentIds =getStudentIdsOfThatTeacher()
    if(len(studentIds) == 0):
        JOptionPane.showMessageDialog(None,"No student id")
    else:
        datas = srv.getStudentDeatailsByStudentIds(studentIds)
        if(datas == False):
            JOptionPane.showMessageDialog(None,"Failed to get the student details ")
        elif(len(datas) == 0):
            # means no any attendence is mained for that teacherId
            JOptionPane.showMessageDialog(None,"No any student is study to you ")
        elif(len(datas) != 0):
            heading.setText(" Student Details")
            tableModel = MyTableModel10(datas) 
            table.setModel(tableModel)
    
def clickAllAttendence(event):    
    global table
    global heading
    
    check = srv.getSpecificTeacherAttendenceByTeacherId()
    if(check == False):
        JOptionPane.showMessageDialog(None,"Failed to get the teacher attendence ")
    elif(len(check) == 0):
        # means no any attendence is mained for that teacherId
        JOptionPane.showMessageDialog(None,"No any attendence is maintained for you ")
    elif(len(check) != 0):
        heading.setText("Attendence")
        tableModel = MyTableModel6(check) # check is treat as datas
        table.setModel(tableModel)
        
def clickAttendenceInMonth(event): 
    value ="for specific teacher attendence in month for teacher logined"
    my.createMonthYearForm(value)
    
def takeMonthYearForSpecificTeacherInMonth(month,year):
    global heading
    global table
    
    check = srv.getSpecificTeacherAttendenceByTeacherIdInMonth(month,year)
    if(check == False):
        JOptionPane.showMessageDialog(None,"Failed to get the teacher attendence ")
    elif(len(check) == 0):
        # means no any attendence is mained for that teacherId
        JOptionPane.showMessageDialog(None,"No any attendence is maintained for you ")
    elif(len(check) != 0):
        heading.setText("Attendence")
        tableModel = MyTableModel6(check) # check is treat as datas
        table.setModel(tableModel)
        
def clickLogout(event):
    global frame
    frame.dispose()
    lp.loginPage()        