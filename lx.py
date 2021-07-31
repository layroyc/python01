#输入函数：
'''
输入函数：
input()     没有参数输出的是一个空白行
input（“提示信息”）
input接收到的都是字符串类型
eval(input(""))   接收到数据的实际数据类型


'''
#a = input("请输入一个整数：")
#print(a)


#输出函数
'''
输出函数：
print()
一次输出多个内容：
1.用逗号链接    不限制数据类型   多个数据之间逗号分隔
2.用加号连接    只能拼接字符串类型的数据
3.格式化输出    print（“格式化输出符号” %  (变量名1，变量名2.......)）
  字符串 %s    整数  %d   浮点数  %f    百分号  %%
num = 9.9555
print("%.2f" % num)       # 保留两位小数
stu_num = 100
print("%06d" % stu_num)     # 六位   不够补零

a = 15
b ='roy'
print('a的值是',a,'b的值是',b)
print('a的值是'+ str(a) +'b的值是'+ b)
print('a的值是%d,b的值是%s' % (a,b))

x = 1.23456
print('%.2f' % x)
y = 123
print('%05d' % y)
'''

#数据类型：
'''
数据类型：
数字型（整型（int）、浮点型（float）、复数（complex））
数字型也包含其他进制    二进制  八进制  十六进制
转二进制bin(X)    转八进制   oct(X)     转十六进制   hex()    转十进制  int(X,base)

num = 20
print('转二进制',bin(num))
print('转八进制',oct(num))
print('转十六进制',hex(num))

print('转十进制',int(0x14))


#检测数据类型：type(X)
print(type(num))


'''

#字符串操作：
#   in     判断字符串包含关系       'a' in 'abcd'  →  True

print('s' in 'transform')
#   空格     以空格分隔的字符串自动合并          'a' 'b' 'c'  →  'abc'

print('123' 'pwd' 'cd')
#   加号     将多个字符串合并     'a' + 'b' + 'c'   →   'abc'

print('123'+'pwd'+'cd')
#   星号     字符串重复输出      'a' * 5    →    'aaaaa'
print('pwd' * 5)



#字符串索引
'''
字符串索引：
可以通过索引去查，但是不能修改
z =  'abcdefg'    
索引号从左到右      z[0] - z[6]             从右到左  z[-1] - z[-7]

字符串长度：len(X)

字符串切片：
获取某一个区间的多个字符
x[start:end]     从start（包括）开始到end（不包括）之前结束
x[start:]    从start开始，一直到最后、
x[:end]     从开头开始，到end（不包括）之前结束
x[:]     返回全部字符


x = 'qwertyuiop'

print(len(x))
print(x[3:7])
print(x[3:])
print(x[:7])
print(x[:])

print(x[-5:])

'''


'''
分支结构：
1.单分支      
	if 表达式:
	    语句块
	后续代码
2.双分支
	if 表达式:
	    语句块1
	else:
	    语句块2
	后续代码
3.多重分支
	if 表达式1:
	    语句块1
	elif 表达式2:
	    语句块2
	......
	else:
	    语句块n
	后续代码
4.分支嵌套（注意缩进）
5.三元运算符
变量 = 表达式为真的结果 if 表达式 else 表达式为假的结果

'''

#单分支
'''
num = int(input('请输入一个整数：'))
if num%2==0:
    print('该数字是偶数')
else:
    print('该数字是奇数')
'''

#多分支
'''
english = float(input('请输入英语成绩：'))
math = float(input('请输入数学成绩：'))

if english>90 and math>90:
    print('成绩优秀')
elif english>80 and math>80:
    print('成绩良好')
elif english>60 and math>60:
    print('成绩不错')
else:
    print('还要继续努力啊！')
'''

#循环结构
'''
循环结构
1.while循环
	while 循环条件:
	    循环体
2.for循环
	for 迭代变量 in 循环对象:
	    代码块
range()   产生一组整数
1.range(a)     从0开始  到a-1结束     range(10)    0-9
2.range(a,b)    从a开始 到b-1结束    range(5,15)   5-14
3.range(a,b,c)     从a开始，到b-1结束，每次跳跃c个数   range(1,10,2)    1 3 5 7 9
3.break（直接终止循环）   continue（跳出此次循环，继续进行下一次循环）   pass（直接跳过，不执行任何操作）

产生一随机数：
1.导入random模板    import random
2.random.randint(a,b)         随机返回一个[a,b]之间的数
'''
#   九九乘法表
w = 1
while w < 10:
    y = 1
    while y<=w:
        print('%d*%d=%2d' % (w,y,w*y),end=' ')
        y+=1
    print()
    w+=1

