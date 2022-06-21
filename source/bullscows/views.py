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

    def guess_numbers(self):
        bulls = 0
        cows = 0
        for i in range(len(self.numbers)):
            if self.numbers[i] == self.secret_numbers[i]:
                bulls += 1
            elif self.numbers[i] in self.secret_numbers:
                cows += 1
        if bulls == 4:
            return "Winner!"
        elif bulls or cows:
            return f"You got {bulls} bulls and {cows} cows"
        else:
            return "No identical numbers"


def bullscows_view(request):
    if request.method == "GET":
        return render(request, 'bullscows_form.html')
    else:
        if Check.one_check():
            first_check = Check.one_check()
            first_check = request.POST.get("first_check")

        else:
            result = Check.guess_numbers()
            result = request.POST.get("result")

        context = {
            first_check: request.POST.get("first_check"),
            result: request.POST.get("result"),
        }
        return render(request, "bullscows_view.html", context)