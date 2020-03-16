import sys

def findMapping(s1, s2):
    s1_set = set()

    for i in s1:
        s1_set.add(i)
        
    if len(s1_set) == len(s2):
        print ("true")
    else:
        print ("false")

if __name__ == '__main__':
    findMapping(sys.argv[1], sys.argv[2])


