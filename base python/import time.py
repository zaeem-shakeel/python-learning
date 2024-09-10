# Python program to explain time.gmtime() method 
# importing time module 
import time 


# # If secs parameter 
# # is not given then 
# # the current time 
# # as returned by time.time() method 
# # is used 

# # Convert the current time in seconds 
# # since the epoch to a 
# # time.struct_time object in UTC 
# obj = time.gmtime() 

# # Print the time.struct.time object 
# print(obj) 



# import time

# print("Start:", time.time())
# time.sleep(2)
# print("End:", time.time())
# # Output:
# # Start: 1602299933.233374
# # End: 1602299935.233376


# import time

# t = time.localtime()
# formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

# print(formatted_time)
# # Output: 2022-11-08 08:45:33


# import time
# curr = time.ctime(1627908313.717886)
# print("Current time:", curr) 


# import time
# for i in range(4):
#     time.sleep(1)
#     print(i)


# print(3)
# time.sleep(3)
# print("this time for your")




# import time
# obj = time.localtime(1627987508.6496193)
# print(obj)



# import time
# obj1 = time.gmtime(1627987508.6496193)
# time_sec = time.mktime(obj1)
# print("Local time (in seconds):", time_sec)



# from time import gmtime, strftime
# s = strftime("%a, %d %b %Y %H:%M:%S", 
#              gmtime(1627987508.6496193))
# print(s)



# str_time=time.asctime()
# print(str_time)




# import time
# obj = time.gmtime(1627987508.6496193)
# time_str = time.asctime(obj)
# print(time_str)
# obj = time.localtime(1627987508.6496193)
# time_str = time.asctime(obj)
# print(time_str)


print(time.time())
obj=time.gmtime(1725965583.3368223)
print(time.ctime(1725965583.3368223))
print(time.localtime().tm_mday)
print(time.mktime(obj))
print(time.asctime(obj))