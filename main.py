# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fantasydesign.ui',
# licensing of 'fantasydesign.ui' applies.
#
# Created: Thu Aug  1 22:57:15 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sqlite3 as sql
from PySide2 import QtCore, QtGui, QtWidgets

conn = sql.connect("data.db") # connecting database

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1003, 704)
        MainWindow.setStyleSheet("background-color: black; color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.mainframe = QtWidgets.QFrame(self.centralwidget)
        self.mainframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainframe.setObjectName("mainframe")
        self.statusframe = QtWidgets.QFrame(self.mainframe)
        self.statusframe.setGeometry(QtCore.QRect(20, 20, 929, 109))
        self.statusframe.setStyleSheet("border: 1px solid white;")
        self.statusframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.statusframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.statusframe.setObjectName("statusframe")
        self.selectionlabel = QtWidgets.QLabel(self.statusframe)
        self.selectionlabel.setGeometry(QtCore.QRect(0, 0, 111, 31))
        self.selectionlabel.setStyleSheet("font-style:italic;")
        self.selectionlabel.setObjectName("selectionlabel")
        self.label = QtWidgets.QLabel(self.statusframe)
        self.label.setGeometry(QtCore.QRect(50, 50, 91, 21))
        self.label.setStyleSheet("border:none;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.statusframe)
        self.label_2.setGeometry(QtCore.QRect(300, 50, 91, 21))
        self.label_2.setStyleSheet("border:none;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.statusframe)
        self.label_3.setGeometry(QtCore.QRect(490, 50, 101, 21))
        self.label_3.setStyleSheet("border:none;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.statusframe)
        self.label_4.setGeometry(QtCore.QRect(730, 50, 121, 21))
        self.label_4.setStyleSheet("border:none;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.statusframe)
        self.label_5.setGeometry(QtCore.QRect(850, 90, 51, 16))
        self.label_5.setStyleSheet("border:none;")
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.statusframe)
        self.lineEdit_5.setGeometry(QtCore.QRect(890, 90, 21, 16))
        self.lineEdit_5.setStyleSheet("border:none;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.batlabel = QtWidgets.QLabel(self.statusframe)
        self.batlabel.setGeometry(QtCore.QRect(150, 50, 31, 21))
        self.batlabel.setStyleSheet("color:blue; font-size:28px;border:none;")
        self.batlabel.setObjectName("batlabel")
        self.bowlabel = QtWidgets.QLabel(self.statusframe)
        self.bowlabel.setGeometry(QtCore.QRect(400, 50, 31, 21))
        self.bowlabel.setStyleSheet("color:blue; font-size:28px;border:none;")
        self.bowlabel.setObjectName("bowlabel")
        self.arlabel = QtWidgets.QLabel(self.statusframe)
        self.arlabel.setGeometry(QtCore.QRect(600, 50, 31, 21))
        self.arlabel.setStyleSheet("color:blue; font-size:28px;border:none;")
        self.arlabel.setObjectName("arlabel")
        self.wklabel = QtWidgets.QLabel(self.statusframe)
        self.wklabel.setGeometry(QtCore.QRect(860, 50, 31, 21))
        self.wklabel.setStyleSheet("color:blue; font-size:28px;border:none;")
        self.wklabel.setObjectName("wklabel")
        self.pointframe = QtWidgets.QFrame(self.mainframe)
        self.pointframe.setGeometry(QtCore.QRect(20, 130, 931, 41))
        self.pointframe.setStyleSheet("")
        self.pointframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pointframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pointframe.setObjectName("pointframe")
        self.label_7 = QtWidgets.QLabel(self.pointframe)
        self.label_7.setGeometry(QtCore.QRect(0, 20, 111, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.pointframe)
        self.label_8.setGeometry(QtCore.QRect(550, 20, 81, 21))
        self.label_8.setObjectName("label_8")
        self.pavlabel = QtWidgets.QLabel(self.pointframe)
        self.pavlabel.setGeometry(QtCore.QRect(100, 20, 41, 20))
        self.pavlabel.setObjectName("pavlabel")
        self.puslabel = QtWidgets.QLabel(self.pointframe)
        self.puslabel.setGeometry(QtCore.QRect(630, 20, 41, 20))
        self.puslabel.setObjectName("puslabel")
        self.teamframe = QtWidgets.QFrame(self.mainframe)
        self.teamframe.setGeometry(QtCore.QRect(19, 170, 931, 421))
        self.teamframe.setStyleSheet("")
        self.teamframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.teamframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.teamframe.setObjectName("teamframe")
        self.frame_5 = QtWidgets.QFrame(self.teamframe)
        self.frame_5.setGeometry(QtCore.QRect(0, 0, 361, 421))
        self.frame_5.setStyleSheet("border:1px solid white;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.radioframe = QtWidgets.QFrame(self.frame_5)
        self.radioframe.setGeometry(QtCore.QRect(0, 0, 361, 51))
        self.radioframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.radioframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.radioframe.setObjectName("radioframe")
        self.batradio = QtWidgets.QRadioButton(self.radioframe)
        self.batradio.setGeometry(QtCore.QRect(10, 10, 51, 20))
        self.batradio.setStyleSheet("border:none;")
        self.batradio.setObjectName("batradio")
        self.bowlradio = QtWidgets.QRadioButton(self.radioframe)
        self.bowlradio.setGeometry(QtCore.QRect(90, 10, 61, 20))
        self.bowlradio.setStyleSheet("border:none;")
        self.bowlradio.setObjectName("bowlradio")
        self.arradio = QtWidgets.QRadioButton(self.radioframe)
        self.arradio.setGeometry(QtCore.QRect(190, 10, 51, 20))
        self.arradio.setStyleSheet("border:none;")
        self.arradio.setObjectName("arradio")
        self.wkradio = QtWidgets.QRadioButton(self.radioframe)
        self.wkradio.setGeometry(QtCore.QRect(280, 10, 51, 20))
        self.wkradio.setStyleSheet("border:none;")
        self.wkradio.setObjectName("wkradio")
        self.availablelist = QtWidgets.QListWidget(self.frame_5)
        self.availablelist.setGeometry(QtCore.QRect(0, 50, 361, 371))
        self.availablelist.setStyleSheet("background-color:white;color:black;")
        self.availablelist.setObjectName("availablelist")
        self.frame_7 = QtWidgets.QFrame(self.teamframe)
        self.frame_7.setGeometry(QtCore.QRect(550, 0, 381, 421))
        self.frame_7.setStyleSheet("border:1px solid white;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.teamnameframe = QtWidgets.QFrame(self.frame_7)
        self.teamnameframe.setGeometry(QtCore.QRect(0, 0, 381, 51))
        self.teamnameframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.teamnameframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.teamnameframe.setObjectName("teamnameframe")
        self.label_9 = QtWidgets.QLabel(self.teamnameframe)
        self.label_9.setGeometry(QtCore.QRect(30, 15, 81, 21))
        self.label_9.setStyleSheet("border:none;")
        self.label_9.setObjectName("label_9")
        self.namelabel = QtWidgets.QLabel(self.teamnameframe)
        self.namelabel.setGeometry(QtCore.QRect(120, 15, 111, 21))
        self.namelabel.setStyleSheet("font-size:20px;color:red;border:none;")
        self.namelabel.setObjectName("namelabel")
        self.usedlist = QtWidgets.QListWidget(self.frame_7)
        self.usedlist.setGeometry(QtCore.QRect(0, 50, 381, 371))
        self.usedlist.setStyleSheet("background-color:white;color:black;")
        self.usedlist.setObjectName("usedlist")
        self.gridLayout.addWidget(self.mainframe, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1003, 26))
        self.menubar.setStyleSheet("background-color:white; color:black;")
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Team = QtWidgets.QAction(MainWindow)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionOpen_Team = QtWidgets.QAction(MainWindow)
        self.actionOpen_Team.setObjectName("actionOpen_Team")
        self.actionSave_Team = QtWidgets.QAction(MainWindow)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.actionEvaluate_Team = QtWidgets.QAction(MainWindow)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")
        self.menuManage_Teams.addAction(self.actionNew_Team)
        self.menuManage_Teams.addAction(self.actionOpen_Team)
        self.menuManage_Teams.addAction(self.actionSave_Team)
        self.menuManage_Teams.addAction(self.actionEvaluate_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        # Adding Events
        self.actionNew_Team.triggered.connect(self.createTeam)
        self.actionSave_Team.triggered.connect(self.savemyteam)
        self.actionOpen_Team.triggered.connect(self.openmyteam)
        self.actionEvaluate_Team.triggered.connect(self.evaluate_tab)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.selectionlabel.setText(QtWidgets.QApplication.translate("MainWindow", "Your Selections", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Batsman(BAT) : ", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Bowlers(BOW) : ", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "All Rounder(AR) : ", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Wicket Keeper(WK) : ", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "Total : ", None, -1))
        self.lineEdit_5.setText(QtWidgets.QApplication.translate("MainWindow", "11", None, -1))
        self.batlabel.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.bowlabel.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.arlabel.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.wklabel.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("MainWindow", "Points Available : ", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("MainWindow", "Points Used: ", None, -1))
        self.pavlabel.setText(QtWidgets.QApplication.translate("MainWindow", "1000", None, -1))
        self.puslabel.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.batradio.setText(QtWidgets.QApplication.translate("MainWindow", "BAT", None, -1))
        self.bowlradio.setText(QtWidgets.QApplication.translate("MainWindow", "Bowl", None, -1))
        self.arradio.setText(QtWidgets.QApplication.translate("MainWindow", "AR", None, -1))
        self.wkradio.setText(QtWidgets.QApplication.translate("MainWindow", "Wk", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("MainWindow", "Team Name: ", None, -1))
        self.namelabel.setText(QtWidgets.QApplication.translate("MainWindow", "----", None, -1))
        self.menuManage_Teams.setTitle(QtWidgets.QApplication.translate("MainWindow", "Manage Teams", None, -1))
        self.actionNew_Team.setText(QtWidgets.QApplication.translate("MainWindow", "New Team", None, -1))
        self.actionOpen_Team.setText(QtWidgets.QApplication.translate("MainWindow", "Open Team", None, -1))
        self.actionSave_Team.setText(QtWidgets.QApplication.translate("MainWindow", "Save Team", None, -1))
        self.actionEvaluate_Team.setText(QtWidgets.QApplication.translate("MainWindow", "Evaluate Team", None, -1))

        #adding Event
        self.availablelist.doubleClicked.connect(self.addto_teamlist)
        self.usedlist.doubleClicked.connect(self.removefrom_teamlist)

        # adding Event for radio button
        self.batradio.clicked.connect(self.loadbatsman)
        self.bowlradio.clicked.connect(self.loadbowler)
        self.arradio.clicked.connect(self.loadallrounder)
        self.wkradio.clicked.connect(self.loadwiket)



        # team data storing 
        self.team_name = ""
        self.player_name = []
        self.point_value = []
        self.player_score = []

    








# Menu bar trigreed function calls 
    def createTeam(self): # When clicked on New Team 
        self.teamtext, self.okPressed = QtWidgets.QInputDialog.getText(self, "Get text","Your name:", QtWidgets.QLineEdit.Normal, "")
        if self.okPressed and self.teamtext != '':
            self.namelabel.setText(self.teamtext)
        self.usedlist.clear()
        self.pavlabel.setText("1000")
        self.puslabel.setText("0")
        self.batlabel.setText("-")
        self.bowlabel.setText("-")
        self.arlabel.setText("-")
        self.wklabel.setText("-")
    
    def savemyteam(self): # When clicked on Save Team
        if len(self.player_name) != 11:
            self.error_cannotSave()
            return None
        self.evaluate_myteam()
        self.team_name = self.namelabel.text()
        cur = conn.cursor()
        cur.execute(f"insert into team_name values('{self.team_name}');")
        cur.execute(f"DROP TABLE IF EXISTS {self.team_name};")
        cur.execute(f"create table {self.team_name}(player_name string, player_score int);")
        for i in range(len(self.player_name)):
            cur.execute(f"insert into {self.team_name} values('{self.player_name[i]}',{self.player_score[i]});")
        conn.commit()
        self.sucess_save()
    
    def openmyteam(self): # When clicked on Open Team
        self.teamtext, self.okPressed = QtWidgets.QInputDialog.getText(self, "Get text","Type the name of Team:", QtWidgets.QLineEdit.Normal, "")
        if self.okPressed and self.teamtext != '':
            cur = conn.cursor()
            cur.execute(f"select * from team_name where name = '{self.teamtext}';")
            rows = cur.fetchall()
            if (len(rows) <= 0):
                self.error_invalidteamname() 
                return None
            cur.execute(f"select * from {self.teamtext};")
            rows = cur.fetchall()
            
            self.usedlist.clear()
            for names in rows:
                self.usedlist.addItem(names[0])

            self.pavlabel.setText("0")
            self.puslabel.setText("0")
            self.batlabel.setText("-")
            self.bowlabel.setText("-")
            self.arlabel.setText("-")
            self.wklabel.setText("-")
            self.namelabel.setText(self.teamtext)

    def evaluate_tab(self): # When clicked on Evaluate Team
        import os 
        os.system('python evaluate.py')
        



# Helping Function Called by savemyteam function 
    def evaluate_myteam(self):
        for name in self.player_name:
            cur = conn.cursor()
            cur.execute(f"select * from team_india where player_name = '{name}';")
            rows = cur.fetchall()
            total = 0
            total = rows[0][1]/2 + rows[0][2] + rows[0][3]*2 + rows[0][8]*10 + rows[0][9]*10 + rows[0][10]*10 + rows[0][11]*10 
            if(rows[0][1] >= 100):
                total+=10
            elif(rows[0][1] >= 50):
                total+=50
            if(rows[0][2] == 0):
                pass
            elif(rows[0][1]/rows[0][2] > 100):
                total+=4
            elif(rows[0][1]/rows[0][2] >= 80):
                total+=2
            if(rows[0][8] >= 5):
                total+=10
            elif(rows[0][8] >= 3):
                total+=5
            if(rows[0][5] == 0):
                pass  
            elif(rows[0][7]/(rows[0][5]/6) < 2):
                total+=10
            elif(rows[0][7]/(rows[0][5]/6) < 3.5):
                total+=7
            elif(rows[0][7]/(rows[0][5]/6) < 4.5):
                total+=4
            self.player_score.append(total)

# Trigred Function When Double cliked on player name 
    def addto_teamlist(self,item):
        if len(self.usedlist.findItems(item.data(),QtCore.Qt.MatchContains)) > 0:
            self.ErrorRepeatplayer()
            return None
        if self.pointchange(item) == "exit":
            return None
        if self.changeselectionlabel(item) == "exit":
            return None
        self.usedlist.addItem(item.data())
        self.availablelist.takeItem(item.row())

# Trigrred Function When Double clicked on player name
    def removefrom_teamlist(self,item):
        if( ")" not in item.data()):
            self.readonly()
            return None

        self.decreasepoints(item)
        self.usedlist.takeItem(item.row())





# Loading the team list on cliking Radio button
    def loadbatsman(self):
        if self.namelabel.text() == "----":
            self.errorteam()
            return None
        self.availablelist.clear() 
        cur = conn.cursor()
        cur.execute("select player_name, catgory, value from team_india;")
        rows = cur.fetchall()
        for row in rows:
            if row[1] == "BAT":
                self.availablelist.addItem(row[0]+" ("+row[1]+")")
    
    def loadbowler(self):
        if self.namelabel.text() == "----":
            self.errorteam()
            return None
        self.availablelist.clear()
        cur = conn.cursor()
        cur.execute("select player_name, catgory, value from team_india;")
        rows = cur.fetchall()
        for row in rows:
            if row[1] == "BWL":
                self.availablelist.addItem(row[0]+" ("+row[1]+")")
        
    def loadallrounder(self):
        if self.namelabel.text() == "----":
            self.errorteam()
            return None
        self.availablelist.clear()
        cur = conn.cursor()
        cur.execute("select player_name, catgory, value from team_india;")
        rows = cur.fetchall()
        for row in rows:
            if row[1] == "AR":
                self.availablelist.addItem(row[0]+"  ("+row[1]+")")

    def loadwiket(self):
        if self.namelabel.text() == "----":
            self.errorteam()
            return None
        self.availablelist.clear()
        cur = conn.cursor()
        cur.execute("select player_name, catgory, value/10 from team_india;")
        rows = cur.fetchall()
        for row in rows:
            if row[1] == "WK":
                self.availablelist.addItem(row[0]+"  ("+row[1]+")")




# function to Change the Number of Player Selected
    def changeselectionlabel(self,item):
        s = item.data()
        self.foo1 = s[len(s)-3:len(s)-1]
        if self.foo1 == "AT":
            self.batlabel.setText(str(int(self.batlabel.text()) + 1))
        elif self.foo1 == "WL":
            self.bowlabel.setText(str(int(self.bowlabel.text()) + 1))
        elif self.foo1 == "AR":
            self.arlabel.setText(str(int(self.arlabel.text()) + 1))
        elif self.foo1 == "WK":
            if self.wklabel.text() == "1":
                self.onlywicket()
                return "exit"
            else:
                self.wklabel.setText(str(int(self.wklabel.text()) + 1))

# Function to Change the Points Used and Points Available
    def pointchange(self,item):
        x = item.data()
        x = x[:len(x)-6]
        cur = conn.cursor()
        cur.execute(f"select value from team_india where player_name ='{x}';")
        rows = cur.fetchall()
    
        y = int(self.pavlabel.text()) - rows[0][0]
        if y < 0:
            self.error_limitexceed()
            return "exit"
        self.pavlabel.setText(str(y))
        self.puslabel.setText(str(int(self.puslabel.text())+ rows[0][0]))

        self.player_name.append(x)
        self.point_value.append(rows[0][0])


# Helping function for removefrom_teamlist
    def decreasepoints(self,item):
        x = item.data()
        x = x[:len(x)-6]
        y = int(self.pavlabel.text()) + self.point_value[self.player_name.index(x)]
        self.pavlabel.setText(str(y))
        self.puslabel.setText(str(int(self.puslabel.text())- self.point_value[self.player_name.index(x)]))
        self.point_value.pop(self.player_name.index(x))
        self.player_name.remove(x)
        x = item.data()
        self.foo1 = item.data()[len(x)-3:len(x)-1]
        if self.foo1 == "AT":
            self.batlabel.setText(str(int(self.batlabel.text()) - 1))
        elif self.foo1 == "WL":
            self.bowlabel.setText(str(int(self.bowlabel.text()) - 1))
        elif self.foo1 == "AR":
            self.arlabel.setText(str(int(self.arlabel.text()) - 1))
        elif self.foo1 == "WK":
            self.wklabel.setText(str(int(self.wklabel.text()) - 1))
        








# Error Handling Function
    def errorteam(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle("Error")

        msg.setText("First Create a Team")
        msg.exec_()

    def ErrorRepeatplayer(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle("Error")

        msg.setText("Player already Present")
        msg.exec_()

    def onlywicket(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle("Error")

        msg.setText("Only One Wicket Keeper can be Selected!")
        msg.exec_()

    def error_limitexceed(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle("Error")

        msg.setText("Not Enough Points\nContinue or Create New Team Again!")
        msg.exec_()


    def error_cannotSave(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle("Error")

        msg.setText("Exactly 11 player should be present!\n Create Team Again!!")
        msg.exec_()

    def error_invalidteamname(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle("Error")

        msg.setText("Team name incorrect!!")
        msg.exec_() 

    def sucess_save(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle("Error")

        msg.setText("Team Saved Succesfully!")
        msg.exec_()

    def readonly(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle("Error")

        msg.setText("Read Only, Cannot Edit!")
        msg.exec_()





   







