from javax.swing import JFrame,JButton,JLabel,JTextField,JPanel,JRadioButton,ButtonGroup,JMenuBar,JMenu,JMenuItem,JTable,JScrollPane,ScrollPaneConstants,JOptionPane
from java.awt import Color
from addcourseform  import *
from addteacherform  import *
from addstudentform import *
from getcoursename import *
from getteachername import * 
from getstudentname import * 
from updatestudent import *
from showtable import * # it means we import all class and method of showtable and we can make the object of that class
from teacherattendenceform import *
from studentattendenceform import *
from studentfeepayform import *

from showloginidpassword import *

import loginpage as lp
import services as srv
heading  = None
frame = None
panel = None
table = None
btnUpdate = None
globalCourseName = None
# we make the table variabls global b/z we can use it in other methods and we make the object of table in adminLogined method
# and we want that any table  to show the list in same table and it is inside the panel
def adminLogined(instObj):
    global panel
    global table
    global heading
    global btnUpdate
    global frame
    
    frame = JFrame("Admin Page ")
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setSize(700,640)
    frame.setLocation(200,200)
    frame.setLayout(None)
    
    
    panel = JPanel()
    panel.setSize(700,620)
    panel.setLocation(0,20)
    panel.setLayout(None)
    panel.setVisible(True)
    panel.setBackground(Color.WHITE)
    
    heading = JLabel()
    heading.setBounds(310,10,200,30)
    
    table = JTable()
    table.setBounds(0,50,700,450)
    sp=  JScrollPane(table,ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS,ScrollPaneConstants.HORIZONTAL_SCROLLBAR_ALWAYS)
    
    btnUpdate = JButton("Update",actionPerformed=clickUpdate)
    btnUpdate.setBounds(300,530,100,30)
    
    bar = JMenuBar()
    courses = JMenu("Course")
    addCourse = JMenuItem("Add Course",actionPerformed=clickAddCourse)
    showCourseList = JMenuItem("Show Course List",actionPerformed=clickShowCourseList)
    courses.add(addCourse)
    courses.add(showCourseList)
    bar.add(courses)
    
    teacher = JMenu("Teacher")
    addTeacher = JMenuItem("Add Teacher",actionPerformed=clickAddTeacher)
    showTeacherList = JMenuItem("Show Teacher List",actionPerformed=clickShowTeacherList)
    showTeacherIdPassword = JMenuItem("Show Teacher Id Password",actionPerformed=clickShowTeacherIdPassword)
    teacher.add(addTeacher)
    teacher.add(showTeacherList)
    teacher.add(showTeacherIdPassword)
    bar.add(teacher)
    
    student = JMenu("Student")
    addStudent = JMenuItem("Add Student",actionPerformed=clickAddStudent)
    showAllStudentList = JMenuItem("Show All Student",actionPerformed=clickShowAllStudent)
    showStudentsByCourse = JMenuItem("Show Student By course",actionPerformed=clickShowStudentByCourse)
    showStudentsByTeacher = JMenuItem("Show Student By Teacher",actionPerformed=clickShowStudentByTeacher)
    showStudentIdPassword = JMenuItem("Show Student Id Password",actionPerformed=clickShowStudentIdPassword)
    student.add(addStudent)
    student.add(showAllStudentList)
    student.add(showStudentsByCourse)
    student.add(showStudentsByTeacher)
    student.add(showStudentIdPassword)
    bar.add(student)
    
    
    attendence = JMenu(" Teacher Attendence")
    teacherAttendence = JMenuItem(" Take Teacher Attendence",actionPerformed=clickTotalAttendence)
    specificTeacherAttendence = JMenuItem("Show Specific Teacher Attendence",actionPerformed=clickShowSpecificTeacherAttendence)
    allTeacherAttendenceMonth = JMenuItem("All Teacher Attendence In Month",actionPerformed=clickShowAllSTeacherAttendenceMonth)
    specificTeacherAttendenceInMonth = JMenuItem("Specific Teacher Attendence In Month",actionPerformed=clickShowSpecificSTeacherAttendenceMonth)
    allTeacherAttendenceStatisticsInMonth = JMenuItem("All Teacher Attendence Statistics In Month",actionPerformed=clickShowAllTeacherAttendenceStatisticsMonth)
    attendence.add(teacherAttendence)
    attendence.add(specificTeacherAttendence)
    attendence.add(allTeacherAttendenceMonth)
    attendence.add(specificTeacherAttendenceInMonth)
    attendence.add(allTeacherAttendenceStatisticsInMonth)
    bar.add(attendence)
    
    studentAttendence = JMenu(" Student Attendence")
    specificTeacherStudentsAttendence = JMenuItem("Show Specific Teacher Students Attendence",actionPerformed=clickShowSpecificTeacherStudentsAttendence)
    specificCourseStudentsAttendence = JMenuItem("Show Specific course Students Attendence",actionPerformed=clickShowSpecificCourseStudentsAttendence)
    specificTeacherStudentsAttendenceInMonth = JMenuItem("Show Specific teacher Students Attendence In month",actionPerformed=clickShowSpecificTeacherStudentsAttendenceInMonth)
    specificCourseStudentsAttendenceInMonth = JMenuItem("Show Specific course Students Attendence In month",actionPerformed=clickShowSpecificCourseStudentsAttendenceInMonth)
    allStudentsAttendenceStatisticsInMonth = JMenuItem("All Students Attendence Statistics In month",actionPerformed=clickShowAllStudentsAttendenceStatisticsInMonth)
    specificTeacherStudentsAttendenceStatisticsInMonth = JMenuItem("Specific Teacher Students Attendence Statistics In month",actionPerformed=clickShowSpecificTeacherStudentsAttendenceStatisticsInMonth)
    specificCourseStudentsAttendenceStatisticsInMonth = JMenuItem("Specific Course Students Attendence Statistics In month",actionPerformed=clickShowSpecificCourseStudentsAttendenceStatisticsInMonth)
    specificStudentAttendenceInMonth = JMenuItem("Specific  Student Attendence In month",actionPerformed=clickShowSpecificStudentAttendenceInMonth)
    studentAttendence.add(specificTeacherStudentsAttendence)
    studentAttendence.add(specificCourseStudentsAttendence)
    studentAttendence.add(specificTeacherStudentsAttendenceInMonth)
    studentAttendence.add(specificCourseStudentsAttendenceInMonth)
    studentAttendence.add(allStudentsAttendenceStatisticsInMonth)
    studentAttendence.add(specificTeacherStudentsAttendenceStatisticsInMonth)
    studentAttendence.add(specificCourseStudentsAttendenceStatisticsInMonth)
    studentAttendence.add(specificStudentAttendenceInMonth)
    bar.add(studentAttendence)
    
    
    studentFee = JMenu("Student Fee ")
    payStudentFee = JMenuItem("Pay" , actionPerformed = clickPayStudentFee)
    showStudentFeeListByCourse = JMenuItem("Student Fee list By Course" , actionPerformed = clickShowStudentFeeListByCourse)
    studentFee.add(payStudentFee)
    studentFee.add(showStudentFeeListByCourse)
    bar.add(studentFee)
    
    logout =JMenuItem("logout",actionPerformed=clickLogout)
    bar.add(logout)
    
    btnUpdate.setVisible(False)
    panel.add(table)
    panel.add(btnUpdate)
    
    
    frame.setJMenuBar(bar)
    frame.add(panel)
    
    frame.setVisible(True)
    
