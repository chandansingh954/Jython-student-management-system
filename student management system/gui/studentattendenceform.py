from javax.swing import JOptionPane,JTable,JLabel,JTextField,JButton,JPanel
from java.lang import Boolean,String

import extra as ex
import services as srv
from showtable import *
from getteachername import *
import getcoursename  as gcn
from monthyear import *
from getstudentname import *

import services as srv
import domain

from monthyear import *

frame = None
table = None
heading = None
btnOk= None
panel  = None

month = None
year = None


def showStudentAttendenceSheetAdminLogined():
    global table
    global heading
    global frame
    global panel
    global btnok
    
    frame = JFrame("Student Attendence Sheet ")
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
    panel.setBackground(Color.WHITE)
    
    heading = JLabel("Student Attendence")
    heading.setBounds(200,10,150,30)
    
    table = JTable()
    table.setBounds(0,50,500,450)
    panel.add(table)
    
    btnOk = JButton("Ok",actionPerformed = clickOk)
    
    btnOk.setBounds(200,540,100,40)

    panel.add(heading)
    panel.add(table)
    panel.add(btnOk)
    
    frame.add(panel)
    
def clickOk(event):
    global frame
    frame.dispose()
    
def clickShowSpecificTeacherStudentsAttendence(event):
    getTeacherName("for student attendence")

def takeTeacherNameForAllStudent(teacherName):
    global table
    studentIds =srv.getStudentIdsOfSpecificTeacher(teacherName)
    if(studentIds == False):
        # some  problem to get the data
        JOptionPane.showMessageDialog(None,"Failed to get the  student id list ")
    elif(len(studentIds) == 0): # if  there is no data then it return the empty lisr
        # means no datas is available, so we have to show thw attendence list for today
        JOptionPane.showMessageDialog(None,"No any student or that teacher")
    elif(len(studentIds) != 0):
        # means we  had done the attendence  on today
        idsList =[]
        for id  in studentIds:
            idsList.append(id[0])
            
        datas = srv.getStudentsAttendenceByStudentId(idsList)
        if(datas == False):
            JOptionPane.showMessageDialog(None,"Failed to get the  student attendence ")
        elif(len(datas) == 0):
            JOptionPane.showMessageDialog(None,"No any attendence is maintanied for that teacher Students ")
        elif(len(datas) != 0):
            showStudentAttendenceSheetAdminLogined()
            tableModel = MyTableModel8(datas) # object has been created  ,the class is avialable in gui package and in showtable module
            table.setModel(tableModel)

def clickShowSpecificCourseStudentsAttendence(event):
    value ="for specfic course student attendence"
    gcn.getCourseName(value)
    
def takeCourseNameForAllStudent(courseName):
    global table
    studentIds =srv.getStudentIdsOfSpecificCourse(courseName)
    if(studentIds == False):
        # some  problem to get the data
        JOptionPane.showMessageDialog(None,"Failed to get the  student id list ")
    elif(len(studentIds) == 0): # if  there is no data then it return the empty lisr
        # means no datas is available, so we have to show thw attendence list for today
        JOptionPane.showMessageDialog(None,"No any student in that course")
    elif(len(studentIds) != 0):
        # means we  had done the attendence  on today
        idsList =[]
        for id  in studentIds:
            idsList.append(id[0])
            
        datas = srv.getStudentsAttendenceByStudentId(idsList)
        if(datas == False):
            JOptionPane.showMessageDialog(None,"Failed to get the  student attendence ")
        elif(len(datas) == 0):
            JOptionPane.showMessageDialog(None,"No any attendence is maintanied for that  Students  course")
        elif(len(datas) != 0):
            showStudentAttendenceSheetAdminLogined()
            tableModel = MyTableModel8(datas) # object has been created  ,the class is avialable in gui package and in showtable module
            table.setModel(tableModel)

def clickShowSpecificTeacherStudentsAttendenceInMonth(event):
    value ="show student attendence for specific teacher in month"
    createMonthYearForm(value)
    
