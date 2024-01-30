from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def documentation_main(request):
    return render(request, 'documentation/main.html')