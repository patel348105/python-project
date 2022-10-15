from django.urls import path

from . import views
urlpatterns=[
   path('',views.index,name='index'),
   path('login/',views.login,name='login'),
   path('signup/',views.signup,name='signup'),
   path('contact/',views.contact,name='contact'),
   path('products/',views.products,name='products'),
   path('addtocart/',views.addtocart,name='addtocart'),
   path('cart/',views.cart,name='cart'),
   path('single/<int:pid>',views.single,name='single'),
   #path('checkout/<int:pk>',views.checkout,name='checkout'),
   path('pay/',views.pay,name='pay'),
   path('paymenthandler/<int:oid>', views.paymenthandler, name='paymenthandler'),
]