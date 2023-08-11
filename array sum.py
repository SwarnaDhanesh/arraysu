def find(array, len, Sum):
    print("The sum of the Pair is : ", Sum)
    for i in range(len):
        for s in range(i, len):
            if (array[i] + array[s]) == Sum:
                print(array[i], array[s])
array = [8 ,2 ,1, 6 ,5 ,3 ,7]
Sum = 8
print("The List of array is = ", array)
find(array, len(array), Sum)