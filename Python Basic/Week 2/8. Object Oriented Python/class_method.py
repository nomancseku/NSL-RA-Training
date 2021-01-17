#ক্লাসের মেথড গুলোর প্রথম প্যারামিটার হিসেবে self ডিফাইন করতে হয়
#কিন্তু ক্লাস মেথড একটু আলাদা। এ ধরনের মেথডকে সরাসরি ক্লাসের মাধ্যমেই কল করা হয় এবং সেই ক্লাস কে ওই মেথডের cls প্যারামিটার হিসেবে পাঠানো হয় (ক্লাস মেথডের প্রথম প্যারামিটার সাধারণত cls হয়ে থাকে)
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)

square = Rectangle.new_square(5)
print(square)
print(square.calculate_area())
