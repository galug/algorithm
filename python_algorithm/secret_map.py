def secret_map(n, arr1:[int], arr2:[int]) ->[str]:
    results = []
    for i in range(n):
        results.append(bin(arr1[i]|arr2[i])[2:]
                        .zfill(n)
                        .replace('1','#')
                        .replace('0',' '))
    return results
arr1 =[9,20,28,18,11]
arr2 = [30,1,21,17,28]
print(secret_map(5,arr1,arr2))