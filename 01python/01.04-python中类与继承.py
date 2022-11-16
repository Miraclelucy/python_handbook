# coding:utf-8
"""
说明：
----类的实例调用----
下面的代码，静态方法调用另一个静态方法，如果改用类方法调用静态方法，可以让cls代替类，
让代码看起来精简一些。也防止类名修改了，不用在类定义中修改原来的类名。
----子类的实例调用----
如果子类继承父类的方法，子类覆盖了父类的静态方法，
子类的实例继承了父类的static_method静态方法，调用该方法，还是调用的父类的方法和类属性。
子类的实例继承了父类的class_method类方法，调用该方法，调用的是子类的方法和子类的类属性。
"""


# coding:utf-8
class Foo(object):
    X = 1
    Y = 14

    @staticmethod
    def averag(*mixes):
        return sum(mixes) / len(mixes)

    @staticmethod
    def static_method():  # 在静态方法中调用静态方法
        print("在静态方法中调用静态方法")
        return Foo.averag(Foo.X, Foo.Y)

    @classmethod
    def class_method(cls):  # 在类方法中使用静态方法
        print("在类方法中使用静态方法")
        return cls.averag(cls.X, cls.Y)


foo = Foo()
print("----类的实例调用----")
print(foo.static_method())


class Son(Foo):
    X = 3
    Y = 5

    @staticmethod
    def averag(*mixes):  # "子类中重载了父类的静态方法"
        print("子类中重载了父类的静态方法")
        print("666 ", mixes)
        return sum(mixes) / 3


p = Son()
print("----子类的实例调用----")
print("result of p.averag(1,5)")
print(p.averag(1, 5))
print("result of p.static_method()")
print(p.static_method())
print("result of p.class_method()")
