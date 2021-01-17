def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32

print(KelvinToFahrenheit(273))
print(int(KelvinToFahrenheit(505.78)))
try:
    print(KelvinToFahrenheit(-5))
except AssertionError:
    print("An assertion error occured")
    raise
finally:
    print("I love this language")
