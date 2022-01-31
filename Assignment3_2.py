def maximum(value):
    elis=[]
    for i in range(value):
        x=int(input())
        elis.append(x)
    return max(elis)

def main():
    no=int(input("Enter number of elements: "))
    ret=maximum(no)
    print(ret)

if __name__=="__main__":
    main()
