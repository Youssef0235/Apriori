import pandas as pd

def loadData():
    map = pd.read_excel("E:\Apriori\data.xlsx")
    return map.to_dict()

# Map Of Itemset : Support
def initialList(data):
    dataList = []
    for i in data:
        freq = {}
        for item in data[i].split(','):
            if item in freq:
                continue
            freq[item] = 1
            if item not in dataList:
                dataList.append(item)
    return dataList

# Takes List Of Joined Itemsets And Calculate Their Support
# Returns Map
def calculateSupport(joinedList, data):
    supportMap = {}
    sz = getItemsetSize(joinedList)
    for item in joinedList:
        for idx in data:
            count = 0
            for letter in item:
                if letter in data[idx]:
                    count += 1
            if count == sz:
                if item in supportMap:
                    supportMap[item] += 1
                else:
                    supportMap[item] = 1
    return supportMap


# Takes Dict Of Item : Support And Prun
# Return Map Of Frequent Itemsets
def cadidatePrunning(dataMap, minSupport, fqit, sup):
    nonFreqItemsets = []
    for item in dataMap:
        if dataMap[item] < minSupport:
            nonFreqItemsets.append(item)
        else:
            fqit.append(item)
            sup.append(dataMap[item])
    for item in nonFreqItemsets:
        dataMap.pop(item)
    return dataMap

def getItemsetSize(data):
    for itemset in data:
        return len(itemset)

# Takes Map Of Frequent Itemsets
# Returns List Of All Itemsets Joined
def joinItemset(dataMap):
    joined = []
    curLen = getItemsetSize(dataMap)
    keys = list(dataMap.keys())
    # Join All
    if curLen == 1:
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                joined.append(keys[i] + keys[j])
    else:
        for i in range(len(keys)):
            sub1 = keys[i][0 : curLen - 1]
            for j in range(i + 1, len(keys)):
                sub2 = keys[j][0 : curLen - 1]
                if sub1 == sub2:
                    joined.append(keys[i] + keys[j][len(keys[j]) - 1])
    return joined