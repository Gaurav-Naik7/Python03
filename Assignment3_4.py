def freq(value):
    elis=[]
    count=0
    for i in range(value):
        x=int(input())
        elis.append(x)
    nn=int(input("Enter element to search: "))
    for i in range(len(elis)):
        if elis[i]==nn:
            count=count+1
    return count


def main():
    no=int(input("Enter number of elements: "))
    ret=freq(no)
    print(ret)

if __name__=="__main__":
    main()
