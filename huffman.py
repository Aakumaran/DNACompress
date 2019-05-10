'''
File where HUFFMAN Decoding and Encoding takes place
Author - Ram Rathi 
Project - DNACompress
'''
import heapq
import random 
import time
import numpy as np
from bitarray import bitarray

def encode(data,variable = True,verbose = False, bestfit = False, cache = 0, flag = False):
	'''
	Takes data as string input
	Outputs as Int of encoded seq
	'''
	if verbose:
		print("[#] HUFFMAN",end=" ")
		if variable: print("[Variable]")
		else: print("[Fixed]",)
	encode_start = time.time()
	data =data.replace('\n', '')
	key = dict()
	comp = lambda _ : _[1]
	encoded = str()
	corp = dict()
	#Fix problem of extremely large string sizes.
	#10^9 Stable limit
	if not flag: 
		ctime = time.time()
		if verbose: print("[ ] Calculating distribution...")
		for _ in data:
			corp[_]=corp.get(_,0)+1
		if verbose: print("[#] Completed in %fs" %(time.time()-ctime))
		#print(corp)
	else:#Corpus is already built and its in best fit
		if verbose: print("[#] Distribution obtained from Cache")
		corp = cache

	#Make corpus if variable huffman coding used
	if variable:
		
		'''
		#Basic method only for DNA
		htree = [(_,corp[_]) for _ in corp]
		htree.sort(reverse = True,key = comp)
		code = 0
		for _ in htree:
			key[_[0]] = code*'1'+'0'
			code+=1
		'''
		htree = [(corp[_],list(_)) for _ in corp]
		key = dict()
		heapq.heapify(htree)
		while len(htree)>1:
			lo = heapq.heappop(htree)
			#print("lo:" ,lo)
			hi = heapq.heappop(htree)
			for _ in lo[1]:
				#print('_ in lo: ',_)
				key[_] = '0' + key.get(_,"")
			for _ in hi[1]:
				key[_]= '1' + key.get(_,"")
			heapq.heappush(htree,(lo[0]+hi[0],lo[1]+hi[1]))       		

	else:
		nitems = len(corp)
		powi = int(pow(nitems,0.5))
		count = 0
		while pow(2,powi)<nitems : powi+=1
		for _ in corp:
			num = str(bin(count))[2:]
			key[_[0]] = (powi-len(num))*'0'+num
			count+=1
		print(key)

	
	buff = str()
	if verbose: print("[ ] Encoding...")
	ctime = time.time()
	for char in data:
		encoded+=key[char]
	rem = len(encoded)%8
	for _ in range(rem):
		encoded+='0'
	encoded = 24*'1'+encoded
	space_uncompressed = (len(data))
	space_compressed = len(encoded)//8
	if verbose: print("[#] Completed in %fs" %(time.time()-ctime))
	

	if verbose: print("[ ] Converting to Integer Value...")
	ctime = time.time()
	encoded = int(encoded,2)
	if verbose: print("[#] Completed in %f s" %(time.time()-ctime))
	

	percentage = (space_uncompressed-space_compressed)*100/space_uncompressed
	if verbose:
		print("[#] Encoding complete with rate: ",percentage,"%")
		print("[#] Encoding time taken: %f" %(time.time()-encode_start))
		print("[#] Old size: ~ %f MB" %(space_uncompressed/1000000))
		print("[#] New size: ~ %f MB" %(space_compressed/1000000))
		print('-'*30)
	

	if bestfit:
		d2,k2 = encode(data, variable = not variable,verbose = verbose, bestfit = False, flag = True, cache = corp)
		if d2<encoded:
			encoded = d2
			key = k2
			if variable : print("[#] Fixed length used")
			elif verbose: print("[#] Variable length used")
				
		else:
			if variable and verbose: print("[#] Variable length used")
			elif verbose: print("[#] Fixed length used")
		if verbose:	print('-'*30)
			
	
	if not bestfit and verbose: print('[#] Huffmann Encoding Complete!\n'+'-'*30)
	return encoded,key
	

def decode(data,key,verbose=False):
	'''
	Input data as Int of encoded seq
	Returns data as string output
	'''
	decoded = str()
	if verbose : print("Converting to binary...")
	b = "{0:b}".format(data)
	print(b)
	return decoded



