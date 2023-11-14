import random

def input_matrix():  # Функция для ввода матрицы с клавиатуры.
    while True:
        n = int(input("Введите количество строк (N): "))
        m = int(input("Введите количество столбцов (M): "))
        if type(n) != int or type(m) != int:
            print("Некорректный ввод. Введите целые числа для N и M.")
        elif n < 0 or m < 0:
            print("Размеры матрицы должны быть положительными числами.")
        else:
            break

    matrix = []
    print("Введите элементы матрицы построчно:")
    while True:
        for i in range(n):
            row = list(map(int, input().split()))
            for j in range(len(row)):
                if type(row[j]) != int:
                    print("Некорректный ввод. Введите целые числа для элементов матрицы.")
                    i -= i
                    break
            if len(row) != m:
                print("Количество элементов в строке должно быть равно ", m, ". Повторите ввод.")
                i -= i
            else:
                matrix.append(tuple(row))
        print("Матрица введена успешно.")
        return matrix


def generate_matrix():  # Функция для генерации случайной матрицы размером n x m.
    while True:
        n = int(input("Введите количество строк (N): "))
        m = int(input("Введите количество столбцов (M): "))
        if type(n) != int or type(m) != int:
            print("Некорректный ввод. Введите целые числа для N и M.")
        elif n <= 0 or m <= 0:
            print("Размеры матрицы должны быть положительными числами.")
        else:
            break

    min_value = int(input("Введите минимальное значение элементов матрицы: "))
    max_value = int(input("Введите максимальное значение элементов матрицы: "))
    matrix = []
    for _ in range(n):
        row = tuple(random.randint(min_value, max_value) for _ in range(m))
        matrix.append(row)
    return matrix


def find_saddle_points(matrix):  # Функция для поиска седловых точек в матрице
    saddle_points = []
    for i in range(len(matrix)):
        min_in_row = min(matrix[i])
        for j in range(len(matrix[i])):
            max_in_col = max(matrix[k][j] for k in range(len(matrix)))
            if matrix[i][j] == min_in_row and matrix[i][j] == max_in_col:
                saddle_points.append(min_in_row)
    return saddle_points

def main():
    matrix = None
    saddle_points = None
    while True:
        print("\nМеню:")
        print("1. Ввести матрицу\n2. Выполнить алгоритм")
        print("3. Вывести результат\n4. Вывести матрицу\n5.Завершить работу")
        choice = input("Выберите действие: ")
        if choice == "1":
            print("1. Ввести матрицу вручную \n2. Сгенерировать матрицу автоматически")
            s = input("Выберите действие: ")
            if s == "1":
                matrix = input_matrix()
                saddle_points = None  # Сбрасываем результаты, так как введены новые данные
            elif s == "2":
                matrix = generate_matrix()
            else:
                print("Некорректный выбор. Попробуйте снова.")
        elif choice == "2":
            if matrix is None:
                print("Сначала введите матрицу.")
            else:
                saddle_points = find_saddle_points(matrix)
                print("Алгоритм выполнен.")
        elif choice == "3":
            if len(saddle_points) == 0:
                print("Седловых точек нет или алгоритм не был выполнен.")
            else:
                print("Седловые точки:")
                for point in saddle_points:
                    print(point)
        elif choice == "4":
            print(matrix)
        elif choice == "5":
            print("Программа завершена.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