def clickAddCourse(event):
    # in gui package there is addcourseform is module and we call the method of name addCourse
    addCourse()
 
def  clickShowCourseList(event):
    global table
    global heading 
    global panel
    global btnUpdate
    
    datas = srv.showCourseList()
    if(datas == False):
        # some  problem to get the data
        JOptionPane.showMessegeDialog(None,"Failed to get the course list ")
    elif(datas == None):
        # means no datas is available
        JOptionPane.showMessegeDialog(None,"No courses has been added ")
    elif(len(datas) != 0):
        # means we  get some data
        heading.setText("Course List")
        panel.add(heading)
        btnUpdate.setVisible(True)
        tableModel = MyTableModel1(datas) # object has been created  ,the class is avialable in gui package and in showtable module
        table.setModel(tableModel) # in table we set the model

def clickAddTeacher(event):
    addTeacher()

def clickShowTeacherList(event):
    global table
    global heading
    global panel
    global btnUpdate
    
    datas = srv.showTeacherList()
    if(datas == False):
        # some  problem tso get the data
        JOptionPane.showMessageDialog(None,"Failed to get the Teacher list ")
    elif(len(datas) == 0):
        # means no datas is available
        JOptionPane.showMessageDialog(None,"No teacher has been added ")
    elif(len(datas) != 0):
        # means we  get some data
        heading.setText("Teacher List")
        panel.add(heading)
        btnUpdate.setVisible(True)
        tableModel = MyTableModel2(datas) # object has been created  ,the class is avialable in gui package and in showtable module
        table.setModel(tableModel) # in table we set the model

