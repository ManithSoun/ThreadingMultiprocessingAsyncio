import threading
import time

def simulate_io_task(file_name, duration):
  print(f"Start I/O task of {file_name}")
  time.sleep(duration)

def run_io_tasks():
  io_tasks = [
    ("file_chunk_1", 3),
    ("file_chunk_2", 2),
    ("file_chunk_3", 4),
    ("file_chunk_4", 1),
    ("file_chunk_5", 2),
  ]

  threads = []

  for file_name, duration in io_tasks:
    thread = threading.Thread(target = simulate_io_task, args=(file_name, duration))
    threads.append(thread)
    thread.start()

  for thread in threads:
    thread.join()