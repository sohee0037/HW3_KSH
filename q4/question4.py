input_ls = [0,2,4,6,8,10,12,14]
def factorial(n):
    if n == 0:
        return 1
    elif n >= 1:
        return n*factorial(n-1)
def main():
    for i in input_ls:
        print("{0}! = {1}".format(i,factorial(i)))

if __name__ == '__main__':
    main()