def clickAddStudent(event):
    selectTeacher() # this method is for adding the student
    
def clickShowAllStudent(event):
    global table
    global heading
    global panel
    global btnUpdate
    
    datas = srv.showAllStudentList()
    print datas
    if(datas == False):
        # some  problem to get the data
        JOptionPane.showMessageDialog(None,"Failed to get the All student list ")
    elif(len(datas)== 0):
        # means no datas is available
        JOptionPane.showMessageDialog(None,"No student has been added ")
    elif(len(datas) != 0):
        # means we  get some data
        heading.setText("Student List")
        panel.add(heading)
        btnUpdate.setVisible(True)
        tableModel = MyTableModel3(datas) # object has been created  ,the class is avialable in gui package and in showtable module
        table.setModel(tableModel) # in table we set the model
        
        
def clickShowStudentByCourse(event):
    value = "for show syudent by course"
    getCourseName(value)
    
def takeStudentCourse(courseName): 
    global table
    global heading
    global panel
    global btnUpdate
    
    datas = srv.showSpecificStudentsByCourse(courseName)
    if(datas == False):
        # some  problem to get the data
        JOptionPane.showMessegeDialog(None,"Failed to get the  student list ")
    elif(datas == None):
        # means no datas is available
        JOptionPane.showMessegeDialog(None,"No student has been added ")
    elif(len(datas) != 0):
        # means we  get some data
        heading.setText("Student List")
        panel.add(heading)
        btnUpdate.setVisible(True)
        tableModel = MyTableModel3(datas) # object has been created  ,the class is avialable in gui package and in showtable module
        table.setModel(tableModel) # in table we set the model
  
def clickShowStudentByTeacher(event):
    getTeacherName("for admin")
    
def takeTeacherName(teacherName): 
    global table
    global heading
    global panel
    global btnUpdate
    
    datas = srv.showSpecificStudentsByTeacher(teacherName)
    if(datas == False):
        # some  problem to get the data
        JOptionPane.showMessegeDialog(None,"Failed to get the  student list ")
    elif(datas == None):
        # means no datas is available
        JOptionPane.showMessegeDialog(None,"No student has been added ")
    elif(len(datas) != 0):
        # means we  get some data
        heading.setText("Student List")
        panel.add(heading)
        btnUpdate.setVisible(True)
        tableModel = MyTableModel3(datas) # object has been created  ,the class is avialable in gui package and in showtable module
        table.setModel(tableModel) # in table we set the model
 
      
def clickUpdate(event):
    global heading
    global table
    global btnUpdate
    
    rowIndex = table.getSelectedRow()
    if(btnUpdate.getText() =="Update"):
        if(heading.getText()== "Course List"):
            courseObj = domain.Course()
            instituteId =table.getValueAt(rowIndex,0)
            courseName =table.getValueAt(rowIndex,1)
            courseId =table.getValueAt(rowIndex,2)
            courseFee =table.getValueAt(rowIndex,3)

            setattr(courseObj,'instituteId',instituteId)
            setattr(courseObj,'courseName',courseName)
            setattr(courseObj,'courseId',courseId)
            setattr(courseObj,'courseFee',courseFee)

            sno = srv.getCoursePrimaryKey(courseObj)
            setattr(courseObj,'sno',sno[0])

            updateCourse(courseObj)

        elif(heading.getText()=="Teacher List"):
            teacherObj = domain.Teacher()

            teacherName = table.getValueAt(rowIndex,1) 
            teacherPhone = table.getValueAt(rowIndex,2) 
            teacherEmail = table.getValueAt(rowIndex,3) 
            teacherAddress = table.getValueAt(rowIndex,4) 
            teacherCourse = table.getValueAt(rowIndex,5) 
            teacherPayment = table.getValueAt(rowIndex,6) 

            setattr(teacherObj,'teacherName',teacherName)
            setattr(teacherObj,'teacherPhone',teacherPhone)
            setattr(teacherObj,'teacherEmail',teacherEmail)
            setattr(teacherObj,'teacherAddress',teacherAddress)
            setattr(teacherObj,'teacherCourse',teacherCourse)
            setattr(teacherObj,'teacherPayment',teacherPayment)

            teacherId = srv.getTeacherPrimaryKey(teacherObj)
            print teacherId[0]

            setattr(teacherObj,'teacherId',teacherId[0])
            updateTeacher(teacherObj)

        elif(heading.getText() == "Student List"):
            studentObj = domain.Student()

            studentName = table.getValueAt(rowIndex,1)
            studentPhone = table.getValueAt(rowIndex,2)
            studentEmail = table.getValueAt(rowIndex,3)
            studentAddress = table.getValueAt(rowIndex,4)
            studentCourse = table.getValueAt(rowIndex,5)
            studentAssignTeacher = table.getValueAt(rowIndex,7)

            setattr(studentObj,'studentName',studentName)
            setattr(studentObj,'studentPhone',studentPhone)
            setattr(studentObj,'studentEmail',studentEmail)
            setattr(studentObj,'studentAddress',studentAddress)
            setattr(studentObj,'courseName',studentCourse)
            setattr(studentObj,'studentAssignTeacher',studentAssignTeacher)

            studentId = srv.getStudentPrimaryKey(studentObj)

            setattr(studentObj,'studentId',studentId[0])

            updateStudent(studentObj)
    elif(btnUpdate.getText() == "Ok"):
        studentId = table.getValueAt(rowIndex,0)
        
        datas = srv.getStudentFeeDetailsByStudentId(studentId)
        StFeeObj = domain.StudentFee()
        
        setattr(StFeeObj,'studentId',datas[0])
        setattr(StFeeObj,'studentName',datas[1].encode('ascii'))
        setattr(StFeeObj,'totalAmount',datas[2])
        setattr(StFeeObj,'paidAmount',datas[3])
        setattr(StFeeObj,'remainingAmount',datas[4])
        
        createStudentFeeForm(StFeeObj)

