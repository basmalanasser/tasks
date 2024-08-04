def remove_occurrences(list,num):
    return[i for i in list if i!=num]
lst=(eval(input("enter a list of integers:")))
num=int(input("enter a number:"))
newlist=remove_occurrences(lst,num)
print(newlist)
 