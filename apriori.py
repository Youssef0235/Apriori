import utils as util
import plot as plt

data = util.loadData()
joinedList = util.initialList(data["items"])


while len(joinedList) != 0:
    supportMap = util.calculateSupport(joinedList, data["items"])
    prunMap = util.cadidatePrunning(supportMap, 3)
    joinedList = util.joinItemset(prunMap)

plt.draw(util.frequentItemsetsList, util.supportList)