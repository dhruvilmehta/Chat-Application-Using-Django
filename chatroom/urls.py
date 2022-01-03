from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('chatpage/',views.hostregister,name="hostregister"),
    # path('userlogin/',views.userlogin,name="userlogin"),
    path('chatpage/logout',views.logout,name="logout"),
    path('chatpage/messagesubmit/',views.submitmessage),
    path('messages/<int:roomcode>',views.loadmessages)
]