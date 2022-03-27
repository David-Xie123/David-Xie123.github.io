class Factors:
# Function to find the Factors of a Number
    def findFactors(number):
        print("Factors of a Given Number {0} are:".format(number))
        for value in range(1, number + 1):
            if number % value == 0:
                print("{0}".format(value), end=" ")
        print()

    # def factors(self):

        # self.findFactors(num)

# initiates class
f = Factors
num = int(input("Enter any Number to find its factors: "))
f.findFactors(num)