import psutil
import termios
import sys

def get_cpu_load():
    cpu_load = psutil.cpu_percent(interval=1)
    return cpu_load

def get_keypress():
    file_descriptor = sys.stdin.fileno()
    old_settings = termios.tcgetattr(file_descriptor)
    try:
        tty.setraw(sys.stdin.fileno())
        key = sys.stdin.read(1)
        return key
    finally:
        termios.tcsetattr(file_descriptor, termios.TCSADRAIN, old_settings)

def main():
    while True:
        key = get_keypress()
        if key.lower() == 'q':
            break
        cpu_load = get_cpu_load()
        print(f"CPU Load: {cpu_load}%")

if __name__ == '__main__':
    main()
