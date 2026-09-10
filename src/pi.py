import random

n = 100000

def Leibniz(n):
        L = 0
        for i in range(1,1000):
            L += ((-1) ** (i + 1)) / (2*i - 1)
        return 4 * L

def Sharp(n):
        S = 0
        for i in range(n):
            S += (2*(-1)**i)*(3**(0.5-i))/(2*i+1)
        return S

def MontePython(n):
    C = 0
    
    for i in range(n):
        x,y = random.random(), random.random()
        d = x**2 + y**2
        if d <= 1:
            C += 1
    return 4 * (C / n)


def main():
    # put all your main program driver code here
    print(Leibniz(n))
    print(Sharp(n))
    print(MontePython(n))
          

# main is called once when the script is executed.    
if __name__ == '__main__':
    main()