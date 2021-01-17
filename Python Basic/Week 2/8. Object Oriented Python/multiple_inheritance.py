class A:
    def where(self):
        print("I am from class A")


class B:
    def where(self):
        print("I am from class B")


class C(B, A):
    pass
an_instance_of_c = C()
an_instance_of_c.where()
print(C.mro())

class C(A, B):
    pass
second_instance_of_c = C()
second_instance_of_c.where()

"""এই অর্ডার ভিত্তিক মেথড খোঁজার জন্য পাইথন নিজস্ব নিয়ম ফলো করে এবং
 সেটা দেখতে চাইলে আমরা প্রোগ্রামে print(C.mro()) স্টেটমেন্টটি ব্যবহার করতে পারি"""
print(C.mro())