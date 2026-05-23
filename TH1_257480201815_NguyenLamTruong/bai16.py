def ptu_gan_nhat(arr, key):
    vitri = []
    for i in range (len(arr)):
        if arr[i] < key:
            gan_x = key - arr[i]
        else:
            gan_x = arr[i] - key
        vitri.append(gan_x)
    gan_x_nhat = min(vitri)
    return vitri.index(gan_x_nhat)
    

try:
    arr = [int(x) for x in input().split()]
    x = int(input())
    if len(arr) == 0:
        print('Mang trong')
    else:
        print(ptu_gan_nhat(arr,x))
except ValueError:
    print('Dinh dang dau vao khong hop le!')
        
        
        