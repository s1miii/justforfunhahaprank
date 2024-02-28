import time
print("file ktp:")
x = input()

sleep_times = [3,4,1.5,2,0.75,4,4,3,2,3,4]
sentence = "RegisterDataSavepharse.txt ErrorThread RegisterDataSavepharse.txt RegisterDataSavepharse.txt RegisterDataSavepharse.txt RegisterDataSavepharse.txt RegisterDataSavepharse.txt RegisterDataSavepharse.txt RegisterDataSavepharse.txt RegisterDataSavepharse.txt"
for sleep_time,word in zip(sleep_times,sentence.split()):
    print(word)
    time.sleep(sleep_time)
