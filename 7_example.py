f = open("예외처리연습.txt", "r", encoding="utf-8")
txt = f.readlines()
try:
    n = int(input())
    for i in range(n):
        print(txt[i])
except IndexError:
    print('모든 행이 출력완료 되었습니다')