#   冒泡排序
list1 = [3,6,9,11,8,56,4]

def sort_list(list):
    n = len(list)
    i = 0
    j = i
    for i in range(n-1):
        for j in range(n-1-i):
            if list[j] < list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]

sort_list(list1)
print(list1)

#循环100内的偶数
#while
'''
i=1
while i<100:
    if i%2==0:
        print("%d是偶数" %i)
    i+=1
'''
#for
'''
for s in range(10):
    print(s)
'''

'''
i = 1
for s in range(i,101):
    if s%2==0:
        print('%d是偶数'%s)


'''
'''
for s in range(2,101,2):
    print('%d是偶数' % s)

'''

'''
x = 10
y = 50
import random
print(random.randint(x,y))
'''


#列表：
'''
1.定义一个列表       
列表名 = [元素1，元素2，.......]         列表名 = list()  
'''
a = [12,15,'asd']
b = list()
print(a)
#空集合
print(b)

'''
2.增
列表名.append()      追加元素到列表的最后面
列表名.insert(index,value)      把元素插入到列表中指定的位置
列表名1.extend(列表名2)    把列表2追加到列表1后面
'''
a.append('qwer')
print(a)
a.insert(3,'886')
print(a)
b = [345]
a.extend(b)
print(a)

'''
3.删
列表名.remove(obj)     将列表中的某个元素移除
列表名.pop(index)   通过索引将元素移除
列表名.clear()    清空列表中的所有元素   列表还存在
del 列表名[index]    通过索引将元素移除
del 列表名    删除列表   列表不存在

a.remove(345)
print(a)
a.pop(2)
print(a)
del a[3]
print(a)
a.clear()
print(a)
del a
print(a)

'''


'''
4.改
列表名[index] = value
5.查
print(列表名)
print(列表名[index])    从左边开始数，第一个索引是0       从右边开始数，第一个索引是-1
print(列表名[a:b])      从a开始  到b-1结束
'''
a[3] = 996
print(a)

print(a[3:])
print(a[2:5])


'''
6.列表名.count()       计算某一个元素在列表中出现的次数
7.列表名.reverse()     将元素反转
8.
列表名.sort()     默认进行升序排列     对列表本身做改变
列表名.sort(reverse=True)     降序排列
列表名.sort(key=len)      根据字符串的长度进行排列
sorted()    对列表进行排序     不改变列表本身，只返回排序后的结果

9.列表也可以进行+ 和 * 操作
'''
b = ['qwe','123','456','rty']
'''
b.count()
print(b)
'''
b.reverse()
print(b)

b.sort()
print(b)

b.sort(reverse=True)
print(b)

c = sorted(b)
print(c)

'''
元组：   
1.定义元组
元组名 = tuple()          元组名 = (元素1，元素2，......)  
a = 'a','b','c'      元组类型        b = (1,)    
2.
元组名.count(obj)     统计查找对象在元组中的出现次数
元组名.index()        找到第一个匹配项的索引值
3.
len()    返回元组长度，也是元素个数
max()    字符串通过它的首字符的ASCLL码判断大小
min()
4.
元组转列表：list(元组名)
列表转元组：tuple(列表名)
'''
x = tuple()
print(x)
x = ('zxc','yy','dw','yy')
print(x)

c = x.count('yy')
print(c)

c = x.index('yy')
print(c)

a = list(x)
print(a)

b = tuple(a)
print(b)


'''
字典：
1.创建字典：
字典名 = {键:值，键:值，......}    键只能是字符串、数字、元组    值可以是任意数据类型
2.查
字典名[键]      获取该键对应的值
字典名.get(键)     获取该键对应的值
字典名.keys()     获取字典中的所有键
字典名.values()     获取字典中的所有值
字典名.items()     获取字典中的所有项           [(键，值)，(键，值)，......]
print(字典名)
3.增和改
字典名[键] = 值           如果键存在，就修改原值      如果键不存在，就新增该键值对
字典名.setdefault(键, 值)       如果键存在，不作操作      如果不存在，就新增该键值对
字典名1.update(字典名2)      将字典2中的键值对合并进字典1中     如果键冲突，则保存字典2中的值
4.删
del 字典名[键]     删除该键对应的键值对
字典名.pop(键)    返回该键对应的值，然后删除该键所在的键值对
字典名.popitem()    删除并返回最后一项键值对
字典名.clear()    清空字典中的所有内容

5.遍历字典
for i in 字典名:
    print(i)       //键
    print(字典名[i])     // 该键对应的值

len(字典名)     计算字典中键的个数

'''
msg = {
    "name":"小王",
    "age":"20",
    "sex":"男",
    "hobby":["singsong","write","tan"]
    }
