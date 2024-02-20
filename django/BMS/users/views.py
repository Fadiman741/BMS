from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from users.models import Order, User, Menu

from django.contrib.auth import authenticate, login, logout
from .serializers import OrderSerializer, UserSerializer, MenuSerialiazer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# ======================AUTHENTICATION========================================


@api_view(["POST"])
@permission_classes([AllowAny])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(request.data["password"])
        user.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(["POST"])
@permission_classes([AllowAny])
def login_view(request):
    email = request.data.get("email")
    password = request.data.get("password")
    user = authenticate(request, username=email, password=password)
    if user is not None:
        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
                "first Name": user.first_name,
                "Last Name": user.last_name,
                "Email": user.email,
                "Role": user.role,
                "Status": user.status,
            }
        )
    return Response({"error": "Invalid credentials"}, status=401)


@api_view(["POST"])
def logout_view(request):
    logout(request)
    return Response({"success": "Logged out successfully"})


# ==============================================MENU========================================


@api_view(["GET"])
@permission_classes([AllowAny])
def menu_list(request):
    menu = Menu.objects.all()  # complex data
    serializer = MenuSerialiazer(menu, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_menu(request):
    user = request.user  # Assuming you are using authentication
    serializer = MenuSerialiazer(data=request.data)
    Menu.objects.create(**request.data, user=user)

    if serializer.is_valid():
        serializer.save(user=user)
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
# @permission_classes([AllowAny])


def update_menu(request, pk=id):
    menu = Menu.objects.get(pk=pk)
    if request.method == "GET":
        serializer = MenuSerialiazer(menu)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = MenuSerialiazer(menu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    if request.method == "DELETE":
        menu.delete()
        return Response("menu deleted successfull")


# ------------------------------------------ORDER--------------------------------------------


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_order(request):
    user = request.user
    serializer = OrderSerializer(data=request.data)
    # items = request.data.get("items")
    # menu_item = items[0]
    # menu_id = menu_item.get("id")
    # print(menu_id)
    # print("\n\n MENU ID", menu_id)
    # menu_obj = Menu.objects.get(id=menu_id)
    # Order.objects.create(**request.data, user=user, items=[menu_obj])

    if serializer.is_valid():
        Order.objects.create(**request.data, user=user)
        serializer.save(user=user)
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
# @permission_classes([AllowAny])
def update_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    if request.method == "GET":
        serializer = MenuSerialiazer(order)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = MenuSerialiazer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    if request.method == "DELETE":
        order.delete()
        return Response("order deleted successfull")


# ------------------------------------------------------------------------------------------------------------------------------
