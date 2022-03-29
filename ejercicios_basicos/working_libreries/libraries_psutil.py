"""_summary_

    Working with library psutil

"""

import psutil

print(f"{psutil.virtual_memory() = }")
# get RAM (virtual memory) in bytes
print(f"{psutil.virtual_memory().total = }")
# get RAM (virtual memory) in gigabytes
print(f"virtual memory in gigabytes: {(psutil.virtual_memory().total / 1024 / 1024 / 1024)//1} GB")

# -----------------------------------------------------------------------------------------------
# get dist usage información
hdd= psutil.disk_usage('/')
print(f"{hdd = }")
# get total
print(f"Total: {hdd.total/(1024**3):.2f} GB")
print(f"Used: {hdd.used/(1024**3):.2f} GB")
print(f"Free: {hdd.free/(1024**3):.2f} GB")