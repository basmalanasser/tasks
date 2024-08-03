def second_largest(numbers):
    
    if len(numbers)<2:
        return None
    
    largest=max(numbers)
    second_largest=max(x for x in numbers if x !=largest)
    return second_largest
numbers=(eval(input("enter a list of integers:")))
result=second_largest(numbers)
print(result)
