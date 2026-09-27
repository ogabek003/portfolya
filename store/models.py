from django.db import models
from django.contrib.auth.models import User


# =========================
# POST
# =========================

class Post(models.Model):

    sarlavha = models.CharField(
        max_length=200
    )

    matn = models.TextField()

    muallif = models.CharField(
        max_length=100
    )

    sana = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.sarlavha


# =========================
# BUYURTMA
# =========================

class Order(models.Model):

    STATUS_CHOICES = [
        ("pending", "Jarayonda"),
        ("approved", "Tasdiqlandi"),
        ("rejected", "Rad etildi"),
    ]

    SERVICE_CHOICES = [
        ("website", "Web sayt"),
        ("bot", "Telegram bot"),
        ("program", "Dastur"),
        ("design", "Dizayn"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=150
    )

    phone = models.CharField(
        max_length=30
    )

    service = models.CharField(
        max_length=30,
        choices=SERVICE_CHOICES
    )

    price = models.DecimalField(
        max_digits=12,
        decimal_places=0
    )

    bot_description = models.TextField(
        blank=True
    )

    comment = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.name} - {self.get_service_display()}"


# =========================
# TECHNOLOGY
# =========================

class Technology(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name


# =========================
# PROJECT
# =========================

class Project(models.Model):

    name = models.CharField(
        max_length=200
    )

    description = models.TextField()

    link = models.URLField(
        blank=True
    )

    technologies = models.ManyToManyField(
        Technology,
        related_name="projects"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


# =========================
# CONTACT MESSAGE
# =========================

class ContactMessage(models.Model):

    name = models.CharField(
        max_length=150
    )

    email = models.EmailField(
        blank=True
    )

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.name} - {self.created_at:%Y-%m-%d %H:%M}"