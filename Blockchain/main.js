const Blockchain = require('./blockchain')

const blockchain = new Blockchain()
urna1 = {'jose':110, 'maria': 200, 'joao': 150, 'nulos': 20, 'brancos':20}
urna2 = {'jose':210, 'maria': 100, 'joao': 130, 'nulos': 120, 'brancos': 220}
urna3 = {'jose':10, 'maria': 20, 'joao': 10, 'nulos': 200, 'brancos':120}
urna4 = {'jose':240, 'maria': 178, 'joao': 157, 'nulos': 5, 'brancos':43}

blockchain.addBlock(urna1)
blockchain.addBlock(urna2)
blockchain.addBlock(urna3)
blockchain.addBlock(urna4)

console.log(blockchain.isValid()) // true
blockchain.blocks[1].urna['jose'] = 3000 // ataque malicioso
console.log(blockchain.isValid()) // false