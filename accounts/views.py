from django.shortcuts import render, redirect
from django.contrib.auth import login 
from .forms import UserCreationForm

def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # Displays a blank form
        form = UserCreationForm()
    else:
        # Process a completed form via POST
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            
            # Login and redirect
            login(request, new_user)
            return redirect('blog:index')
    
    context = {'form': form}
    return render(request, 'registration/register.xhtml', context)
    

