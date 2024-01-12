8import time

sleep_times = [3,4,1.5,2,0.75,4,4,3,2,3,4]
sentence = "MintedSucces MintedSucces ErrorTxpool MintedSucces MintedSucces MintedSucces MintedSucces MintedSucces GassFeeError GasFeeError GassFeeError"
for sleep_time,word in zip(sleep_times,sentence.split()):
    print(word)
    time.sleep(sleep_time)   

