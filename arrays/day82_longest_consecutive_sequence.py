arr = sorted(list(map(int, input("Enter: ").split())))

if len(arr) == 0:
    print(0)
else:
    max_len = 1
    curr_len = 1

    for i in range(1, len(arr)):

        if arr[i] == arr[i - 1]:
            continue

        elif arr[i] == arr[i - 1] + 1:
            curr_len += 1

        else:
            max_len = max(max_len, curr_len)
            curr_len = 1

    max_len = max(max_len, curr_len)

    print(max_len)
