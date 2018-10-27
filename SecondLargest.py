# Find the second Largest number
# [3543,544,56,34] output should be 544
def secondLargest(a):
    largest=None
    secondLargest=None
    for current in a:
        if largest == None:
            largest=current
        elif current>largest:
            secondLargest=largest
            largest=current
        elif secondLargest is None:
            secondLargest=current
        elif current > secondLargest:
            secondLargest=current
    return secondLargest

print(secondLargest([223,4,54,452,64]))
