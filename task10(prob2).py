numbers=(eval(input("enter a list of integers:")))
def find_missing_num(numbers):
    start=min(numbers)
    end=max(numbers)
    ex_sum=(start+end)*(end-start+1)//2
    act_sum=sum(numbers)
    return ex_sum-act_sum
missingnum=find_missing_num(numbers)
print("The missung number is:",missingnum)
