T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))

    list_a.sort()
    list_b.sort()

    # print(list_a, list_b)
    cnt_ = 0

    for i in list_b:
        check = [False, False]
        left = 0
        right = N - 1

        while left <= right:
            mid = (left + right) // 2

            if list_a[mid] == i:
                cnt_ += 1
                break
            elif list_a[mid] < i:
                if check[1] == True:
                    break
                else:
                    left = mid + 1
                    check[0] = False
                    check[1] = True
            else:
                if check[0] == True:
                    break
                else:
                    right = mid - 1
                    check[0] = True
                    check[1] = False
    print(f'#{tc} {cnt_}')
