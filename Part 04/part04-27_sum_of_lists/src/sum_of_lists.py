def list_sum(list1 : int, list2 : int):
    combined_list = []
    for i in len(list1):
        combined_list.append(list1[i] + list2[i])
    return combined_list





if __name__ == "__main__":
    a = [1,2,1,2,1,2]
    b = [2,3,4,5,6,7]
    print(list_sum(a, b)) # [8, 10, 12]