# Find the largest number in  the list

def secondLargest(a):
    largest=None
    for current in a:
        if largest == None:
            largest=current
        elif current>largest:
            largest=current
    return largest
print(secondLargest([1,7,2,12,67]))
