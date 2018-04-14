#Jordan Ristow
#Implementing a selection sort function
#The selection sort function stores the largest value it has found as it progresses through the list.
#When it reaches the end of the list it then stores that largest value as the nth element.
#This process is repeated until it has examined all elements in the list

def selectionSort(list):
    
    for n in range(len(list)-1, 0, -1):
        #defining the variable which will store the value for the max number position
        maxNumPosition = 0
        for i in range(1, n+1):
            #if condition checks whether the value in ith position is larger than the value in the current maxNumPosition
            if list[i] > list[maxNumPosition]:
                #If value in ith position is larger, i becomes new maxNumPosition
                maxNumPosition = i
        #updates list values with new positions based on value of maxNumPosition           
        list[n], list[maxNumPosition] = list[maxNumPosition], list[n]

        
def main():
    #initializing a test list
    testlist = [23, 1, 5, 13, 35, 0, 100, 10, 1, 20]
    #printing the testlist to show initial position of values
    print('List before sorting: ', testlist)
    #executing the selection sort function
    selectionSort(testlist)
    #printing the list after sorting to show final position of values
    print('List after sorting: ', testlist)
    
main()