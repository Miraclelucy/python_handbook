# coding:utf-8
"""
说明：
调用实例方法，静态方法，类方法
调用和修改实例变量
"""

class Book(object):

    def __init__(self, title):
        self.title = title

    @classmethod
    def class_method_create(cls, title):
        book = cls(title=title)
        return book

    @staticmethod
    def static_method_create(title):
        book = Book(title)
        return book


book1 = Book("use instance_method_create book instance111")
book4 = Book("use instance_method_create book instance444")
book2 = Book.class_method_create("use class_method_create book instance")
book3 = Book.static_method_create("use static_method_create book instance")
print(book1.title)
print(book2.title)
print(book3.title)
print(book4.title)
book4.title = "use instance_method_create book instance444-update"
print(book4.title)
