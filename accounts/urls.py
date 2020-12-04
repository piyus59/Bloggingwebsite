from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	path('register',views.register, name='register'),
	path('login' ,views.login, name='login'),
	path('logout' ,views.logout, name='logout'),
	path('index' ,views.index, name='index'),
	path('about' ,views.about,name='about'),
	path('contact' ,views.contact,name='contact'),

	path('reset_password',
		auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
		name="reser_password"),
	
	path('reset_password',
		auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
		name="reser_password"),
	
	path('reset_password',
		auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
		name="reser_password"),
	
	path('reset_password',
		auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
		name="reser_password")
]