#i = 1
#while i:
#	if (i % 2 == 1) and (i % 3 == 2) and (i % 5 == 4) and (i % 6 == 5) and (i % 7 == 0):
#		print(i)
#		break
#	else:
#		i = i + 1

x = 7
i = 1
flag = 0

while i <= 100:
    if (x%2 == 1) and (x%3 == 2) and (x%5 == 4) and (x%6==5):
        flag = 1
    else:
        x = 7 * (i+1)
    i += 1

if flag == 1:
    print('result is', x)
else:
    print('sorry, can not find the answer.')