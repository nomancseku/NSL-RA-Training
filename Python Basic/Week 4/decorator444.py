"""যদি কখনো এমন দরকার পরে যে একটা ফাংশনের ফাংশনালিটি একটু পরিবর্তন/পরিবর্ধন 
করা দরকার কিন্তু আমরা সেই ফাংশনের কোড পরিবর্তন করতে চাচ্ছি না। 
তখন ডেকোরেটর ব্যবহার করে আমরা সেই কাজটা করতে পারবো।"""

def my_appriciation(func):
	def appriciation():
		print("You are awesome!")
		func()
		print("Really awesome!")
	return appriciation

def good_work():
	print("Your paper has been published in IEEE")

aap = my_appriciation(good_work)
aap()

# actually ekhane ami good work function take decorate korlam
#my_appriciation এর কাছে আসা ফাংশনকে এই appriciation ফাংশনটি এক্সিকিউট করে। কিন্তু তার আগে ও পরে দুটি অতিরিক্ত প্রিন্ট স্টেটমেন্ট যোগ করে স্টাইল করে দেয়।
@my_appriciation
def good_book():
	print("You have written an amazing book on python.")

print(good_book())