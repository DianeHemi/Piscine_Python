from time import sleep, time


lst = range(1000)
ret = 0


def ft_progress(lst):
    length = 25
    start_time = time()
    
    for i in lst:
        filledLength = int(length * i // len(lst))
        bar = "=" * filledLength
        spaces = ' ' * (length - filledLength - 1)
        elapsed = (time() - start_time)
        eta = (elapsed / (i + 1)) * (len(lst))
        print(f"ETA: {eta:.2f}s [{bar}>{spaces}] - {i+1}/{len(lst)} | Elapsed time {elapsed:.2f}s ", end = "\r")
        yield i


for elem in ft_progress(lst):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)