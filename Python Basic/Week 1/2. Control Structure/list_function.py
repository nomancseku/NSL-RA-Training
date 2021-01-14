print(dir(list))
print(help(list.append))
#append
nums = [1,2,3]
nums.append(4)
print(nums)

#insert
words = ["A", "C"]
index = 1
words.insert(index, "B")

print(words)


#index
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))
print(letters.index('u'))

#count (liked this one)
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.count('p'))


#max min len
nums = [1, 2, 4, 20, 50, 3, 4]
print(max(nums))
