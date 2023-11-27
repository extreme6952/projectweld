from django.urls import path

from . import views

app_name = 'welder'


urlpatterns = [
    path('',views.index_list,name='home'),
    path('<int:year>/<int:month>/<int:day>/<slug:product>',views.detail,name='product_detail'),
    path('<int:product_id>/comment',views.comment_product,name='comment')
    
]