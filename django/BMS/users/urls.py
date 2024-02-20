from django.urls import path
from .views import (
    signup,
    logout_view,
    login_view,
    menu_list,
    create_menu,
    update_menu,
    create_order,
    update_order,
)

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("create_menu/", create_menu, name="create_menu"),
    path("menus/", menu_list, name="menu_list"),
    path("menu/<int:pk>/", update_menu, name="update_menu"),
    path("create_order/", create_order, name="create_order"),
    path("update_order/<int:order_id>/", update_order, name="update_order"),
]
