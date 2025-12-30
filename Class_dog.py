class dog:
  def __init__(self, breed, current_age, name):
    self.breed= breed
    self.current_age= current_age
    self.name= name
dog1= dog("poodle", 10, "mochi")
dog2= dog("maltipoo", 8, "remo")
print("\nThe dog",dog1.breed, "is", dog1.current_age, "years old currently and its name is", dog1.name)
print("The dog",dog2.breed, "is", dog2.current_age, "years old currently and its name is", dog2.name,"\n")
