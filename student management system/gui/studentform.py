from javax.swing import JFrame,JButton,JLabel,JTextField,JPanel,JMenuBar,JMenu,JMenuItem,JTable,JScrollPane,ScrollPaneConstants,JOptionPane
from java.awt import Color
from showtable import * # it means we import all class and method of showtable and we can make the object of that class

import services as srv
from showstudentprofile import *
from changepasswordform import *
import monthyear as my
import loginpage as lp

heading  = None
frame = None
panel = None
table = None

def studentLogined(stObj):
    global panel
    global table
    global heading
    global frame
    
    frame = JFrame("Student  Page ")
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
    showProfile = JMenuItem("Show Profile",actionPerformed=clickShowStudentProfile)
    changePassword = JMenuItem("Change Password",actionPerformed=changeStudentPassword)
    profile.add(showProfile)
    profile.add(changePassword)
    bar.add(profile)
    
    attendence = JMenu("Attendence")
    showAllAttendence = JMenuItem("Show All Attendence",actionPerformed=clickAllAttendence)
    showAttendenceInMonth = JMenuItem("show attendence in month",actionPerformed=clickAttendenceInMonth)
    attendence.add(showAllAttendence)
    attendence.add(showAttendenceInMonth)
    bar.add(attendence)
    
    logout =JMenuItem("logout",actionPerformed=clickLogout)
    bar.add(logout)
    
    panel.add(table)
    
    
    frame.setJMenuBar(bar)
    frame.add(panel)
    
    frame.setVisible(True)


def clickShowStudentProfile(event):
    datas = srv.getStudentInfo()
    if(datas ==False):
        JOptionPane.showMessageDialog(None,"Failed to get the Student information")
    elif(len(datas ) != 0):
        studentProfileForm(datas)
    
def changeStudentPassword(event):
    value ="change password for student"
    changePasswordForm(value)
    
def clickAllAttendence(event):
    global table
    datas = srv.getSpecificStudentAttendenceByStudentId()
    if(datas == False):
        JOptionPane.showMessageDialog(None,"Failed to get the student attendence")
    elif(len(datas) == 0):
        JOptionPane.showMessageDialog(None,"No any attendence is maintained for you")
    elif(len(datas) != 0):
        tableModel = MyTableModel14(datas)
        table.setModel(tableModel)
    
def clickAttendenceInMonth(event):
    value = "for student logined get month year for attendence"
    my.createMonthYearForm(value)
    
def takeMonthYearForStudentLoginedAttendence(month,year):
    global table
    datas = srv.getSpecificStudentAttendencInMonthByStudentId(month,year)
    if(datas == False):
        JOptionPane.showMessageDialog(None,"Failed to get the student attendence")
    elif(len(datas) == 0):
        JOptionPane.showMessageDialog(None,"No any attendence is maintained for you in that month")
    elif(len(datas) != 0):
        tableModel = MyTableModel14(datas)
        table.setModel(tableModel)
   
def clickLogout(event):
    global frame
    frame.dispose()
    lp.loginPage()        