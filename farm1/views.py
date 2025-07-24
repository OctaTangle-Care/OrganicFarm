from django.shortcuts import render
def landing_page(request):
    return render(request, 'landing_page.html')
# Create your views here.
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        
#         # Here you would typically authenticate the user
#         # For now, we will just render a simple response
#         return render(request, 'login_success.html', {'username': username})
    
#     return render(request, 'login.html')


# def signup_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        
#         # Here you would typically create a new user
#         # For now, we will just render a simple response
#         return render(request, 'login_success.html', {'username': username})
    
#     return render(request, 'signup.html')


def opening_page(request):
    return render(request, 'loading_page.html')


def index(request):
    return render(request, 'index.html')


def contactus(request):
    return render(request, 'contact_us.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def unknown(request):
    return render(request, '404.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')


def accessibility_statement(request):
    return render(request, 'accessibility_statement.html')

def terms_and_conditions(request):
    return render(request, 'terms_and_conditions.html')

def shipping_policy(request):
    return render(request, 'shipping_policy.html')

def refund_policy(request):
    return render(request, 'refund_policy.html')


def products(request):
    return render(request, 'products.html')