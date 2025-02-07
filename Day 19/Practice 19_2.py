# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P_18_2_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):

    i_encode = "cp949"
    o_encode = "cp949"
    
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 625)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.txt__edit = QtWidgets.QTextEdit(self.centralwidget)
        self.txt__edit.setGeometry(QtCore.QRect(10, 9, 780, 481))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code Light")
        font.setPointSize(12)
        self.txt__edit.setFont(font)
        self.txt__edit.setObjectName("txt__edit")
        
        self.txt__open = QtWidgets.QTextEdit(self.centralwidget)
        self.txt__open.setGeometry(QtCore.QRect(10, 500, 780, 31))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code Light")
        font.setPointSize(12)
        self.txt__open.setFont(font)
        self.txt__open.setObjectName("txt__open")
        
        self.txt__save = QtWidgets.QTextEdit(self.centralwidget)
        self.txt__save.setGeometry(QtCore.QRect(10, 540, 780, 31))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code Light")
        font.setPointSize(12)
        self.txt__save.setFont(font)
        self.txt__save.setObjectName("txt__save")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        
        self.m__ie = QtWidgets.QMenu(self.menuSetting)
        self.m__ie.setObjectName("m__ie")
        
        self.m__oe = QtWidgets.QMenu(self.menuSetting)
        self.m__oe.setObjectName("m__oe")
        
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)
        
        self.act__open = QtWidgets.QAction(MainWindow)
        self.act__open.setObjectName("act__open")
        
        self.act__save = QtWidgets.QAction(MainWindow)
        self.act__save.setObjectName("act__save")
        
        self.act__reset = QtWidgets.QAction(MainWindow)
        self.act__reset.setObjectName("act__reset")

        self.act__i_utf = QtWidgets.QAction(MainWindow)
        self.act__i_utf.setObjectName("act__i_utf")
        
        self.act__i_ansi = QtWidgets.QAction(MainWindow)
        self.act__i_ansi.setObjectName("act__i_ansi")
        
        self.act__o_utf = QtWidgets.QAction(MainWindow)
        self.act__o_utf.setObjectName("act__o_utf")
        
        self.act__o_ansi = QtWidgets.QAction(MainWindow)
        self.act__o_ansi.setObjectName("act__o_ansi")

        
        self.act__i_utf.setCheckable(True)
        self.act__i_utf.setChecked(False)
        
        self.act__o_utf.setCheckable(True)
        self.act__o_utf.setChecked(False)
        
        self.act__i_ansi.setCheckable(True)
        self.act__i_ansi.setChecked(True)
        
        self.act__o_ansi.setCheckable(True)
        self.act__o_ansi.setChecked(True)
        
        self.menuFile.addAction(self.act__open)
        self.menuFile.addAction(self.act__save)
        self.menuFile.addAction(self.act__reset)
        self.m__ie.addAction(self.act__i_utf)
        self.m__ie.addAction(self.act__i_ansi)
        self.m__oe.addAction(self.act__o_utf)
        self.m__oe.addAction(self.act__o_ansi)

        self.menuSetting.addAction(self.m__ie.menuAction())
        self.menuSetting.addAction(self.m__oe.menuAction())
        
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())

        self.txt__open.setEnabled(False)
        self.txt__save.setEnabled(False)

        self.statusbar.showMessage("READY")

        self.act__open.triggered.connect(self.open)
        self.act__save.triggered.connect(self.save)
        self.act__reset.triggered.connect(self.reset)

        self.act__i_utf.triggered.connect(self.i_utf_type)
        self.act__i_ansi.triggered.connect(self.i_ansi_type)
        self.act__o_utf.triggered.connect(self.o_utf_type)
        self.act__o_ansi.triggered.connect(self.o_ansi_type)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def open_select(self):

        path = QtWidgets.QFileDialog.getOpenFileName(self, "Select Directory")
        
        return path[0]

    def save_select(self):

        path = QtWidgets.QFileDialog.getSaveFileName(self, "Select Directory")
     
        return path[0]

    def i_utf_type(self):

        self.i_encode = "utf-8"
        
        self.act__i_utf.setChecked(True)
        self.act__i_ansi.setChecked(False)

    def i_ansi_type(self):

        self.i_encode = "cp949"

        self.act__i_utf.setChecked(False)
        self.act__i_ansi.setChecked(True)

    def o_utf_type(self):

        self.o_encode = "utf-8"
        
        self.act__o_utf.setChecked(True)
        self.act__o_ansi.setChecked(False)

    def o_ansi_type(self):

        self.o_encode = "cp949"
        
        self.act__o_utf.setChecked(False)
        self.act__o_ansi.setChecked(True)

    def open(self):
        
        try:

            self.txt__edit.setEnabled(True)
            self.txt__edit.setText("")
            self.txt__save.setText("")            
            
            path = self.open_select()
            self.txt__open.setText(path)
            
            f = open(path, "r", encoding = self.i_encode)

            for i in f:
            
                temp = self.txt__edit.toPlainText()
                self.txt__edit.setText(f"{temp}{i}")

            f.close()

            self.statusbar.showMessage("파일이 정상적으로 열렸습니다.")
            
        except:
            
            self.statusbar.showMessage("다시 시도해 주세요.")

    def save(self):
        
        try:
            
            temp = self.txt__edit.toPlainText()
            
            path = self.save_select()            
            self.txt__save.setText(path)

            f = open(path, "w", encoding = self.o_encode)

            f.write(temp)

            f.close()

            self.statusbar.showMessage("파일이 정상적으로 저장되었습니다.")
            self.txt__edit.setEnabled(False)
            
        except:
            
            self.statusbar.showMessage("다시 시도해 주세요.")

    def reset(self):

        self.txt__edit.setText("")
        self.txt__open.setText("")
        self.txt__save.setText("")
        self.txt__edit.setEnabled(True)
        self.statusbar.showMessage("READY")
            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TEXT EDITOR"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.m__ie.setTitle(_translate("MainWindow", "Input Encoding"))
        self.m__oe.setTitle(_translate("MainWindow", "Output Encoding"))
        self.act__open.setText(_translate("MainWindow", "File Open"))
        self.act__save.setText(_translate("MainWindow", "File Save"))
        self.act__reset.setText(_translate("MainWindow", "Window Reset"))
        self.act__i_utf.setText(_translate("MainWindow", "UTF-8"))
        self.act__i_ansi.setText(_translate("MainWindow", "ANSI"))
        self.act__o_utf.setText(_translate("MainWindow", "UTF-8"))
        self.act__o_ansi.setText(_translate("MainWindow", "ANSI"))

if __name__ == "__main__":
    
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
