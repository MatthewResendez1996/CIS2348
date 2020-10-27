#Matthew James Resendez
#1431242
uword=list(input().split(" "))
wcount = []
for w in uword:
    wcount.append(uword.count(w))
for i in range(len(uword)):
    print(uword[i], wcount[i])