#L local
#food is a variable that can be accessed only within the function
def order():
    food = "Briyani"
    print("Order is:", food)

order()
#E enclosing
# discount- a variable inside a parent fun can be accessed by child fun
def cart():
    discount = 25

    def checkout():
        print("Applying discount:", discount)

    checkout()

cart()

#G global
#all functions can access the variable
user_id = "udhay_925"
def homepage():
    print("Welcome",user_id)
def profile():
    print("Welcome to the profile page:",user_id)
homepage()
profile()

#B built in
print(__file__)
