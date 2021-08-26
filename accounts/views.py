from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def home(request):
  numbers = [1, 2, 3, 4, 5]
  name = 'Max Goodnite'
  context = {
    'name': name,
    'numbers': numbers,
  }

  return render(request, 'accounts/home.html', context)

#
# def RegisterView(request):
#   if request.method == 'POST':
#     form = UserCreationForm(request.POST)
#     print("Errors", form.errors)
#     if form.is_valid():
#       form.save()
#       return redirect('polls:starter')
#     else:
#       context = {
#         'form': form
#       }
#       return render(request, 'accounts/registration/register.html', context)
#   else:
#     form = UserCreationForm()
#     context = {'form': form}
#     return render(request, 'accounts/registration/register.html', context)
