#What's your name
def print_full_name(first, last):
  print("Hello " +first+" "+last+ "! you just delve into python")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)