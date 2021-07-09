from time import sleep


def load(size, delta=0.23):
    """size is count of equals to load
    minimal recommended delay is 0.23"""
    proc = 0
    print("", end="")
    for _ in range(size + 1):
        print("\r" + "#" + "=" * proc + " " * (size - proc) + "#", end="")
        proc += 1
        sleep(delta)
    print("\a\nComplete!")


def running_string(text, delay=0.23, visible=5):
    """ text is text to run
    visible how hutch chars show
    minimal recommended delay is 0.23"""
    print("", end="", flush=True)
    for _ in range(len(text) + 1):
        print("\r"+text[:visible], end="", flush=True)
        text = text[1:] + text[0]
        sleep(delay)


def write_text(text, speed=0.23):
    """writing text by char
    speed - how much delay between write chars"""
    for i in range(len(text)):
        print(text[i], end="", flush=True)
        if (i > 0 and text[i] == text[i-1]) or not text[i].isalnum() and not text[i].isalpha():
            sleep(speed/3)
            continue
        sleep(speed)


if __name__ == '__main__':
    running_string(" "*len(" qwerty ") + "computer password is: qwerty", visible=len(" qwerty "))
    print("\nPassword: ", end="")
    sleep(0.3)
    write_text("qwerty", 0.35)
    print()
    load(20)
    sleep(0.3)
    write_text("Your computer has been hacked!", 0.22)