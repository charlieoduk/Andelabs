def min_max(arr):
    # sets the first item in array as the smallest number
    min_num = arr[0]
    # sets the first item in array as the biggest number
    max_num = arr[0]
    new_arr =[]
    # loops through the array
    for i in range (len(arr)):
        # if number at index arr[i] is less than the minimum number
        if arr[i] < min_num:
            # then that number becomes the new minimum number
            min_num = arr[i]
    # the minimum number is then pushed to the new array
    new_arr.append(min_num)
    # we loop through the array again this time looking for the biggest number
    for i in range (len(arr)):
        # if number at inder arr[i] is bigger than max_num
        if arr[i] > max_num:
            # that number becomes the new max_num
            max_num = arr[i]
            # we check if our max num is the same as our min num
            if max_num == new_arr[0]:
                # if it is we short circuit the program. It stops here
                return
            # if it is not then we push the max number into the new array
            new_arr.append(max_num)
    # new array is returned
    return new_arr
