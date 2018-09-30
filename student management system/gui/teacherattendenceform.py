from javax.swing import JOptionPane,JTable,JLabel,JTextField,JButton,JPanel
from java.lang import Boolean,String

import extra as ex
import services as srv
import getteachername as gtn

from showtable import *
from monthyear import *

import services as srv
import domain

from monthyear import *

frame = None
table = None
heading = None
btnSave= None
btnCancel = None
panel  = None

globalTeacherName = None

def showAttendenceSheet():
    global table
    global heading
    global frame
    global panel
    global btnSave
    global btnCancel
    
    frame = JFrame("Teacher Attendence Sheet ")
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
    
    panel.remove(btnSave)
    btnCancel.setBounds(200,540,100,40)

def clickTotalAttendence(event):
    global table
    global heading
   
    todayDate  = ex.getDate()
    datas = srv.getTodayAttendence(todayDate)
    if(datas == False):
        # some  problem to get the data
        JOptionPane.showMessageDialog(None,"Failed to get the  teacher attendence list ")
    elif(len(datas) == 0): # list is emp
        # means no datas is available, so we have to show thw attendence list for today
        takeTodayAttendence(todayDate)
    
    elif(len(datas) != 0):
        # means we  had done the attendence  on today
        showAttendenceSheet()
        heading.setText("Update Attendence")
        tableModel = MyTableModel5(datas) # object has been created  ,the class is avialable in gui package and in showtable module
        table.setModel(tableModel) # in table we set the model

      
def takeTodayAttendence(todayDate):
    global table
    global heading
    
    datas = srv.getTeacherDetails()
    
    if(datas == False):
        # some  problem to get the data
        JOptionPane.showMessageDialog(None,"Failed to get the  teacher name and id ")
    elif(len(datas) == 0):
        # means no datas is available, so we have to show thw attendence list for today
        JOptionPane.showMessageDialog(None,"There is no any teacher in institute ")
        
    elif(len(datas) != 0):
        # means we  get some data
        showAttendenceSheet()
        heading.setText("Attendence")
        tableModel = MyTableModel4(datas,todayDate) # object has been created  ,the class is avialable in gui package and in showtable module
        table.setModel(tableModel) # in table we set the model


def clickSaveBtn(event):
    global table
    global frame
    global heading
    rowCount = table.getRowCount()
    i=0
    if(heading.getText() == "Attendence"):
        while(i<rowCount):
            teacherId = table.getValueAt(i,0)
            teacherName = table.getValueAt(i,1)
            date = table.getValueAt(i,2)
            if (Boolean.parseBoolean(str(table.getValueAt(i, 3)))):
                present = 'P'
            else:
                present = 'A'

            ta = domain.TeacherAttendence()
            setattr(ta,'teacherId',teacherId)
            setattr(ta,'teacherName',teacherName)
            setattr(ta,'date',date)
            setattr(ta,'present',present)
            i=i+1
            srv.saveTeacherAttendence(ta)

        JOptionPane.showMessageDialog(None,"Attendence for today has been saved") 
        
    elif(heading.getText() == "Update Attendence"):
        while(i<rowCount):
            teacherId = table.getValueAt(i,0)
            date = table.getValueAt(i,2)
            if (Boolean.parseBoolean(str(table.getValueAt(i, 3)))):
                present = 'P'
            else:
                present = 'A'
            i=i+1    
            srv.updateTeacherAttendence(teacherId,date,present)

        JOptionPane.showMessageDialog(None,"Attendence for today has been updated") 
    
    frame.dispose()           
              
def clickCancelBtn(event):
    global frame
    frame.dispose()
    
def clickShowSpecificTeacherAttendence(event):
    gtn.getTeacherName("for teacher attendence")

def takeTeacherName(teacherName):
    global table
    datas = srv.getSpecificTeacherAttendence(teacherName)
    if(datas == False):
        # some  problem to get the data
        JOptionPane.showMessageDialog(None,"Failed to get the  teacher attendence list ")
    elif(len(datas) == 0): # if  there is no data then it return the empty lisr
        # means no datas is available, so we have to show thw attendence list for today
        JOptionPane.showMessageDialog(None,"No any attendence is mantained yet  1")
        
    elif(len(datas) != 0):
        # means we  had done the attendence  on today
        showAttendenceSheet()
        adjustFrame()
        tableModel = MyTableModel6(datas) # object has been created  ,the class is avialable in gui package and in showtable module
        table.setModel(tableModel) # in table we set the model
        
        
def clickShowAllSTeacherAttendenceMonth(event):
    value = "show all teacher attendence in month"
    createMonthYearForm(value)
    
def takeMonthYear(month,year):
    global table
    datas = srv.getAllTeacherAttendenceInMonth(month,year)
    if(datas == False):
        # some  problem to get the data
        JOptionPane.showMessageDialog(None,"Failed to get the  teacher attendence list in month ")
    elif(len(datas) == 0):
        # means no datas is available, so we have to show thw attendence list for today
        print datas
        JOptionPane.showMessageDialog(None,"No any attendence is mantained yet 2 ")
        
    elif(len(datas) != 0):
        # means we  had done the attendence  on today
        showAttendenceSheet()
        adjustFrame()
        tableModel = MyTableModel6(datas) # object has been created  ,the class is avialable in gui package and in showtable module
        table.setModel(tableModel) # in table we set the model
        

def clickShowSpecificSTeacherAttendenceMonth(event):
    value = "for specific teacher attendence in month"
    gtn.getTeacherName(value)
     
def takeTeacherNameSpecificMonth(teacherName):
    global globalTeacherName
    globalTeacherName = teacherName
    
    value = "for specific teacher attendence in month"
    createMonthYearForm(value)
     
def takeMonthYearSpecificTeacher(month,year):
    # monthyear in local variable and teacherName is in global variable
    
    global globalTeacherName
    global table
    
    datas = srv.getSpecificTeacherAttendenceInMonth(globalTeacherName,month,year)
    if(datas == False):
        # some  problem to get the data
        JOptionPane.showMessageDialog(None,"Failed to get the  teacher attendence list n month ")
    elif(len(datas) == 0):
        # means no datas is available, so we have to show thw attendence list for today
        JOptionPane.showMessageDialog(None,"No any attendence is mantained yet ")
        
    elif(len(datas) != 0):
        # means we  had done the attendence  on today
        showAttendenceSheet()
        adjustFrame()
        tableModel = MyTableModel6(datas) # object has been created  ,the class is avialable in gui package and in showtable module
        table.setModel(tableModel) # in table we set the model
             

def clickShowAllTeacherAttendenceStatisticsMonth(event):
    value ="show all  teacher attendence statistics in month"
    createMonthYearForm(value)
    
def takeMonthYearAllTeacherAttendenceStatistics(month,year):
    global table
    
    datas = srv.getAllTeacherAttendenceStatisticsInMonth(month,year)
    if(datas == False):
        # some  problem to get the data
        JOptionPane.showMessageDialog(None,"Failed to get the  teacher attendence statistics in month ")
    elif(len(datas) == 0):
        # means no datas is available, so we have to show thw attendence list for today
        JOptionPane.showMessageDialog(None,"No any attendence is mantained yet ")
        
    elif(len(datas) != 0):
        # means we  had done the attendence  on today
        showAttendenceSheet()
        adjustFrame()
        tableModel = MyTableModel7(datas) # object has been created  ,the class is avialable in gui package and in showtable module
        table.setModel(tableModel) # in table we set the model
        
    