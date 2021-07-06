from django.contrib import messages

from .tasks import send_mail_to, quotes
from django.shortcuts import render

from .forms import SendMailForm
from django.utils import timezone


now = timezone.now()


def send(request):
    quotes.delay()
    if request.method == 'POST':
        form = SendMailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            time = form.cleaned_data['time']
            dif = time - now
            if dif.days > 2 or dif.days < 0:
                messages.success(request, "Wrong date, it should be not in the past and less than 2 days in the future.")
            else:
                send_mail_to.apply_async(('Remind', text, email), eta=time)
                messages.success(request, "Success.")
            return render(request, 'cl_hw/index.html', {'form': form, 'message': messages})
    else:
        form = SendMailForm()

    data = {
        'form': form,
    }

    return render(request, 'cl_hw/index.html', data)


