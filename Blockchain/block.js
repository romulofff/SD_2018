const sha256 = require('crypto-js/sha256')

class Block {
    constructor(index = 0, previousHash = null, urna = null) {
        this.index = index
        this.previousHash = previousHash
        /*this.jose = urna['jose']
        this.maria = urna['maria']
        this.joao = urna['joao']
        this.nulos = urna['nulos']
        this.brancos = urna['brancos']*/
        this.urna = urna
        this.timestamp = new Date()
        this.hash = this.generateHash()
                
    }

    generateHash() {
        return sha256(this.index + this.previousHash + JSON.stringify(this.urna) + this.timestamp).toString()
    }
}

module.exports = Block

