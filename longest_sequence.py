#abcdef
#abcabcbb
#3
# longest string.
# Need to implement sub-string ie pwwkew is wke - substring pwke is sequence
def function(n):
    result=set()
    first_val=""
    for i in n:
        if first_val is "":
            first_val=i
        if i not in result:
            first_val=i
            result.add(i)
    return len(result)

print(function("abcabcbb"))
print(function("bbbbb"))
print(function("pwwkew"))
