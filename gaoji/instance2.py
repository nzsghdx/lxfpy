

L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = ???

#[s.lower() if isinstance(L1[s],str) for s in L1]
print(L1)
for s in L1:
    if isinstance(s,str):
        s.lower()
        print(s)
#print(L1)
