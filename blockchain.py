#!/usr/bin/python
# coding=UTF-8
# encoding=UTF-8

import json
import os
import hashlib
import datetime

class Block:
    def __init__(self, index, data, previousHash='00000'):
        self.index = index
        self.timestamp = str(datetime.datetime.now())
        self.data = data
        self.previousHash = previousHash
        self.hash = self.calculateHash()

    def update(self, dic):
        self.__dict__=dic
        return self

    def calculateHash(self):
        return hashlib.sha256(str(self.index)
         + self.previousHash 
         + str(self.data)
         + self.timestamp).hexdigest()

    def isValid(self):
        return self.hash == self.calculateHash()

    def printBlock(self):
        return ("\nBlock #" + str(self.index) 
                + "\nData: " + str(self.data)
                + "\nTimeStamp: " + str(self.timestamp)
                + "\nBlock Hash: " + str(self.hash)
                + "\nBlock Previous Hash: " + str(self.previousHash)
                +"\n---------------")

class BlockChain:
    def __init__(self, file="blochchain.blockchain"):
        self.chain = [Block(0, "Origin")]
        self.file=file

    def getLatestBlock(self):
        return self.chain[len(self.chain)-1]

    def getNextIndex(self):
        return self.getLatestBlock().index + 1

    def generateBlock(self, data):
        self.chain.append(Block(self.getNextIndex(), data, self.getLatestBlock().hash))

    def isChainValid(self):
        for i in range (1, len(self.chain)):
            if not self.chain[i].isValid():
                return False
            if self.chain[i].previousHash != self.chain[i-1].hash:
                return False
        return True

    def printBlockChain(self):
        return ''.join([self.chain[i].printBlock() for i in range(1, len(self.chain))])

    def save(self):
        if(self.isChainValid()):
            with open(self.file, "w") as f:
                f.write(json.dumps(self, default=lambda obj: obj.__dict__))
            return
        
        # delete file throw exception and request a new file from network
        raise ValueError('The blockchain is invalid!')

    def open(self):
        # if(os.path.exists(str(file))):
            with open(self.file) as f:
                data = json.load(f)
                self.__dict__ = data 
                self.chain = [Block("","").update(dic) for dic in data["chain"]]

def main():
    teste = BlockChain()
    teste.open()
    print(teste.printBlockChain())

    # blockchain = BlockChain()
    # blockchain.generateBlock("Hello World!")
    # blockchain.generateBlock(3)
    # blockchain.generateBlock({"account": "123123","amount": 100,"action": "buy"})
    # print(blockchain.printBlockChain())
    # print ("Chain valid? " + str(blockchain.isChainValid()))
    # blockchain.save()

    # blockchain.chain[1].data = "Hello Darkness my old friend!"
    # print(blockchain.printBlockChain())
    # print ("Chain valid? " + str(blockchain.isChainValid()))
    # blockchain.save()

    # blockchain.open()
    # print(teste.printBlockChain())
    # print ("Chain valid? " + str(blockchain.isChainValid()))
    # blockchain.save()

if __name__ == '__main__':
    main()