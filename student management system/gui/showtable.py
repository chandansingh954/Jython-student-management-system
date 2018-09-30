from javax.swing.table import DefaultTableModel
from java.util import Vector
from java.lang import Boolean

class MyTableModel1(DefaultTableModel):
    def __init__(self,datas):
        #constructor will call when we create the object
        self.cols = None  # Vector<String>
        self.data = None  # Vector<Vector>
        
        self.initCols()
        self.initData(datas)
        self.setDataVector(self.data,self.cols)
        
    def initCols(self):
        self.cols = Vector()
        self.cols.add("Institute Id")
        self.cols.add("Course Name")
        self.cols.add("Course Id")
        self.cols.add("Course Fee")
        
    def initData(self,datas):    
        self.data = Vector()
        for data in datas:
            v = Vector()
            v.add(data[1])
            v.add(data[2].encode('ascii'))
            v.add(data[3].encode('ascii'))
            v.add(data[4])
            self.data.add(v)
        
        
class MyTableModel2(DefaultTableModel):
    def __init__(self,datas):
        #constructor will call when we create the object
        self.cols = None  # Vector<String>
        self.data = None  # Vector<Vector>
        
        self.initCols()
        self.initData(datas)
        self.setDataVector(self.data,self.cols)
        
    def initCols(self):
        self.cols = Vector()
        self.cols.add("Institute Id")
        self.cols.add("Teacher Name")
        self.cols.add("phone")
        self.cols.add("Email")
        self.cols.add("Address")
        self.cols.add("Course")
        self.cols.add("Payment")
        
    def initData(self,datas):    
        self.data = Vector()
        for data in datas:
            v = Vector()
            v.add(data[1])
            v.add(data[2].encode('ascii'))
            v.add(data[3].encode('ascii'))
            v.add(data[9].encode('ascii'))
            v.add(data[4].encode('ascii'))
            v.add(data[5].encode('ascii'))
            v.add(data[6])
            self.data.add(v)
                
                
                
class MyTableModel3(DefaultTableModel):
    def __init__(self,datas):
        #constructor will call when we create the object
        self.cols = None  # Vector<String>
        self.data = None  # Vector<Vector>
        
        self.initCols()
        self.initData(datas)
        self.setDataVector(self.data,self.cols)
        
    def initCols(self):
        self.cols = Vector()
        self.cols.add("Institute Id")
        self.cols.add("Student Name")
        self.cols.add("phone")
        self.cols.add("Email")
        self.cols.add("Address")
        self.cols.add("Course Name")
        self.cols.add("Course Fee")
        self.cols.add("Student assign teacher")
        
    def initData(self,datas):    
        self.data = Vector()
        for data in datas:
            v = Vector()
            v.add(data[1])
            v.add(data[2].encode('ascii'))
            v.add(data[3].encode('ascii'))
            v.add(data[4].encode('ascii'))
            v.add(data[5].encode('ascii'))
            v.add(data[6].encode('ascii'))
            v.add(data[7])
            v.add(data[10].encode('ascii'))
            self.data.add(v)
 
class MyTableModel4(DefaultTableModel):
    def __init__(self,datas,todayDate):
        #constructor will call when we create the object
        self.cols = None  # Vector<String>
        self.data = None  # Vector<Vector>
        
        self.initCols()
        self.initData(datas,todayDate)
        self.setDataVector(self.data,self.cols)
        
    def initCols(self):
        self.cols = Vector()
        self.cols.add("Teacher Id")
        self.cols.add("Teacher Name")
        self.cols.add("Date")
        self.cols.add("Present")
        
    def initData(self,datas,todayDate):    
        self.data = Vector()
        for data in datas:
            v = Vector()
            v.add(data[0])
            v.add(data[1].encode('ascii'))
            v.add(todayDate)
            v.add(False)
            self.data.add(v)

    def getColumnClass( self,columnIndex):
        if (columnIndex == 3): 
            type = Boolean
            return type
        else: 
            return super(MyTableModel4, self).getColumnClass(columnIndex)
            
        
        
    
    def isCellEditable( self,row,column): 
        if (column == 0 or column == 1 or column==2 ):
            return False
        else:
            return True
                  
                                            
