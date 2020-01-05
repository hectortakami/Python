#encoding: UTF-8
#Analisis y dise;o de Algoritmos
#Hector Manuel Takami Flores - A01377647

def radixSortAlgorithm(dataList):
    
    mod = 10
    div = 1
    nList = len(dataList)
    
    while True:
        buckets = [[], [], [], [], [], [], [], [], [], []]
        for value in dataList:
            leastDigit = value % mod
            leastDigit //= div
            buckets[leastDigit].append(value)
        mod = mod * 10
        div = div * 10

        if len(buckets[0]) == nList:
            return buckets[0]

        dataList = []
        data = dataList.append
        for x in buckets:
            for y in x:
                data(y)

def main():

    print("\n***RadixSort Algorithm***\n")
    dataList = [89,56,23,12,45,78,14,25,36,47,58,69]
    print("- List: %s" % str(dataList))    
    orderedList = radixSortAlgorithm(dataList)
    print("- OrderedList: %s\n" % str(orderedList))
    
    dataList = [147,258,369,789,456,123,741,852,963]
    print("- List: %s" % str(dataList))    
    orderedList = radixSortAlgorithm(dataList)
    print("- OrderedList: %s\n" % str(orderedList))
    
main()
