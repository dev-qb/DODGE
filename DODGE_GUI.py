import sys
import pickle
from PyQt5 import uic
from PyQt5.QtWidgets import *
import DODGE

form_class = uic.loadUiType("GUI.ui")[0]

class MainWindow(QMainWindow, form_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.ExitButton.clicked.connect(self.exit_button)
        self.StartButton.clicked.connect(self.start_button)
        
    def exit_button(self):
        sys.exit()
        
    def start_button(self):
        if not self.nameinput.text() == '':
            name = self.nameinput.text()
            score = float(DODGE.main(50))
            self.add_ranking(name, score)
        
    def renew_ranking(self):
        ranking_file = open('ranking.dat','rb')
        ranking_dic = pickle.load(ranking_file)
        ranking_file.close()
        ranking_list = []
        for value in reversed(sorted(ranking_dic.values())):
            for key in ranking_dic.keys():
                if ranking_dic[key] == value:
                    ranking_list.append(key)
                    ranking_list.append(str(value) + '초')
        self.rankn1.setText(ranking_list[0])
        self.rankt1.setText(ranking_list[1])
        self.rankn2.setText(ranking_list[2])
        self.rankt2.setText(ranking_list[3])
        self.rankn3.setText(ranking_list[4])
        self.rankt3.setText(ranking_list[5])
        self.rankn4.setText(ranking_list[6])
        self.rankt4.setText(ranking_list[7])
        self.rankn5.setText(ranking_list[8])
        self.rankt5.setText(ranking_list[9])
        self.rankn6.setText(ranking_list[10])
        self.rankt6.setText(ranking_list[11])
        self.rankn7.setText(ranking_list[12])
        self.rankt7.setText(ranking_list[13])
        self.rankn8.setText(ranking_list[14])
        self.rankt8.setText(ranking_list[15])
        self.rankn9.setText(ranking_list[16])
        self.rankt9.setText(ranking_list[17])
        self.rankn10.setText(ranking_list[18])
        self.rankt10.setText(ranking_list[19])
        
    def add_ranking(self, name, score):
        ranking_file = open('ranking.dat','rb')
        ranking_dic = pickle.load(ranking_file)
        ranking_file.close()
        if score > sorted(ranking_dic.values())[0]:
            for key in ranking_dic.keys():
                if ranking_dic[key] == sorted(ranking_dic.values())[0]:
                    del ranking_dic[key]
                    break
            i = 0
            savename = name
            while savename in ranking_dic:
                savename = name + alpha_string[i]
                i += 1
            ranking_dic[savename] = score
            ranking_file = open('ranking.dat','wb')
            pickle.dump(ranking_dic, ranking_file)
            ranking_file.close()
        self.renew_ranking()
        
alpha_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
app = QApplication(sys.argv)
myWindow = MainWindow()
myWindow.renew_ranking()
myWindow.show()
app.exec_()
