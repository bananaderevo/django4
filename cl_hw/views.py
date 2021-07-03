from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from .forms import SendMailForm


def send(request):
    if request.method == 'POST':
        form = SendMailForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, 'cl_hw/index.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SendMailForm()

    data = {
        'form': form,
    }

    return render(request, 'cl_hw/index.html', data)
