def input_matrix():
    pass

def generate_matrix():
    pass
def find_saddle_points(matrix):
    pass

def main():
    while True:
        print("\nМеню:")
        print("1. Ввести матрицу\n2. Выполнить алгоритм")
        print("3. Вывести результат\n4. Вывести матрицу\n5.Завершить работу")
        choice = input("Выберите действие: ")
        if choice == "1":
            print("1. Ввести матрицу вручную \n2. Сгенерировать матрицу автоматически")
            s = input("Выберите действие: ")
        elif choice == "5":
            print("Программа завершена.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
