#Jordan Ristow
#Final Project, implementing a solution to minimum number of dice throws
#required to win Chutes and Ladders

#global variables defined here
n = 100 #Number of squares on the board
moves = [-1] * n

#Ladders
moves[1] = 38
moves[4] = 14
moves[9] = 31
moves[21] = 42
moves[28] = 84
moves[36] = 44
moves[51] = 67
moves[71] = 91
moves[80] = 100

#Chutes
moves[16] = 6
moves[47] = 26
moves[49] = 11
moves[56] = 53
moves[62] = 19
moves[64] = 60
moves[87] = 24
moves[93] = 73
moves[95] = 75
moves[98] = 78

class QueueEntry(object):
    def __init__(self, v = 0, dist = 0):
        self.v = v
        self.dist = dist
        
def getMinDiceThrow(move, n):
    
    visited = [False] * n
    
    queue = []
    
    visited[0] = True
    
    queue.append(QueueEntry(0,0))
    
    qe = QueueEntry()
    
    while queue:
        
        qe = queue.pop(0)
        v = qe.v
        
        if v == n - 1:
            break
        
        j = v + 1
        
        while j <= v + 6 and j < n:
            
            
            if visited[j] is False:
                
                a = QueueEntry()
                a.dist = qe.dist + 1
                visited[j] = True
                
                a.v = move[j] if move[j] != -1 else j
                
                queue.append(a)
            
            j += 1
            
    return qe.dist


print('Min dice throws required is {}'.format(getMinDiceThrow(moves, n)))