# Importing libraries
from hashlib import sha256 # for hash generation
from time import asctime, time # for timestamping and benchmarking

# Block class
class Block:

	time_required = 0

    # Class constructor
	def __init__(self, transactions, previousHash = ''):
		self.transactions = transactions
		self.previousHash = previousHash
		self.timestamp = asctime()
		self.nonce = 0
		self.hash = self._calculate_hash()
		self.time_required = Block.time_required

    # Human - readable representation of each block
	def __repr__(self):
		return f'\n\nTimestamp: {self.timestamp} \nTransactions: {self.transactions} \nPrevious Hash: {self.previousHash} \nHash: {self.hash} \nNonce: {self.nonce} \nTime Required: {self.time_required}'

    # calculating has for each new block
	def _calculate_hash(self):
		return sha256(str((self.timestamp, self.transactions, self.previousHash, self.nonce)).encode('utf-8')).hexdigest()

    # to mine block of each set of transactions
	def _mine_block(self, difficulty):
		start_time = time()
		while self.hash[0:difficulty] != ''.join('0' for i in range(difficulty)):
			self.nonce += 1
			self.hash = self._calculate_hash()
		end_time = time()
		Block.time_required = end_time - start_time
		return f'BLOCK MINED: {self.hash}'

# Blockchain class
class Blockchain:

	difficulty = 3

    # class constructor
	def __init__(self):
		self.chain = [self._create_genesis_block()]
		self.pendingTransactions = []
		self.miningReward = 100 # mining reward for each block is set to default 100

	# representation of the blockchain
	def __repr__(self):
		dbc = ''
		for i in self.chain:
			dbc += repr(i)
		return dbc

	@classmethod
	def set_difficulty(cls, difficulty):
		cls.difficulty = difficulty

    # adds the 1st block of the blockchain
	def _create_genesis_block(self):
		return Block([], '0')

    # returns latest block in the chain

	def get_latest_block(self):
		return self.chain[len(self.chain) - 1]

    # creates transaction
	def create_transaction(self, transaction):
		self.pendingTransactions.append(transaction)

	def mine_pending_transactions(self, miningRewardAddress):

		rewardTx = Transaction(None, miningRewardAddress, self.miningReward)
		self.pendingTransactions.append(rewardTx)

		block = Block(self.pendingTransactions, self.get_latest_block().hash)
		block._mine_block(Blockchain.difficulty)
		self.chain.append(block)

		self.pendingTransactions = []

	def is_chain_valid(self):

		true = 'Chain is valid'
		false = 'Chain is invalid'

		for i in range(len(self.chain)):
			currentBlock = self.chain[i+1]
			previousBlock = self.chain[i]

			if currentBlock.hash != currentBlock._calculate_hash():
				return false

			if currentBlock.previousHash != previousBlock.hash:
				return false

			else:
				return true

	def get_balance(self, address):

		balance = 0

		for block in self.chain:
			for trans in block.transactions:
				if  trans.fromAddress == address:
					balance -= trans.amount

				if trans.toAddress == address:
					balance += trans.amount

		return f'{address.upper()} is worth {balance} cryptocoins'

class Transaction:

	def __init__(self, fromAddress, toAddress, amount):
		self.fromAddress = fromAddress
		self.toAddress = toAddress
		self.amount = amount

	def __repr__(self):
		return f'From: {self.fromAddress}, To: {self.toAddress}, Amount: {self.amount}'
