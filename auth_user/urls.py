from django.urls import path, reverse_lazy
from .views import Login, UserLogoutView, SignUpView
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView, PasswordResetView, LogoutView


urlpatterns = [
    path('', Login.as_view(), name = 'login'),
    path('signup/', SignUpView.as_view(), name = 'signup'),
    path('logout/', UserLogoutView.as_view(), name = 'logout'),
####
    path('reset_password/',PasswordResetView.as_view(template_name = "registration/password_reset_custom.html", email_template_name='registration/password_reset_email_custom.html', success_url = reverse_lazy("password_reset_done")), name='reset'),
    path('reset/<uidb64>/<str:token>',PasswordResetConfirmView.as_view(template_name = "registration/password_reset_confirm_custom.html"), name='password_reset_confirm'),
    path('reset/done/',PasswordResetDoneView.as_view(template_name='registration/reset_done_custom.html'), name='password_reset_done'),
    path('reset/complete/',PasswordResetCompleteView.as_view(template_name='registration/reset_complete_custom.html'), name='password_reset_complete'),
]
