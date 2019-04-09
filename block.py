import hashlib
import datetime

class Block:
    
    def __init__(self, data, previous_hash = ""):
        self.counter = 0
        self.index = 0
        self.timestamp = str(datetime.datetime.now())
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.generate_hash()
        
    
    def generate_hash(self):
        input_data = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.counter)
        return hashlib.sha256(input_data.encode()).hexdigest()
    
    def mine_block(self, num_of_zeros):
        difficulty = "0"*num_of_zeros
        while self.hash[:num_of_zeros] != difficulty:
            self.counter += 1
            self.hash = self.generate_hash()
        
        print("Block mined: " + self.hash)
