array=[1,2,3,4,4,5,6]
element=10
index=3
for i in range(len(array) - 1, index, -1):
    array[i] = array[i - 1]
array[index] = element
print(array)