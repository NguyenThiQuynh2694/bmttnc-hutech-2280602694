def tao_tuple_tu_list(lst):
    return tuple(lst)
    input_list = input("nhap danh sach cac so, cach nhau bang dau phay: ")
    numbers = list(map(int, input_list.splist(',')))
    my_tuple = tao_tuple_tu_list(numbers)
    print("list: ", numbers)
    print("Tuple tuwf list:", my_tuple)