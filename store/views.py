from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie

from .forms import RegisterForm, ContactMessageForm
from .models import Order, Project


# =========================
# BOSH SAHIFA
# =========================
def home(request):

    projects = Project.objects.prefetch_related(
        "technologies"
    ).order_by(
        "-created_at"
    )[:3]

    return render(
        request,
        "store/home.html",
        {
            "projects": projects
        }
    )


# =========================
# BIZ HAQIMIZDA
# =========================

def biz_haqimizda(request):

    return render(
        request,
        "store/biz_haqimizda.html"
    )


# =========================
# ALOQA
# =========================

def aloqa(request):

    return render(
        request,
        "store/aloqa.html"
    )


# =========================
# REGISTER
# =========================

def register(request):

    if request.method == "POST":

        print("POST KELDI")

        form = RegisterForm(
            request.POST
        )

        if form.is_valid():

            print("FORM TOGRI")

            form.save()

            return redirect(
                "register_success"
            )

        else:

            print(form.errors)

    else:

        form = RegisterForm()

    return render(
        request,
        "store/register.html",
        {
            "form": form
        }
    )


# =========================
# REGISTER SUCCESS
# =========================

def register_success(request):

    return render(
        request,
        "store/register_success.html"
    )


# =========================
# ZAKAZ
# =========================

@login_required
def zakaz(request):

    return render(
        request,
        "store/zakaz.html"
    )


# =========================
# ZAKAZ FORM
# =========================

@login_required
@ensure_csrf_cookie
def zakaz_form(request):

    services = {

        "website": {
            "name": "🌐 Web Sayt",
            "price": 1500000,
        },

        "bot": {
            "name": "🤖 Telegram Bot",
            "price": 800000,
        },

        "program": {
            "name": "💻 Dastur",
            "price": 2000000,
        },

        "design": {
            "name": "🎨 Dizayn",
            "price": 500000,
        },

    }

    service = request.GET.get(
        "service"
    )

    if service not in services:

        return redirect(
            "zakaz"
        )

    data = services[service]

    if request.method == "POST":

        Order.objects.create(

            user=request.user,

            name=request.POST.get(
                "name"
            ),

            phone=request.POST.get(
                "phone"
            ),

            service=service,

            price=data["price"],

            bot_description=request.POST.get(
                "bot_description",
                ""
            ),

            comment=request.POST.get(
                "comment",
                ""
            ),

        )

        return redirect(
            "buyurtmalarim"
        )

    return render(

        request,

        "store/zakaz-form.html",

        {
            "service": service,

            "service_name": data["name"],

            "price": f"{data['price']:,}".replace(
                ",",
                " "
            ),
        }
    )


# =========================
# MENING BUYURTMALARIM
# =========================

@login_required
def buyurtmalarim(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by(
        "-created_at"
    )

    return render(

        request,

        "store/buyurtmalarim.html",

        {
            "orders": orders
        }
    )


# =========================
# PORTFOLIO / LOYIHALAR
# =========================

def loyihalar(request):

    projects = Project.objects.prefetch_related(
        "technologies"
    ).order_by(
        "-created_at"
    )

    return render(

        request,

        "store/loyihalar.html",

        {
            "projects": projects
        }
    )


# =========================
# BOG'LANISH
# =========================

def boglanish(request):

    if request.method == "POST":

        form = ContactMessageForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                "boglanish_success"
            )

    else:

        form = ContactMessageForm()

    return render(

        request,

        "store/boglanish.html",

        {
            "form": form
        }
    )


# =========================
# BOG'LANISH SUCCESS
# =========================

def boglanish_success(request):

    return render(
        request,
        "store/boglanish_success.html"
    )