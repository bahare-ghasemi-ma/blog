from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)  # شناسه یکتا
    name = models.CharField(max_length=150)  # نام کاربر
    email = models.EmailField(unique=True)  # ایمیل یکتا
    username = models.CharField(max_length=150, unique=True)  # نام کاربری یکتا
    password = models.CharField(max_length=128)  # رمز عبور (بدون رمزنگاری)

    def __str__(self):
        return self.username

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')  # ارتباط با کاربر
    title = models.CharField(max_length=200)  # عنوان پست
    content = models.TextField()  # محتوای پست
    created_at = models.DateTimeField(auto_now_add=True)  # تاریخ ایجاد
    updated_at = models.DateTimeField(auto_now=True)  # تاریخ آخرین بروزرسانی

    def __str__(self):
        return self.title
