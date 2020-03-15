# 请利用print()输出1024 * 768 = xxx
def move(n,a='A',b='B',c='C'):
    if n == 1:
      print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        print(a, '-->', c)
        move(n - 1, b, a, c)
move(3)        