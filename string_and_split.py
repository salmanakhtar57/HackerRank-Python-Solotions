#string split and join

def split_and_join(line):
    a = line.split()
    x = "-".join(a)
    return 

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)