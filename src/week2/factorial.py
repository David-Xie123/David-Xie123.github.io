class factorial:
    def __init__(self):
        self.factSeq = [0, 1]
    def __call__(self, n):
        if n < len(self.factSeq):
            return self.factSeq[n]
        else:
            # Compute the requested factorial number
            fact_number = self(n - 1) * self(n - 2) # two recursive calls to self (__call__(self, n))
            self.factSeq.append(fact_number) # builds list, with most nested of the calculations 1st... may hurt your head
        return self.factSeq[n]
    def factorial(self):
        fact_of = factorial()
        num = int(input("Enter any Number to find its factorial: "))
        self.fact_of(num)
        print(fact_of(5)) # object running __call__ method