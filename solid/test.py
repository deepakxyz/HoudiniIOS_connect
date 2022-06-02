import time
start = time.time()
time.sleep(max(1. / 100 - (time.time() - start), 0))
print('hey')