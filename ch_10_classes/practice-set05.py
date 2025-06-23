from random import randint

class Train:
    
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no:{self.trainNo} from {fro} to {to}")

    def getStatus(self):
        (f"Train no:{self.trainNo} is running on timme")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(1, 5555)}")

t = Train(12399)

t.book("Kalyan", "Prayagraj")
t.getStatus()
t.getFare("Prayagraj", "Kalyan")
