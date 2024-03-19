def cal_p(k, prob):
    global ans, cnt
    cnt = cnt + 1  # 함수 호출 횟수 증가
    if k == N:  # 모든 일이 배정된 경우
        if ans < prob:  # 기존 최대 확률보다 현재 확률이 크면 업데이트
            ans = prob
        return
    for work_num in range(N):  # 각 일에 대해 반복
        if not assigned[work_num] and prob * p_mat[k][work_num] * 0.01 > ans:
            # 해당 일이 배정되지 않았고, 현재 확률이 최대 확률보다 크면
            assigned[work_num] = 1  # 일 배정 표시
            cal_p(k+1, prob * p_mat[k][work_num] * 0.01)  # 다음 단계의 확률 계산
            assigned[work_num] = 0  # 백트래킹: 일 배정 취소
 
# 테스트 케이스의 개수 입력받기
T = int(input())
# 각 테스트 케이스에 대해 반복
for t in range(1, T+1):
    N = int(input())  # 일의 개수 입력받기
    p_mat = [list(map(int, input().split())) for _ in range(N)]  # 확률 행렬 입력받기
    ans = 0  # 최대 확률 초기화
    assigned = [0]*(N+1)  # 일이 배정되었는지 나타내는 리스트 초기화
    cnt = 0  # 함수 호출 횟수 초기화
    cal_p(0, 1)  # 백트래킹을 사용하여 가능한 모든 경우 계산
    print(f'#{t} {ans*100:.6f}')  # 결과 출력
