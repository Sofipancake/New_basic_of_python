def recording(*argv):
    func, price = argv
    with open('bakery.csv', 'a+', encoding='utf-8') as fr:
        fr.write(f'{price}\n')

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        recording(sys.argv)
    else:
        print("Неизвестная цена")
