from django.urls import path
from .views import index,blog_detail,create_comment,edit_comment,delete_comment

app_name="blog"
urlpatterns = [
    path('',index, name="index"),
    path('detail/<int:id>/', blog_detail, name='detail'),
    path('detail/comments/<int:id>', create_comment, name='add_comment'),
    path('detail/edit/<int:id>', edit_comment, name='edit_comment'),
    path('detail/delete/<int:id>', delete_comment, name='delete_comment')
]
