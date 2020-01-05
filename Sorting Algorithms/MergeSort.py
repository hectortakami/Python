#encoding: UTF-8
#Analisis y dise;o de Algoritmos
#Hector Manuel Takami Flores - A01377647

def mergeSortAlgorithm(dataList):
    
    if len(dataList) <= 1:
        return dataList
    else:
        split = int(len(dataList)/2)        
        left = mergeSortAlgorithm(dataList[:split])
        right = mergeSortAlgorithm(dataList[split:])
        sortedArray  = [0]*len(dataList)
        l = 0
        r = 0
        for i in range(len(dataList)):

            try:
                if left[l] < right[r]:
                    sortedArray[i] = left[l]
                    l = l+1
                else:
                    sortedArray[i] = right[r]
                    r = r+1
            except:
                if r < len(right):
                    for j in range(len(dataList) - r-l):
                        sortedArray[i+j] = right[r+j]
                    break
                else:
                    for j in range( len(dataList) - r-l):
                        sortedArray[i+j] = left[l+j]
                    break

        return sortedArray



def main():

    print("\n***MergeSort Algorithm***\n")
    dataList = [20,19,18,17,16,15,2,4,6,8,10]
    print("- List: %s" % str(dataList))    
    orderedList = mergeSortAlgorithm(dataList)
    print("- OrderedList: %s\n" % str(orderedList))
    
    dataList = [256,128,64,32,16,8,4,2]
    print("- List: %s" % str(dataList))    
    orderedList = mergeSortAlgorithm(dataList)
    print("- OrderedList: %s\n" % str(orderedList))
    
main()