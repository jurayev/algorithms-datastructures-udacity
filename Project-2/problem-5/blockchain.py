import hashlib
from datetime import datetime


class Block:

    def __init__(self, data, previous_hash='0'):
        self.timestamp = str(datetime.utcnow())
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        data_encoded = self.data.encode('utf-8')
        timestamp_encoded = self.timestamp.encode('utf-8')
        prev_hash_encoded = self.previous_hash.encode('utf-8')
        sha.update(data_encoded + timestamp_encoded + prev_hash_encoded)
        return sha.hexdigest()


class BlockChain:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    """
    Adds a new block at O(1) by adding the new block to the tail pointer.
    Complexities:
    ~ Runtime O(1)
    ~ Space O(1), technically for each new block we have to allocate more memory, 
    but since we just add a ref to the new pointer this complexity can be omitted
    """
    def add_block(self, data):
        if not self.head:
            self.head = Block(data)
            self.tail = self.head
        else:
            self.tail.next = Block(data, self.tail.hash)
            self.tail = self.tail.next
        self.size += 1

    def get_size(self):
        return self.size

    def display(self):
        print(">" * 10, "Printing blockchain", "<" * 10)
        if not self.head:
            print("\nBlockchain is empty\n")
        else:
            current = self.head
            index = 1
            while current:
                print(f"\nDisplay block {index}\n")
                print(f"Block data: {current.data}")
                print(f"Previous hash: {current.previous_hash}")
                print(f"Hash: {current.hash}\n")
                current = current.next
                index += 1
            print(f"\nThere are {index-1} blocks in the blockchain")
        print(">" * 10, "Printing completed", "<" * 10)


def _test_blockchain():
    blockchain = BlockChain()
    blockchain.add_block("This is a crypto block 1")
    blockchain.add_block("This is a crypto block 2")
    blockchain.add_block("This is a crypto block 2")

    # test blocks are chained using previous_hash attribute
    assert blockchain.head.hash == blockchain.head.next.previous_hash
    assert blockchain.head.next.hash == blockchain.head.next.next.previous_hash

    # next block hash should not match prev block hash
    assert blockchain.head.hash != blockchain.head.next.hash
    assert blockchain.head.next.hash != blockchain.head.next.next.hash
    assert blockchain.head.hash != blockchain.head.next.next.hash

    # test expected size is 3
    assert blockchain.get_size() == 3
    blockchain.display()


_test_blockchain()
