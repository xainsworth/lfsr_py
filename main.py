from os import system, name
from sty import fg, bg, ef, rs
import numpy as np
import time

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
# f = "0101111011011011"
f = "0000000000000000111111111111111101010101101010100101010110101010000000001111111100000000111111110000111100001111000011110000111100110011001100110011001100110011010101010101010101010101010101010101101010100101010110101010010101100110100110010110011010011001000000001111111111111111000000000000011000000000100000000000000000110011001100111100110011001100000011111111000000001111111100000101010110101010101010100101010101100110111001101111100110011001010101010101010110101010101010100110011010011001100110010110011000111100110000110011110011000011001011111111010011111001100111110110100101101001011010010110100100111100110000111100001100111100001111000011110000111100001111000111100110010111011010111101011001011010010110101010010110100101001100111100110011001100001100110110100101101001100101101001011000001111000011111111000011110000011010011001011010010110011010010011001111001100001100111100110001011010010110100101101001011010001111000011110011000011110000110110011001100110011001100110011001011010101001011010010101011010"
output = ""

def printHeader(n):
    print('\n\n')
    print('-'*(7*(n+2)+n+3))
    print('|   N   |',end='')
    for i in range(n-1,-1,-1):
        print('  2^'+str(i)+'  |', end='')
    print('  OUT  |')
    print('-'*(7*(n+2)+n+3))

def printLine(n):
    print('-'*(7*(n+2)+n+3))

def printRow(n):
    bstr = format(n, '08b')
    
    print('|  ',str(n),' '*(5-len(str(n))), sep='', end='|')
    for i in range(0,an):
        print('   ',bstr[(8-an)+i],'   ', sep='',end='|')
    print('   ',f[n],'   |', sep='')

def printRenk(n):
    bstr = format(n, '08b')
    print(fg.li_green, '|  ',str(n),' '*(5-len(str(n))), sep='', end='|')
    for i in range(0,an):
        print('   ',bstr[(8-an)+i],'   ', sep='',end='|')
    print('   ',f[n],'   |', fg.rs, sep='')

print('Bir n değeri girin: ', end='')
n = int(input())
an = n
lfsr = np.random.randint(2, size=(n,n))
for i in range(0,n):
    print('LFSR '+str(i+1)+': ', end='')
    print(*lfsr[i], sep='')

print('\nKaydırma işlemine geçmek için bir tuşa basın.')
input()
clear()

for i in range(0, pow(2, n)):
    b_output = ""
    for j in range(0, n):
        print('LFSR '+str(j+1)+': ', end='')
        print(*lfsr[j], sep='')
        if n in [2,3,4,6,7,9]:
            first_bit = lfsr[j][n - 1] ^ lfsr[j][n - 2]
        elif n == 5:
            first_bit = lfsr[j][n - 4] ^ lfsr[j][n - 1]
        elif n == 8:
            first_bit = (lfsr[j][n - 1] ^ lfsr[j][n - 3]) ^ (lfsr[j][n - 4] ^ lfsr[j][n - 5])
        else:
            first_bit = lfsr[j][n - 4] ^ lfsr[j][n - 1]
        b_output += str(lfsr[j][n - 1])
        
        for k in range(n-1, 0, -1):
            lfsr[j][k] = lfsr[j][k-1]
        lfsr[j][0] = first_bit
        
    y = int(b_output, 2)
    output += f[y]
    if n > 4:
        printHeader(n)
        if (y - 2) >= 0:
            printRow(y-2)
            printRow(y-1)
        printRenk(y)
        if (y + 2) < len(f):
            printRow(y+1)
            printRow(y+2)
        printLine(n)
    else:
        printHeader(n)
        for x in range(0,pow(2,n)):
            if x != y: printRow(x)
            else: printRenk(x)
        printLine(n)
    
    print('\n\nOutput: '+b_output)
    print('Fonksiyondan çıkan: ' +f[y]+'\nBitstream: '+output+'\nDevam etmek için bir tuşa basın.')
    input()
    clear()

asc = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
sifre = ""
for i in range(0,len(output), 6):
    if (i+6 < len(output)):
        sifre += asc[int(output[i:i+6], 2)]
    else:
        ak = len(output)-i
        sifre += asc[int(output[i:i+ak], 2) << (6-ak)]

while len(sifre) % 4 != 0:
    sifre += "="

print('İşlem bitti', 'Bitstream: '+output, 'Elde edilen anahtar: '+sifre, sep='\n')
time.sleep(1000)
input()