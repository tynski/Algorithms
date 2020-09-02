def get_c(a,b):
    if not a:
        return []

    if not b:
        return a
    
    number_frequency_dict = get_number_frequency(b)

    prime_numbers = get_prime_numbers_list(max(number_frequency_dict.values()))    

    skip_them = [k for k, v in number_frequency_dict.items() if v in prime_numbers]

    return [c_element for c_element in a if not c_element in skip_them]

def get_number_frequency(numbers_list):
    number_freq = {}
    
    for number in numbers_list:
        if number in number_freq:
            number_freq[number] += 1
        else:
            number_freq[number] = 1
    
    return number_freq

def get_prime_numbers_list(end):
    prime_numbers = [2]

    for i in range(3, end+1):
        for j in range(2,i):
            if (i%j==0):
                break
        else:
            prime_numbers.append(i)
    
    return prime_numbers

def testGet_c(a, b, c, testNumber):
    if get_c(a, b) == c:
        print(f'Test{testNumber} passed!')
    else:
        print(f'Test{testNumber} failed!')

if __name__ == "__main__":
    A = input("Enter A list:\n")
    B = input("Enter B list:\n")
    print("Thank you!\nHere is result C list:\n")
    print(get_c(A,B))

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
# the time comlexity will be O(n^2)
