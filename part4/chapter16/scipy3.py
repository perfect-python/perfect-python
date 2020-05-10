from scipy import integrate


a = 0

def func(x):
    ''' グローバル変数に依存する関数 '''
    global a

    a += x
    return a


# 1回目の積分 
result, error = integrate.quad(func, 0, 10)

# 結果
print(result) #=> 77211.16917935389


# 2回目の積分 
result, error = integrate.quad(func, 0, 10)

# 1回目とは結果が変わってしまう
print(result) #-> 210889.2941793539
