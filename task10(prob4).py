def roated_sorted_array(numbers):
    num=len(numbers)
    low, high=0,num-1
    while low<=high:
        mid=(low+high)//2

        if numbers[mid]<numbers[(mid-1)%num]:
            return mid
        
        if numbers[mid]>numbers[high]:
            low=mid+1
        else:
            high=mid-1

    return 0
    
nums=(eval(input("enter list of integers:")))
result=roated_sorted_array(nums)
print(result)