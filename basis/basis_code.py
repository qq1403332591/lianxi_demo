class Person:
    name = 'wangwu'
    age = '20'
    sex = '女'


    @classmethod
    def characteristic(self):
        self.name = 'lisi'
        self.age = '18'
        self.sex = '男'
        return self.name


# 直接调用类方法是不能够调用的，除非类函数上加上装饰器
print(Person.characteristic())