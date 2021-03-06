from time import sleep
from texts import chapters


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


def write_chapter(id, delay=0.5):
    text = chapters[id]
    write_text(text, 0.12)
    print()


def check_choice(variants: list):
    """variants is variants of user choice
    choice: '?????? ??????????: {variant}'
    error: '?????????????????????? ????????????!'"""
    variants = [str(elem) for elem in variants]
    while True:
        try:
            answer = input('?????? ??????????: ')
            if answer in variants:
                return answer
        except Exception:
            pass
        print("?????????????????????? ????????????!")


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


def write_status_crew(crew: list) -> None:
    """crew[i] -> [{stability: int}, {name: str}, {location: str}]
    write: '#========  # {name} - {location}'"""
    for person in crew:
        print("#" + "=" * (person[0] // 10) + " " * (10 - person[0] // 10) + "# " + person[1] + " - " + person[2])


class User:
    def __init__(self, name: str, stability: int, location: str, live: bool):
        self.name = name
        self.is_live = live
        self.stability = 100 if stability > 100 else stability  # ???? ?????????? ???????? ???????????? 100
        self.location = location

    def update_stability(self, delta: int):
        self.stability += delta
        self.stability = 100 if self.stability > 100 else self.stability  # ???? ?????????? ???????? ???????????? 100

    def go_to(self, location):
        self.location = location

    def is_alive(self):
        return self.stability > 0 and self.is_live


class Room:
    def __init__(self, location):
        # location name
        self.location = location

    def entry(self, user: User):
        """Change location for user"""
        user.go_to(self.location)

    def make_action_with_user(self, user):
        """Action there"""
        pass


if __name__ == '__main__':
    """save_arg("sad", "yes")
    save_arg("sad2", "yes")
    save_arg("sad3", "yes")
    delete_arg("sad3")
    save_arg("sad2", "no")"""
    write_chapter(1)
    choice = make_choice([["???????????????? ????????????????????", 1], ["???????????????????? ????????????????????", 2]])
    if choice == 1:
        if yes_or_no("???????????????? ?????????"):
            running_string(" "*len(" qwerty ") + "computer password is: qwerty", visible=len(" qwerty "))
            print("\nPassword: ", end="")
            sleep(0.3)
            write_text("qwerty", 0.15)
            print()
            load(20)
            sleep(0.3)
            write_text("Your computer has been hacked!", 0.1)
            print()
        else:
            write_text("Your computer has not been hacked!", 0.1)
            print()
    else:
        write_text("Technology demonstration has been skipped!", 0.1)
        print()
input("?????????????? Inter ?????? ???? ??????????")