from time import sleep


def save_arg(arg, value):
    """Save/rewrite your argument to txt file
    First parameter is name of argument, second his value"""
    f = open("test_file.txt", "r")
    dict_arg = {}
    for line in f.read().split("\n"):
        if line.split() != []:
            ln = line.split()
            dict_arg[ln[0]] = " ".join(ln[1:])
    f.close()
    f = open("test_file.txt", "w")
    dict_arg[arg] = value
    for key in list(dict_arg.keys()):
        print(f"{key} {dict_arg[key]}")
        f.write(f"{key} {dict_arg[key]}\n")
    f.close()


def delete_arg(arg):
    """Delete argument from txt file
    First parameter is name of argument"""
    f = open("test_file.txt", "r")
    dict_arg = {}
    for line in f.read().split("\n"):
        if line.split() != []:
            ln = line.split()
            if ln[0] != arg:
                dict_arg[ln[0]] = " ".join(ln[1:])
    f.close()
    f = open("test_file.txt", "w")
    for key in list(dict_arg.keys()):
        print(f"{key} {dict_arg[key]}")
        f.write(f"{key} {dict_arg[key]}\n")
    f.close()


def load(size, delta=0.23) -> None:
    """size is count of equals to load
    minimal recommended delay is 0.23"""
    proc = 0
    print("", end="")
    for _ in range(size + 1):
        print("\r" + "#" + "=" * proc + " " * (size - proc) + "#", end="")
        proc += 1
        sleep(delta)
    print("\a\nComplete!")


def running_string(text, delay=0.23, visible=5) -> None:
    """ text is text to run
    visible how hutch chars show
    minimal recommended delay is 0.23"""
    print("", end="", flush=True)
    for _ in range(len(text) + 1):
        print("\r"+text[:visible], end="", flush=True)
        text = text[1:] + text[0]
        sleep(delay)


def write_text(text, speed=0.23) -> None:
    """writing text by char
    speed - how much delay between write chars"""
    for i in range(len(text)):
        print(text[i], end="", flush=True)
        if (i > 0 and text[i] == text[i-1]) or not text[i].isalnum() and not text[i].isalpha():
            sleep(speed/3)
            continue
        sleep(speed)


def check_choice(variants: list):
    """variants is variants of user choice
    choice: 'Ваш выбор: {variant}'
    error: 'Некоректные данные!'"""
    variants = [str(elem) for elem in variants]
    while True:
        try:
            answer = input('Ваш выбор: ')
            if answer in variants:
                return answer
        except Exception:
            pass
        print("Некоректные данные!")


def make_choice(variants: list) -> int:
    """variants[i] -> [{variant: str}, {id: int}]
    variant: '{id} - {variant}'
    :return player choice id"""
    for variant in variants:
        print(str(variant[1]) + " - " + variant[0])
    return int(check_choice(list(map(lambda x: x[1], variants))))


def yes_or_no(question: str) -> bool:
    """question is question for user
    like: {question}
    'yes (y/1) / no (n/2)'
    :return boolean of user choice"""
    print(question)
    print('yes (y/1) / no (n/2)')
    user_choice = check_choice(["yes", "y", "1", "no", "n", "2"])
    if user_choice in ["yes", "y", "1"]:
        return True
    return False


if __name__ == '__main__':
    """save_arg("sad", "yes")
    save_arg("sad2", "yes")
    save_arg("sad3", "yes")
    delete_arg("sad3")
    save_arg("sad2", "no")"""

    choice = make_choice([["смотреть технодемку", 1], ["пропустить технодемку", 2]])
    if choice == 1:
        if yes_or_no("Взломать комп?"):
            running_string(" "*len(" qwerty ") + "computer password is: qwerty", visible=len(" qwerty "))
            print("\nPassword: ", end="")
            sleep(0.3)
            write_text("qwerty", 0.35)
            print()
            load(20)
            sleep(0.3)
            write_text("Your computer has been hacked!", 0.22)
        else:
            write_text("Your computer has not been hacked!", 0.22)
    else:
        write_text("Technology demonstration has been skipped!", 0.22)