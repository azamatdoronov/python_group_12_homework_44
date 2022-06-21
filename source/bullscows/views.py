from django.shortcuts import render

numbers_cache = []
steps_cache = []
step = {'step': 0}


class Check:

    def __init__(self) -> None:
        self.numbers = None

    secret_numbers = [1, 2, 3, 4]

    def one_check(self, numbers_str):
        numbers = [int(s) for s in numbers_str]
        if len(numbers) != 4:
            return "You must enter 4 digits"
        if len(numbers) != len(set(numbers)):
            return "Numbers should be unique"
        for i in numbers:
            if i < 0 or i > 10:
                return "Numbers should be in range 1 to 9"
        self.numbers = numbers

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
        return render(request, 'bullscows_view.html')
    else:
        try:
            numbers = list(map(int, request.POST.get('numbers').split()))
            check = Check()
            if check.one_check(numbers):
                one_check = check.one_check(numbers)
                context = {'run': one_check}
                return render(request, 'bullscows_view.html', context)
            else:
                second_check = check.guess_numbers()
                numbers = list(numbers)
                numbers_cache.append(numbers)
                step['step'] += 1
                steps_cache.append(step['step'])
                context = {'run': second_check}
                return render(request, 'bullscows_view.html', context)
        except ValueError:
            context = {'run': "You should enter only digits"}
            return render(request, 'bullscows_view.html', context)


def steps_cache_view(request):
    context = {'step': steps_cache,
               'numbers_cache': numbers_cache
               }
    return render(request, 'steps_cache.html', context)