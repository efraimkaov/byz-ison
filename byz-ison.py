#!/usr/bin/python3

# BYZ ISON
# ---------------
# author    : EfraimKAOV
#             https://github.com/efraimkaov
# project   : https://github.com/efraimkaov/byz-ison
# license   : LGPL-3.0 (http://opensource.org/licenses/lgpl-3.0.html)

import sys
from PyQt5.QtWidgets import QApplication
from ui.mainwindow import Ui_MainWindow
from PyQt5  import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from pygame import mixer

class ByzWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.actionAbout.triggered.connect(self.helpAbout)
        self.pushButton_vu2.clicked.connect(self.vu2)
        self.pushButton_pa2.clicked.connect(self.pa2)
        self.pushButton_ni2.clicked.connect(self.ni2)
        self.pushButton_zo.clicked.connect(self.zo)
        self.pushButton_ke.clicked.connect(self.ke)
        self.pushButton_di.clicked.connect(self.di)
        self.pushButton_ga.clicked.connect(self.ga)
        self.pushButton_vu.clicked.connect(self.vu)
        self.pushButton_pa.clicked.connect(self.pa)
        self.pushButton_ni.clicked.connect(self.ni)
        self.pushButton_zo0.clicked.connect(self.zo0)
        self.pushButton_ke0.clicked.connect(self.ke0)
        self.pushButton_di0.clicked.connect(self.di0)
        self.pushButton_ga0.clicked.connect(self.ga0)
        self.comboBox.activated.connect(self.notesCombo)
        self.pushButton_stop.clicked.connect(self.stop)
        self.actionExit.triggered.connect(self.exitApp)

        self.show()
        
    def helpAbout(self):
        QMessageBox.about(self, 'About', \
                          'This application plays isokratima (ison)\nfor chanters of Byzantine music.\nMade by EfraimKAOV')
        
    def vu2(self):
        ci = self.comboBox.currentIndex()
        if ci == 0:
            path = 'ogg/dt/'
            freq = '646.6'
        if ci == 1:
            path = 'ogg/en/'
            freq = '659.2'
        if ci == 2:
            path = 'ogg/sc/'
            freq = '646.6'
        if ci == 3:
            path = 'ogg/hc/'
            freq = '672.0'
        mixer.init()
        mixer.music.load(path+'vu2.ogg')
        mixer.music.play(-1)
        self.label.setText('Vu\' '+freq)
        
    def pa2(self):
        ci = self.comboBox.currentIndex()
        if ci == 0:
            path = 'ogg/dt/'
            freq = '587.2'
        if ci == 1:
            path = 'ogg/en/'
            freq = '587.2'
        if ci == 2:
            path = 'ogg/sc/'
            freq = '565.0'
        if ci == 3:
            path = 'ogg/hc/'
            freq = '554.4'
        mixer.init()
        mixer.music.load(path+'pa2.ogg')
        mixer.music.play(-1)
        self.label.setText('Pa\' '+freq)
        
    def ni2(self):
        ci = self.comboBox.currentIndex()
        if ci == 0:
            path = 'ogg/dt/'
            freq = '523.2'
        if ci == 1:
            path = 'ogg/en/'
            freq = '523.2'
        if ci == 2:
            path = 'ogg/sc/'
            freq = '523.2'
        if ci == 3:
            path = 'ogg/hc/'
            freq = '523.2'
        mixer.init()
        mixer.music.load(path+'ni2.ogg')
        mixer.music.play(-1)
        self.label.setText('Ni\' '+freq)
        
    def zo(self):
        ci = self.comboBox.currentIndex()
        if ci == 0:
            path = 'ogg/dt/'
            freq = '484.4'
        if ci == 1:
            path = 'ogg/en/'
            freq = '466.1'
        if ci == 2:
            path = 'ogg/sc/'
            freq = '484.4'
        if ci == 3:
            path = 'ogg/hc/'
            freq = '503.4'
        mixer.init()
        mixer.music.load(path+'zo.ogg')
        mixer.music.play(-1)
        self.label.setText('Zo '+freq)
        
    def ke(self):
        ci = self.comboBox.currentIndex()
        if ci == 0:
            path = 'ogg/dt/'
            freq = '440.0'
        if ci == 1:
            path = 'ogg/en/'
            freq = '440.0'
        if ci == 2:
            path = 'ogg/sc/'
            freq = '423.3'
        if ci == 3:
            path = 'ogg/hc/'
            freq = '415.3'
        mixer.init()
        mixer.music.load(path+'ke.ogg')
        mixer.music.play(-1)
        self.label.setText('Ke '+freq)
        
    def di(self):
        ci = self.comboBox.currentIndex()
        if ci == 0:
            path = 'ogg/dt/'
            freq = '392.0'
        if ci == 1:
            path = 'ogg/en/'
            freq = '392.0'
        if ci == 2:
            path = 'ogg/sc/'
            freq = '392.0'
        if ci == 3:
            path = 'ogg/hc/'
            freq = '392.0'
        mixer.init()
        mixer.music.load(path+'di.ogg')
        mixer.music.play(-1)
        self.label.setText('Di '+freq)
        
    def ga(self):
        ci = self.comboBox.currentIndex()
        if ci == 0:
            path = 'ogg/dt/'
            freq = '349.2'
        if ci == 1:
            path = 'ogg/en/'
            freq = '349.2'
        if ci == 2:
            path = 'ogg/sc/'
            freq = '349.2'
        if ci == 3:
            path = 'ogg/hc/'
            freq = '349.2'
        mixer.init()
        mixer.music.load(path+'ga.ogg')
        mixer.music.play(-1)
        self.label.setText('Ga '+freq)
        
    def vu(self):
        ci = self.comboBox.currentIndex()
        if ci == 0:
            path = 'ogg/dt/'
            freq = '323.3'
        if ci == 1:
            path = 'ogg/en/'
            freq = '329.6'
        if ci == 2:
            path = 'ogg/sc/'
            freq = '323.3'
        if ci == 3:
            path = 'ogg/hc/'
            freq = '336.0'
        mixer.init()
        mixer.music.load(path+'vu.ogg')
        mixer.music.play(-1)
        self.label.setText('Vu '+freq)
        
    def pa(self):
        ci = self.comboBox.currentIndex()
        if ci == 0:
            path = 'ogg/dt/'
            freq = '293.6'
        if ci == 1:
            path = 'ogg/en/'
            freq = '293.6'
        if ci == 2:
            path = 'ogg/sc/'
            freq = '282.5'
        if ci == 3:
            path = 'ogg/hc/'
            freq = '277.2'
        mixer.init()
        mixer.music.load(path+'pa.ogg')
        mixer.music.play(-1)
        self.label.setText('Pa '+freq)
        
    def ni(self):
        ci = self.comboBox.currentIndex()
        if ci == 0:
            path = 'ogg/dt/'
            freq = '261.6'
        if ci == 1:
            path = 'ogg/en/'
            freq = '261.6'
        if ci == 2:
            path = 'ogg/sc/'
            freq = '261.6'
        if ci == 3:
            path = 'ogg/hc/'
            freq = '261.6'
        mixer.init()
        mixer.music.load(path+'ni.ogg')
        mixer.music.play(-1)
        self.label.setText('Ni '+freq)
        
    def zo0(self):
        ci = self.comboBox.currentIndex()
        if ci == 0:
            path = 'ogg/dt/'
            freq = '242.2'
        if ci == 1:
            path = 'ogg/en/'
            freq = '233.1'
        if ci == 2:
            path = 'ogg/sc/'
            freq = '242.2'
        if ci == 3:
            path = 'ogg/hc/'
            freq = '251.7'
        mixer.init()
        mixer.music.load(path+'zo0.ogg')
        mixer.music.play(-1)
        self.label.setText('Zo, '+freq)
        
    def ke0(self):
        ci = self.comboBox.currentIndex()
        if ci == 0:
            path = 'ogg/dt/'
            freq = '220.0'
        if ci == 1:
            path = 'ogg/en/'
            freq = '220.0'
        if ci == 2:
            path = 'ogg/sc/'
            freq = '211.7'
        if ci == 3:
            path = 'ogg/hc/'
            freq = '207.6'
        mixer.init()
        mixer.music.load(path+'ke0.ogg')
        mixer.music.play(-1)
        self.label.setText('Ke, '+freq)
        
    def di0(self):
        ci = self.comboBox.currentIndex()
        if ci == 0:
            path = 'ogg/dt/'
            freq = '196.0'
        if ci == 1:
            path = 'ogg/en/'
            freq = '196.0'
        if ci == 2:
            path = 'ogg/sc/'
            freq = '196.0'
        if ci == 3:
            path = 'ogg/hc/'
            freq = '196.0'
        mixer.init()
        mixer.music.load(path+'di0.ogg')
        mixer.music.play(-1)
        self.label.setText('Di, '+freq)
        
    def ga0(self):
        ci = self.comboBox.currentIndex()
        if ci == 0:
            path = 'ogg/dt/'
            freq = '174.6'
        if ci == 1:
            path = 'ogg/en/'
            freq = '174.6'
        if ci == 2:
            path = 'ogg/sc/'
            freq = '174.6'
        if ci == 3:
            path = 'ogg/hc/'
            freq = '174.6'
        mixer.init()
        mixer.music.load(path+'ga0.ogg')
        mixer.music.play(-1)
        self.label.setText('Ga, '+freq)
        
    def notesCombo(self):
        pass
        
    def stop(self):
        mixer.init()
        mixer.music.stop()
        self.label.setText('Frequency')
        
    def exitApp(self):
        self.close()

app = QApplication(sys.argv)
byz = ByzWindow()
sys.exit(app.exec_())
