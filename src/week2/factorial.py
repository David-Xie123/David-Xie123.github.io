class factorial:
    def __init__(self):
        self.fact = 1
    def __call__(self, n):
        if n <= 1:
            return 1
        else:
            # Compute the requested factorial number
            fact_number = n * self(n - 1) # two recursive calls to self (__call__(self, n))
            return fact_number # builds list, with most nested of the calculations 1st... may hurt your head

    def factorial(self):
        fact_of = factorial()

        # self.fact_of(num)
        print(fact_of(num)) # object running __call__ method

# initiates class
f = factorial
num = int(input("Enter any Number to find its factorial: "))
f.factorial(num)