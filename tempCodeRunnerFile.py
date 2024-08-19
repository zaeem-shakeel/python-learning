questions=[
           ["which language used to create fb?","python","French","javascript","php","none",4],  
           ["which language used to create fb?","python","French","javascript","php","none",4],  
           ["which language used to create fb?","python","French","javascript","php","none",4],  
           ["which language used to create fb?","python","French","javascript","php","none",4],  
           ]
levels=[1000,2000,5000,7000,10000,40000,500000,70000,80000,100000,320000,5000000,700000,10000000]
i=0
money=0
for i in range(len(questions)):
    question=questions[i]
    print(f"\n\n\nQuestion for Rs {levels[i]}")
    print(f"a.{question[1]}         b.{question[2]}")
    print(f"c.{question[3]}         d.{question[4]}")
    i=+1
    reply=int(input("Enter your answerse 1-4 or 0 to quit:"))
    if(reply==0):
        money==levels[i]
        break 
    if(reply==question[-1]):
        print(f"Correct answers , your have won.{levels[i]}")
    if(i==4):
        money==10000
    elif(i==9):
        money==100000
    elif(i==13):
        money==10000000
    else: 
        print("Wrong answers")
        break
    print(f"you take money home is {money}")    
        
       