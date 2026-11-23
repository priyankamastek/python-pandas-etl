class Employee:
   # encapsulation - wrap - variables + functions (methods)
   # variables - class variables and instance variables are assigned to objects
   # constructor is a special method that defines the instance variable for objects
   # self is a variable that refers to the current object
   # self is similar to "this" variable in other OOP languages like Java, typescript, c++
   def __init__(self, e_name, e_age):
      self.name = e_name # self.name is an instance variable
      self.age = e_age # self.age is an instance variable

   # custom method
   def print_employee_details(self): 
     print(f" Employee Name - {self.name} \n Employee Age {self.age}")


def main():
   e1 = Employee("John", 34) # object e1, () is call to __init__()
   e2 = Employee("Jill", 33) # object e2  () is call to __init__()
   print (f" {e1}") # object occupies memory
   print (f" {e2}")
   e1.print_employee_details() #objectname.method()
   e2.print_employee_details()

# call the execute the filename.py file directly(module)
if __name__ == "__main__":   
   main()