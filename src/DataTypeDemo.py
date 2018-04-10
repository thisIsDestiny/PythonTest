
""""""
"""
标准数据类型
Python3 中有六个标准的数据类型：
    Number（数字）
        int
        float
        bool    新加入
        complex（复数）
        Long 移除
        
    String（字符串）
    List（列表）
    Tuple（元组）
    Sets（集合）
    Dictionary（字典）
"""

# 默认为int
int1 = 111
print(type(int))
print(isinstance(int1,int))

# 判断类型
'''
type(obj) == class       obj 是否是 class的实例对象--直接实现类          
isinstance(obj,class)    obj 是否是 class的本类或子类实例对象
'''
class super:pass
class son(super):pass
print(type(son()) == super)
print(isinstance(son(),super))

#删除对象
sonObj1 = son();print(sonObj1)
sonObj2 = son();print(sonObj2)
sonObj3 = son();print(sonObj3)
del sonObj1;print(sonObj1)
del sonObj1,sonObj2,sonObj3;print(sonObj1)

"""
注意：
1、Python可以同时为多个变量赋值，如a, b = 1, 2。
2、一个变量可以通过赋值指向不同类型的对象。
3、数值的除法（/）总是返回一个浮点数，要获取整数使用//操作符。
4、在混合计算时，Python会把整型转换成为浮点数。
"""

"""
数值类型实例
int	        float	        complex
10	        0.0	        3.14j
100	        15.20	        45.j
-786	    -21.9	        9.322e-36j
080       	32.3e+18	    .876j
-0490	    -90.	        -.6545+0J
-0x260  	-32.54e100	    3e+26J
0x69	    70.2E-12    	4.53e-7j
"""
