
from transaction import update_data_base_transaction, get_value_transaction
from transaction import count_transaction, commit, rollback


info = '''SET - сохраняет аргумент в базе данных.
\nGET - возвращает, ранее сохраненную переменную.
\nUNSET - удаляет, ранее установленную переменную.
\nCOUNTS - показывает сколько раз данные значение встречается в базе данных.
\nEND - закрывает приложение.
\nBEGIN - начало транзакции.
\nROLLBACK - откат самой внутренней транзакции
\nCOMMIT - фиксация изменений от всех транзакций.'''


data_base = {}


def main():
    print(info)
    get_user_command = input(">>")

    while get_user_command.split()[0] != "END":
        if get_user_command.split()[0] == "BEGIN":

            while get_user_command.split()[0] != ("COMMIT"):
                print('TRANSACTION')
                get_user_command = input(">>")

                if get_user_command.split()[0] == "SET":
                    try:

                        update_data_base_transaction(get_user_command.split()[
                            1], get_user_command.split()[2], data_base)
                    except IndexError:
                        print(info)

                elif get_user_command.split()[0] == "GET":
                    try:
                        get_value_transaction(
                            get_user_command.split()[1], data_base)
                    except IndexError:
                        print(info)

                elif get_user_command.split()[0] == "UNSET":
                    try:
                        delete_key(get_user_command.split()[1])
                    except IndexError:
                        print(info)

                elif get_user_command.split()[0] == "COUNTS":
                    try:
                        list_of_set_values = []
                        count_transaction(get_user_command.split()[
                            1], data_base, list_of_set_values)
                    except IndexError:
                        print(info)
                
                elif get_user_command.split()[0] == "ROLLBACK":
                    rollback(data_base)

                elif get_user_command.split()[0] == "COMMIT":
                    commit(data_base)
                
                elif get_user_command.split()[0] == "BEGIN":
                    pass
                
                else:
                    print('COMMIT YOUR TRANSACTION')

            get_user_command = input(">>")

        else:

            if get_user_command.split()[0] == "SET":
                try:
                    update_data_base(get_user_command.split()[
                        1], get_user_command.split()[2])

                except IndexError:
                    print(info)

            elif get_user_command.split()[0] == "GET":
                try:
                    get_value(get_user_command.split()[1])
                except IndexError:
                    print(info)

            elif get_user_command.split()[0] == "UNSET":
                try:
                    delete_key(get_user_command.split()[1])
                except IndexError:
                    print(info)
            
            elif get_user_command.split()[0] == "COUNTS":
                try:
                    count(get_user_command.split()[1])
                except IndexError:
                    print(info)

            else:
                print(info)

            get_user_command = input(">>")

    print("FINIHING PROGRAMM")


def update_data_base(key, value):
    if value is not None and key is not None:
        data_base[key] = value


def get_value(key):
    if key in data_base:
        print(data_base[key])
    else:
        print('NULL')


def delete_key(key):
    if key in data_base:
        data_base.pop(key, None)
    else:
        print(('There is no such element').upper())


def count(value):
    number_of_same_values = list(data_base.values()).count(value)
    print(number_of_same_values)


if __name__ == "__main__":
    main()
