# 类对象,类属性,类方法,实例属性,实例对象


class House(object):
    # 类属性: 类名.类属性 = 修改类属性的值
    houseNum = 0  # 公有类属性
    __age = 12  # 私有类属性
    
    # 实例方法
    def __init__(self, name, color):
        # name 是实例属性
        self.name = name 
        # color 是实例属性
        self.color = color
        # 使用实例对象.类方法
        self.setHouseNum()
    
    # 类方法 ---> 通过类方法来修改类属性
    @classmethod
    def setHouseNum(cls):
        cls.houseNum += 1

# bailobfma 实例对象    
bailongma = House("白龙马","白色")
# 通过类对象修改类属性中的值
# House.houseNum += 1
# 先在实例属性中查找有没有这个houseNum属性,如果没有就在类属性中查找,如果也没有就报错
print(bailongma.houseNum)

# chituma 实例对象  
chituma = House("赤兔马","红色")
# 通过类对象修改类属性中的值
# House.houseNum += 1
# 先在实例属性中查找有没有这个houseNum属性,如果没有就在类属性中查找,如果也没有就报错
print(chituma.houseNum)

print("="*30)

# 总结:类属性(公有属性与私有属性)
#   类对象(类名).公有类属性    :可以直接通过类对象直接访问类的公有属性
#   实例对象.公有类属性    :可以直接通过实例对象访问类的公有属性(先查找实例属性,没有在查找类的公有属性)
#   类对象(类名).私有类属性    :不能在类外部通过类对象访问类的私有属性
#   实例对象.私有类属性    :不能在类外部通过实例对象访问类的私有属性
#注意:    实例对象.类的公有属性 = "修改值" ---> 只是增加了一个与类属性同名的实例属性

# 总结:实例属性
#   类对象(类名).实例属性    :类对象不能访问实例属性
#   实例对象.实例属性    :实例对象可以访问实例属性

# 总结:类方法
#   类对象(类名).类方法    :类对象可以直接调用类方法
#   实例对象.类方法    :实例对象可以调用类方法

# 总结:实例方法
#   类对象(类名).实例方法    :类对象不能调用实例方法
#   实例对象.实例方法    :实例对象可以调用实例方法 




















