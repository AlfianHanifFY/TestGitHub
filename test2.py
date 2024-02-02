#sorting algo

arr = [0,123,4,23,4,5,123,123,4123,54,7,3,5,73,41,3,123,1442]



for i in range(len(arr)):
    for j in range(i, len(arr)):
        if arr[i] > arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
            
print(arr)