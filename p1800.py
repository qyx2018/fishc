def mFun(*param, base=3):
    result = 0
    for each in param:
        result += each

    result *= base
    
    print('Result is: ', result)

mFun(1, 2, 3, 4, 5, base=5)


不知道是和原因，第一行，最后base参数总报语法错误，与文档、书等对比，没有问题。待查。