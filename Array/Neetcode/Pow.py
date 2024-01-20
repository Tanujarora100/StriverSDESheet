class Pow:
    def myPow(self, x, n):
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.calculate(x, -n)
        else:
            return self.calculate(x, n)

    def calculate(self, x, n):
        if n == 0:
            return 1
        elif n % 2 == 0:
            return self.calculate(x * x, n // 2)
        else:
            return x * self.calculate(x * x, (n - 1) // 2)

# Example Usage:
# pow_instance = Pow()
# result = pow_instance.myPow(2.0, 10)
# print("Result:", result)
