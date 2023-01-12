def main():
    while True:                     # ask user for n
        n = int(input("What's n?"))
        if n > 0:
            break
    meow(n)

def meow(n):
        for i in range(n):          #makes cat output thoughts n times
            print("Meow")         #outputs the cat's thoughts

main()