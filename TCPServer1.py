import time
from socket import *

start=time.time()
serverPort = 1201
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print "The server is ready to receive" 

def SieveOfEratosthenes(lb, ub): 
 
	prime = [True for i in range(ub+1)] 
	p = 2
	while (p * p <= ub): 
		
		if (prime[p] == True): 
			 
			for i in range(p * 2, (ub+1), p): 
				prime[i] = False
		p += 1
	count =0
	for p in range(lb, ub): 
		if prime[p]: 
			count+=1
	return count

while 1:
	connectionSocket, addr = serverSocket.accept()
	sub_range1 = connectionSocket.recv(1024).decode("utf-8")
	print ("Input received")
	ran = eval(sub_range1)
	
	num_primes=0
	num_primes=SieveOfEratosthenes(ran[0], int(ran[1]))		

	res = ("%d,%f" %(num_primes, (time.time()-start)))

	connectionSocket.send(res.encode('utf-8'))
	connectionSocket.close()


	



