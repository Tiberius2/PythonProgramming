import utils

def main():
    while(True):
        x = input("Please enter a number or 'q' to stop the application: ")
        if x == 'q':
            return
        try:
            x = int(x)
        except ValueError:
            print("You have entered the wrong input! Please try again!")
        else:
            print(utils.process_item(x))

if __name__ == '__main__':
    main()