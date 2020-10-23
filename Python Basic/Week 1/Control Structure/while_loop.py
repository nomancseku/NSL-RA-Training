i = 1
while i <= 5:
   print(i)
   i = i + 1

print("I am priting eventually cause the WHILE loop is done with his job.")

#Break
i = 0
while 1 == 1:
   print(i)
   i = i + 1
   if i >= 5:
      print("Breaking")
      break

print("Finished")


# Continue
i = 0
while True:
   i = i +1
   if i == 2:
      print("Skipping 2")
      continue
   if i == 5:
      print("Breaking")
      break
   print(i)

print("Finished")
