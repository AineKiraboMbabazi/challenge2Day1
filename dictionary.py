def dictionary(lower, upper):
    mydic=dict()
    for x in range(lower,upper):
        mydic[x]=x**2
    return mydic

if __name__ == '__main__':
    print(dictionary(2,15))
    print(dictionary(,3))