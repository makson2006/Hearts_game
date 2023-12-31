# написати функцію якам приймає рядок і повертає словник у якому
# ключами є всі символи, які зустрічаються в цьому рядку, а значення - відповідні
# вірогідності зустріти цей символ в цьому рядку.
# № код повинен бути структурований за допомогою конструкції if __name__ == "__main__":,
# всі аргументи і значення що функція повертає повинні бути типізовані, функція має рядок документації
from collections import Counter


# за допомогою тернарного оператора релізувати логіку:
# є параметри x та у,
# якщо x < y - друкуємо x + y,
# якщо x == y - друкуємо 0,
# якщо x > y - друкуємо x - y,
# якщо x == 0 та y == 0 друкуємо "game over"


def get_symbols_frequency_with_counter(text):
    texts_len = len(text)
    return {key: value / texts_len for key, value in Counter(text).items()}


def get_symbols_frequency(text):
    result_dict = {}
    tests_len = len(text)
    for symbol in set(text):
        result_dict[symbol] = text.count(symbol) / tests_len
    return result_dict


def get_ternary(x, y):
    return str(
        x + y
        if (x < y)
        else x - y
        if (x > y)
        else "game over"
        if (x == 0 and y == 0)
        else 0
    )


if __name__ == "__main__":
    cases = (
        (1, 2, "3"),
        (1, 1, "0"),
        (2, 1, "3"),
        (0, 0, "game over"),
    )
    for x, y, result in cases:
        func_res = get_ternary(x, y)
        assert (
            func_res == result
        ), f"ERROR: get_ternary({x}, {y}) returned {func_res}, but expected: {result}"

    print(get_symbols_frequency("1234sdfghjkjhgfdsdfghjk   rrrrrrrrrrrrrrr"))
