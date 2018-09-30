from javax.swing import JFrame,JButton,JLabel,JTextField,JPanel,JTextArea,JScrollPane
from java.awt import Color
from java.awt import Font
import domain 
import services as  srv

import loginpage as lp

tfName = None
tfPhone = None
taAddress =None
tfAdminLoginId = None
tfAdminPassword = None
frame =None

def instReg():
    global frame
    global tfName
    global tfPhone
    global taAddress
    global tfAdminLoginId
    global tfAdminPassword
    
    frame = JFrame("Registration Form ")
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setSize(500,550)
    frame.setLocation(200,200)
    frame.setLayout(None)
    frame.setVisible(True)
    
    panel = JPanel()
    panel.setSize(500,550)
    panel.setLocation(0,0)
    panel.setLayout(None)
    panel.setBackground(Color.LIGHT_GRAY)
    
    heading = JLabel("Institute Registration Form ")
    heading.setBounds(200,30,150,30)
    
    lbName = JLabel("Name")
    lbPhone =JLabel("Phone no ")
    lbAddress = JLabel("Address")
    lbAdminLoginId = JLabel("Admin login  ")
    lbAdminPassword =JLabel("Admin Password")

    font =  Font("Courier",Font.PLAIN,16)		
    
    tfName = JTextField()
    tfPhone = JTextField()
    taAddress =JTextArea()
    tfAdminLoginId = JTextField()
    tfAdminPassword = JTextField()
    
    lbName.setBounds(70,100,150,40)
    lbPhone.setBounds(70,150,150,40)
    lbAddress.setBounds(70,200,150,40)
    lbAdminLoginId.setBounds(70,310,150,40)
    lbAdminPassword.setBounds(70,360,150,40)
    
    tfName = JTextField()
    tfPhone = JTextField()
    taAddress = JTextArea()
    tfAdminLoginId = JTextField()
    tfAdminPassword = JTextField()
    
    tfName.setBounds(250,100,200,40)
    tfPhone.setBounds(250,150,200,40)
    taAddress.setBounds(250,200,200,100)
    tfAdminLoginId.setBounds(250,310,200,40)
    tfAdminPassword.setBounds(250,360,200,40)
    
    tfName.setFont(font)
    tfPhone.setFont(font)
    taAddress.setFont(font)
    tfAdminLoginId.setFont(font)
    tfAdminPassword.setFont(font) 
    
    sp = JScrollPane(taAddress)
    c = frame.getContentPane()
    
    btnSave = JButton("Save",actionPerformed=clickAdminReg)
    btnSave.setBounds(350,420,80,30)
    
    
    
    #panel.add(lbName)
    #panel.add(lbPhone)
    #panel.add(lbAddress)
    #panel.add(lbAdminLoginId)
    #panel.add(lbAdminPassword)
    #panel.add(tfName)
    #panel.add(tfPhone)
    #panel.add(c)
    #panel.add(tfAdminLoginId)
    #panel.add(tfAdminPassword)
    #panel.add(btnSave)
    #panel.add(btnLogin)
    
    c.add(lbName)
    c.add(lbPhone)
    c.add(lbAddress)
    c.add(lbAdminLoginId)
    c.add(lbAdminPassword)
    c.add(tfName)
    c.add(tfPhone)
    c.add(taAddress)
    c.add(tfAdminLoginId)
    c.add(tfAdminPassword)
    c.add(btnSave)
    
    frame.add(c)
    
    
def clickAdminReg(event):
    global tfName
    global tfPhone
    global taAddress
    global tfAdminLoginId
    global tfAdminPassword
    
    insObj = domain.Institute()
    setattr(insObj,'name',tfName.getText())
    setattr(insObj,'phone',tfPhone.getText())
    setattr(insObj,'address',taAddress.getText())
    setattr(insObj,'adminLoginId',tfAdminLoginId.getText())
    setattr(insObj,'adminPassword',tfAdminPassword.getText())
    
    check = srv.instituteRegistration(insObj) # this is the module in different package sowe call the method by package name
    if(check == True): 
        # means successfully registered
        frame.dispose()
        lp.loginPage()

    