# true value means 3 to 16 code run

st = input("enter  message :")
words = st.split(" ")
coding = True  # True means code exist to 1 to 16 and Flse means code exists to 18 to 23
if coding:
    nwords =[]
    for word in words:
        if len(word) >= 3:
            r1 = "dsf"
            r2 = "jkr"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords = []
    for word in words:
        stnew = word[3:-3]
        stnew = stnew[-1] + stnew[:-1]
        nwords.append(stnew)
    print(" ".join(nwords))


