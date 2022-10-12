# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P_17_5_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import random as r


class Ui_main(object):

    one = 0                             # 랜덤한 비밀번호가 들어갈 자리
    two = 0
    thr = 0
    
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        main.setFont(font)
        self.centralwidget = QtWidgets.QWidget(main)
        self.centralwidget.setObjectName("centralwidget")
        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(70, 60, 331, 311))
        self.dial.setProperty("value", 0)
        self.dial.setNotchesVisible(True)
        self.dial.setObjectName("dial")
        self.btn__chk = QtWidgets.QPushButton(self.centralwidget)
        self.btn__chk.setGeometry(QtCore.QRect(580, 420, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(15)
        self.btn__chk.setFont(font)
        self.btn__chk.setObjectName("btn__chk")
        self.num__one = QtWidgets.QLCDNumber(self.centralwidget)
        self.num__one.setGeometry(QtCore.QRect(130, 420, 111, 61))
        self.num__one.setObjectName("num__one")
        self.num__two = QtWidgets.QLCDNumber(self.centralwidget)
        self.num__two.setGeometry(QtCore.QRect(280, 420, 111, 61))
        self.num__two.setProperty("intValue", 0)
        self.num__two.setObjectName("num__two")
        self.num__thr = QtWidgets.QLCDNumber(self.centralwidget)
        self.num__thr.setGeometry(QtCore.QRect(430, 420, 111, 61))
        self.num__thr.setObjectName("num__thr")
        self.lbl__one = QtWidgets.QLabel(self.centralwidget)
        self.lbl__one.setGeometry(QtCore.QRect(130, 490, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl__one.setFont(font)
        self.lbl__one.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl__one.setObjectName("lbl__one")
        self.lbl__two = QtWidgets.QLabel(self.centralwidget)
        self.lbl__two.setGeometry(QtCore.QRect(280, 490, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl__two.setFont(font)
        self.lbl__two.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl__two.setObjectName("lbl__two")
        self.lbl__thr = QtWidgets.QLabel(self.centralwidget)
        self.lbl__thr.setGeometry(QtCore.QRect(430, 490, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl__thr.setFont(font)
        self.lbl__thr.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl__thr.setObjectName("lbl__thr")
        self.lbl__dial = QtWidgets.QLabel(self.centralwidget)
        self.lbl__dial.setEnabled(False)
        self.lbl__dial.setGeometry(QtCore.QRect(500, 70, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(25)
        self.lbl__dial.setFont(font)
        self.lbl__dial.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl__dial.setObjectName("lbl__dial")
        self.btn__reset = QtWidgets.QPushButton(self.centralwidget)
        self.btn__reset.setGeometry(QtCore.QRect(580, 490, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(11)
        self.btn__reset.setFont(font)
        self.btn__reset.setObjectName("btn__reset")
        self.lbl__hint = QtWidgets.QLabel(self.centralwidget)
        self.lbl__hint.setEnabled(False)
        self.lbl__hint.setGeometry(QtCore.QRect(500, 140, 271, 201))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.lbl__hint.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(30)
        self.lbl__hint.setFont(font)
        self.lbl__hint.setText("")
        self.lbl__hint.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl__hint.setObjectName("lbl__hint")
        main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main)
        self.statusbar.setObjectName("statusbar")
        main.setStatusBar(self.statusbar)

        self.choose()
        
        self.dial.valueChanged.connect(self.draw)
                                                # dial의 값이 바뀌면 함수 실행
        self.btn__chk.clicked.connect(self.chk_clicked)
                                                # 체크버튼을 클릭 시 함수 실행
        self.btn__reset.clicked.connect(self.reset)
                                                # 리셋버튼 클릭 시 함수 실행

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def choose(self):

        a = r.randrange(0, 100)                  # 0 ~ 99 사이에서 랜덤한 정수 하나 뽑기
        b = r.randrange(0, 100)
        c = r.randrange(0, 100)

        while (a == b) or (b == c) or (a == c) :

            b = r.randrange(0, 100)
            c = r.randrange(0, 100)

        self.one = a
        self.two = b
        self.thr = c
            

    def draw(self):                             # dial 값이 바뀔 때

        temp = self.dial.value()                # lbl__dial에 그 값을 표시
        self.lbl__dial.setText(f"{temp:02d}")
        
        self.lbl__hint.setText("")              # hint 라벨은 비었다가

        if (self.num__one.isEnabled() == True) & (self.one == temp):
                                                # 첫번째 숫자가 풀리기 전에
            self.lbl__hint.setText("CLICKED!")  # dial 값과 1번 비밀번호가 일치할때
                                                # hint 라벨에 CLICKED! 표시
        elif (self.num__one.isEnabled() == False) & (self.two == temp):

            self.lbl__hint.setText("CLICKED!")  # 첫번째 숫자가 풀린 후
                                                # 2번 비밀번호가 dial 값과 일치할때 
        elif (self.num__two.isEnabled() == False) & (self.thr == temp):
                                                
            self.lbl__hint.setText("CLICKED!")  # 두번째 숫자가 풀린 후
                                                # 3번 비밀번호가 dial 값과 일치할때 
        

    def chk_clicked(self):                      # clicked! 가 떠있을 때 체크버튼을 누르기!

        temp = self.lbl__dial.text()            # lbl__dial의 값이 temp에 저장

        if int(temp) == self.one:               # temp와 1번 비밀번호가 일치할 때
                                                # 체크버튼을 누르면
            self.lbl__hint.setText("UNLOCKED!") # hint 라벨이 UNLOCKED!로 변하고
            self.num__one.display(self.one)     # 첫번째 숫자칸에 정답 표시 후
            self.num__one.setEnabled(False)     # 비활성화

        elif (self.num__one.isEnabled() == False) & (self.two == int(temp)):
                                                # 반복
            self.lbl__hint.setText("UNLOCKED!")
            self.num__two.display(self.two)
            self.num__two.setEnabled(False)

        elif (self.num__two.isEnabled() == False) & (self.thr == int(temp)):

            self.lbl__hint.setText("UNLOCKED!")
            self.num__thr.display(self.thr)
            self.num__thr.setEnabled(False)

        if (self.num__one.isEnabled() == False) & (self.num__two.isEnabled() == False) & (self.num__thr.isEnabled() == False):
                                                # 모든 숫자칸이 비활성화 상태가 되면
            self.lbl__hint.setText("GREAT!\nSOLVED!")
            self.btn__chk.setEnabled(False)     # 체크버튼과 hint 라벨이 solved로 변하고 
            self.btn__chk.setText("! SOLVED !") # 체크버튼이 비활성화

    def reset(self):                            # 모든 칸 리셋

        self.lbl__hint.setText("")
        self.lbl__dial.setText("00")

        self.btn__chk.setText("! CHECK !")
        self.btn__chk.setEnabled(True)

        self.num__one.display(0)
        self.num__two.display(0)
        self.num__thr.display(0)
        self.num__one.setEnabled(True)
        self.num__two.setEnabled(True)
        self.num__thr.setEnabled(True)

        self.one = r.randrange(0, 100)
        self.two = r.randrange(0, 100)
        self.thr = r.randrange(0, 100)

        self.dial.setValue(0)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Guess Passwords"))
        self.btn__chk.setText(_translate("main", "! CHECK !"))
        self.lbl__one.setText(_translate("main", "Password ONE"))
        self.lbl__two.setText(_translate("main", "Password TWO"))
        self.lbl__thr.setText(_translate("main", "Password THR"))
        self.lbl__dial.setText(_translate("main", "00"))
        self.btn__reset.setText(_translate("main", "RESET"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QMainWindow()
    ui = Ui_main()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())
