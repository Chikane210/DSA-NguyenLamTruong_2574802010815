danh_ba = {'ten':['Nguyen Lam Truong', 'Trinh Van Teo'],
           'sdt':['0945529960', '0901234560']}

def quanly_danhba(danh_ba, chuc_nang):
    ds_ten = danh_ba['ten']
    ds_sdt = danh_ba['sdt']
    #Them lien he (ten, sdt)
    if chuc_nang == 1:
        step = 0
        try:
            n = int(input('So luong nguoi them vao danh ba: '))
        except ValueError:
            print('Dinh dang so nguoi them vao khong hop le!')
        else:
            while step < n:
                ten = input('Ten: ').title()
                so_dth = input('So dien thoai: ')
                if ten in ds_ten:
                    print('Ten da ton tai')
                elif so_dth in ds_sdt:
                    print('So dien thoai da ton tai')
                elif len(so_dth) != 10:
                    print('So dien thoai khong hop le')
                else:
                    ds_ten.append(ten)
                    ds_sdt.append(so_dth)
                    step += 1
        return ds_ten, ds_sdt
                
    #Tim so dien thoai theo ten
    elif chuc_nang == 2:
        ten = input()
        for i in range (len(ds_ten)):
            if ds_ten[i] == ten:
                return danh_ba['sdt'][i]
    
    #Tim ten theo sdt
    elif chuc_nang == 3:
        sdt = input()
        for i in range (len(ds_sdt)):
            if ds_sdt[i] == sdt:
                return danh_ba['ten'][i]
        return 'So dien thoai khong ton tai'
    
    #Dem so lien he
    elif chuc_nang == 4:
        dem = 0
        so_lh = input('Nhap 3 so dau cua sdt can dem: ')
        if len(so_lh) != 3:
            print('Khong hop le. Vui long nhap lai') 
        for i in range(len(ds_sdt)):
            if ds_sdt[i][:3] == so_lh:
                dem += 1
        return dem
            
print('---CHUONG TRINH QUAN LY DANH BA DIEN THOAI---')
print('Chon chuc nang:')
print('''1. Thêm liên hệ gồm tên và số điện thoại
2. Tìm số điện thoại theo tên
3. Tìm tên theo số điện thoại
4. Đếm số liên hệ có số điện thoại''')
print("Nhan '0' de thoat khoi chuong trinh")
while True:
    try:
        chuc_nang = int(input('Chon chuc nang muon su dung: '))
        if chuc_nang == 0:
            break
        if chuc_nang < 0 or chuc_nang > 4:
            print('Chuc nang khong ton tai')
    except ValueError:
        print('Dinh dang dau vao khong hop le!')
    else:
        print(quanly_danhba(danh_ba, chuc_nang))
        
        
    
        
    