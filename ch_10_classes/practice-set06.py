
# What if we placed diferent word inplace of self

from random import randint

class Train:
    
    def __init__(mayur, trainNo):
        mayur.trainNo = trainNo

    def book(mayur, fro, to):
        print(f"Ticket is booked in train no:{mayur.trainNo} from {fro} to {to}")

    def getStatus(mayur):
        (f"Train no:{mayur.trainNo} is running on timme")

    def getFare(mayur, fro, to):
        print(f"Ticket fare in train no: {mayur.trainNo} from {fro} to {to} is {randint(1, 5555)}")

t = Train(12399)

t.book("Kalyan", "Prayagraj")
t.getStatus()
t.getFare("Prayagraj", "Kalyan")


# No diffrence 
# which mean it still work as they before
# O/P remain same