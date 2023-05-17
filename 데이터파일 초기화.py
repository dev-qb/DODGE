import pickle

ranking_dic = {"없음_1":0.09,"없음_2":0.08,"없음_3":0.07,"없음_4":0.06,"없음_5":0.05,"없음_6":0.04,"없음_7":0.03,"없음_8":0.02,"없음_9":0.01,"없음_10":0.00}
ranking_file = open('ranking.dat','wb')
pickle.dump(ranking_dic, ranking_file)
ranking_file.close()

print(ranking_dic)
