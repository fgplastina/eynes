import random
from operator import itemgetter


def get_data():
    data = [{'id': iterator, 'age': random.randrange(100)} for iterator in range(0,10)]
    return data


def order_data_by_age(data:list):
    new_list = sorted(data, key=itemgetter('age'), reverse=True)
    print(f'Youngest person in list {new_list[-1]}')
    print('\n')
    print(f'Oldest person in list {new_list[0]}')
    return new_list


def main():
    order_data_by_age(get_data())


if __name__ == "__main__":
    main()
