import psutil

def get_system_info():
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    memory_utilization = memory.percent
    disk_utilization = disk.percent

    return memory_utilization, disk_utilization

def main():
    try:
        while True:
            memory_utilization, disk_utilization = get_system_info()
            print(f"Memory Utilization: {memory_utilization}%")
            print(f"Disk Utilization: {disk_utilization}%")
    except KeyboardInterrupt:
        # Custom exit code or cleanup operations
        print("Exiting...")

if __name__ == '__main__':
    main()

    
