def get_c(a,b):
    if not a:
        return []

    if not b:
        return a
    
    number_frequency_dict = get_number_frequency(b)

    prime_numbers = get_prime_numbers_list(max(number_frequency_dict.values()))    

    skip_them = [k for k, v in number_frequency_dict.items() if v in prime_numbers]

    return [i for i in a if not i in skip_them]

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
    a = [4,5,3,1,5,6,34]
    print(f'List A:\n{a}')
    b = [4,4,1,1,15,5]
    print(f'List B:\n{b}')
    print(f'Result C list:\n{get_c(a,b)}')

