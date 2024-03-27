from . import views
from django.urls import path


urlpatterns = [
    path('',views.register_view,name='register'),
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path("allemployees/", views.allemployees, name="allemployees"),
    path("singleemployee/", views.singleemployee, name="singleemployee"),
    path("addemployee/", views.addemployee, name="addemployee"),
    path("deleteemployee/<int:empid>/", views.deleteemployee, name="deleteemployee"),
    path("updateemployee/<int:empid>/", views.updateemployee, name="updateemployee"),
    path("doupdateemployee/<int:empid>/", views.doupdateemployee, name="doupdateemployee"),
    path('employee/<int:employee_id>/monthly_salary/', views.employee_monthly_salary, name='employee_monthly_salary'),
    
]
