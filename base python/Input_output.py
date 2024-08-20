#with open ("practive.txt ", "w") as f:
    #f.write("Hi everyone. \n my name is zaeem")
   # f.write("I am reading python.\n I want to code programming")
    #data=f.read()
   # print(data)
    
"""
with open("practive.txt", "r") as f:
  data=f.read()
  
  new_data=data.replace("python","java")
  
  with open ("practive.txt" ,"w") as f:
    f.write(new_data)
    """

"""
def chech_word():
  word="learing "
  with open("practive.txt", "r") as f:
     data=f.read()
  if(data.find(word)!=-1):
      print('found')
  else:
      print("not found")



def check_for_line():
  word="I"
  data=True
  no_line=1
  with open("practive.txt","r") as f:
    while data:
      data=f.readline()
      if(word in data):
         print(no_line)
         return
      no_line+=1
        
    return -1
print(check_for_line())
"""

    
    
#f=open("sample.txt", "r")
#data=f.read() 
#print(data)


count=0
with open("sample.txt","r") as f:
  data=f.read()
  print(data)
  nums=data.split(",")
  for val in nums:
   if(int(val) % 2== 0):
      count+=1
      
print(count)           