class MyTableModel5(DefaultTableModel):
    def __init__(self, datas):
        #constructor will call when we create the object
        self.cols = None  # Vector<String>
        self.data = None  # Vector<Vector>
        
        self.initCols()
        self.initData(datas)
        self.setDataVector(self.data,self.cols)
        
    def initCols(self):
        self.cols = Vector()
        self.cols.add("Teacher Id")
        self.cols.add("Teacher Name")
        self.cols.add("Date")
        self.cols.add("Present")
        
    def initData(self,datas):    
        self.data = Vector()
        for data in datas:
            v = Vector()
            v.add(data[0])
            v.add(data[1].encode('ascii'))
            v.add(data[2])
            ch = data[3].encode('ascii')
            if(ch == 'P'):
                v.add(True)
            elif(ch == 'A'):
                v.add(False)
            self.data.add(v)

    def getColumnClass(self,columnIndex):
        if (columnIndex == 3): 
            type = Boolean
            return type
        else: 
           return super(MyTableModel5, self).getColumnClass(columnIndex)
            
          
        
    def isCellEditable(self,row,column): 
        if (column == 0 or column == 1 or column==2 ):
            return False
        else:
            return True
                                                             
                    
class MyTableModel6(DefaultTableModel):
    def __init__(self,datas):
        #constructor will call when we create the object
        self.cols = None  # Vector<String>
        self.data = None  # Vector<Vector>
        
        self.initCols()
        self.initData(datas)
        self.setDataVector(self.data,self.cols)
        
    def initCols(self):
        self.cols = Vector()
        self.cols.add("Teacher Id")
        self.cols.add("Teacher Name")
        self.cols.add("Date")
        self.cols.add("Present")
        
    def initData(self,datas):    
        self.data = Vector()
        for data in datas:
            v = Vector()
            v.add(data[0])
            v.add(data[1].encode('ascii'))
            v.add(data[2])
            ch = data[3].encode('ascii')
            if(ch == 'P'):
                v.add(True)
            elif(ch == 'A'):
                v.add(False)
            self.data.add(v)
    def getColumnClass(self,columnIndex):
        if (columnIndex == 3): 
            type = Boolean
            return type
        else: 
            return super(MyTableModel6, self).getColumnClass(columnIndex)
            
           
        
        
    def isCellEditable(self,row,column): 
        if (column == 0 or column == 1 or column==2 or column==3):
            return False
        else:
            return True
                                                             
class MyTableModel7(DefaultTableModel):
    def __init__(self,datas):
        #constructor will call when we create the object
        self.cols = None  # Vector<String>
        self.data = None  # Vector<Vector>
        
        self.initCols()
        self.initData(datas)
        self.setDataVector(self.data,self.cols)
        
    def initCols(self):
        self.cols = Vector()
        teacherId = "Teacher Id"
        teacherName ="Teacher Name"
        noOfdDays ="No of days"
        noOfPresentDays ="No of present days"
        noOfAbsentDays= "No of absent days"
        
        self.cols.add(teacherId)
        self.cols.add(teacherName)
        self.cols.add(noOfdDays)
        self.cols.add(noOfPresentDays)
        self.cols.add(noOfAbsentDays)
        
    def initData(self,datas):    
        self.data = Vector()
        for data in datas:
            v = Vector()
            v.add(data[0])
            v.add(data[1].encode('ascii'))
            v.add(data[2])
            v.add(data[3])
            v.add(data[4])
            self.data.add(v)
    
    def isCellEditable(self,row,column): 
        if (column == 0 or column == 1 or column==2 or column==3 or column==4):
            return False
        else:
            return True
                                                             
