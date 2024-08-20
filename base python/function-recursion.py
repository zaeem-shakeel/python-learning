"""
herors=["iromen","supermam","spiderman","batman"]
def calac_list(list):
        print(list,end=" ")
calac_list(herors)
"""

"""
def calc_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
calc_fact(5)
    """

"""
def converter(usd_val):
    inr_val=usd_val*250
    print(usd_val,"USD",inr_val,"INR")
converter(70)
    """
    
    
    #recursion fuction
    
"""
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5)
"""

"""
def fact(n):
    if(n==0 or n==1):
        return 1
    return n*fact(n-1)
print(fact(4))


def calc_sum(n):
    if(n==0):
        return 0
    return calc_sum(n-1)+n
sum=calc_sum(5)
print(sum)
"""

def print_list(list, idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
    
    fruits=["mango","apple","bananon","litch",]
    print_list(fruits)
    