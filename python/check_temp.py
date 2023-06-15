import psutil

def get_cpu_temperature():
    temperatures = psutil.sensors_temperatures()
    if 'coretemp' in temperatures:
        return temperatures['coretemp'][0].current
    elif 'cpu_thermal' in temperatures:
        return temperatures['cpu_thermal'][0].current
    else:
        return None

def main():
    cpu_temperature = get_cpu_temperature()
    if cpu_temperature is not None:
        print(f"CPU Temperature: {cpu_temperature}°C")
    else:
        print("CPU Temperature measurement not available.")

if __name__ == '__main__':
    main()
