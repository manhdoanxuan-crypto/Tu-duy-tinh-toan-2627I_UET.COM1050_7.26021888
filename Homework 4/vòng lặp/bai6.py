while True:
    try:
        a = list(map(int, input().split()))
        print(sum(a))
    except EOFError:
        break