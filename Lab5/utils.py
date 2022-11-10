
def process_item(x):
    x+=1
    is_prime = 0
    while(is_prime == False):
        is_prime = 0
        if x > 1:
            for i in range(2,int(x/2) + 1):
                if x % i == 0:
                    x +=1
                else:
                    is_prime = 1
                    break
        else:
            is_prime = 0
            break

    return x


def main():

    x = int(input("Give number:"))
    print(process_item(x))

if __name__ == '__main__':
    main()



