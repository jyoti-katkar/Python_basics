class Calculator:
    def __init__(self):
        self.result = 0

    def addition(self, *integers):
        for x in integers:
            self.result = self.result + x
        return self.result

    def subtraction(self,*integers):
        numbers = list(integers)
        self.result = numbers[0] - sum(numbers[1:])
        return self.result

    def multiplication(self,*integers):
        self.result = 1
        for x in integers:
            self.result *= x
        return self.result

    def division(self,*integers):
        numbers = list(integers)
        self.result = numbers[0]
        for x in numbers[1:]:
            self.result= self.result / x
        return self.result


if __name__ == "__main__":

    cal = Calculator()
    print("1. ADDITION")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")
    print("Enter numbers for Operations as (separated by space)")
    choice = 1
    while choice != 0:
        choice = int(input("Enter your choice:[1-4]: "))
        if choice == 1:
            num = map(float, input().split())
            print(cal.addition(*num))
        elif choice == 2:
            num = map(float, input().split())
            print(cal.subtraction(*num))
        elif choice == 3:
            num = map(float, input().split())
            print(cal.multiplication(*num))
        elif choice == 4:
            num = map(float, input().split())
            print(cal.division(*num))
        else:
            print("Invalid choice..")
