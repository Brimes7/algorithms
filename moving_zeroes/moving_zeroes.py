'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == 0:
            x = 0
            end = len(arr) - 1
            lastvalue = arr[end]
            arr[end] = x
            while lastvalue == 0 and end is not i:
                end -= 1
                temp = arr[end]
                arr[end] = lastvalue
                lastvalue = temp

            arr[i] = lastvalue

            # if lastvalue == 0:
            #     z = arr[len(arr)-1]
            #     z =
            #     arr[len(arr)-1] = lastvalue
            #
            # arr[i] = lastvalue
    return arr








if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")