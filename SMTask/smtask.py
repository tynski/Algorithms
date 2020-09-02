def get_c(a,b):
    if not a:
        return []

    if not b:
        return a
    
    number_frequency_dict = get_number_frequency(b)

    prime_numbers = get_prime_numbers_list(max(number_frequency_dict.values()))    

    skip_them = [k for k, v in number_frequency_dict.items() if v in prime_numbers]

    c = []
    for i in a:
        if not i in skip_them:
            c.append(i)
    #return [c_element for c_element in a if not c_element in skip_them]
    return c

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

if __name__ == "__main__":
    A = input("Enter A list:\n")
    B = input("Enter B list:\n")
    print("Thank you!\nHere is result C list:")
    print("".join(get_c(A,B)))

