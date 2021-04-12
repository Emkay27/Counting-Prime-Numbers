# Counting Prime Numbers.
___This project calculates how many prime numbers there are between 1 and 1 000 000.___

## Task 1 :
___The first task is to write a nondistributed program that will count the required number of prime numbers. This simple program will also print the time it takes to obtain this number.___

## Task 2 :
___The second task is to write a distributed version of the program, using the client-server approach, where A TCP connection is established between a client and each
one of three servers. The client sends the server two numbers that specify the lower and upper limits of
the number range to be searched. Each server, on its part, returns the number (count) of primes in its
range, using the count primes() method implemented on its side.___

___The client divides the total range into a number of subranges in some way, passes each subrange over to
a server, collects the replies from the servers, and adds them up. The servers must be started on different
machines, and operate at the same time.___
