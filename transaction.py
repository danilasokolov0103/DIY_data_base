def update_data_base_transaction(key, value, data_base):
    if value and key:
        if key in data_base:
            if isinstance(data_base[key], list):
                data_base[key].append(value)
            else:
                data_base[key] = [data_base[key]]
                data_base[key].append(value)
        else:
            data_base[key] = [value]


def get_value_transaction(key, data_base):
    try:
        if isinstance(data_base[key], list):
            number_of_elements = len(data_base[key])
            print(data_base[key][int(number_of_elements) - 1])
        else:
            print(data_base[key])
    except KeyError:
        print('NULL')


def count_transaction(value, data_base, list_of_last_set_values):
    list_of_last_set_values = []
    for key in data_base:
        if isinstance(data_base[key], list):
            list_of_last_set_values.append(
                data_base[key][len(data_base[key])-1])

        else:
            list_of_last_set_values.append(data_base[key])
    print(list_of_last_set_values.count(value))


def rollback(data_base):
    for key in data_base:
        if isinstance(data_base[key], list):
            data_base[key] = data_base[key][0]



def commit(data_base):
    for key in data_base:
        if isinstance(data_base[key], list):
            data_base[key] = data_base[key][len(data_base[key])-1]
