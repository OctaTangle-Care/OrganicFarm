from django.urls import path
from . import views

urlpatterns = [
     
     path('', views.opening_page, name='opening_page'),
     path('index/',views.index,name='index'),
     
     path('contactus/',views.contactus,name="contactus"),
     path('aboutus/',views.aboutus,name="aboutus"),
     
     path('unknown/', views.unknown, name='unknown'),
     path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
     path('accessibility_statement/', views.accessibility_statement, name='accessibility_statement'),
     path('terms_and_conditions/', views.terms_and_conditions, name='terms_and_conditions'),
     path('shipping_policy/', views.shipping_policy, name='shipping_policy'),
        path('refund_policy/', views.refund_policy, name='refund_policy'),
        path('products/', views.products, name='products'),  # Assuming products are listed on the index page
        
    # path('login/', views.login_view, name='login'),
    # path('signup/', views.signup_view, name='signup'),
   
    # path('api/gpt-process/', views.gpt_process),
    # path('about/', views.about, name='about'),
]
