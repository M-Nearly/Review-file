# 接受任意关键字参数的函数
def anyargs(*args, **kwargs):
    print(args) # A tuple
    print(kwargs) # A dict



# 只接受关键字参数的函数
def recv(maxsize, *, block):
    'Receives a message'
    pass

recv(1024, True) # TypeError
recv(1024, block=True) # Ok



# 给函数添加元信息
def add(x:int, y:int) -> int:
    return x + y

>>> add.__annotations__  # 存储在函数的 __annotations__ 属性中
{'y': <class 'int'>, 'return': <class 'int'>, 'x': <class 'int'>} 



# 函数返回多个值 直接return 一个元祖
>>> def myfun():
... return 1, 2, 3
...
>>> a, b, c = myfun()
>>> a
1
>>> b
2
>>> c
3


# 减少可调用函数的对象的参数个数
? 如果你需要减少某个函数的参数个数,functools.partial(),partial() 函数允许你给一个或多个参数设置固定的值,减少接下来被调用时的参数个数.
演示
def spam(a, b, c, d):
    print(a, b, c, d)

现在我们使用 partial() 函数来固定某些参数值：

>>> from functools import partial
>>> s1 = partial(spam, 1) # a = 1
>>> s1(2, 3, 4)
1 2 3 4
>>> s1(4, 5, 6)
1 4 5 6
>>> s2 = partial(spam, d=42) # d = 42
>>> s2(1, 2, 3)
1 2 3 42
>>> s2(4, 5, 5)
4 5 5 42
>>> s3 = partial(spam, 1, 2, d=42) # a = 1, b = 2, d = 42
>>> s3(3)
1 2 3 42
>>> s3(4)
1 2 4 42
>>> s3(5)
1 2 5 42
>>>



# 闭包

# 访问闭包中的变量
def sample():
    n = 0
    # Closure function
    def func():
        print('n=', n)

    # Accessor methods for n
    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # Attach as function attributes
    func.get_n = get_n
    func.set_n = set_n
    return func

>>> f = sample()
>>> f()
n= 0
>>> f.set_n(10)
>>> f()
n= 10
>>> f.get_n()
10
>>>



# 带额外状态的回调函数

def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)

https://python3-cookbook.readthedocs.io/zh_CN/latest/c07/p10_carry_extra_state_with_callback_functions.html


------类

# 创建大量对象时,节省内存的方法
class Date:
    __slots__ = ['year', 'month', 'day']
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

关于__slots__ 的一个常见误区是它可以做为一个封装工具来防止用户给实例添加新的属性,
尽管slots可以达到这样的目的.但是这个并不是它 的初衷
__slots__ 更多的是用来作为一个内存优化的工具



# 在类中封装属性名

class A:
    def __init__(self):
        self._internal = 0 # An internal attribute
        self.public = 1 # A public attribute

    def public_method(self):
        '''
        A public method
        '''
        pass

    def _internal_method(self):
        pass

单下划线: 任何以单下划线_开头的名字都应该是内部实现.(通过遵循一定的属性和方法命令规约来达到)



	class B:
	    def __init__(self):
	        self.__private = 0

	    def __private_method(self):
	        pass

	    def public_method(self):
	        pass
	        self.__private_method()

双下划线: 使用双下划线会导致访问名称变成其他形式. 
		在一个类B中,私有属性会被分别重命名为 _B__private.
		这样重命名的目的是什么, 答案就是继承 --  这种属性通过继承是无法被覆盖的.
	class C(B):
	    def __init__(self):
	        super().__init__()
	        self.__private = 1 # Does not override B.__private

	    # Does not override B.__private_method()
	    def __private_method(self):
	        pass

	这里，私有名称 __private 和 __private_method 被重命名为 _C__private 和 _C__private_method ，这个跟父类B中的名称是完全不同的。




单下划线作为后缀_ : 防止命名冲突和而不是知名这个属性时私有的.
	如果你定义的一个变量和某个保留关键字冲突,这时候可以使用单下划线作为后缀
	lambda_ = 2.0 # Trailing _ to avoid clash with lambda keyword



# 创建可管理的属性
自定义某个属性的一种简单方法是将它定义为一个property