#删除对象
class super:pass
class son(super):pass
sonObj1 = son();print(sonObj1)
sonObj2 = son();print(sonObj2)
sonObj3 = son();print(sonObj3)
del sonObj1
#print(sonObj1)
del sonObj2,sonObj3;
#print(sonObj2)
#print(sonObj3)