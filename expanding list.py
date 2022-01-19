def Expanding(l):
    lst=[]
    for i in range(1,l+1):
        numbers=int(input(f"{i}. Enter here: "))
        lst.append(numbers)
    print("first list:",lst)
    lst2=[]
    for i in range(1,len(lst)):
        new_num=abs(lst[i]-lst[i-1])
        lst2.append(new_num)
    print("new list:",lst2)
    a=True
    for i in range(1,len(lst2)):
        if lst2[i]<=lst2[i-1]:
            a=False
    return a
    
l=int(input("number of elements in list: "))
print(Expanding(l))
