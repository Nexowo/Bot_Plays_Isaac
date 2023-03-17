import psutil

for proc in psutil.process_iter():
    try:
        name = proc.name()
        pid = proc.pid
        mem = proc.memory_info().rss
        print(f"{name} ({pid}) : {mem} octets")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
