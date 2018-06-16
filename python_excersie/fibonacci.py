# coding=utf-8

# 使用循环的方法计算斐波那契数列
# 循环方法相比递归求法的效率要高1000倍以上，数字越大提升效率越高
def get_fibonacci_number(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    elif n > 3:
        previous = 1
        current = 2
        next = 3
        for i in range(n):
            if i + 3 == n:
                return next
            next = previous + current
            previous = current
            current = next
    else:
        try:
            print("函数输入异常")
        except:
            return 0


for i in range(1000):
    fibonacci = get_fibonacci_number(i + 1)
    print("第%d个数为：%d" % (i + 1, fibonacci))
