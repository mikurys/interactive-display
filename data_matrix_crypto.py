#works correctly, but rework is needed to make code more readable
#this class contains static methods:
#-first one allows to encode integer number (from range 0-65535) to two dimensional matrix.
#-second one allows to decode matrix (6x6) to integer number.
#need to write unit tests.

import math;

class DataMatrixCrypto:
    def __init__(self):
        self;

    @staticmethod
    def encode(num):
        num = int(num);
        tab = [[0 for col in range(6)] for row in range(6)];
        for i in range(6):
            tab[i][0] = 1;
            tab[5][i] = 1;
            if (i%2 == 0):
                tab[0][i] = 1;
            else:
                tab[i][5] = 1;
        tempTab = [];
        while(int(num)>0):
            tempTab.append(int(num)%2);
            num = num/2;
        i=4;
        j=4;
        for bit in tempTab:
            if (j==0):
                j=4;
                i=i-1;
            tab[i][j] = bit;
            j=j-1;
        return(tab);

    @staticmethod
    def decode(twoDimArray):
        num=0;
        i=1;
        j=1;
        k=15;
        while (k>=0):
            if(k==0):
                if (twoDimArray[i][j]==0):
                    break;
            if (j==5):
                j=1;
                i=i+1;
            num += ((twoDimArray[i][j]*2)**k);
            j = j+1;
            k=k-1;
        return num;

#temp tests:
#print(DataMatrix.encode(2678));
#print(DataMatrix.decode([[1,0,1,0,1,0],[1,0,0,0,0,1],[1,0,0,1,0,0],[1,1,0,1,0,1],[1,1,0,1,1,0],[1,1,1,1,1,1]])); #683

if __name__ == "__main__":
    before = 62792
    matrix = DataMatrixCrypto.encode(before)
    after = DataMatrixCrypto.decode(matrix)
    print("Before encode and decode: " + str(before) + " After: " + str(after))
