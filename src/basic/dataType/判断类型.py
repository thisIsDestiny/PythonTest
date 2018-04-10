# 判断类型
'''
type(obj) == class       obj 是否是 class的实例对象--直接实现类
isinstance(obj,class)    obj 是否是 class的本类或子类实例对象
'''
class super:pass
class son(super):pass
print(type(son()) == super)
print(isinstance(son(),super))