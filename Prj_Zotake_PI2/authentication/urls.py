# Arquivo de mapeamento URL de Authentication

from django.urls import path
from django.contrib.auth import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path(
        "alterar_senha/", views.PasswordChangeView.as_view(), name="alteracao_de_senha"
    ),
    path(
        "alterar_senha/solicitada/",
        views.PasswordChangeDoneView.as_view(),
        name="alteracao_de_senha_solicitada",
    ),
    path("redefinir_senha/", views.PasswordResetView.as_view(), name="redefinicao_de_senha"),
    path(
        "redefinir_senha/solicitada/",
        views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "redefinir_senha/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(),
        name="confirmacao_de_redefinicao_de_senha",
    ),
    path(
        "redefinir_senha/concluida/",
        views.PasswordResetCompleteView.as_view(),
        name="redefinicao_de_senha_concluida",
    ),
]