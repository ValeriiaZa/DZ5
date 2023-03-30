
lst1 = [1, 2, 3]
if len(lst1) % 2 == 0:
    lstnew = [lst1[0:len(lst1) //2],lst1[len(lst1)// 2:]]
    print(lstnew)
elif len(lst1) % 2 != 0:
    lstnew =[lst1[0:(len(lst1)+ 1) // 2 ], lst1[(len(lst1)+ 1) // 2:]]
    print(lstnew)
elif len(lst1) == 0:
    lstnew =[lst1[:]],[lst1[:]]
    print(lstnew)




