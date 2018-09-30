# In main.py we call the first login page of gui  .we make the  gui package in which the first login page 
# is one module and other gui form is inside the gui package and all are imported in __init__.py module and 
# we call the login form module by package name .so we make login frame in method then we import all the methods of gui
#in __init__.py and we call the login frmame.


# we have to import the gui package
# we call this module first and call the method by  gui package ^and call the method  
import gui as g
g.loginPage()