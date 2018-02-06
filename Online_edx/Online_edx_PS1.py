"""TASK A:
Print number of vowels in a string"""
s = 'azcbobobegghakl'

vowels = 'aeiou'

def count_vowels(s):
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    print("Number of vowels: %s " % count)


count_vowels(s)

"""TASK B:
Print number of times 'bob' appears in a string"""
#def string_in_string(s,char):


def bobcounter(s):
    count = 0
    for i in range(len(s)+1):
        if s[i:i+3] == "bob": #Here is the key diff
            count += 1
    print("Number of times bob occurs is: %s " % count)

bobcounter(s)


"""TASK C:
Longest tring in alphabetical order"""

s = 'azcbobobegghakl'

from itertools import count

def substring(s):
    maxsubstr = s[0:0]
    for start in range(len(s)):
        for end in count(start + len(maxsubstr) + 1):
            substr = s[start:end]
            if len(substr) != (end - start):  # found duplicates or EOS
                break
            if sorted(substr) == list(substr):
                maxsubstr = substr
    return maxsubstr


print("Longest substring in alphabetical order is: %s" % substring(s))