def takeMonthYearForSpecificTeacherStudentsAttendence(m,y):
    global month 
    global year 
    
    month =m
    year =y
    
    value ="for specific teacher Student attendence in month"
    getTeacherName(value)
    
def takeTeacherNameForStudentAttendenceInMonth(teacherName):
    global month 
    global year 
    global table
    
    studentIds =srv.getStudentIdsOfSpecificTeacher(teacherName)
    if(studentIds == False):
        # some  problem to get the data
        JOptionPane.showMessageDialog(None,"Failed to get the  student id list ")
    elif(len(studentIds) == 0): # if  there is no data then it return the empty lisr
        # means no datas is available, so we have to show thw attendence list for today
        JOptionPane.showMessageDialog(None,"No any student are study to that teacher")
    elif(len(studentIds) != 0):
        # means we  had done the attendence  on today
        idsList =[]
        for id  in studentIds:
            idsList.append(id[0])
            
        datas = srv.getStudentsAttendenceByStudentIdInMonth(idsList,month,year)
        if(datas == False):
            JOptionPane.showMessageDialog(None,"Failed to get the  student attendence ")
        elif(len(datas) == 0):
            JOptionPane.showMessageDialog(None,"No any attendence is maintanied for that teacher students")
        elif(len(datas) != 0):
            showStudentAttendenceSheetAdminLogined()
            tableModel = MyTableModel8(datas) 
            table.setModel(tableModel)

def clickShowSpecificCourseStudentsAttendenceInMonth(event):
    value ="show student attendence for specific course in month"
    createMonthYearForm(value)
    
def takeMonthYearForSpecificCourseStudentsAttendence(m,y):
    global month
    global year
    
    month =m
    year =y
    
    value ="for specific course Student attendence in month"
    gcn.getCourseName(value)
    
def takeCourseNameForAllStudentsInMonth(courseName):
    global month
    global year
    global table
    
    studentIds =srv.getStudentIdsOfSpecificCourse(courseName)
    if(studentIds == False):
        # some  problem to get the data
        JOptionPane.showMessageDialog(None,"Failed to get the  student id list ")
    elif(len(studentIds) == 0): # if  there is no data then it return the empty lisr
        # means no datas is available, so we have to show thw attendence list for today
        JOptionPane.showMessageDialog(None,"No any student are study to that course")
    elif(len(studentIds) != 0):
        # means we  had done the attendence  on today
        idsList =[]
        for id  in studentIds:
            idsList.append(id[0])
            
        datas = srv.getStudentsAttendenceByStudentIdInMonth(idsList,month,year)
        if(datas == False):
            JOptionPane.showMessageDialog(None,"Failed to get the  student attendence ")
        elif(len(datas) == 0):
            JOptionPane.showMessageDialog(None,"No any attendence is maintanied for that course")
        elif(len(datas) != 0):
            showStudentAttendenceSheetAdminLogined()
            tableModel = MyTableModel8(datas) 
            table.setModel(tableModel)

def clickShowAllStudentsAttendenceStatisticsInMonth(event):
    value ="show all student attendence statistics in month"
    createMonthYearForm(value)
    
def takeMonthYearForAllStudentStatisticsInMonth(month,year):
    global table
    
    datas = srv.getAllStudentAttendenceStatisticsInMonth(month,year)
    if(datas == False):
        # some  problem to get the data
        JOptionPane.showMessageDialog(None,"Failed to get the  student attendence stat n month ")
    elif(len(datas) == 0):
        # means no datas is available, so we have to show thw attendence list for today
        JOptionPane.showMessageDialog(None,"No any attendence is mantained yet ")
        
    elif(len(datas) != 0):
        # means we  had done the attendence  on today
        showStudentAttendenceSheetAdminLogined()
        tableModel = MyTableModel9(datas) # object has been created  ,the class is avialable in gui package and in showtable module
        table.setModel(tableModel) # in table we set the model
 
def clickShowSpecificTeacherStudentsAttendenceStatisticsInMonth(event):      
    value ="show student attendence statistics for specific teacher in month"
    createMonthYearForm(value)
    
