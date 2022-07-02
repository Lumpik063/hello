import os

file_name = "/test/study"
file_stats = os.stat(file_name)
print(file_stats.st_size)