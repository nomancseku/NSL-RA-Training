"""যখন স্বাধীনভাবে কোন পাইথন স্ক্রিপ্টকে রান করানো 
য় তখন স্বয়ংক্রিয়ভাবে এর জন্য একটি __name__ নামের 
ভ্যারিয়েবল তৈরি হয় যার ভ্যালু সেট করা হয় স্ট্রিং 
"__main__" . """

def my_module_func():
    print("Abdullah Al Noman")

if __name__ == "__main__":
    print("Noman")


print("It will be printed")