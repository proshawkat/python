
def solve(s):
    x = ' '.join(i[:1].upper() + i[1:] for i in s.split(' '))
    return x

if __name__ == '__main__':
    fptr = open('file.txt', 'w')
    s = input()
    result = solve(s)
    fptr.write(result)
    fptr.close()
    f = open("file.txt", "r")
    print(f.read())