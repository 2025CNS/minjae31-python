c = input()  # 문자 1개 입력받기

for i in range(ord('a'), ord(c)+1):
    print(chr(i), end=' ')
