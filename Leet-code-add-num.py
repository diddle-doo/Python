# Check all the combinations in a list if it matches to target and return the result
# [1,2,3]
#target=4
#(1,3),(3,1)

num_list=[1,4,6,5,3,7]
target=10
result=[(num_list[i],num_list[j]) for i  in range(len(num_list)) for j in range(len(num_list)) if num_list[i]+num_list[j]==target and i!=j]
print (result)
