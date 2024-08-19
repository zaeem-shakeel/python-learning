questions=[
           ["which language used to create fb?","python","French","javascript","php","none",4],  
           ["which language used to create fb?","python","French","javascript","php","none",4],  
           ["which language used to create fb?","python","French","javascript","php","none",4],  
           ["which language used to create fb?","python","French","javascript","php","none",4],  
           ]
levels=[1000,2000,5000,7000,10000,40000,500000,70000,80000,100000,320000,5000000,700000,10000000]

money=0
for i in range(len(questions)):
    question=questions[i]
    print(f"\n\n\nQuestion for Rs {levels[i]}")
    print(f"a.{question[1]}         b.{question[2]}")
    print(f"c.{question[3]}         d.{question[4]}")
  
    reply=int(input("Enter your answerse 1-4 or 0 to quit:"))
    
    if(reply==0):
        money==levels[i-1]
        break 
    if(reply==question[-1]):
        print(f"Correct answers , your have won.{levels[i]}")
    else: 
        print("Wrong answers")
        break
    
    if i==4:
        money==10000
    elif i==9 :
        money==100000
    elif i==13 :
        money==10000000
    print(f"you take money home is {money}")    
        
                
                
# questions = [
#     ["Which language was used to create Facebook?", "Python", "French", "JavaScript", "PHP", "None", 4],
#     ["Which language was used to create Facebook?", "Python", "French", "JavaScript", "PHP", "None", 4],
#     ["Which language was used to create Facebook?", "Python", "French", "JavaScript", "PHP", "None", 4],
#     ["Which language was used to create Facebook?", "Python", "French", "JavaScript", "PHP", "None", 4],
# ]
# levels = [1000, 2000, 5000, 7000, 10000, 40000, 500000, 70000, 80000, 100000, 320000, 5000000, 700000, 10000000]
# money = 0

# for i in range(len(questions)):
#     question = questions[i]
#     print(f"\n\n\nQuestion for Rs {levels[i]}")
#     print(f"a. {question[1]}         b. {question[2]}")
#     print(f"c. {question[3]}         d. {question[4]}")

#     reply = int(input("Enter your answer (1-4) or 0 to quit: "))
    
#     if reply == 0:
#         money = levels[i-1] if i > 0 else 0
#         break 

#     if reply == question[-1]:
#         print(f"Correct answer! You have won Rs {levels[i]}.")
#         money = levels[i]
#     else:
#         print("Wrong answer.")
#         break

#     if i == 4:
#         money = 10000
#     elif i == 9:
#         money = 100000
#     elif i == 13:
#         money = 10000000

#     print(f"You take home Rs {money}.")

# print(f"Final amount: Rs {money}")