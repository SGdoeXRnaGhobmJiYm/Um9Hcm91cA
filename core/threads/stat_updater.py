from time import time, sleep

def stat_updater(count_queue):
    global foundcount
    count_cache = {}

    while True:
        while True:
            try:
                for ts, count in count_queue.get(block=False):
                    ts = int(ts)
                    count_cache[ts] = count_cache.get(ts, 0) + count
            except:
                break
            
        now = time()
        total_count = 0
        for ts, count in tuple(count_cache.items()):
            if now - ts > 60:
                count_cache.pop(ts)
                continue
            total_count += count
        
        print(f"\rTotal Groups Found: {foundcount} | CPM: {total_count}", end="\n")
        sleep(0.1)
