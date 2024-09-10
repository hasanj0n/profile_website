from .models import Home, About, Profile, Category, Skills, Portfolio, Message
from django.shortcuts import render
from .forms import ContactForm

def index(request):

    # Home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)


    # Skills
    categories = Category.objects.all()

    # Portfolio
    portfolios = Portfolio.objects.all()

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios,
    }



    return render(request, 'index.html', context=context)



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
    else:
        form = ContactForm()
    
    return render(request, 'index.html', {'form': form})
