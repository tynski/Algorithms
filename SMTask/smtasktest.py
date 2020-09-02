from SMTask import get_c

def testGet_c(a, b, c, testNumber):
    if get_c(a, b) == c:
        print(f'Test{testNumber} passed!')
    else:
        print(f'Test{testNumber} failed!')

#Test1
A1 = [2,3,9,2,5,1,3,7,10]
B1 = [2,1,3,4,3,10,6,6,1,7,10,10,10]
C1 = [2,9,2,5,7,10]
testGet_c(A1, B1, C1, 1)

#Test2
A2 = [4,5,2,4,6,2,3,5,6,1]
B2 = [3,4,4,2,3,2,1,2,2,13,4,1,2,3,4,6,73]
C2 = [4,5,4,6,5,6]
testGet_c(A2, B2, C2, 2)

#Test3
A3 = [4,2,1,412,323,45,23,545]
B3 = [4,32,4,2343,2323,1221,36356,3232,445]
C3 = [2,1,412,323,45,23,545]
testGet_c(A3, B3, C3, 3)

#Test4
A4 = []
B4 = [4,32,4,2343,2323,1221,36356,3232,445]
C4 = []
testGet_c(A4, B4, C4, 4)

#Test5
A5 = [4,5,6,2,32,4,3]
B5 = []
C5 = [4,5,6,2,32,4,3]
testGet_c(A5, B5, C5, 5)