from django.urls import path
from CustomerApp.views import index ,all_customer,detail,add,addcustomer,deletecustomer,customer_list,customer_detail

urlpatterns = [
    path('',index),
    path('all_customer/',all_customer),
    path('<int:customer_id>/',detail,name='detail'),
    path('add/',add),
    path('add_customer/',addcustomer),
    path('<int:customer_id>/deletecustomer/',deletecustomer,name='deletecustomer'),
    path('customer_api/customers/',customer_list),
    path('customer_api/customers/<int:pk>/',customer_detail)
]