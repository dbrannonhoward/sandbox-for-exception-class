def add(a, b):
    try:
        temp_sum = a + b
        return temp_sum
    except TypeError as ex:
        print(get_object_type(ex))
        print(ex.args)
        raise ex


def get_object_type(object_to_check):
    return type(object_to_check)


def main():
    a = 13
    b = 'a'
    _sum = add(a, b)
    print(_sum)


if __name__ == '__main__':
    main()
