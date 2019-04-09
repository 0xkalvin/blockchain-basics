from block import Block

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
    
    


