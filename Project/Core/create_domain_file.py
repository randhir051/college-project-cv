import pickle

domain = [{"name": "entry", "x": 24, "y": 50}, {"name": "exit", "x": 150, "y": 50}]

with open("mySavedDict.txt", "wb") as myFile:
    pickle.dump(domain, myFile)