#encoding: UTF-8
#Analisis y dise;o de Algoritmos
#Hector Manuel Takami Flores - A01377647

def shiftNodes(start, count, dataList):  
        root = start  
  
        while root * 2 + 1 < count:  
            child = root * 2 + 1  
            if child < count - 1:
               if dataList[child] < dataList[child + 1]:  
                    child += 1  
            if dataList[root] < dataList[child]:  
                dataList[root], dataList[child] = dataList[child], dataList[root]  
                root = child  
            else:  
                return  
            
def heapSortAlgorithm(dataList):  
    count = len(dataList)  
    start = count // 2 - 1  
    end = count - 1  
  
    while start >= 0:  
        shiftNodes(start, count, dataList)  
        start -= 1  
  
    while end > 0:  
        dataList[end], dataList[0] = dataList[0], dataList[end]  
        shiftNodes(0, end, dataList)  
        end -= 1  
        
        
def main():

    print("\n***HeapSort Algorithm***\n")
    dataList = [63,89,15,47,602,12,486,35,47,96]
    print("- List: %s" % str(dataList))    
    heapSortAlgorithm(dataList)
    print("- OrderedList: %s\n" % str(dataList))
    
    dataList = [9,6,0,4,7,6,3,1]
    print("- List: %s" % str(dataList))    
    heapSortAlgorithm(dataList)
    print("- OrderedList: %s\n" % str(dataList))
    
main()