class MyTableModel8(DefaultTableModel):
    def __init__(self,datas):
        #constructor will call when we create the object
        self.cols = None  # Vector<String>
        self.data = None  # Vector<Vector>
        
        self.initCols()
        self.initData(datas)
        self.setDataVector(self.data,self.cols)
        
    def initCols(self):
        self.cols = Vector()
        self.cols.add("Student Id")
        self.cols.add("Student Name")
        self.cols.add("Date")
        self.cols.add("Present")
        
    def initData(self,datas):    
        self.data = Vector()
        for data in datas:
            v = Vector()
            v.add(data[0])
            v.add(data[1].encode('ascii'))
            v.add(data[2])
            ch = data[3].encode('ascii')
            if(ch == 'P'):
                v.add(True)
            elif(ch == 'A'):
                v.add(False)
            self.data.add(v)
    def getColumnClass(self,columnIndex):
        if (columnIndex == 3): 
            type = Boolean
            return type
        else: 
            return super(MyTableModel8, self).getColumnClass(columnIndex)
            
        
    def isCellEditable(self,row,column): 
        if (column == 0 or column == 1 or column==2 or column==3):
            return False
        else:
            return True
        
class MyTableModel9(DefaultTableModel):
    def __init__(self,datas):
        #constructor will call when we create the object
        self.cols = None  # Vector<String>
        self.data = None  # Vector<Vector>
        
        self.initCols()
        self.initData(datas)
        self.setDataVector(self.data,self.cols)
        
    def initCols(self):
        self.cols = Vector()
        self.cols.add("student Id")
        self.cols.add("student name")
        self.cols.add("No of days")
        self.cols.add("No of present days")
        self.cols.add("No of Absent days ")
        
    def initData(self,datas):    
        self.data = Vector()
        for data in datas:
            v = Vector()
            v.add(data[0])
            v.add(data[1].encode('ascii'))
            v.add(data[2])
            v.add(data[3])
            v.add(data[4])
            self.data.add(v)
    
    def isCellEditable(self,row,column): 
        if (column == 0 or column == 1 or column==2 or column==3 or column==4):
            return False
        else:
            return True
                     
class MyTableModel10(DefaultTableModel):
    def __init__(self,datas):
        #constructor will call when we create the object
        self.cols = None  # Vector<String>
        self.data = None  # Vector<Vector>
        
        self.initCols()
        self.initData(datas)
        self.setDataVector(self.data,self.cols)
        
    def initCols(self):
        self.cols = Vector()
        self.cols.add("student Id")
        self.cols.add("student name")
        self.cols.add("Student Phone")
        self.cols.add("student Email")
        self.cols.add("Student Address ")
        self.cols.add("Course name")
    def initData(self,datas):    
        self.data = Vector()
        for data in datas:
            v = Vector()
            v.add(data[0])
            v.add(data[1].encode('ascii'))
            v.add(data[2].encode('ascii'))
            v.add(data[3].encode('ascii'))
            v.add(data[4].encode('ascii'))
            v.add(data[5].encode('ascii'))
            self.data.add(v)
    
    def isCellEditable(self,row,column): 
        if (column == 0 or column == 1 or column==2 or column==3 or column==4 or column==5):
            return False
        else:
            return True
                  
class MyTableModel11(DefaultTableModel):
    def __init__(self,datas):
        #constructor will call when we create the object
        self.cols = None  # Vector<String>
        self.data = None  # Vector<Vector>
        
        self.initCols()
        self.initData(datas)
        self.setDataVector(self.data,self.cols)
        
    def initCols(self):
        self.cols = Vector()
        self.cols.add("student Id")
        self.cols.add("student name")
        self.cols.add("Total Amount")
        self.cols.add("Paid Amount")
        self.cols.add("Remaining Amount ")
        
    def initData(self,datas):    
        self.data = Vector()
        for data in datas:
            v = Vector()
            v.add(data[0])
            v.add(data[1].encode('ascii'))
            v.add(data[2])
            p = int(data[2]) - int(data[4])
            v.add(p)
            v.add(data[4])
            self.data.add(v)
    
    def isCellEditable(self,row,column): 
        if (column == 0 or column == 1 or column==2 or column==3 or column==4):
            return False
        else:
            return True
                     
