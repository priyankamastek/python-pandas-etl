import pandas as pd

class DataExt:
  #constructor 
   def __init__(self, file_path:str):
      self.file_path = file_path

   def load_csv(self):
      # Write your custom logic
      df = pd.read_csv(self.file_path)
      print(df)
     

obj = DataExt('src\\data\\incoming\\orders.csv')
obj.load_csv()


