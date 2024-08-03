def number_of_occurrences(numbers,target):

    count=numbers.count(target)
    first_index=numbers.index(target)
    last_index=len(numbers)-numbers[::-1].index(target)-1

    print(f"Number of occurrences:{count}")
    print(f"First index:{first_index}, Last index:{last_index}")

    return count
numbers=(eval(input("enter a list:")))
target=int(input("enter the target number:"))
result=number_of_occurrences(numbers,target)
print(result)