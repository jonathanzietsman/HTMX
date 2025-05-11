from django.shortcuts import render
from django.http import HttpResponse
from .forms import SampleForm

def example(request):
    return render(request, 'ex.html')

def sample_post(request):
    form = SampleForm(request.POST or None)
    if form.is_valid():
        return HttpResponse('<p class="success">Form submitted successfully! ✅</p>')
    return HttpResponse(f'<p class="error">Form has errors: {form.errors}</p>')