print(msg["hobby"][2])
print(msg.get("name"))

print(list(msg.keys()))
print(msg.values())
print(list(msg.items()))
#增和改
msg["height"] = 185
msg["age"] = 19
msg.setdefault("weight","110")
msg.setdefault("height",180)

# 遍历
for i in msg:
    print("%s : %s" % (i,msg[i]))


#集合：
#差集-    对称差集^   交集&     并集|
a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(a.symmetric_difference(b))
print(a-b)
print(a^b)
print(a.intersection(b))
print(a&b)
print(a.union(b))
print(a|b)
print(a)


#函数
'''
内置函数：   print()    input()    int()    str()   range()  ......
自定义函数：     先定义后执行
	def 函数名([参数]):
 	    函数体
	    return [指定返回值]

w = "我是浩子"


def money(apple1,weight2):
    price = apple * weight
    #在函数内部有效修改全局变量
    global w
    w = "我变成了耗子"
    #print("本次消费了"+str(price)+"元")
    #函数内部访问全局变量
    print(w)
    return price

apple = float(input("价格"))
weight = float(input("重量"))

#将函数返回值保存到SUM_PRICE
SUM_PRICE = money(apple,weight)

print("总价为"+str(SUM_PRICE)+"元")

print(w)

'''


'''
文件操作：    打开文件   ----   操作文件    ----  关闭文件
打开文件：
	file = open("文件路径"[,"文件打开方式",buffering="缓冲方式",encoding="字符集"])
	with open("文件路径"[,"文件打开方式",buffering="缓冲方式",encoding="字符集"]) as file:
	    # 进行文件操作
	    pass
文件打开方式：
	r    只读
		file.read()  读取文件的全部内容     file.read(n)  读取文件的前n个字符   
		file.readline()    读取文件的一行内容
		file.readlines()     读取文件所有行的内容     返回的是一个列表，每一行就是列表中的一个元素
	w   覆盖写入
	a    追加写入
		file.write("...")      存在缓冲区    file.close()    存入文件
目录操作：
	import os      # 导入模块
创建一个目录：
	os.mkdir("hello")       创建在当前工作目录下
	os.mkdir("C:/Users/Administrator/Desktop/Python/aaa")      在指定目录下创建文件夹
当前工作目录：
	os.getcwd()
删除空目录:
	os.rmdir()
删除文件：
	os.remove()
重命名：
	os.rename("C:/Users/Administrator/Desktop/Python/aaa","C:/Users/Administrator/Desktop/Python/bbb")

import os
print(os.getcwd())
#os.mkdir('hh')
os.rmdir('hh')


	
'''
#面向对象：

class Wy:
    name = "王"
    sex = "男"
    age = "20"
    #方法
    def eat(self):
        self.food = "番茄炒蛋"
#实例化对象  对象名 = 类名（）
wy1 = Wy()
wy2 = Wy()
#访问类属性
#1.通过类名访问类属性
print(Wy.name)
#2.通过对象名访问类属性
print(wy1.age)
#通过对象名访问实例属性
wy1.eat()
print(wy1.food)


#封装
class Students:
    def __init__(self,name):
        self.name = name
        self.__age = 20
    def set(self,age):
        self.__age = age
    def get(self):
        a = self.__age
        return a

s1 = Students('roy')#实例化对象
print(s1.get())
s1.set(19)
print(s1.get())
        
#继承
class House:
    def live(self):
        print("能住")

class Car:
    def run(self):
        print("能跑")

class FangChe(House,Car):
    pass
h1 = FangChe()
h1.live()
h1.run()

#多态
class Animals:
    def __init__(self,kinds):
        self.kinds = kinds

    def skill(self,s):
        self.s = s

        print(self.kinds+"的特长是："+self.s)

cat = Animals("猫")
cat.skill("抓老鼠")

dog = Animals("狗")
dog.skill("吃粑粑")



