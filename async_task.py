import asyncio

async def async_write_to_file(filename, data, duration):
    print(f"Start async task of {filename}")
    await asyncio.sleep(duration)
   

    # Writing the prime numbers to the file
    with open(filename, "w") as f:
        for number in data:
            f.write(f"{number}\n")
    print("\n")
    print(f"Finished {filename}")

async def run_async_tasks(prime_numbers):
    chunk_size = len(prime_numbers) // 5  # Assuming you want to create 5 files
    async_tasks = [
        ("prime_numbers1.txt", prime_numbers[:chunk_size], 2),
        ("prime_numbers2.txt", prime_numbers[chunk_size:2*chunk_size], 1),
        ("prime_numbers3.txt", prime_numbers[2*chunk_size:3*chunk_size], 3),
        ("prime_numbers4.txt", prime_numbers[3*chunk_size:4*chunk_size], 1.5),
        ("prime_numbers5.txt", prime_numbers[4*chunk_size:], 1.5),
    ]

    await asyncio.gather(*[async_write_to_file(file, data, duration) for file, data, duration in async_tasks])
