import functools 

def main():
    while True:
        number = input("please write an integer number")
        if number[0] in ("+", "-"):
            if number[1:].isdigit():
                print(functools.reduce(lambda x, y: x + y, [int(digit) for digit in list(number[1:])]))
                return
        else:
            if number.isdigit():
                print(functools.reduce(lambda x, y: x + y, [int(digit) for digit in list(number)]))
                return


if __name__ == "__main__":
    main()
