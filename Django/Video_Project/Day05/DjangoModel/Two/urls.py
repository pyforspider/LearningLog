from django.urls import path

from Two import views

urlpatterns = [
	path('hello/', views.hello, name='index'),
	path('addperson/', views.add_person, name='add_person'),
	path('addidcard/', views.add_idcard, name='add_id_card'),
	path('bindcard/', views.bind_card, name='bind_card'),
	path('removeperson/', views.remove_person, name='remove_person'),
	path('removeidcard/', views.remove_idvard, name='remove_idcard'),
	path('getidcard/', views.get_idcard, name='get_idcard'),
	path('getperson/', views.get_person, name='get_person'),

	path('addcustomer/', views.add_customer, name='add_customer'),
	path('addgoods/', views.add_goods, name='add_goods'),
	path('addtocart/', views.add_to_cart, name='add_to_cart'),
	path('getgoodslist/<int:customer_id>/', views.get_goods_list, name='get_goods_list'),

	path('adddog/', views.add_dog, name='add_dog'),
	path('addcat/', views.add_cat, name='add_cat'),
	path('getdog/', views.get_dog, name='get_dog'),
]
