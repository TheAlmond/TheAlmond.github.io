

print("aa")

array = [1,2,3,4,5]

for x in array:
    print(array[x-1])

for x in array:
    if array[x-1]>1 and array[x-1]<4:
        array[x-1] = True
    else:
        array[x-1] = False

print(array)