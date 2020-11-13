import sys

N = int(sys.stdin.readline().strip())

student_list = []
for _ in range(N):
    name, kor, eng, math = sys.stdin.readline().split()
    student_list.append((name, int(kor), int(eng), int(math)))

student_list.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))
for value in student_list:
    print(value[0])