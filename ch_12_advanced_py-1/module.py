def myFunc():
    print("Hello I am from module")

myFunc()
print(__name__)

# It gives output as: __main__



if __name__ == "__main__":
    # If this code is directly executd by running the file iys present in
    print("We are directly running this code")