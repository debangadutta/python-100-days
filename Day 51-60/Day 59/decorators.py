def greet(fx):
    def modified_fx():
        print("Good morning!")
        fx()
        print("Function over.")
    return modified_fx

@greet
def hello():
    print("Hello!")

hello()

#same output if used without decorator line (@)
# greet(hello)()