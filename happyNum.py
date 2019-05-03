class Sol:
    def happyNum(self,num):
        sum=0
        c=0
        while num>9:
            for digit in str(num):
                sum+=int(digit)**2
            num=sum
            sum=0
            c+=1
        if num == 1:
           print("True")
        elif num < 10:
           print("False")
        return c

if __name__ == '__main__':
    p1=Sol()
    p1.happyNum(12)
