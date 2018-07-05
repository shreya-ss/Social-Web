from django.urls import path
from django.contrib.auth.views import login,logout,logout_then_login, password_change, password_change_done,password_reset,password_reset_done,password_reset_complete,password_reset_confirm
from . import views

urlpatterns = [
	#post views
	#previous login view
	#path('login/',views.user_login, name='login'),

	#login / logout urls
	path('login/',login,name='login'),
	path('logout/',logout,name='logout'),
	path('logout-then-login/',logout_then_login,name='logout_then_login'),
	path('',views.dashboard, name='dashboard'),
	path('password-change/',password_change,name='password_change'),
	path('password-change-done/',password_change_done,name='password_change_done'),
	path('password-reset/',password_reset,name='password_reset'),
	path('password-rest/done',password_reset_done,name='password_reset_done'),
	path('password-reset/complete',password_reset_complete,name='password_reset_complete'),
	path('password-reset/confirm/<uidb64>/<token>/',password_reset_confirm,name='password_reset_confirm'),
	path('register/',views.register, name='register'),
	path('edit/',views.edit,name='edit'),
]