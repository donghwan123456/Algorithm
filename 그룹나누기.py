def link_check(idx):
    if not visited[idx]:
        visited[idx] = 1

    for i in group[idx]:
        if not visited[i]:
            link_check(i)

T = int(input()) 

for tc in range(1, T + 1):  
    N, M = map(int, input().split()) 
    list_ = list(map(int, input().split()))  
    visited = [0]*(N+1)
    group = [[]for _ in range(N+1)]
    ans = 0

    for i in range(0,M):
        a, b = lsit_[i*2], list_[i*2+1]
        group[a].append(b)
        group[b].append(a)
    
        # 모든 정점에 대해 연결 그룹 확인
    for i in range(1, N + 1):
        if not visited[i]:  # 방문하지 않은 정점인 경우
            link_check(i)  # 해당 정점이 속한 연결 그룹 확인
            ans += 1  # 연결 그룹 개수 증가

    print(f'#{tc} {ans}')  # 결과 출력
