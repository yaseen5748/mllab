import csv
import random
import math
 
def loadcsv(filename):
	lines = csv.reader(open(filename, "r"));
	dataset = list(lines)
	for i in range(len(dataset)):
		dataset[i] = [float(x) for x in dataset[i]]
        
	return dataset
 
def splitdataset(dataset, splitratio):
    #67% training size
	trainsize = int(len(dataset) * splitratio);
	trainset = []
	copy = list(dataset);    
	while len(trainset) < trainsize:
		index = random.randrange(len(copy));       
		trainset.append(copy.pop(index))    
	return [trainset, copy]
 
main()
























