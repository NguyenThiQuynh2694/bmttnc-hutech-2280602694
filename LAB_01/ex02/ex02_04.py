#tạo một danh sách để lưu kết quả
j=[]
#duyệt các số trong đoạn từ 200-3200, kt i có chia ht cho 7 và không phải là bội số của 5 k
for i in range(2000, 3200):
    if (i % 7== 0) and (i % 5 != 0):
        j.append(str(i))
print(','.join(j))