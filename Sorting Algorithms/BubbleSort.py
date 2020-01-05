#encoding: UTF-8
#Analisis y dise;o de Algoritmos
#Hector Manuel Takami Flores - A01377647

#Algorithm: Bubble Sort

def bubbleSortAlgorithm(dataList):

    for i in range (0,len(dataList)-1):
        for j in range (0,(len(dataList)-1)-i):
            if dataList[j]>dataList[j+1]:
                dataList[j],dataList[j+1] = dataList[j+1],dataList[j]
    return dataList
    
    
    
    
def main():
    print("\n***BubbleSort Algorithm***\n")
    dataList = [6,0,1,7,3,5,4,2]
    print("- List: %s" % str(dataList))    
    bubbleSortAlgorithm(dataList)
    print("- OrderedList: %s\n" % str(dataList))
    
    stringList = ["Zeus","Poseidon","Ares","Hermes","Atenea","Apolo"]
    print("- List: %s" % str(stringList))
    bubbleSortAlgorithm(stringList)    
    print("- OrderedList: %s\n" % str(stringList))
    
main()