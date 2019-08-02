def coin_change(arr, leng, tot):
    if tot == 0:
        return 1
    
    if tot < 0:
        return 0
    
    if leng <= 0 and tot >=1:
        return 0
        
    return coin_change(arr, leng-1, tot) + coin_change(arr, leng, tot-arr[leng-1])
    
arr = [1, 3, 5]
tot = 6
print(coin_change(arr, len(arr), tot))
