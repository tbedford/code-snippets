import psutil

def get_running_applications():
    running_apps = []
    for proc in psutil.process_iter(['name']):
        try:
            app_name = proc.info['name']
            running_apps.append(app_name)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return running_apps

def main():
    running_applications = get_running_applications()
    for app_name in running_applications:
        print(app_name)

if __name__ == '__main__':
    main()
