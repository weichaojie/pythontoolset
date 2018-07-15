# 斐波那契数列（Fibonacci sequence），又称黄金分割数列、
# 因数学家列昂纳多·斐波那契（Leonardoda Fibonacci）以兔子繁殖为例子而引入，故又称为“兔子数列”，
# 指的是这样一个数列：1、1、2、3、5、8、13、21、34、……在数学上，
# 斐波纳契数列以如下被以递归的方法定义：F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=2，n∈N*）
# 在现代物理、准晶体结构、化学等领域，斐波纳契数列都有直接的应用，
# 为此，美国数学会从1963年起出版了以《斐波纳契数列季刊》为名的一份数学杂志，用于专门刊载这方面的研究成果。
# 以上文字引用百度百科：
# https://baike.baidu.com/item/%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0%E5%88%97/99145?fr=aladdin

# coding=utf-8
# 斐波那契数列（Fibonacci sequence），又称黄金分割数列、
# 因数学家列昂纳多·斐波那契（Leonardoda Fibonacci）以兔子繁殖为例子而引入，故又称为“兔子数列”，
# 指的是这样一个数列：1、1、2、3、5、8、13、21、34、……在数学上，
# 斐波纳契数列以如下被以递归的方法定义：F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=2，n∈N*）
# 在现代物理、准晶体结构、化学等领域，斐波纳契数列都有直接的应用，
# 为此，美国数学会从1963年起出版了以《斐波纳契数列季刊》为名的一份数学杂志，用于专门刊载这方面的研究成果。

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


for i in range(100):
    fibonacci = get_fibonacci_number(i + 1)
    print("第%d个数为：%d" % (i + 1, fibonacci))
