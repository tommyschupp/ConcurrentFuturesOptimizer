import multiprocessing
from concurrent.futures import ThreadPoolExecutor
import time
import advisorScrape
def testerFunction():
    print('Test began')
    time.sleep(3)
    print('Test ended')



def optimizeMyWorkers(f, testIterations, testLength, *args, **kwargs):
    maximum = multiprocessing.cpu_count() * 5 
    minimum = 1
    resultDict = {}
    flag = False
    for numWorkers in range(minimum, maximum + 1):
        print('numWrkers ' + str(numWorkers))
        if __name__ == '__main__':
                with ThreadPoolExecutor(max_workers=numWorkers) as executor:
                    startTime = time.time()
                    futures = []
                    for testIteration in range(testIterations):
                        futures.append(executor.submit(f, *args, **kwargs))

                                        
                    while True:
                        if startTime + testLength <= time.time():
                            flag = True
                            print('flag up')
                            executor.shutdown(wait=True, cancel_futures=True)
                            results = testIterations
                            for future in futures:
                                if future.cancelled():
                                    results -= 1 
                            print(results)
                            break
                    if flag == True:
                        resultDict.update({numWorkers : results})
                        continue
    return resultDict
print(optimizeMyWorkers(testerFunction, 100, 5))
#testIterations should be a higher number than should be possible in the time frame for the maximum number of workers
#testLength should be how long each number of workers should be tested for

