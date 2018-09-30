from javax.swing import JOptionPane,JTable,JLabel,JTextField,JButton,JPanel,JFrame
from java.awt import Color
from java.lang import Boolean,String

import extra as ex

from showtable import *
import getstudentname as gsn
import monthyear as my

import services as srv
import domain


frame = None
table = None
heading = None
btnSave= None
btnCancel = None
panel  = None

globalStudentName  = None


def showStudentAttendenceSheetTeacherLogin():
    global table
    global heading
    global frame
    global panel
    global btnSave
    global btnCancel
    
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
    
    heading = JLabel()
    heading.setBounds(200,10,150,30)
    
    table = JTable()
    table.setBounds(0,50,500,450)
    panel.add(table)
    
    btnSave = JButton("Save",actionPerformed = clickSaveBtn)
    btnCancel = JButton("Cancel",actionPerformed = clickCancelBtn)
    
    btnSave.setBounds(350,540,100,40)
    btnCancel.setBounds(70,540,100,40)

    panel.add(heading)
    panel.add(table)
    panel.add(btnSave)
    panel.add(btnCancel)
    
    frame.add(panel)

def adjustFrame():
    global btnSave
    global btnCancel
    global panel
    global heading
    
    heading.setText("Student Attendence")
    panel.remove(btnSave)
    btnCancel.setBounds(200,540,100,40)
    

def getStudentIdsOfThatTeacher():
    row = domain.Teacher.teacherObj
    teacherName = row[2].encode('ascii')
    ids = srv.getStudentIdsOfSpecificTeacher(teacherName)
    print ids
    idList =[]
    if(ids == False):
        JOptionPane.showMessageDialog(None,'failed to get student id list')
        return idList
    elif(len(ids) == 0):
        JOptionPane.showMessageDialog(None,'No any student are study to that teacher')
        return idList
    elif(len(ids) != 0):
        for id in ids:
            idList.append(id[0])
        return idList
            

def clickTakeStudentAttendence(event):
    global table
    global heading
   
    
    studentIdList =getStudentIdsOfThatTeacher()
    if(len(studentIdList) == 0):
        JOptionPane.showMessageDialog(None,'No any student List')
    else:    
        todayDate  = ex.getDate()
        datas = srv.getTodayStudentAttendence(todayDate,studentIdList)
        if(datas == False):
            # some  problem to get the data
            JOptionPane.showMessageDialog(None,"Failed to get the  Student attendence list ")
        elif(len(datas) == 0): # list is emp
            # means no datas is available, so we have to show thw attendence list for today
            takeTodayStudentAttendence(todayDate)

        elif(len(datas) != 0):
            # means we  had done the attendence  on today
            showStudentAttendenceSheetTeacherLogin()
            heading.setText("Update Attendence")
            tableModel = MyTableModel13(datas) # object has been created  ,the class is avialable in gui package and in showtable module
            table.setModel(tableModel) # in table we set the model


def takeTodayStudentAttendence(todayDate):
    global table
    global heading
    
    row = domain.Teacher.teacherObj
    teacherName = row[2].encode('ascii')
    datas = srv.getStudentIdAndNameByTeacherName(teacherName)
    
    if(datas == False):
        # some  problem to get the data
        JOptionPane.showMessageDialog(None,"Failed to get the  student name and id ")
    elif(len(datas) == 0):
        # means no datas is available, so we have to show thw attendence list for today
        JOptionPane.showMessageDialog(None,"There is no any student to that teacher ")
        
    elif(len(datas) != 0):
        # means we  get some data
        showStudentAttendenceSheetTeacherLogin()
        heading.setText("Attendence")
        tableModel = MyTableModel12(datas,todayDate) # object has been created  ,the class is avialable in gui package and in showtable module
        table.setModel(tableModel) # in table we set the model


