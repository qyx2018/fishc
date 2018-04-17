f1 = open('C:\\python\\fishc\\OpenMe.mp3')
f2 = open('C:\\python\\fishc\\OpenMe_new.mp3', 'w')

f2.write(f1.read())
f2.close()
f1.close()