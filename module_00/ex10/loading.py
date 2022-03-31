from time import sleep, time


lst = range(1000)
ret = 0


def ft_progress(listy):
    length = 25
    start_time = time()
    
    for i in lst:
        filled_length = int(length * i // len(listy))
        bar = "=" * filled_length
        spaces = ' ' * (length - filled_length - 1)
        elapsed = (time() - start_time)
        eta = (elapsed / (i + 1)) * (len(listy))
        print(f"ETA: {eta:.2f}s [{bar}>{spaces}] - {i+1}/{len(listy)} | Elapsed time {elapsed:.2f}s ", end = "\r")
        yield i


for elem in ft_progress(lst):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)
