from collections import deque

# 테스트 케이스의 개수(T)를 입력 받습니다.
T = int(input())

# 각 테스트 케이스에 대해 실행합니다.
for tc in range(1, T + 1):
    # 비용(cost)과 각 달의 이용 계획(list_)을 입력 받습니다.
    cost = list(map(int, input().split()))
    list_ = list(map(int, input().split()))

    # 초기 최소 비용(ans)을 설정합니다.
    # 전체를 일일 이용으로 계산했을 때의 비용 또는 1년 이용권 비용(cost[3]) 중 작은 값을 초기화합니다.
    ans = min(sum(list_) * cost[0], cost[3])

    # BFS를 위한 deque를 생성합니다.
    q = deque()
    # 초기 상태를 큐에 삽입합니다. (현재 비용, 현재 월)
    q.append((0, 0))

    # 큐가 빌 때까지 반복합니다.
    while q:
        # 현재 비용(curr_cost)과 현재 월(curr_month)을 큐에서 추출합니다.
        curr_cost, curr_month = q.popleft()

        # 현재 비용이 ans보다 작고 현재 월이 12 미만인 경우:
        if curr_cost < ans and curr_month < 12:
            # 일간 이용을 추가하고 큐에 삽입합니다.
            q.append((curr_cost + list_[curr_month] * cost[0], curr_month + 1))
            # 월간 이용을 추가하고 큐에 삽입합니다.
            q.append((curr_cost + cost[1], curr_month + 1))
            # 분기 이용을 추가하고 큐에 삽입합니다.
            q.append((curr_cost + cost[2], curr_month + 3))
        # 현재 월이 12 이상인 경우:
        elif curr_month >= 12:
            # 현재 비용과 ans를 비교하여 최소값을 업데이트합니다.
            ans = min(curr_cost, ans)

    # 최종적으로 최소 비용을 출력합니다.
    print(f'#{tc} {ans}')