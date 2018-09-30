from javax.swing import JFrame,JButton,JLabel,JTextField,JTextArea,JScrollPane,JPanel
from java.awt import Color
import services as srv
import domain

tfStudentId =None
tfStudentName= None
tfTotalAmount = None
tfPaidAmount = None
tfRemainingAmount = None
frame = None


def createStudentFeeForm(stFeeObj):
    
    global tfStudentId
    global tfStudentName
    global tfTotalAmount
    global tfPaidAmount
    global tfRemainingAmount 
    global frame
    
    frame = JFrame("Student Fee Form ")
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setSize(500,500)
    frame.setLocation(200,200)
    frame.setLayout(None)
    frame.setVisible(True)
    
    panel = JPanel()
    panel.setSize(500,500)
    panel.setLocation(0,0)
    panel.setLayout(None)
    panel.setVisible(True)
    panel.setBackground(Color.LIGHT_GRAY)
    
    heading = JLabel("STUDENT FEE")
    heading.setBounds(200,30,150,40)

    lbStudentId = JLabel(" Student id")
    lbStudentName = JLabel(" student name")
    lbTotalAmount = JLabel("Total Amount ")
    lbPaidAmount = JLabel("Paid Amount")
    lbRemainingAmount = JLabel("Remaining amount")
    
    studentId =getattr(stFeeObj,'studentId')
    studentName =getattr(stFeeObj,'studentName')
    totalAmount =getattr(stFeeObj,'totalAmount')
    paidAmount =getattr(stFeeObj,'paidAmount')
    remainingAmount =getattr(stFeeObj,'remainingAmount')
    
    
    tfStudentId = JTextField(str(studentId))
    tfStudentName = JTextField(str(studentName))
    tfTotalAmount = JTextField(str(totalAmount))
    tfPaidAmount = JTextField(str(paidAmount))
    tfRemainingAmount = JTextField(str(remainingAmount))
    
    tfStudentId.setEditable(False)
    tfStudentName.setEditable(False)
    tfTotalAmount.setEditable(False)
    tfRemainingAmount.setEditable(False)
    
    lbStudentId.setBounds(70,100,130,30)
    lbStudentName.setBounds(70,150,130,30)
    lbTotalAmount.setBounds(70,200,130,30)
    lbPaidAmount.setBounds(70,250,130,30)
    lbRemainingAmount.setBounds(70,300,130,30)
    
    tfStudentId.setBounds(220,100,130,30)
    tfStudentName.setBounds(220,150,130,30)
    tfTotalAmount.setBounds(220,200,130,30)
    tfPaidAmount.setBounds(220,250,130,30)
    tfRemainingAmount.setBounds(220,300,130,30)
    
    btnPay = JButton("Paid",actionPerformed=clickPay)
    btnPay.setBounds(350,410,100,40)
    
    btnCancel = JButton("Cancel",actionPerformed=clickbtnCancelForm)
    btnCancel.setBounds(50,410,100,40)
    
    panel.add(heading)
    panel.add(lbStudentId)
    panel.add(lbStudentName)
    panel.add(lbTotalAmount)
    panel.add(lbPaidAmount)
    panel.add(lbRemainingAmount)
    panel.add(tfStudentId)
    panel.add(tfStudentName)
    panel.add(tfTotalAmount)
    panel.add(tfPaidAmount)
    panel.add(tfRemainingAmount)
    panel.add(btnPay)
    panel.add(btnCancel)
    
    frame.add(panel)
def clickbtnCancelForm(event):
    global frame
    frame.dispose()

def clickPay(event):
    global tfStudentId
    global tfStudentName
    global tfTotalAmount
    global tfPaidAmount
    global tfRemainingAmount 
    global frame
    
    if(int(tfPaidAmount.getText()) > int(tfRemainingAmount.getText())):
        JOptionPane.showMessageDialog(None,"Pay Amountis greter than remaining amount")
    elif(int(tfPaidAmount.getText()) <= int(tfRemainingAmount.getText())):
        remainingAmount = int(tfRemainingAmount.getText()) - int(tfPaidAmount.getText())
        print remainingAmount
        check = srv.updateStudentFee(remainingAmount,tfStudentId.getText())
        if(check==True):
            frame.dispose()
    
 