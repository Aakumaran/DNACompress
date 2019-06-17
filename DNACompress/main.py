import huffman as hf 
import tensorflow as tf 
from keras.layers import Dense,LSTM
from keras.models import Sequential
import numpy as np 
import random
from keras.utils.np_utils import to_categorical
size = 10

def ref(x):
	if x[0]==1:
		return 't'
	elif x[1]==1:
		return 'a'
	elif x[2]==1:
		return 'c'
	elif x[3]==1:
		return 'g'


dkey = {'t':0,'a':1, 'c':2, 'g':3,0:'t',1:'a',2:'c',3:'g'}
length = 100
DNA = ''
initial = DNA[:size]
for i in range(length):DNA+=(dkey[random.randint(0,3)])

DNA_backup = DNA
y = DNA[size:]
y = [int(dkey[i]) for i in y]
y = to_categorical(y)
DNA = [int(dkey[x]) for x in DNA]
DNA = to_categorical(DNA)
x = []
for i in range(len(DNA)-size):
	x.append([DNA[x] for x in range(i,i+size)])
x = np.array(x)

model = Sequential()
model.add(LSTM(50, input_shape = (size,4)))

model.add(Dense(4))
model.compile(loss='binary_crossentropy', optimizer='adam')
model.fit(x, y, validation_data = (x,y),epochs=500,verbose =1 )
y_test = (model.predict(x))
for i in y_test:
	i[np.where(i==np.max(i))] = 1
	for j in range(4):
		if i[j]!=1:
			i[j]=0
# print(y_test)
wrong = 0
total  =0
current = 0
compressed=''
for i in range(len(y)):
	flag =0
	# print(y_test[i],y[i])
	for z in range(4):
		if current>=9:
			if current!=0:compressed+=str(current)
			current=0
		if y_test[i][z]!=y[i][z]:
			flag = 1
	if flag ==1:
		if current!=0: compressed+=str(current)+ref(y[i])
		current = 0
		wrong+=1
	else:
		current+=1
	total+=1
print("Accuracy: ",(1-wrong/total)*100)
print("Wrong: ",wrong)
print("Total",total)
# print(compressed)

val,key = hf.encode(compressed)
# print(val)

print("Length of DNA: ",len(DNA_backup))
print("Lenght of LSTM Compress: ",len(compressed))
print("After Huffman: ", len(str(val)))
print("Just Huffman: ",len(str(hf.encode(DNA_backup)[0])))

print("Final Compression: ",((len(DNA_backup)-len(str(val)))*100/len(DNA_backup)))
print("Just Huffman Compression: ",(len(DNA_backup)-len(str(hf.encode(DNA_backup)[0])))*100/len(DNA_backup))