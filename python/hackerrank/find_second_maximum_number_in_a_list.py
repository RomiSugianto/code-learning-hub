if __name__ == '__main__':
    # n = int(input())
    arr = map(int, input().split())
    my_list = list(set(arr))
    max_number = max(my_list)
    my_list.remove(max_number)
    sorted_list = sorted(my_list)

    print (sorted_list[-1])