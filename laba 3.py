def hanoi(n, source, target, auxiliary):
    if n == 1:
        print("Переместить диск 1 с", source, "на", target)
        return

    hanoi(n - 1, source, auxiliary, target)

    print("Переместить диск", n, "с", source, "на", target)

    hanoi(n - 1, auxiliary, target, source)


n = int(input("Введите количество дисков: "))
hanoi(n, 'A', 'C', 'B')