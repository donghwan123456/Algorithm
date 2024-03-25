#방법1
T = int(input())
for t in range(T):
    N,color = map(str,input().split())

    if N == '6': #16진수다
        print(f'#{t+1} {int(color,16):024b}')
    else:
        print(f'#{t+1} {int(color, 2):06X}')
#방법2
T = int(input())
HEX = {
    '0000' : '0',
    '0001' : '1',
    '0010' : '2',
    '0011' : '3',
    '0100' : '4',
    '0101' : '5',
    '0110' : '6',
    '0111' : '7',
    '1000' : '8',
    '1001' : '9',
    '1010' : 'A',
    '1011' : 'B',
    '1100' : 'C',
    '1101' : 'D',
    '1110' : 'E',
    '1111' : 'F',
}
HEX2 = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',s
    'D' : '1101',
    'E' : '1110',
    'F' : '1111',
}


HEX3 = dict((value, key) for key, value in HEX.items())
# print(HEX3)

for t in range(T):
    N,color = map(str,input().split())
    result = ''
    if N == '24':
        for i in range(0,24,4):
            result += HEX.get(color[i:i+4])
    else:
        for c in color:
            result += HEX3.get(c)

    print(f'#{t+1} {result}')
