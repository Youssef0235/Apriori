import utils as util
import matplotlib.pyplot as plt

data = util.loadData()
joinedList = util.initialList(data["items"])

frequentItemsets = []
support = []

while len(joinedList) != 0:
    supportMap = util.calculateSupport(joinedList, data["items"])
    prunMap = util.cadidatePrunning(supportMap, 3, frequentItemsets, support)
    joinedList = util.joinItemset(prunMap)

plt.bar(frequentItemsets, support, color = 'skyblue')

plt.title('Apriori Algorithm')
plt.xlabel('Frequent Itemsets')
plt.ylabel('Support')

plt.show()
