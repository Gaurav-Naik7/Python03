import MarvellousNum

def ListPrime(value):
    elis=[]
    count=0
    for i in range(value):
        x=int(input())
        elis.append(x)

    for i in range(len(elis)):
        if MarvellousNum.ChkPrime(elis[i]) is True:
            count=count+elis[i]
    return count


def main():
    no=int(input("Enter number of elements: "))
    ret=ListPrime(no)
    print(ret)

if __name__=="__main__":
    main()
