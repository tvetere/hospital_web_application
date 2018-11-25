import sys
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication

# import modules
from welcome_page import welcome_page_UI
from login_or_register import login_or_register_UI
from common_login import common_login_UI
from access_code import access_code_UI
from common_signup import common_signup_UI
from menu import menu_UI


class test(object):
    # By default, initialize window to welcome_page.UI
    def __init__(self, parent=None):
        w = welcome_page_UI()
        w.setupUi(MainWindow)

        # when user selects an option(patientBtn for now), set window to login_or_register.py
        w.patientBtn.clicked.connect(lambda: self.setwindowTo_login_or_reigster(1))
        w.doctorBtn.clicked.connect(lambda: self.setwindowTo_login_or_reigster(2))
        w.nurseBtn.clicked.connect(lambda: self.setwindowTo_login_or_reigster(3))
        w.departmentAdminBtn.clicked.connect(
            lambda: self.setwindowTo_login_or_reigster(4)
        )

        MainWindow.showMaximized()

    def setwindowTo_login_or_reigster(self, num):
        w = login_or_register_UI()
        w.setupUi(MainWindow, num)

        w.commonLoginBtn.clicked.connect(lambda: self.setwindowTo_common_login(num))
        w.accesscodeBtn.clicked.connect(lambda: self.setwindowTo_access_code(num))

        MainWindow.showMaximized()

    def setwindowTo_common_login(self, num):
        w = common_login_UI()
        w.setupUi(MainWindow, num)

        w.loginBtn.clicked.connect(lambda: self.authenticate_user(w))

        MainWindow.showMaximized()

    def authenticate_user(self, w):
        w.authenticate_user(cur)

        # if user exists
        if w.ID is not None:
            self.setwindowTo_menu(w)
        # else, still on event listener

    def setwindowTo_access_code(self, num):
        w = access_code_UI()
        w.setupUi(MainWindow, num)
        w.pushButton.clicked.connect(lambda: self.authenticate_access_code(w))
        MainWindow.showMaximized()

    def authenticate_access_code(self, w):
        w.authenticate_access_code(cur)

        if w.rowcount != 0:
            self.setwindowTo_common_signup()

    def setwindowTo_common_signup(self):
        w = common_signup_UI()
        w.setupUi(MainWindow)

        MainWindow.showMaximized()

    def setwindowTo_menu(self, w):
        menu_UI().setupUi(
            MainWindow,
            w.firstName,
            w.lastName,
            w.phoneNumber,
            w.emailAddress,
            w.ID,
            w.age,
            w.ssn,
            w.weight,
            w.height,
            w.creditCardNumber,
            w.billingAmount,
            w.insuranceNumber,
            w.medicationList,
            w.appointmentDates,
            w.startTimes,
            w.endTimes,
            w.appointmentIDs,
            cur,
            conn,
        )

        MainWindow.showMaximized()


if __name__ == "__main__":
    # Initialize database connection
    # commented out by Daeun for test run
    """
    conn = pymysql.connect(
        host="localhost", port=3306, user="root", passwd="root", db="hospital"
    )
    """
    conn = pymysql.connect(
        host="10.245.235.98",
        port=3306,
        user="root",
        passwd="hospitalCSE305!",
        db="hospital",
    )

    # Initialize the database cursor
    cur = conn.cursor()

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()

    # Create an instance of test
    m = test()

    sys.exit(app.exec_())
