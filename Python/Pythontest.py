

print("aa")

array = [1,6,10,4,5]

for x in range(len(array)):
    print(array[x-1])

for x in range(len(array)):
    if array[x-1]>1 and array[x-1]<7:
        array[x-1] = True
    else:
        array[x-1] = False

print(array)
