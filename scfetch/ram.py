import psutil

def get_ram():
    ram_gb = psutil.virtual_memory().total / (1024 ** 3)
    return str(round(ram_gb, 2)) + " GB"