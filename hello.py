def hello(to="World"):              #Defines Greeting function, default variable set to world
    print("Hello,", to)


hello() # prints default version of Hello
name = input("What's your name? ").strip().title() # Request users name, removes spaces and formats it
hello(name) #prints message