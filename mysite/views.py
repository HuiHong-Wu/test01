from django.shortcuts import render
import random 

def index(request):
    name = "Richard Ho"
    return render(request, "index.html", locals())

def lotto(request):
    lucky = random.randint(1, 99)
    return render(request, "lotto.html", locals())
