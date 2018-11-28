import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class menu_UI(object):

    def setupUi(self, Menu, firstName, lastName, phoneNumber, emailAddress, ID, age, ssn, weight, height,
                creditCardNumber, billingAmount, insuranceNumber, medicationList, appointmentDates, startTimes,
                endTimes, appointmentIDs, doctorID, nurseID, departmentAdminID, num, cur, conn):
        
        # Backup since needed when user want to update profile
        self.ID = ID
        self.age = age
        self.weight = weight
        self.height = height
        self.phoneNumber = phoneNumber[0:3]+'-'+phoneNumber[3:6]+ "-"+phoneNumber[6:10]
        self.ssn = ssn # no formatting for Employee's DptID (ssn is a placeholder for DptID)
        if(num==1):
            self.ssn = ssn[0:3]+'-'+ssn[3:5]+ "-"+ssn[5:10]
        

        Menu.setObjectName("Menu")
        self.centralWidget = QtWidgets.QWidget(Menu)
        self.centralWidget.setObjectName("centralWidget")

        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_7.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setObjectName("gridLayout_7")

        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName("tabWidget")

        # Profile
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")

        self.gridLayout = QtWidgets.QGridLayout(self.tab_1)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")

        self.label_1 = QtWidgets.QLabel(self.tab_1)
        self.label_1.setStyleSheet("color: rgb(46, 125, 132);\n"
                                   "font-weight: bold;\n"
                                   "font: 12pt \"Lucida Calligraphy\";")
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 2, 0, 1, 1)

        self.lineEdit_1 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_1.setText(firstName)
        self.lineEdit_1.setEnabled(False)
        self.gridLayout.addWidget(self.lineEdit_1, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tab_1, "")

        self.label_2 = QtWidgets.QLabel(self.tab_1)
        self.label_2.setStyleSheet("color: rgb(46, 125, 132);\n"
                                   "font-weight: bold;\n"
                                   "font: 12pt \"Lucida Calligraphy\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 3, 1, 1)
        self.lineEdit_2.setText(lastName)
        self.lineEdit_2.setEnabled(False)

        self.label_3 = QtWidgets.QLabel(self.tab_1)
        self.label_3.setStyleSheet("color: rgb(46, 125, 132);\n"
                                   "font-weight: bold;\n"
                                   "font: 12pt \"Lucida Calligraphy\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 4, 1, 1, 1)
        self.lineEdit_3.setText(self.phoneNumber)  
        self.lineEdit_3.setEnabled(False)

        self.label_4 = QtWidgets.QLabel(self.tab_1)
        self.label_4.setStyleSheet("color: rgb(46, 125, 132);\n"
                                   "font-weight: bold;\n"
                                   "font: 12pt \"Lucida Calligraphy\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 2, 1, 1)

        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 4, 3, 1, 1)
        self.lineEdit_4.setText(emailAddress)
        self.lineEdit_4.setEnabled(False)

        self.label_5 = QtWidgets.QLabel(self.tab_1)
        self.label_5.setStyleSheet("color: rgb(46, 125, 132);\n"
                                   "font-weight: bold;\n"
                                   "font: 12pt \"Lucida Calligraphy\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)

        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 6, 1, 1, 1)
        self.lineEdit_5.setText(ID)
        self.lineEdit_5.setEnabled(False)

        self.label_6 = QtWidgets.QLabel(self.tab_1)
        self.label_6.setStyleSheet("color: rgb(46, 125, 132);\n"
                                   "font-weight: bold;\n"
                                   "font: 12pt \"Lucida Calligraphy\";")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 2, 1, 1)

        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 6, 3, 1, 1)
        self.lineEdit_6.setText(self.ssn)
        self.lineEdit_6.setEnabled(False)

        self.label_7 = QtWidgets.QLabel(self.tab_1)
        self.label_7.setStyleSheet("color: rgb(46, 125, 132);\n"
                                   "font-weight: bold;\n"
                                   "font: 12pt \"Lucida Calligraphy\";")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 1)

        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 8, 1, 1, 1)
        self.lineEdit_7.setText(weight)
        self.lineEdit_7.setEnabled(False)

        self.label_8 = QtWidgets.QLabel(self.tab_1)
        self.label_8.setStyleSheet("color: rgb(46, 125, 132);\n"
                                   "font-weight: bold;\n"
                                   "font: 12pt \"Lucida Calligraphy\";")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 8, 2, 1, 1)

        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 8, 3, 1, 1)
        self.lineEdit_8.setText(height)
        self.lineEdit_8.setEnabled(False)

        self.label_9 = QtWidgets.QLabel(self.tab_1)
        self.label_9.setStyleSheet("color: rgb(46, 125, 132);\n"
                                   "font-weight: bold;\n"
                                   "font: 12pt \"Lucida Calligraphy\";")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 10, 0, 1, 1)

        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 10, 1, 1, 1)
        self.lineEdit_9.setText(age)
        self.lineEdit_9.setEnabled(False)

        self.label_10 = QtWidgets.QLabel(self.tab_1)
        self.label_10.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 12pt \"Lucida Calligraphy\";")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 10, 2, 1, 1)

        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_10.setText(medicationList)
        self.gridLayout.addWidget(self.lineEdit_10, 10, 3, 1, 1)
        self.lineEdit_10.setEnabled(False)



        self.EditBtn = QtWidgets.QPushButton(self.tab_1)
        self.EditBtn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.EditBtn.setObjectName("EditBtn")
        self.gridLayout.addWidget(self.EditBtn, 1, 3, 1, 1, QtCore.Qt.AlignRight)

        self.SaveBtn = QtWidgets.QPushButton(self.tab_1)
        self.SaveBtn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.SaveBtn.setObjectName("SaveBtn")
        self.SaveBtn.setEnabled(False)
        self.gridLayout.addWidget(self.SaveBtn, 12, 3, 1, 1, QtCore.Qt.AlignRight)
        

        # Appointmt
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.lineEdit19_1 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit19_1.setMaximumSize(QtCore.QSize(589, 16777215))
        self.lineEdit19_1.setObjectName("lineEdit19_1")
        self.lineEdit19_1.setVisible(False)
        self.gridLayout_2.addWidget(self.lineEdit19_1, 18, 0, 1, 1)
        self.lineEdit19_1.setReadOnly(True)

        self.pushButton19_1 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton19_1.setObjectName("pushButton19_1")
        self.pushButton19_1.setVisible(False)
        self.gridLayout_2.addWidget(self.pushButton19_1, 19, 0, 1, 1)

        self.lineEdit19_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit19_2.setObjectName("lineEdit19_2")
        self.lineEdit19_2.setVisible(False)
        self.gridLayout_2.addWidget(self.lineEdit19_2, 18, 1, 1, 1)
        self.lineEdit19_2.setReadOnly(True)

        self.pushButton19_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton19_2.setObjectName("pushButton19_2")
        self.pushButton19_2.setVisible(False)
        self.gridLayout_2.addWidget(self.pushButton19_2, 19, 1, 1, 1)

        self.lineEdit19_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit19_3.setMaxLength(300)
        self.lineEdit19_3.setReadOnly(True)
        self.lineEdit19_3.setVisible(False)
        self.lineEdit19_3.setObjectName("lineEdit19_3")
        self.gridLayout_2.addWidget(self.lineEdit19_3, 18, 3, 1, 1)

        self.pushButton19_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton19_3.setObjectName("pushButton19_3")
        self.pushButton19_3.setVisible(False)
        self.gridLayout_2.addWidget(self.pushButton19_3, 19, 3, 1, 1)

        self.lineEdit19_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit19_4.setObjectName("lineEdit19_4")
        self.lineEdit19_4.setVisible(False)
        self.gridLayout_2.addWidget(self.lineEdit19_4, 18, 4, 1, 1)
        self.lineEdit19_4.setReadOnly(True)

        self.pushButton19_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton19_4.setObjectName("pushButton19_4")
        self.pushButton19_4.setVisible(False)
        self.gridLayout_2.addWidget(self.pushButton19_4, 19, 4, 1, 1)

        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 12pt Lucida Calligraphy;")
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 1, 3, 1, 1)

        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 12pt Lucida Calligraphy;")
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 3, 3, 1, 1)

        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 12pt Lucida Calligraphy;")
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 5, 3, 1, 1)

        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_19.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 18pt \"Lucida Calligraphy\";")
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 17, 0, 1, 4)

        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.calendarWidget_1 = QtWidgets.QCalendarWidget(self.groupBox)
        self.calendarWidget_1.setObjectName("calendarWidget_1")
        self.calendarWidget_1.setVerticalHeaderFormat(0)

        self.gridLayout_3.addWidget(self.calendarWidget_1, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 2, 0, 1, 1)

        self.label20 = QtWidgets.QLabel(self.groupBox)
        self.label20.setStyleSheet("color: rgb(46, 125, 132);\n"
                                   "font-weight: bold;\n"
                                   "font: 12pt Lucida Calligraphy")
        self.label20.setObjectName("label20")
        self.gridLayout_4.addWidget(self.label20, 1, 0, 1, 1)

        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 9, 2)

        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 12pt Lucida Calligraphy;")
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 0, 3, 1, 2)

        self.pushButton_15 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_2.addWidget(self.pushButton_15, 7, 3, 2, 1)

        self.dateEdit_16 = QtWidgets.QDateEdit(self.tab_2)
        self.dateEdit_16.setObjectName("dateEdit_16")
        self.gridLayout_2.addWidget(self.dateEdit_16, 2, 3, 1, 1)

        self.timeEdit_17 = QtWidgets.QTimeEdit(self.tab_2)
        self.timeEdit_17.setObjectName("timeEdit_17")
        self.gridLayout_2.addWidget(self.timeEdit_17, 4, 3, 1, 1)

        self.timeEdit_18 = QtWidgets.QTimeEdit(self.tab_2)
        self.timeEdit_18.setObjectName("timeEdit_18")
        self.gridLayout_2.addWidget(self.timeEdit_18, 6, 3, 1, 1)

        if num == 1:
            self.tabWidget.addTab(self.tab_2, "")

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_6.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")

        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 12pt \"Lucida Calligraphy\";")
        self.label_11.setObjectName("label_11")
        self.gridLayout_6.addWidget(self.label_11, 0, 0, 1, 1)

        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_11.setMaximumSize(QtCore.QSize(300, 50))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_6.addWidget(self.lineEdit_11, 1, 0, 1, 1)
        self.lineEdit_11.setText(insuranceNumber)

        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 12pt \"Lucida Calligraphy\";")
        self.label_12.setObjectName("label_12")
        self.gridLayout_6.addWidget(self.label_12, 2, 0, 1, 1)

        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_12.setMaximumSize(QtCore.QSize(300, 50))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_6.addWidget(self.lineEdit_12, 3, 0, 1, 1)
        self.lineEdit_12.setText(creditCardNumber)

        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 12pt \"Lucida Calligraphy\";")
        self.label_13.setObjectName("label_13")
        self.gridLayout_6.addWidget(self.label_13, 4, 0, 1, 1)

        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_13.setMaximumSize(QtCore.QSize(300, 50))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout_6.addWidget(self.lineEdit_13, 5, 0, 1, 1)
        self.lineEdit_13.setText(billingAmount)

        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 12pt Lucida Calligraphy;")
        self.label_14.setObjectName("label_14")
        self.gridLayout_6.addWidget(self.label_14, 6, 0, 1, 1)

        self.lineEdit_14 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_14.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_14.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout_6.addWidget(self.lineEdit_14, 7, 0, 1, 1)

        self.pushButton_14 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_14.setMaximumSize(QtCore.QSize(100, 200))
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_6.addWidget(self.pushButton_14, 7, 1, 1, 1)

        # Billing Info
        if num == 1:
            self.tabWidget.addTab(self.tab_3, "")

        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")


        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")

        self.calendarWidget = QtWidgets.QCalendarWidget(self.tab_4)
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.setVerticalHeaderFormat(0)
        self.gridLayout_5.addWidget(self.calendarWidget, 0, 0, 1, 1)

        self.treeWidget = QtWidgets.QTreeWidget(self.tab_4)
        self.treeWidget.setObjectName("treeWidget")

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)

        self.gridLayout_5.addWidget(self.treeWidget, 0, 1, 1, 1)

        if num != 1:
            self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout_7.addWidget(self.tabWidget, 0, 1, 1, 1)
        Menu.setCentralWidget(self.centralWidget)

        self.mainToolBar = QtWidgets.QToolBar(Menu)
        self.mainToolBar.setObjectName("mainToolBar")
        Menu.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)

        self.statusBar = QtWidgets.QStatusBar(Menu)
        self.statusBar.setObjectName("statusBar")
        Menu.setStatusBar(self.statusBar)

        self.retranslateUi(Menu, num)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Menu)

        self.pushButton19_1.clicked.connect(lambda: self.cancelAppt(1, appointmentIDs, cur, conn))

        self.pushButton19_2.clicked.connect(lambda: self.cancelAppt(3, appointmentIDs, cur, conn))
        self.pushButton19_3.clicked.connect(lambda: self.cancelAppt(5, appointmentIDs, cur, conn))
        self.pushButton19_4.clicked.connect(lambda: self.cancelAppt(7, appointmentIDs, cur, conn))
        self.pushButton_15.clicked.connect(lambda: self.scheduleAppt(cur, conn, doctorID, nurseID, departmentAdminID, ID, self.dateEdit_16.date(), self.timeEdit_17.time(), self.timeEdit_18.time(), self.lineEdit19_1, self.lineEdit19_2, self.lineEdit19_3, self.lineEdit19_4, self.pushButton19_1, self.pushButton19_2, self.pushButton19_3, self.pushButton19_4))
        self.pushButton_14.clicked.connect(lambda: self.Pay(ID, cur, conn))

        earliestDate = None

        numDates = 0
        for row in appointmentDates:
            if (earliestDate == None):
                earliestDate = row[0]
            else:
                if (row[0] < earliestDate):
                    earliestDate = row[0]
            if (numDates == 0):
                self.lineEdit19_1.setVisible(True)
                self.pushButton19_1.setVisible(True)
                self.lineEdit19_1.setText(row[0].strftime('%m/%d/%Y'))
                numDates = numDates + 1
            elif (numDates == 1):
                self.lineEdit19_2.setVisible(True)
                self.pushButton19_2.setVisible(True)
                self.lineEdit19_2.setText(row[0].strftime('%m/%d/%Y'))
                numDates = numDates + 1
            elif (numDates == 2):
                self.lineEdit19_3.setVisible(True)
                self.pushButton19_3.setVisible(True)
                self.lineEdit19_3.setText(row[0].strftime('%m/%d/%Y'))
                numDates = numDates + 1
            elif (numDates == 3):
                self.lineEdit19_4.setVisible(True)
                self.pushButton19_4.setVisible(True)
                self.lineEdit19_4.setText(row[0].strftime('%m/%d/%Y'))
                numDates = numDates + 1


        numStarts = 0
        for row in startTimes:
            if (numStarts == 0):
                hours, remainder = divmod(row[0].seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                self.lineEdit19_1.setText(
                    self.lineEdit19_1.text() + "                " + str(hours) + ":" + str(minutes) + ":" + str(
                        seconds))
                numStarts = numStarts + 1
            elif (numStarts == 1):
                hours, remainder = divmod(row[0].seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                self.lineEdit19_2.setText(
                    self.lineEdit19_2.text() + "               " + str(hours) + ":" + str(minutes) + ":" + str(seconds))
                numStarts = numStarts + 1
            elif (numStarts == 2):
                hours, remainder = divmod(row[0].seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                self.lineEdit19_3.setText(
                    self.lineEdit19_3.text() + "                " + str(hours) + ":" + str(minutes) + ":" + str(seconds))
                numStarts = numStarts + 1
            elif (numStarts == 3):
                hours, remainder = divmod(row[0].seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                self.lineEdit19_4.setText(
                    self.lineEdit19_4.text() + "                " + str(hours) + ":" + str(minutes) + ":" + str(seconds))
                numStarts = numStarts + 1

        numEnds = 0
        for row in endTimes:
            if (numEnds == 0):
                hours, remainder = divmod(row[0].seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                self.lineEdit19_1.setText(
                    self.lineEdit19_1.text() + "                " + str(hours) + ":" + str(minutes) + ":" + str(seconds))
                numEnds = numEnds + 1
            elif (numEnds == 1):
                hours, remainder = divmod(row[0].seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                self.lineEdit19_2.setText(
                    self.lineEdit19_2.text() + "                " + str(hours) + ":" + str(minutes) + ":" + str(seconds))
                numEnds = numEnds + 1
            elif (numEnds == 2):
                hours, remainder = divmod(row[0].seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                self.lineEdit19_3.setText(
                    self.lineEdit19_3.text() + "                " + str(hours) + ":" + str(minutes) + ":" + str(seconds))
                numEnds = numEnds + 1
            elif (numEnds == 3):
                hours, remainder = divmod(row[0].seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                self.lineEdit19_4.setText(
                    self.lineEdit19_4.text() + "                " + str(hours) + ":" + str(minutes) + ":" + str(seconds))
                numEnds = numEnds + 1

    def retranslateUi(self, Menu, num):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Menu"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("Menu", "Profile"))

        self.label_9.setText(_translate("Menu", "Age:"))
        self.label_3.setText(_translate("Menu", "Phone Number:"))
        self.label_10.setText(_translate("Menu", "Medication List:"))
        self.label_6.setText(_translate("Menu", "SSN:"))
        self.label_5.setText(_translate("Menu", "ID:"))
        self.label_8.setText(_translate("Menu", "Height:"))
        self.label_2.setText(_translate("Menu", "Last Name:"))
        self.label_7.setText(_translate("Menu", "Weight:"))
        self.label_1.setText(_translate("Menu", "First Name:"))
        self.label_4.setText(_translate("Menu", "Email Address:"))


        # Employee
        if num != 1:
            self.label_6.setText("DepartmentID")
            self.label_9.setVisible(False)
            self.lineEdit_9.setVisible(False)
            self.label_10.setVisible(False)
            self.lineEdit_10.setVisible(False)

            if num == 2 or num == 3: # Doct / Nurse
                self.label_7.setText("Specialty")
                self.label_8.setText("Medical License")
            else:  # Admin
                self.label_7.setText("Security code")
                self.label_8.setVisible(False)
                self.lineEdit_8.setVisible(False)

        


        self.EditBtn.setText(_translate("Menu", "Edit"))
        self.SaveBtn.setText(_translate("Menu", "Save"))

        self.pushButton19_1.setText(_translate("Menu", "Cancel Appointment"))
        self.pushButton19_2.setText(_translate("Menu", "Cancel Appointment"))
        self.pushButton19_3.setText(_translate("Menu", "Cancel Appointment"))
        self.pushButton19_4.setText(_translate("Menu", "Cancel Appointment"))

        self.label_19.setText(_translate("Menu", "Appointments: { Date | Start Time | End Time}"))
        self.label_17.setText(_translate("Menu", "Start Time:"))
        self.label_18.setText(_translate("Menu", "End Time:"))
        self.label_16.setText(_translate("Menu", "Date:"))
        self.label20.setText(_translate("Menu", "Next Appointment Highlighted in Gray: "))
        self.label_15.setText(_translate("Menu", "Schedule Appointment: Max 4"))
        self.pushButton_15.setText(_translate("Menu", "Schedule:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Menu", "Appointment"))
        self.label_14.setText(_translate("Menu", "Payment Amount:"))
        self.label_12.setText(_translate("Menu", "Credit Card Number:"))
        self.label_11.setText(_translate("Menu", "Insurance Number:"))
        self.label_13.setText(_translate("Menu", "Billing Amount:"))
        self.pushButton_14.setText(_translate("Menu", "Pay"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Menu", "Billing Info"))
        self.treeWidget.headerItem().setText(0, _translate("Menu", "Date"))
        self.treeWidget.headerItem().setText(1, _translate("Menu", "Doctor"))
        self.treeWidget.headerItem().setText(2, _translate("Menu", "Patient"))
        self.treeWidget.headerItem().setText(3, _translate("Menu", "Nurse"))
        self.treeWidget.headerItem().setText(4, _translate("Menu", "Medication List"))
        self.treeWidget.headerItem().setText(5, _translate("Menu", "Insurance"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Menu", "New Item"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("Menu", "New Subitem"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Menu", "Appointment Info"))

    def Pay(self, ID, cur, conn):
        if(self.lineEdit_14.text() == "" or self.lineEdit_14.text().replace('.', 1).isdigit() == False):
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setText("Error: Payment Amount Must Be A Number!")
            error_dialog.exec()
        elif (self.lineEdit_13.text() < self.lineEdit_14.text()):
            diff = float(self.lineEdit_14.text()) - float(self.lineEdit_13.text())
            self.lineEdit_14.setText(str(diff))
            self.lineEdit_13.setText("0")
            cur.execute('UPDATE Patient SET BillingAmount = (%s) WHERE PatientID = (%s)', (0, ID))
            conn.commit()
        elif (self.lineEdit_13.text() == self.lineEdit_14.text()):
            self.lineEdit_14.setText("0")
            self.lineEdit_13.setText("0")
            cur.execute('UPDATE Patient SET BillingAmount = (%s) WHERE PatientID = (%s)', (0, ID))
            conn.commit()
        # Negative balance?
        else:
            diff2 = float(self.lineEdit_13.text()) - float(self.lineEdit_14.text())
            self.lineEdit_13.setText(str(diff2))
            self.lineEdit_13.setText("0")
            cur.execute('UPDATE Patient SET BillingAmount = (%s) WHERE PatientID = (%s)', (diff2, ID))
            conn.commit()

    def scheduleAppt(self, cur, conn, doctorID, nurseID, departmentAdminID, ID, Date, StartTime, EndTime, lineEdit1, lineEdit2, lineEdit3, lineEdit4, cancel1, cancel2, cancel3, cancel4):
        if (lineEdit1.isVisible() == True and lineEdit2.isVisible() == True and lineEdit3.isVisible() == True and lineEdit4.isVisible() == True):
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setText("Error: Maximum Scheduled Appointments is 4! Cannot Exceed this Amount!")
            error_dialog.exec()
        else:
            apptID = 1
            cur.rowcount = -1
            cur.execute('SELECT * FROM Appointment WHERE AppointmentID = (%s)', apptID)
            apptID = apptID + 1
            cur.execute('INSERT INTO Appointment(AppointmentID, DoctorID, NurseID, PatientID, DepartmentAdminID, Location, Date, StartTime, EndTime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', (308, 222, 333, 111, 444, "SBU2", '1998-06-06', '12:11:11', '11:12:11'))

            """
            while (cur.rowcount != 0):
                cur.execute('SELECT * FROM Appointment WHERE AppointmentID = (%s)', apptID)
                apptID = apptID + 1
                cur.execute('INSERT INTO Appointment(AppointmentID, DoctorID, NurseID, PatientID, DepartmentAdminID, Location, Date, StartTime, EndTime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                (308, 222, 333, 111, 444, "SBU2", '1998-06-06', '12:11:11', '11:12:11'))
                #(apptID, doctorID[0][0], nurseID[0][0], ID, departmentAdminID[0][0], "Healthcare United", '1998-06-06', '12:11:11', '11:12:11'))
            """           
            if (lineEdit1.isVisible() == False):
                lineEdit1.setVisible(True)
                cancel1.setVisible(True)
                self.setDateAndTimeForViewing(lineEdit1, Date, StartTime, EndTime)

            elif (lineEdit2.isVisible() == False):
                lineEdit2.setVisible(True)
                cancel2.setVisible(True)
                self.setDateAndTimeForViewing(lineEdit2, Date, StartTime, EndTime)

            elif (lineEdit3.isVisible() == False):
                lineEdit3.setVisible(True)
                cancel3.setVisible(True)
                self.setDateAndTimeForViewing(lineEdit3, Date, StartTime, EndTime)

            elif (lineEdit4.isVisible() == False):
                lineEdit4.setVisible(True)
                cancel4.setVisible(True)
                self.setDateAndTimeForViewing(lineEdit4, Date, StartTime, EndTime)

    def setDateAndTimeForViewing(self, lineEdit, Date, StartTime, EndTime):
        
        date = Date.toString("MM'/'dd'/'yyyy")
        sTime = StartTime.toString("                h:m:s ap")
        eTime = EndTime.toString("                h:m:s ap")

        lineEdit.setText(date+ sTime + eTime)
        
        # https://doc-snapshots.qt.io/qt5-5.11/qtime.html
        # I can't remove ap for some reason - Daeun

        """
        hours, remainder = divmod(StartTime.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        lineEdit.setText(
            lineEdit.text() + "                " + str(hours) + ":" + str(minutes) + ":" + str(seconds))
        hours2, remainder2 = divmod(EndTime.seconds2, 3600)
        minutes2, seconds2 = divmod(remainder2, 60)
        lineEdit.setText(
            lineEdit.text() + "                " + str(hours2) + ":" + str(minutes2) + ":" + str(seconds2))
        """

    def cancelAppt(self, num, appointmentIDs, cur, conn):
        if (num == 1):
            self.lineEdit19_1.setText("")
            self.lineEdit19_1.setVisible(False)
            self.pushButton19_1.setVisible(False)
            numAppointment = 0
            appointNum = -1
            for row in appointmentIDs:
                if (numAppointment == 0):
                    appointNum = row[0]
                numAppointment = numAppointment + 1
            cur.execute('DELETE FROM Appointment WHERE AppointmentID = (%s)', appointNum)
            conn.commit()
        if (num == 3):
            self.lineEdit19_2.setText("")
            self.lineEdit19_2.setVisible(False)
            self.pushButton19_2.setVisible(False)
            numAppointment = 0
            appointNum = -1
            for row in appointmentIDs:
                if (numAppointment == 1):
                    appointNum = row[0]
                numAppointment = numAppointment + 1
            print(appointNum)
            cur.execute('DELETE FROM Appointment WHERE AppointmentID = (%s)', appointNum)
            conn.commit()
        if (num == 5):
            self.lineEdit19_3.setText("")
            self.lineEdit19_3.setVisible(False)
            self.pushButton19_3.setVisible(False)
            numAppointment = 0
            appointNum = -1
            for row in appointmentIDs:
                if (numAppointment == 2):
                    appointNum = row[0]
                numAppointment = numAppointment + 1
            cur.execute('DELETE FROM Appointment WHERE AppointmentID = (%s)', appointNum)
            conn.commit()
        if (num == 7):
            self.lineEdit19_4.setText("")
            self.lineEdit19_4.setVisible(False)
            self.pushButton19_4.setVisible(False)
            numAppointment = 0
            appointNum = -1
            for row in appointmentIDs:
                if (numAppointment == 3):
                    appointNum = row[0]
                numAppointment = numAppointment + 1
            cur.execute('DELETE FROM Appointment WHERE AppointmentID = (%s)', appointNum)
            conn.commit()
    
    def editProfile(self, num, cur, conn):
        self.EditBtn.setEnabled(False)
        self.SaveBtn.setEnabled(True)

        self.lineEdit_1.setEnabled(True)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_5.setEnabled(True)
        self.lineEdit_6.setEnabled(True)
        self.lineEdit_7.setEnabled(True)
        self.lineEdit_8.setEnabled(True)
        self.lineEdit_9.setEnabled(True)
        self.lineEdit_10.setEnabled(True)

        # CANNOT be edited
        if num == 1: # Patient
            self.lineEdit_5.setEnabled(False)  # ID
            self.lineEdit_10.setEnabled(False) # Medication List
        else: # Employee
            self.lineEdit_5.setEnabled(False)   # ID
            self.lineEdit_6.setEnabled(False)   # DepartmentID   
            self.lineEdit_7.setEnabled(False)   # Specialty for Doc, Nur and Security Code for Admin

        self.SaveBtn.clicked.connect(lambda: self.saveProfile(num, cur, conn))


    def saveProfile(self, num, cur, conn):

        # Person Error Checking - phone number
        
        if  (self.IsDigitorSpeChar(self.lineEdit_3.text(), "-", 12) == False) or self.lineEdit_3.text()[3] != '-' or self.lineEdit_3.text()[7] != '-' :
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setText("Error: Phone Number Incorrect! Format: xxx-xxx-xxxx")
            error_dialog.exec()

            # Reset to previous data
            self.lineEdit_3.setText(self.phoneNumber)

        else:  
            # phone number reformatted using self.reformat(str)
            cur.execute('UPDATE Person SET FirstName = (%s), LastName = (%s), PhoneNumber = (%s), EmailAddress = (%s) WHERE ID = (%s)', (self.lineEdit_1.text(), self.lineEdit_2.text(), self.reformat(self.lineEdit_3.text()), self.lineEdit_4.text(), self.ID))
            
        if num==1:  # Patient
            # Patient Error Checking - SSN
            if (self.IsDigitorSpeChar(self.lineEdit_6.text(), "-", 11) == False) or self.lineEdit_6.text()[3] != '-' or self.lineEdit_6.text()[6] != '-':
                error_dialog = QtWidgets.QMessageBox()
                error_dialog.setText("Error: SSN Incorrect! Must be 9 numbers long! Format: xxx-xx-xxxx")
                error_dialog.exec()
                self.lineEdit_6.setText(self.ssn)

            elif (self.IsDigitorSpeChar(self.lineEdit_7.text(), ".", -1) == False):
                error_dialog = QtWidgets.QMessageBox()
                error_dialog.setText("Error: Weight Must Be A Number")
                error_dialog.exec()
                self.lineEdit_7.setText(self.weight)

            elif (self.IsDigitorSpeChar(self.lineEdit_8.text(), ".", -1) == False):
                error_dialog = QtWidgets.QMessageBox()
                error_dialog.setText("Error: Height Must Be A Number")
                error_dialog.exec()
                self.lineEdit_8.setText(self.height)

            elif (self.IsDigitorSpeChar(self.lineEdit_9.text(), "", -1) == False):
                error_dialog = QtWidgets.QMessageBox()
                error_dialog.setText("Error: Age Must Be A Number")
                error_dialog.exec()
                self.lineEdit_9.setText(self.age)
          
            # Update self with valid inputs
            self.ssn = self.lineEdit_6.text()
            self.age = self.lineEdit_9.text()
            self.weight = self.lineEdit_7.text()
            self.height = self.lineEdit_8.text()

            cur.execute('UPDATE Patient SET SSN = (%s), Weight = (%s), Height = (%s), Age = (%s) WHERE PatientID = (%s)', (self.reformat(self.lineEdit_6.text()), self.lineEdit_7.text(), self.lineEdit_8.text(), self.lineEdit_9.text(), self.ID))
            
            if num==2: # Doctor
                cur.execute('UPDATE Doctor SET MedicalLicense = (%s) WHERE DoctorID = (%s)', (self.lineEdit_8.text(), self.ID))
            
            if num==3: # Nurse
                cur.execute('UPDATE Nurse SET MedicalLicense = (%s) WHERE NurseID = (%s)', (self.lineEdit_8.text(), self.ID))
            # Admin can't change anything else then Person attributes
            conn.commit()


        self.lineEdit_1.setEnabled(False)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_8.setEnabled(False)
        self.lineEdit_9.setEnabled(False)
        self.lineEdit_10.setEnabled(False)

        self.SaveBtn.setEnabled(False)
        self.EditBtn.setEnabled(True)

    # Remove dashes 
    def reformat(self, str):
        for char in str:
            if char in "-":
                str = str.replace(char, '')
        return str

    # Check if digit or spechar of len = num
    def IsDigitorSpeChar(self, str, spechar, num):
        if(num!=-1): # num=-1 when no need to check len
            if len(str)!=num:
                return False

        for char in str:
            if (char.isdigit() == False) and char not in spechar :
                return False 
         
        return True               

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Menu = QtWidgets.QMainWindow()
    ui = menu_UI()
    ui.setupUi(Menu)
    Menu.show()
    sys.exit(app.exec_())
