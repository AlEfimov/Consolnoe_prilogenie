import linecache


def create_user():
    with open("user_data.txt", "w") as fout:
        user_name = input("Введите ФИО: ")
        fout.write(user_name + "\n")
        user_birth = int(input("Введите год рождения: "))
        fout.write(str(user_birth) + "\n")
        print("Создан аккаунт:", user_name, "(" + str(2024 - user_birth) + " лет)")
        user_password_creat = input("Создайте пароль для аккаунта: ")
        fout.write(user_password_creat)
        print("Аккаунт успешно зарегистрирован!")
    with open("user_balance.txt", "w") as fout:
        fout.write("0")
    with open("count_transaction.txt", "w") as fout:
        fout.write("0")
    with open("limit.txt", "w") as fout:
        fout.write("1000000000000000000")
    with open("list_of_transaction.txt", "w") as fout:
        fout.close()
    return user_password_creat


def write_new_balance(user_balance):
    with open("user_balance.txt", "w") as fout:
        fout.write(str(user_balance))


def add_balance(user_balance):
    balance_add = int(input("Введите сумму пополнения: "))
    with open("user_balance.txt") as fin:
        user_balance_new = user_balance + balance_add
        write_new_balance(user_balance_new)
        print("Счёт успешно пополнен!")
    return user_balance_new


def check_password(user_password):
    password = input("Введите пароль: ")
    if user_password == password:
        return True
    else:
        print("Не верный пароль")
        return False


def take_money(user_balance, user_password):
    check = check_password(user_password)
    if check == True:
        balance = int(input("Ваш баланс: " + str(user_balance) + " руб. Введите сумму для снятия: "))
        if balance > user_balance:
            print("Сумма для снятия превышает текущий баланс")
        else:
            user_balance = user_balance - balance
            print("Снятие успешно завершено, ваш баланс:", user_balance, "руб.")
            write_new_balance(user_balance)
    return user_balance


def check_balance(user_balance, user_password):
    check = check_password(user_password)
    if check == True:
        print("Ваш баланс: " + str(user_balance) + " руб.")


def add_transaction(list_transaction):
    with open("list_of_transaction.txt", "a") as fout:
        symma_transaction = int(input("Введеите сумму транзакции: "))
        comment_transaction = input("Введите комментарий к транзакции: ")
        fout.write(str(symma_transaction) + "\n")
        fout.write(comment_transaction + "\n")
        list_transaction.append(str(symma_transaction))
        list_transaction.append(comment_transaction)
    with open("count_transaction.txt", "w") as fout:
        count_transaction = len(list_transaction) // 2
        fout.write(str(count_transaction))
        print("Количество ожидаемых пополнений: " + str(count_transaction))
    return list_transaction


def add_limit():
    new_limit = int(input("Введите значение максимальной суммы, которая может быть на счету: "))
    with open("limit.txt", "w") as fout:
        fout.write(str(new_limit))
    return new_limit


def check_transaction(salaries):
    salaries_new = {}
    for i in range(len(salaries)):
        if i % 2 == 0:
            symma_transaction = salaries[i]
            if symma_transaction in salaries_new:
                salaries_new[symma_transaction] = salaries_new[symma_transaction] + 1
            else:
                salaries_new[symma_transaction] = 1
    for name in salaries_new:
        print(str(name) + " руб: " + str(salaries_new[name]) + " платеж(а)")


