
def find_info(info_sv, mssv):
    ds_masv = info_sv['ma_sv']
    for i in range (len(ds_masv)):
        if ds_masv[i] == mssv:
            return ds_masv[i], info_sv['ho_ten'][i], info_sv['diem_tb'][i]
    return -1

info_sv = {'ma_sv':['100','101','102','103','104'],
           'ho_ten':['Nguyen Van A', 'Tran Thi B', 'Le Quoc C', 'Tam Thai Tu', 'Dat Van Tay'],
           'diem_tb':[8.0, 9.2, 7.8, 9.8, 10]}
try:
    mssv = input()
    if mssv == '':
        print('Khong duoc de trong!')
    ma_sv, hoten, dtb = find_info(info_sv, mssv)
    print('---THONG TIN SINH VIEN')
    print(f'MSSV: {ma_sv} | Ho ten: {hoten}')
    print('Diem trung binh', dtb)
except Exception:
    print('Khong tim thay thong tin sinh vien. Vui long kiem tra lai!')