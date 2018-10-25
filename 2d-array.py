# 2d array
# Add diagonaly
# 1+3+7=11
test=[[1,2,3],
      [2,3,4],
      [5,6,7]]
total=0
for i in range(len(test)):
    total+=test[i][i]
print(total)
