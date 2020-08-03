                    
def getPentagonalNumber(n):
        pentagonalNumber=n*(3*n-1)/2
        return pentagonalNumber

def main():
        total=eval(input("total:"))
        amountPerRow=eval(input("amount per row:"))
        for i in range(total):
                obj=int(getPentagonalNumber(i+1))
                if (i+1)%amountPerRow==0:
                        print(format(obj,"<6d"))
                else:
                        print(format(obj,"<6d"),end='')

main()
