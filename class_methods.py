class A(object):
    x = 0

    def say_hi(self):
        pass

    @staticmethod
    def say_hi_static():
        pass

    @classmethod
    def say_hi_class(cls):
        pass

    def run_self(self):
        self.x += 1
        print self.x # outputs 1
        self.say_hi()
        self.say_hi_static()
        self.say_hi_class()

    @staticmethod
    def run_static():
        print A.x  # outputs 0
        # A.say_hi() #  wrong
        A.say_hi_static()
        A.say_hi_class()

    @classmethod
    def run_class(cls):
        print cls.x # outputs 0
        # cls.say_hi() #  wrong
        cls.say_hi_static()
        cls.say_hi_class()


obj = A()
obj.run_self()
obj.run_static()
obj.run_class()

# A.run_self() #  wrong
A.run_static()
A.run_class()