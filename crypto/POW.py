#!/usr/bin/env python
# example of proof of work algorithm

import hashlib

max_nonce = 2 ** 32 # 4 billion

def proof_of_work(header, difficulty_bits):

	target = 2 ** (256-difficulty_bits)
	for nonce in xrange(max_nonce):
		hash_result = hashlib.sha256(str(header)+str(nonce)).hexdigest()

		if long(hash_result, 16) < target:
			print str(header) + str(nonce)
			print "Hash is %s" % hash_result
			return (hash_result, nonce)

	print "Failed after %d (max_nonce) tries" % nonce
	return nonce

if __name__ == '__main__':
	nonce = 0
	hash_result = ''
	for difficulty_bits in xrange(32):
		difficulty = 2 ** difficulty_bits
		new_block = 'D8SEK5' + hash_result
		(hash_result, nonce) = proof_of_work(new_block, difficulty_bits)
