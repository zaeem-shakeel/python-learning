
st=input("enter message")
words=st.split(" ")
codind=True
if(coding):
    nwords=[]
    for word in words:
        if(len(word)>=3):
            r1="dsf"
            r2="jkr"
            stnew=r1+ word[1:]+word[0]+r2
            nword.append(strnew)
        else:
            nword.append(word[::-1])
            print(" ".join(nword))
else:
    nwords=[]
    for word in words:
        stnew=word[3:-3]
        stnew=stnew[-1]+stnew[:-1]
        nwords.append(stnew)
    else:
        nwords.append(word[::-1])
        print(" ".join(nwords))
            