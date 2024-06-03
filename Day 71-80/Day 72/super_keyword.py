class ParentClass:
    def parent_method(self):
        print("Parent method!")

class ChildClass(ParentClass):
    def parent_method(self):
        print("\nParent method but inside child class!")
        super().parent_method()

    def child_method(self):
        print("\nChild method.")
        super().parent_method()

child_obj = ChildClass()
child_obj.child_method()
child_obj.parent_method()