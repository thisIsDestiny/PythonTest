#encoding=utf-8

class A:

    def action(self): print("a")

class B(A):

    def action(self): print("b")

class C:

    def action(self): print("c")

class  D(B,A,C):

    pass

#test
"""
多继承时
父类方法名重复时
优先继承靠前父类的父类方法
"""
D().action()