def solution(arr1, arr2):
    if (len(arr1)==len(arr2)) and (len(arr1[0])==len(arr2[0])):
        for i in range(len(arr1)):
            for j in range(len(arr1[i])):
                arr1[i][j]=arr1[i][j]+arr2[i][j]
    return arr1