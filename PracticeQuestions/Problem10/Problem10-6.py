# Can you change the self-parameter inside a class to something else (say “rohan”). Try changing self to “slf” or “rohan” and see the effects.

class Person:
  def __init__(slf, name, age):
    slf.name = name
    slf.age = age

  def myfunc(rohan):
    print(f"Hello my name is {rohan.name}.")
    print(f"My age is {rohan.age}.")

p1 = Person("Reigns", 40)
p1.myfunc()

# No change at all, the output is constant even if the 'self' is changed to 'slf' or 'rohan'.
# However, the above code reduce the readibility of the code significantly. 

