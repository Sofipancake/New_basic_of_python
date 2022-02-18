def show(start: int, finish: int):
    with open('bakery.csv', 'r', encoding = 'utf-8') as fr:
        line = fr.readline()
        s = 1
        while (s <= finish) or (finish == 0 and line):
            if s >= start:
                print(line.strip())
            line = fr.readline()
            s = s + 1


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        show(1, 0)
    elif len(sys.argv) == 2:
        program, start = sys.argv
        show(int(start), 0)
    elif len(sys.argv) == 3:
        program, start, finish = sys.argv
        show(int(start), int(finish))
    else:
        print("Программа введена неверно")
