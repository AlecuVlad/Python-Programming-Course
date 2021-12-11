def your_function(*args, **_) -> int:
    my_sum = 0
    for val in args:
        if type(val) is int:
            my_sum += val
    return my_sum


def sum_calculator(n: int) -> (int, int, int):
    if n == 0:
        return 0, 0, 0

    if n % 2 == 0:
        return n + sum_calculator(n - 1)[0], n + sum_calculator(n - 1)[1], sum_calculator(n - 1)[2]
    else:
        return n + sum_calculator(n - 1)[0], sum_calculator(n - 1)[1], n + sum_calculator(n - 1)[2]


def check_int() -> int:
    number = input("Scrie ceva: ")
    try:
        curr_int = int(number)
        return curr_int
    except ValueError as _:
        return 0


def main() -> None:
    print(f"Sum = {your_function(1, 5, -3, 'abc', [12, 56, 'cad'])}")
    print(f"Sum = {your_function()}")
    print(f"Sum = {your_function(2, 4, 'abc', param_1=2)}")

    suma = sum_calculator(7)
    print(f"Suma toate: {suma[0]}\nSuma pare: {suma[1]}\nSuma impare: {suma[2]}")

    print(check_int())


if __name__ == "__main__":
    main()
