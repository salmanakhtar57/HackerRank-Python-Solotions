def reverse_and_swap_cases(sentence):
    s = sentence.swapcase()
    s = s.split()
    p = s[::-1]
    s = ' '.join(p)
    return s

if __name__ == '__main__':
    sentence = input("Enter a sentence: ")
    result = reverse_and_swap_cases(sentence)
    print(result)
