#Jordan Ristow
#This program implements a bubble sort function and then tests functionality
#The bubble sort algorithm iteratively compares the first two values in a list to determine which is larger
#The larger value 'moves up' in the list and is compared to the next value in the list
#This process repeats until all values have been compared and the largest value has 'bubbled up' to the end of the list.

def bubbleSort(list):
    for n in range(len(list)-1, 0, -1):
        for i in range(n):
            if list[i] > list[i+1]: #Compares ith value with the one in i+1 position
            #If ith value is larger, values are swapped via simultaneous assignment            
                list[i], list[i+1] = list[i+1], list[i]
                
                
def main():
    #initializing a test list
    testlist = [23, 1, 5, 13, 35, 0, 100, 10, 1, 20]
    #printing the testlist to show initial position of values
    print('List before sorting: ', testlist)
    #executing the bubble sort function
    bubbleSort(testlist)
    #printing the list after sorting to show final position of values
    print('List after sorting: ', testlist)
    
    
main()
    