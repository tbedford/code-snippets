import psutil
import keyboard

def get_cpu_load():
    cpu_load = psutil.cpu_percent(interval=1)
    return cpu_load

def main():
    while True:
        if keyboard.is_pressed('q'):
            break
        cpu_load = get_cpu_load()
        print(f"CPU Load: {cpu_load}%")

if __name__ == '__main__':
    main()
