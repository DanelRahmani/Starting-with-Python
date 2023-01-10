def main():                         # Request users name, removes spaces and formats it
    name = input("what's your name? ").strip().title()
    hello(name)

def hello(to="World"):              #Defines Greeting function, default variable set to world
    print("Hello,", to)



main()