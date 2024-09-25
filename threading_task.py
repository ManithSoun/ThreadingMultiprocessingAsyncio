import threading
import time

def simulate_io_task(file_name, duration):
  print(f"Start I/O task of {file_name}")
  time.sleep(duration)

def run_io_tasks():
  io_tasks = [
    ("prime_numbers1", 3),
    ("prime_numbers2", 2),
    ("prime_numbers3", 4),
    ("prime_numbers4", 1),
    ("prime_numbers5", 2),
  ]

  threads = []

  for file_name, duration in io_tasks:
    thread = threading.Thread(target = simulate_io_task, args=(file_name, duration))
    threads.append(thread)
    thread.start()

  for thread in threads:
    thread.join()