def takeMonthYearForSpecificTeacherStudentsAttendenceStatistics(m,y):
    global month 
    global year 
    
    month =m
    year =y
    
    value ="for specific teacher Student attendence statistics in month"
    getTeacherName(value)
    
def takeTeacherNameForStudentAttendenceStatisticsInMonth(teacherName):
    global month 
    global year 
    global table
    
    studentIds =srv.getStudentIdsOfSpecificTeacher(teacherName)
    if(studentIds == False):
        # some  problem to get the data
        JOptionPane.showMessageDialog(None,"Failed to get the  student id list ")
    elif(len(studentIds) == 0): # if  there is no data then it return the empty lisr
        # means no datas is available, so we have to show thw attendence list for today
        JOptionPane.showMessageDialog(None,"No any student are study to that teacher")
    elif(len(studentIds) != 0):
        # means we  had done the attendence  on today
        idsList =[]
        for id  in studentIds:
            idsList.append(id[0])
            
        datas = srv.getStudentsAttendenceStatisticsByStudentIdInMonth(idsList,month,year)
        if(datas == False):
            JOptionPane.showMessageDialog(None,"Failed to get the  student attendence statistics ")
        elif(len(datas) == 0):
            JOptionPane.showMessageDialog(None,"No any attendence is maintanied for that teacher students")
        elif(len(datas) != 0):
            showStudentAttendenceSheetAdminLogined()
            tableModel = MyTableModel9(datas) 
            table.setModel(tableModel)

def clickShowSpecificCourseStudentsAttendenceStatisticsInMonth(event):
    value ="show student attendence statistics for specific course in month"
    createMonthYearForm(value)
    
def takeMonthYearForSpecificCourseStudentsAttendenceStatistics(m,y):
    global month
    global year
    
    month =m
    year =y
    
    value ="for specific course Student attendence statistics in month"
    gcn.getCourseName(value)
    
def takeCourseNameForAllStudentsStatisticsInMonth(courseName):
    global month
    global year
    global table
    
    studentIds =srv.getStudentIdsOfSpecificCourse(courseName)
    if(studentIds == False):
        # some  problem to get the data
        JOptionPane.showMessageDialog(None,"Failed to get the  student id list ")
    elif(len(studentIds) == 0): # if  there is no data then it return the empty lisr
        # means no datas is available, so we have to show thw attendence list for today
        JOptionPane.showMessageDialog(None,"No any student are study to that course")
    elif(len(studentIds) != 0):
        # means we  had done the attendence  on today
        idsList =[]
        for id  in studentIds:
            idsList.append(id[0])
            
        datas = srv.getStudentsAttendenceStatisticsByStudentIdInMonth(idsList,month,year)
        if(datas == False):
            JOptionPane.showMessageDialog(None,"Failed to get the  student attendence  statistics")
        elif(len(datas) == 0):
            JOptionPane.showMessageDialog(None,"No any attendence is maintanied for that course")
        elif(len(datas) != 0):
            showStudentAttendenceSheetAdminLogined()
            tableModel = MyTableModel9(datas) 
            table.setModel(tableModel)

def clickShowSpecificStudentAttendenceInMonth(event):
    value = "for specific student attendence in month"
    createMonthYearForm(value)
    
def takeMonthYearForSpecificStudentAttendenceInMonth(m,y): 
    global month
    global year
    
    month = m
    year =y
    
    value =" get student name for specific student attendence in month"
    getStudentName(value)

def takeStudentNameForSpecificStudentAttendenceInMonth(studentName):
    global  month
    global year
    global table
    
    instituteId = domain.Institute.instId
    datas =srv.getSpecificStudentAttendenceInMonth(instituteId,studentName,month,year) 
    if(datas == False):
        JOptionPane.showMessageDialog(None,"Failed to get the student attendence")
    elif(len(datas) ==0):
        JOptionPane.showMessageDialog(None,"No any student attendence of that name")
    elif(len(datas) !=0):
        showStudentAttendenceSheetAdminLogined()
        tableModel = MyTableModel8(datas) 
        table.setModel(tableModel)