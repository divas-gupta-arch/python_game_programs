
d2={'c':40,'d':50,'c':60}
for i in d2:
    if i in d1.keys():
        d1[i]=d1[i]+d2[i]
    else:
        d1[i]=d2[i]
print(d1)
