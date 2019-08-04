import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
conn= sqlite3.connect("data.db")

class Ui_EvaluateWindow(object):
    def setupUi(self, EvaluateWindow):
        EvaluateWindow.setObjectName("EvaluateWindow")
        EvaluateWindow.resize(699, 509)
        self.centralwidget = QtWidgets.QWidget(EvaluateWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 180, 521, 251))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.PlayerList = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.PlayerList.setObjectName("listView")
        self.horizontalLayout.addWidget(self.PlayerList)
        
        self.ScoreList = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.ScoreList.setObjectName("listView_2")
        self.horizontalLayout.addWidget(self.ScoreList)

        
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(100, 110, 501, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        #label players
        self.Players = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Players.setFont(font)
        self.Players.setAlignment(QtCore.Qt.AlignCenter)
        self.Players.setIndent(10)
        self.Players.setObjectName("Players")
        self.horizontalLayout_2.addWidget(self.Players)

        #label points
        self.Points = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Points.setFont(font)
        self.Points.setAlignment(QtCore.Qt.AlignCenter)
        self.Points.setIndent(10)
        self.Points.setObjectName("Points")
        self.horizontalLayout_2.addWidget(self.Points)

        #PUSHBUTTON
        self.Calculate = QtWidgets.QPushButton(self.centralwidget)
        self.Calculate.setGeometry(QtCore.QRect(300, 440, 93, 28))
        self.Calculate.setObjectName("Calculate")
        

        #combox 1
        self.SelectTeam = QtWidgets.QComboBox(self.centralwidget)
        self.SelectTeam.setGeometry(QtCore.QRect(150, 50, 141, 22))
        self.SelectTeam.setObjectName("SelectTeam")
        self.SelectTeam.addItem("")
        self.SelectTeam.addItem("")
        self.SelectTeam.addItem("")
        self.SelectTeam.addItem("")
        self.SelectTeam.addItem("")
        self.SelectTeam.addItem("")
        self.SelectTeam.addItem("")
        self.SelectTeam.addItem("")
        self.SelectTeam.addItem("")
        self.SelectTeam.addItem("")
        self.SelectTeam.addItem("")
        self.SelectTeam.addItem("")
        
        #combox2
        self.Selectmatch = QtWidgets.QComboBox(self.centralwidget)
        self.Selectmatch.setGeometry(QtCore.QRect(400, 50, 141, 22))
        self.Selectmatch.setObjectName("Selectmatch")
        self.SelectTeam.addItem("")
        self.Selectmatch.addItem("")
        self.Selectmatch.addItem("")
        self.Selectmatch.addItem("")
        self.Selectmatch.addItem("")
        self.Selectmatch.addItem("")
        
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(60, 80, 591, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        EvaluateWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(EvaluateWindow)
        self.statusbar.setObjectName("statusbar")
        EvaluateWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EvaluateWindow)
        QtCore.QMetaObject.connectSlotsByName(EvaluateWindow)

        self.loadteam()
        
    def retranslateUi(self, EvaluateWindow):
        _translate = QtCore.QCoreApplication.translate
        EvaluateWindow.setWindowTitle(_translate("EvaluateWindow", "MainWindow"))
        self.Players.setText(_translate("EvaluateWindow", "Players"))
        self.Points.setText(_translate("EvaluateWindow", "Points"))
        self.Calculate.setText(_translate("EvaluateWindow", "Calculate"))
        self.SelectTeam.setItemText(0,_translate('EvaluateWindow', "--SELECT TEAM--"))
        self.Selectmatch.setItemText(0,_translate('EvaluateWindow', "--SELECT MATCH--"))
        self.Selectmatch.setItemText(1,_translate('EvaluateWindow', " Match 1 "))
        self.Selectmatch.setItemText(2,_translate('EvaluateWindow', " Match 2 "))
        self.Selectmatch.setItemText(3,_translate('EvaluateWindow', " Match 3 "))
        self.Calculate.clicked.connect(self.show_myteam)


    
    def loadteam(self):
        cur = conn.cursor()
        cur.execute(f"select * from team_name;")
        rows = cur.fetchall()
        for i in range(len(rows)):
            self.SelectTeam.setItemText(i,rows[i][0])


    def show_myteam(self):
        x = self.SelectTeam.currentText()
        cur = conn.cursor()
        cur.execute(f"select * from {x};")
        rows = cur.fetchall()
        total = 0
        for row in rows:
            self.PlayerList.addItem(row[0])
            self.ScoreList.addItem(str(row[1]))
            total += int(row[1])
        
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle("Total Score")

        msg.setText(f"Your Team Score : {total}")
        msg.exec_()

        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EvaluateWindow = QtWidgets.QMainWindow()
    ui = Ui_EvaluateWindow()
    ui.setupUi(EvaluateWindow)
    EvaluateWindow.show()
    sys.exit(app.exec_())
