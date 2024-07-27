def is_sorted(list):
    for i in range(len(list)-1):
        if list[i]>list[i+1]:
            return False
    return True
user_input=input("enter a list of integers:")
my_list=eval(user_input)
print(is_sorted(my_list))

    
    
