active = True
while active:
    result = 1
    n = input("请输入正整数n,计算其阶乘,输入quit以结束程序: ")
    if n == "quit":
        active = False
    #计算阶乘
    else:
        n = int(n)
        while n > 0:
            result *= n
            n -= 1                  
        print(result)
