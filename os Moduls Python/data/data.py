import os

if(not os.path.exists("zaeem")):
  os.mkdir("zaeem")



for i in range(0,100):
    os.mkdir(f"zaeem/day{i+1}")
    