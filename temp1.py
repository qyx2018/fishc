import pickle

boy1_f = open('C:\\python\\fishc\\boy_1.txt', 'rb')
boy2_f = open('C:\\python\\fishc\\boy_2.txt', 'rb')
boy3_f = open('C:\\python\\fishc\\boy_3.txt', 'rb')

girl1_f = open('C:\\python\\fishc\\girl_1.txt', 'rb')
girl2_f = open('C:\\python\\fishc\\girl_2.txt', 'rb')
girl3_f = open('C:\\python\\fishc\\girl_3.txt', 'rb')

boy1 = []
boy2 = []
boy3 = []

girl1 = []
girl2 = []
girl3 = []

boy1 = pickle.load(boy1_f)
boy2 = pickle.load(boy2_f)
boy3 = pickle.load(boy3_f)

girl1 = pickle.load(girl1_f)
girl2 = pickle.load(girl2_f)
girl3 = pickle.load(girl3_f)

boy1_f.close()
boy2_f.close()
boy3_f.close()

girl1_f.close()
girl2_f.close()
girl3_f.close()

print(boy1)
print(boy2)
print(boy3)

print(girl1)
print(girl2)
print(girl3)