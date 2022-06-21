from django.shortcuts import render


class Check:

    def __init__(self) -> None:
        self.numbers = None

    secret_numbers = [1, 2, 3, 4]

    def one_check(self, numbers_str):
        try:
            numbers = [int(s) for s in numbers_str]
            if len(numbers) != 4:
                return "You should enter only 4 numbers"
            if len(numbers) != len(set(numbers)):
                return "Numbers should be unique"
            for i in numbers:
                if i < 0 or i > 10:
                    return "Numbers should be in range 1 to 9"
            self.numbers = numbers
        except:
            return " The value should be integers"