def clickShowTeacherIdPassword(event):
    value = "fot teacher Id password"
    getTeacherName(value)

def takeTeacherNameForIdPassword(teacherName):
    data = srv.getTeacherIdPassword(teacherName)
    if(data == False):
        # some  problem to get the data
        JOptionPane.showMessageDialog(None,"Failed to get the Teacher Id and password ")
    elif(data == None):
        # means no datas is available
        JOptionPane.showMessageDialog(None,"No teacher of this name ")
    elif(len(data) != 0):
        showLoginIdPassword(data)
 
def clickShowStudentIdPassword(event):
    value ="for student id password"
    getCourseName(value)
    
def takeStudentCourseForIdPassword(courseName):
    global globalCourseName 
    globalCourseName = courseName
    
    value ="for student id password"
    getStudentName(value)

def takeStudentName(studentName):
    global globalCourseName
    
    data = srv.getStudentIdPassword(studentName,globalCourseName)
    if(data == False):
        # some  problem to get the data
        JOptionPane.showMessageDialog(None,"Failed to get the Student Id and password ")
    elif(data == None):
        # means no datas is available
        JOptionPane.showMessageDialog(None,"No student of this name ")
    elif(len(data) != 0):
        showLoginIdPassword(data)
    
    
    
def clickPayStudentFee(event):
    value ="pay student fee"
    getStudentName(value)
    
def takeStudentNameForPaidFee(studentName):
    global table
    global heading
    global btnUpdate
    
    datas = srv.getStudentDetailsByStudentName(studentName)
    if(datas == False):
        # some  problem to get the data
        JOptionPane.showMessageDialog(None,"Failed to get the Student details ")
    elif(len(datas) == 0):
        # means no datas is available
        JOptionPane.showMessageDialog(None,"No student for that student name ")
    elif(len(datas) != 0):
        # means we  get some data
        heading.setText("Student Fee Pay")
        btnUpdate.setVisible(True)
        btnUpdate.setText("Ok")
        tableModel = MyTableModel10(datas) # object has been created  ,the class is avialable in gui package and in showtable module
        table.setModel(tableModel) # in table we set the model


def clickShowStudentFeeListByCourse(event):
    value ="for show student fee list"
    getCourseName(value)
    
def takeCourseNameForShowStudentFeeList(courseName):
    global table
    global heading
    global btnUpdate
    
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
            
        datas = srv.getStudentsFeeListByStudentId(idsList)
        print datas
        if(datas == False):
            JOptionPane.showMessageDialog(None,"Failed to get the  student fee List ")
        elif(len(datas) == 0):
            JOptionPane.showMessageDialog(None,"No any fee List is maintanied for that course")
        elif(len(datas) != 0):
            heading.setText("Student Fee List")
            btnUpdate.setVisible(False)
            tableModel = MyTableModel11(datas) 
            table.setModel(tableModel)

def clickLogout(event):
    global frame
    frame.dispose()
    lp.loginPage()