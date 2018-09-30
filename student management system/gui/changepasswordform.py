from javax.swing import JButton,JLabel,JTextField,JPanel,JFrame,JOptionPane
from java.awt import Color
import services as srv
import domain

frame= None
value = None
tfOldPassword = None
tfNewPassword = None
tfConfirmPassword = None

def changePasswordForm(check):    
    global frame
    global tfOldPassword
    global tfNewPassword
    global tfConfirmPassword
    global value
    
    value = check
    
    frame = JFrame("Change Password")
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
    
    heading = JLabel("Change Password")
    heading.setBounds(200,30,150,40)
    
    lbOldPassword = JLabel("Old Password")
    lbNewPassword = JLabel("New Password")
    lbConfirmPassword = JLabel("Confirm Password")
    
    tfOldPassword = JTextField()
    tfNewPassword = JTextField()
    tfConfirmPassword = JTextField()
    
    
    lbOldPassword.setBounds(50,100,150,30)
    lbNewPassword.setBounds(50,150,150,30)
    lbConfirmPassword.setBounds(50,200,150,30)
    
    tfOldPassword.setBounds(220,100,150,30)
    tfNewPassword.setBounds(220,150,150,30)
    tfConfirmPassword.setBounds(220,200,150,30)
    
    btnSave = JButton("Save",actionPerformed=clickSave)
    btnCancel = JButton("Cancel",actionPerformed=clickCancel)
    
    btnSave.setBounds(350,280,100,30)
    btnCancel.setBounds(50,280,100,30)
    
    panel.add(heading)
    panel.add(lbOldPassword)
    panel.add(lbNewPassword)
    panel.add(lbConfirmPassword)
    panel.add(tfOldPassword)
    panel.add(tfNewPassword)
    panel.add(tfConfirmPassword)
    panel.add(btnSave)
    panel.add(btnCancel)
   
    frame.add(panel)

def clickSave(event):
    global frame
    global tfOldPassword
    global tfNewPassword
    global tfConfirmPassword
    
    if(value == "change password for teacher"):
        teacherId = domain.Teacher.teacherId
        check = srv.getTeacherPassword(teacherId)
        if(check == False):
            JOptionPane.showMessageDialog(None,"Failed to match the password")
        elif(len(check) == 0):
            JOptionPane.showMessageDialog(None,"No any teacher of that loginId")
        elif(len(check) != 0):
            if(check[0].encode('ascii') == tfOldPassword.getText()):
                if(tfNewPassword.getText() == tfConfirmPassword.getText()):                    
                    ck = srv.updateTeacherPassword(tfNewPassword.getText())
                    if(ck == False):
                        JOptionPane.showMessageDialog(None,"Failed to update the password")
                    elif(True):
                        JOptionPane.showMessageDialog(None,"Successfully password has been updated")
                        frame.dispose()
                else:
                    JOptionPane.showMessageDialog(None,"new password and confirm password has been not matched and reentered the new password")
                    tfOldPassword.setText("") 
                    tfNewPassword.setText("") 
                    tfConfirmPassword.setText("") 
            else:
                JOptionPane.showMessageDialog(None,"You are not entered the correct old password")
    elif(value == "change password for student"):
        studentId = domain.Student.studentId
        check = srv.getStudentPassword(studentId)
        if(check == False):
            JOptionPane.showMessageDialog(None,"Failed to match the password")
        elif(len(check) == 0):
            JOptionPane.showMessageDialog(None,"No any studnet of that loginId")
        elif(len(check) != 0):
            if(check[0].encode('ascii') == tfOldPassword.getText()):
                if(tfNewPassword.getText() == tfConfirmPassword.getText()):
                    ck = srv.updateStudentPassword(tfNewPassword.getText())
                    if(ck == False):
                        JOptionPane.showMessageDialog(None,"Failed to update the password")
                    elif(True):
                        JOptionPane.showMessageDialog(None,"Successfully password has been updated")
                        frame.dispose()
                else:
                    JOptionPane.showMessageDialog(None,"new password and confirm password has been not matched and reentered the new password")
                    tfOldPassword.setText("") 
                    tfNewPassword.setText("") 
                    tfConfirmPassword.setText("") 
            else:
                JOptionPane.showMessageDialog(None,"You are not entered the correct old password")
def clickCancel(event):
    global frame
    frame.dispose()