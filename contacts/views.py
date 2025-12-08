from django.shortcuts import render

# ... your other view functions

def contacts(request):
    return render(request, 'contacts/contact.html')