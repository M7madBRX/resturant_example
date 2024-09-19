class  Restaurant():
  def __init__(self,restaurant_name,cuisine_type):
      self.restaurant_name = restaurant_name
      self.cuisine_type = cuisine_type
      self.number_served  = 0
  def  descripe_resturant (self):
   print (f"Resturant name :{ self.restaurant_name}")
   print (f"cuisine name :{ self.cuisine_type}:")

  def set_number_served(self,number):
      self.number_served = number

  def increasment_sreved (self,peopleserved):
      self.number_served += peopleserved
      print(f"people that served is :{self.number_served}")



  def open_restaurant(self):
    print(f"The:{self.restaurant_name} is open")
# my_resturant = Restaurant("kabsa","arab")
# my_resturant.descripe_resturant()
# my_resturant.open_restaurant()
# print("="*50)
# my_resturant1 = Restaurant("nahda b","E-d")
# my_resturant1.descripe_resturant()
# my_resturant1.open_restaurant()

# my_resturant1.set_number_served(40)
# print(f"served number is :{my_resturant1.number_served}")
# my_resturant1.set_number_served(50)
# print(f"served number is :{my_resturant1.number_served}")
# my_resturant1.increasment_sreved(30)
# print(f"served number is :{my_resturant1.number_served}")
class IceCream (Restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavor):
        super().__init__(restaurant_name,cuisine_type)
        self.flavor =flavor
    def display_flavor (self):
        print(f"The Flavor  are:")
        for flavor in self.flavor :
            print(f"- {flavor}")

ice_cream = IceCream(")bnana","choco",["banna","mint","choco"])
ice_cream.display_flavor()
