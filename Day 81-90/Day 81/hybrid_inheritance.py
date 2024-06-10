#hybrid inheritance

class BaseClass:
    pass

class Derived1(BaseClass):
    pass    #combined with base, single inh.

class Derived2(BaseClass):
    pass

class Derived3(Derived1, Derived2):
    pass    #combined with derived 1 and derived 2, multiple

#all combined-> hybrid

'''
       Base
        /\
    D1      D2
      \    /
        D3
'''