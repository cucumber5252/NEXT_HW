from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('new/', views.new, name = 'new'),
    path('detail/<int:post_pk>', views.detail, name = 'detail'),
    path('update/<int:post_pk>', views.update, name = 'update'),
    path('delete/<int:post_pk>', views.delete, name = 'delete'),
    path('deleteComment/<int:post_pk>/<int:comment_id>/', views.deleteComment, name='deleteComment'),

]