from collections import Counter
def min_removals_to_equal_frequency(s):
    char_count=Counter(s)
    freqs=list(char_count.values())
    freq_counter=Counter(freqs)
    min_removals=float('inf')
    for target_freq in freq_counter:
        removals=0
        for freq,count in freq_counter.items():
            if freq>target_freq:
                removals+=(freq-target_freq)*count

            elif freq<target_freq:
                removals+=freq*count

        min_removals=min(min_removals,removals)
    return min_removals
string=input("enter a string:")
result=min_removals_to_equal_frequency(string)
print(result)