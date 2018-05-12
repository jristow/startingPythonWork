class HashDictionary:
    def __init__(self):
        self.size = 64 #Sets size of the array
        self.Table = [None] *self.size #Array for which we're storing data, set to None so we can construct a list with fixed length
     
    # return the index for key in hash list
    def getindex(self,key):
        hash = 0
        for char in str(key):
            hash+= ord(char)
        return hash % self.size
     
    #Insert the key and name 
    def add(self, key, name): #Takes a key and name
        hash_id = self.getindex(key)
        label_name = [key, name] #Constructing a key and passing in a name for the key
         
        if self.Table[hash_id] is None:
            self.Table[hash_id] = list ([label_name])
            return True
        else:
            for pair in self.Table[hash_id]:
                if pair[0] == key:
                    pair[1] = name
                    return True
            self.Table[hash_id].append(label_name)
            return True
    # Iterate through the list and return name if name is true else return None
    def get(self, key):
        hash_id = self.getindex(key)
        if self.Table[hash_id] is not None:
            for pair in self.Table[hash_id]:
                if pair[0] == key:
                    return pair[1]
        return None
     
    #Locate the cell which corresponds to the index and delete name, pop item off list
    def delete(self, key):
        hash_id = self.getindex(key)
        if self.Table[hash_id] is None:
            return False
        for i in range (0, len(self.Table[hash_id])):
            if self.Table[hash_id][i][0] == key:
                self.Table[hash_id].pop(i)
                return True
     
    def print(self):
        print('**SWDV 610: Data Structures Students**')
        for item in self.Table:
            if item is not None:
                print(str(item))
 
t = HashDictionary()
t.add('1','Anthony Brown')
t.add('2','Yen Ching')
t.add('3','Dylan Eye')
t.add('4','Daniel Jackson')
t.add('5','Fadil Karajic')
t.add('6','Quentin Ochieng')
t.add('7','Sultana Parvin')
t.add('8','Safeen Rasool')
t.add('9','Jared Wheet')
 
''' Testing Functions in Hash Dictionary '''
t.print()
print('Name: ' + t.get('2'))
t.delete('2')
t.print()