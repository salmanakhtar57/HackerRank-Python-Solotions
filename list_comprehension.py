#list Comprehension

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
#x, y, z, n = (int(input()) for _ in range(4))  short form of the above program

print ([[a,b,c] 
        for a in range(0, x+1) 
        for b in range(0,y+1) 
        for c in range(0,z+1) 
        
        if a + b + c != n ])