import hashlib
import json
import jsonpickle
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
        var = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.counter)
        return hashlib.sha256(var.encode()).hexdigest()
    
    def mine_block(self, difficulty):
        string = "0"*difficulty
        while self.hash[:difficulty] != string:
            self.counter += 1
            self.hash = self.generate_hash()
        
        print("Block mined: " + self.hash)


class Blockchain:

    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 5
    
    def create_genesis_block(self):

        return Block("Kalvin on brink of falling asleep")
    
    def get_latest_block(self):
        lenght = len(self.chain) - 1
        return self.chain[lenght]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        new_block.index = self.get_latest_block().index + 1
        self.chain.append(new_block)
        

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.generate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True
    
    


shitcoin = Blockchain()
print("mining block 1...")
shitcoin.add_block(Block("hahahahahaha"))
print("mining block 2...")
shitcoin.add_block(Block("lmfaoooooo"))

x = jsonpickle.encode(shitcoin)
parsed = json.loads(x)
print(json.dumps(parsed, indent=4, sort_keys=True))
