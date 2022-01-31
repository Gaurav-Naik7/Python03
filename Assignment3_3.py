def minimum(value):
    elis=[]
    for i in range(value):
        x=int(input())
        elis.append(x)
    return min(elis)

def main():
    no=int(input("Enter number of elements: "))
    ret=minimum(no)
    print(ret)

if __name__=="__main__":
    main()
