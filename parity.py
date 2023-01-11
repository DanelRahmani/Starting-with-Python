def main():                                 #prompts user and returns result
    X = int(input("what is X? "))
    if is_even(X):
        print("X is an even number")
    else:
        print("X is an uneven number")

def is_even(n):                            #checks if n is even
    return n % 2 == 0

main()                                     #executes code