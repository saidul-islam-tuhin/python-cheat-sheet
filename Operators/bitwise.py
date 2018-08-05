0 & 0 # OUTPUT: 0
0 & 1 # OUTPUT: 0
1 & 0 # OUTPUT: 0
1 & 1 # OUTPUT: 1
3 & 5 # OUTPUT: 1

0 | 0 # OUTPUT: 1
0 | 1 # OUTPUT: 1
1 | 0 # OUTPUT: 1
1 | 1 # OUTPUT: 0
3 | 5 # OUTPUT: 7

0 ^ 0 # OUTPUT: 0
0 ^ 1 # OUTPUT: 1
1 ^ 0 # OUTPUT: 1
1 ^ 1 # OUTPUT: 0
2 ^ 4 # OUTPUT: 6

~0 # OUTPUT: -1
~8 # OUTPUT: -9
~0b1000 # OUTPUT: -9


bin(0b101 << 2) # OUTPUT: '0b10100'
0b101 << 2 # OUTPUT: 20
5 << 2 # OUTPUT: 20

bin(0b101 >> 2) # OUTPUT: '0b1'
0b101 >> 2 # OUTPUT: 1
5 >> 2 # OUTPUT: 1