class MyTableModel12(DefaultTableModel): # for add the student attendence
    def __init__(self,datas,todayDate):
        #constructor will call when we create the object
        self.cols = None  # Vector<String>
        self.data = None  # Vector<Vector>
        
        self.initCols()
        self.initData(datas,todayDate)
        self.setDataVector(self.data,self.cols)
        
    def initCols(self):
        self.cols = Vector()
        self.cols.add("Student Id")
        self.cols.add("Student Name")
        self.cols.add("Date")
        self.cols.add("Present")
        
    def initData(self,datas,todayDate):    
        self.data = Vector()
        for data in datas:
            v = Vector()
            v.add(data[0])
            v.add(data[1].encode('ascii'))
            v.add(todayDate)
            v.add(False)
            self.data.add(v)

    def getColumnClass( self,columnIndex):
        if (columnIndex == 3): 
            type = Boolean
            return type
        else: 
            return super(MyTableModel12, self).getColumnClass(columnIndex)
            
        
        
    
    def isCellEditable( self,row,column): 
        if (column == 0 or column == 1 or column==2 ):
            return False
        else:
            return True
                  
class MyTableModel13(DefaultTableModel): # for updatestudent today attendence 
    def __init__(self, datas):
        #constructor will call when we create the object
        self.cols = None  # Vector<String>
        self.data = None  # Vector<Vector>
        
        self.initCols()
        self.initData(datas)
        self.setDataVector(self.data,self.cols)
        
    def initCols(self):
        self.cols = Vector()
        self.cols.add("Student Id")
        self.cols.add("Student Name")
        self.cols.add("Date")
        self.cols.add("Present")
        
    def initData(self,datas):    
        self.data = Vector()
        for data in datas:
            v = Vector()
            v.add(data[0])
            v.add(data[1].encode('ascii'))
            v.add(data[2])
            ch = data[3].encode('ascii')
            if(ch == 'P'):
                v.add(True)
            elif(ch == 'A'):
                v.add(False)
            self.data.add(v)

    def getColumnClass(self,columnIndex):
        if (columnIndex == 3): 
            type = Boolean
            return type
        else: 
           return super(MyTableModel13, self).getColumnClass(columnIndex)
            
          
        
    def isCellEditable(self,row,column): 
        if (column == 0 or column == 1 or column==2 ):
            return False
        else:
            return True
                                                  
class MyTableModel14(DefaultTableModel): # for show the student attendence (no update)
    def __init__(self, datas):
        #constructor will call when we create the object
        self.cols = None  # Vector<String>
        self.data = None  # Vector<Vector>
        
        self.initCols()
        self.initData(datas)
        self.setDataVector(self.data,self.cols)
        
    def initCols(self):
        self.cols = Vector()
        self.cols.add("Student Id")
        self.cols.add("Student Name")
        self.cols.add("Date")
        self.cols.add("Present")
        
    def initData(self,datas):    
        self.data = Vector()
        for data in datas:
            v = Vector()
            v.add(data[0])
            v.add(data[1].encode('ascii'))
            v.add(data[2])
            ch = data[3].encode('ascii')
            if(ch == 'P'):
                v.add(True)
            elif(ch == 'A'):
                v.add(False)
            self.data.add(v)

    def getColumnClass(self,columnIndex):
        if (columnIndex == 3): 
            type = Boolean
            return type
        else: 
           return super(MyTableModel14, self).getColumnClass(columnIndex)
            
          
        
    def isCellEditable(self,row,column): 
        if (column == 0 or column == 1 or column==2 or column==3):
            return False
        else:
            return True
                                                                                                  