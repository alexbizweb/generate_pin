import random


def generate_pin(lenght: int) -> str:
    return ''.join(str(random.randint(0, 9)) for _ in range(lenght))


def replace_fives(a_list: list, value: str) -> list[str]:
    return [element.replace('5', value) for element in a_list]


def write_file(filename: str, data: str):
    with open(filename, 'a') as file:
        file.write(data)


if __name__ == '__main__':
    pins = [generate_pin(8) for _ in range(5)]
    pins_without_fives = replace_fives(pins, '6')
    str_list = '\n'.join(pins_without_fives)
    write_file('pincode.txt', str_list)
