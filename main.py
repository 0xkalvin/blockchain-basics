import json
import jsonpickle

from blockchain import *

my_blockchain = Blockchain()
print("mining block 1...")
my_blockchain.add_block(Block("some data"))
print("mining block 2...")
my_blockchain.add_block(Block(":p"))

x = jsonpickle.encode(my_blockchain)
parsed = json.loads(x)
print(json.dumps(parsed, indent=4, sort_keys=True))
