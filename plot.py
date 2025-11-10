import matplotlib.pyplot as plt

def draw(freqItList, supList):
    plt.bar(freqItList, supList, color='skyblue')

    plt.title('Apriori Algorithm')
    plt.xlabel('Frequent Itemsets')
    plt.ylabel('Support')

    plt.show()