def clickSaveBtn(event):
    global table
    global frame
    global heading
    rowCount = table.getRowCount()
    i=0
    if(heading.getText() == "Attendence"):
        while(i<rowCount):
            studentId = table.getValueAt(i,0)
            studentName = table.getValueAt(i,1)
            date = table.getValueAt(i,2)
            if (Boolean.parseBoolean(str(table.getValueAt(i, 3)))):
                present = 'P'
            else:
                present = 'A'

            sa = domain.StudentAttendence()
            setattr(sa,'studentId',studentId)
            setattr(sa,'studentName',studentName)
            setattr(sa,'date',date)
            setattr(sa,'present',present)
            i=i+1
            srv.saveStudentAttendence(sa)

        JOptionPane.showMessageDialog(None,"Attendence for today has been saved") 
        
    elif(heading.getText() == "Update Attendence"):
        while(i<rowCount):
            studentId = table.getValueAt(i,0)
            date = table.getValueAt(i,2)
            if (Boolean.parseBoolean(str(table.getValueAt(i, 3)))):
                present = 'P'
            else:
                present = 'A'
            i=i+1    
            srv.updateStudentAttendence(studentId,date,present)

        JOptionPane.showMessageDialog(None,"Attendence for today has been updated") 
    
    frame.dispose()           
              
def clickCancelBtn(event):
    global frame
    frame.dispose()
    
def clickShowAllStudentAttendenceInMonth(event):
    value="for teacher logined show student attendence in month"
    
    my.createMonthYearForm(value)
    
def  takeMonthYearForTeacherLoginedStudentAttendenceInMonth(month,year):   
    
    idList = getStudentIdsOfThatTeacher()
    if(len(idList)== 0):
        JOptionPane.showMessageDialog(None,"Failed to get student for you")
    else:
        datas =srv.getStudentsAttendenceByStudentIdInMonth(idList,month,year) 
        if(datas == False):
            # some  problem to get the data
            JOptionPane.showMessageDialog(None,"Failed to get the  student  attendence  ")
        elif(len(datas) == 0):
            # means no datas is available, so we have to show thw attendence list for today
            JOptionPane.showMessageDialog(None,"There is no any student to that teacher  ")
        elif(len(datas) != 0):
            # means we  get some data
            showStudentAttendenceSheetTeacherLogin()
            adjustFrame()
            
            tableModel = MyTableModel14(datas) # object has been created  ,the class is avialable in gui package and in showtable module
            table.setModel(tableModel) # in table we set the model

def clickShowSpecificStudentAttendenceInMonth(event):
    
    value="for teacher logined show specific student attendence in month"    
    gsn.getStudentName(value)

def takeStudentNameForStudentAttendenceInTeacherLogined(studentName):
    global globalStudentName 
    
    globalStudentName = studentName
    value = "for teacher logined show specific student attendence in month"
    my.createMonthYearForm(value)

def takeMonthYearForTeacherLoginedSpecificStudentAttendenceInMonth(month,year):
    global globalStudentName
    instituteId = domain.Teacher.instId
    datas = srv.getSpecificStudentAttendenceInMonth(instituteId,globalStudentName,month,year)
    if(datas == False):
        # some  problem to get the data
        JOptionPane.showMessageDialog(None,"Failed to get the  student  attendence  ")
    elif(len(datas) == 0):
        # means no datas is available, so we have to show thw attendence list for today
        JOptionPane.showMessageDialog(None,"There is no any attendence in that month fot that student  ")
    elif(len(datas) != 0):
        # means we  get some data
        showStudentAttendenceSheetTeacherLogin()
        adjustFrame()
        tableModel = MyTableModel14(datas) # object has been created  ,the class is avialable in gui package and in showtable module
        table.setModel(tableModel) # in table we set the model

def clickShowStudentAttendenceStatisticsInMonth(event):
    value="for teacher logined show student attendence statistics in month"
    
    my.createMonthYearForm(value)
    
def  takeMonthYearForTeacherLoginedStudentAttendenceStatisticsInMonth(month,year):   
    
    idList = getStudentIdsOfThatTeacher()
    if(len(idList)== 0):
        JOptionPane.showMessageDialog(None,"Failed to get student for you")
    else:
        datas =srv.getStudentsAttendenceStatisticsByStudentIdInMonth(idList,month,year) 
        if(datas == False):
            # some  problem to get the data
            JOptionPane.showMessageDialog(None,"Failed to get the  student  attendence statistics ")
        elif(len(datas) == 0):
            # means no datas is available, so we have to show thw attendence list for today
            JOptionPane.showMessageDialog(None,"There is no any student to that teacher  ")
        elif(len(datas) != 0):
            # means we  get some data
            showStudentAttendenceSheetTeacherLogin()
            adjustFrame()
            
            tableModel = MyTableModel9(datas) # object has been created  ,the class is avialable in gui package and in showtable module
            table.setModel(tableModel) # in table we set the model
