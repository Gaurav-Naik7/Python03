def sum(value):
    elis=[]
    sum=0
    for i in range(value):
        x=int(input())
        elis.append(x)
        sum=sum+x
    return sum

def main():
    no=int(input("Enter number of elements: "))
    ret=sum(no)
    print(ret)

if __name__=="__main__":
    main()
