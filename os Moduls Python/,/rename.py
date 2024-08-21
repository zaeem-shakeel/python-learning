import os


# for i in range(0,100):
#     os.rename(f"zaeem/toturial{i+1}",f"zaeem/toturial {i+1}")
    
    
    
    
folder=os.listdir("zaeem")
print(folder)


for folders in folder:
    print(folders)
    print(os.listdir(f"zaeem/{folders}"))
    
    
# cmd='date'
# os.system(cmd)