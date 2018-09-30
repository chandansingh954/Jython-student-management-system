from javax.swing import JButton,JLabel,JTextField,JPanel,JFrame
from java.awt import Color
import services as srv

frame= None

def showLoginIdPassword(data):    
    global frame
    
    frame = JFrame("Show Id  Password ")
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setSize(500,350)
    frame.setLocation(200,200)
    frame.setLayout(None)
    frame.setVisible(True)
    
    panel = JPanel()
    panel.setSize(500,350)
    panel.setLocation(0,0)
    panel.setLayout(None)
    panel.setVisible(True)
    panel.setBackground(Color.LIGHT_GRAY)
    
    heading = JLabel("LoginId AND Password")
    heading.setBounds(200,30,150,40)
    
    lbLoginId = JLabel("LoginId")
    lbPassword = JLabel("password")
    
    tfLoginId = JTextField(data[0].encode('ascii'))
    tfPassword = JTextField(data[1].encode('ascii'))
    
    tfLoginId.setEditable(False)
    tfPassword.setEditable(False)
    
    lbLoginId.setBounds(50,100,150,30)
    lbPassword.setBounds(50,150,150,30)
    
    tfLoginId.setBounds(220,100,150,30)
    tfPassword.setBounds(220,150,150,30)
    
    btnOk = JButton("Ok",actionPerformed=clickOk)
    
    btnOk.setBounds(250,220,100,30)
    
    panel.add(heading)
    panel.add(lbLoginId)
    panel.add(lbPassword)
    panel.add(tfLoginId)
    panel.add(tfPassword)
    panel.add(btnOk)
    frame.add(panel)

def clickOk(event):
    global frame
    frame.dispose()