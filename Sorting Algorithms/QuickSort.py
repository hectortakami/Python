#encoding: UTF-8
#Analisis y dise;o de Algoritmos
#Hector Manuel Takami Flores - A01377647

def quickSortAlgorithm(dataList):
   quickSort(dataList,0,len(dataList)-1)

def quickSort(dataList,first,last):
   if first<last:
       splitpoint = partition(dataList,first,last)
       quickSort(dataList,first,splitpoint-1)
       quickSort(dataList,splitpoint+1,last)
       
def partition(dataList,first,last):
   pivotvalue = dataList[first]
   leftmark = first+1
   rightmark = last
   done = False
   while not done:
       while leftmark <= rightmark and dataList[leftmark] <= pivotvalue:
           leftmark = leftmark + 1
       while dataList[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1
       if rightmark < leftmark:
           done = True
       else:
           temp = dataList[leftmark]
           dataList[leftmark] = dataList[rightmark]
           dataList[rightmark] = temp

   temp = dataList[first]
   dataList[first] = dataList[rightmark]
   dataList[rightmark] = temp
   
   return rightmark
   
def main():

    print("\n***QuickSort Algorithm***\n")
    dataList = [20,19,18,17,16,15,2,4,6,8,10,12,14,1,3,5,7,9,11,13]
    print("- List: %s" % str(dataList))    
    quickSortAlgorithm(dataList)
    print("- OrderedList: %s\n" % str(dataList))
    
    stringList = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    print("- List: %s" % str(stringList))
    quickSortAlgorithm(stringList)    
    print("- OrderedList: %s\n" % str(stringList))
    
main()
