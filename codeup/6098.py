# 10x10 미로 입력 받기
maze = [list(map(int, input().split())) for _ in range(10)]

# 개미의 시작 위치
x, y = 1, 1

while True:
    # 현재 위치를 9로 표시
    if maze[x][y] == 0:
        maze[x][y] = 9
    elif maze[x][y] == 2:  # 먹이를 만나면 표시하고 종료
        maze[x][y] = 9
        break

    # 오른쪽으로 먼저 이동
    if maze[x][y + 1] != 1:
        y += 1
    # 오른쪽이 벽이면 아래로 이동
    elif maze[x + 1][y] != 1:
        x += 1
    # 둘 다 막히면 종료
    else:
        break

# 결과 출력
for row in maze:
    print(' '.join(map(str, row)))
