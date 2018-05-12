#Jordan Ristow
#Implementing an insertion sort function
#The insertion sort algorithm iteratively builds up a sorted sublist of the first i elements in the original list



def insertionSort(list):
    #For loop iterates through the whole list
    for i in range(1, len(list)):
        #Storing the ith value as the current value
        currentValue = list[i]
        position = i
        #Checking if current position is 0 and the i-1 value is larger than current value
        while position > 0 and list[position - 1] > currentValue:
            #If position is not 0 and i-1 value is larger than current value
            #assign the value at position to the position-1 slot
            list[position] = list[position - 1]
            position = position - 1
        #Once position is 0, insert the currentValue at position    
        list[position] = currentValue
        
def main():
    #initializing a test list
    testlist = [23, 1, 5, 13, 35, 0, 100, 10, 1, 20]
    #printing the testlist to show initial position of values
    print('List before sorting: ', testlist)
    #executing the insertion sort function
    insertionSort(testlist)
    #printing the list after sorting to show final position of values
    print('List after sorting: ', testlist)
    
    
main()