def apply_transaction(user_balance, limit, list_transaction):
    salaries = []
    i = 0
    while i < len(list_transaction):
        symma_transaction = int(list_transaction[i])
        name_transaction = list_transaction[i + 1]
        user_balance = user_balance + symma_transaction
        if user_balance > limit:
            user_balance = user_balance - symma_transaction
            print("Транзакция «" + name_transaction + "» на сумму " + str(
                symma_transaction) + "руб. не может быть применена (превышен лимит).")
            salaries.append(symma_transaction)
            salaries.append(name_transaction)
        else:
            print(
                "Транзакция «" + name_transaction + "» на сумму " + str(symma_transaction) + " руб. успешно применена.")
        i = i + 2
    with open("list_of_transaction.txt", "w") as fout:
        for i in range(len(salaries)):
            fout.write(str(salaries[i]) + "\n")
        fout.close()
    with open("count_transaction.txt", "w") as fout:
        fout.write(str(len(salaries) // 2))
        fout.close()
    with open("user_balance.txt", "w") as fout:
        fout.write(str(user_balance))
        fout.close()
    return user_balance, salaries


def filter_pending_opetation(list_transaction):
    for i in check_limit_transaction(list_transaction):
        print(f'Транзакция {list_transaction[i + 1]} на сумму {list_transaction[i]} руб.')


def check_limit_transaction(list_transaction):
    i = 0
    limit_filter = int(input("Введети сумму для проверки отложенных операции больше указанной Вами: "))
    while i < len(list_transaction):
        if int(list_transaction[i]) >= limit_filter:
            yield i
        i += 2


def new_save():
    with open("limit.txt", "w") as foat:
        foat.close()
    with open("count_transaction.txt", "w") as foat:
        foat.close()
    with open("list_of_transaction.txt", "w") as foat:
        foat.close()
    with open("user_balance.txt", "w") as foat:
        foat.close()
    with open("user_data.txt", "w") as foat:
        foat.close()


if __name__ == "__main__":
    check_save = input("Хотите ли востановить данные из файла: (Да/Нет) ")
    if check_save == "Нет":
        new_save()
        count_transaction = 0
        list_transaction_old = []
    else:
        try:
            with open("user_data.txt") as check_file_user_data, open("limit.txt") as check_file_limit, open(
                    "count_transaction.txt") as check_file_count, open("user_balance.txt") as check_file_user_balance:
                check_file_user_data.close()
            user_password_old = linecache.getline("user_data.txt", 3).rstrip('\n')
            user_balance_old = int(linecache.getline("user_balance.txt", 1))
            count_transaction = int(linecache.getline("count_transaction.txt", 1))
            user_limit = int(linecache.getline("limit.txt", 1))
            list_transaction_old = []
            with open("list_of_transaction.txt") as fin:
                i = 1
                for i in range(count_transaction):
                    symma_transaction = fin.readline().rstrip('\n')
                    comment_transaction = fin.readline().rstrip('\n')
                    list_transaction_old.append(symma_transaction)
                    list_transaction_old.append(comment_transaction)
        except FileNotFoundError:
            print("Отсутствует файл сохранения")
            exit()

    while True:
        try:
            print("1 - создать аккаунт")
            print("2 - положить деньги на счет")
            print("3 - снять деньги")
            print("4 - вывести баланс на экран")
            print("5 - выставление ожидаемого пополнения")
            print("6 - выставление лимита на счёт")
            print("7 - применить транзакции")
            print("8 - вывести статистику по ожидаемым пополнениям")
            print("9 - фильтрация отложенных пополнений")
            print("10 - выйти из программы")
            number_operation = int(input("Введите номер операции, которую хотите выполнить, из списка выше: "))
            if number_operation == 1:
                user_password_old = create_user()
                user_balance_old = 0
                count_transaction = 0
                list_transaction_old = []
            elif number_operation == 2:
                user_balance_old = add_balance(user_balance_old)
            elif number_operation == 3:
                user_balance_old = take_money(user_balance_old, user_password_old)
            elif number_operation == 4:
                check_balance(user_balance_old, user_password_old)
            elif number_operation == 5:
                list_transaction_old = add_transaction(list_transaction_old)
                count_transaction = count_transaction + 1
            elif number_operation == 6:
                user_limit = add_limit()
            elif number_operation == 7:
                user_balance_old, list_transaction_old = apply_transaction(user_balance_old, user_limit,
                                                                           list_transaction_old)
                count_transaction = len(list_transaction_old) // 2
            elif number_operation == 8:
                check_transaction(list_transaction_old)
            elif number_operation == 9:
                filter_pending_opetation(list_transaction_old)
            elif number_operation == 10:
                print("Спасибо за пользование нашей программой, до свидания!")
                break
            else:
                print("Введен номер несуществующей операции.")
            print("")
        except ValueError:
            print("Введены некоректные данные. Неоходимо ввести сумму числом" + "\n")
