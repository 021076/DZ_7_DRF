from django.contrib import admin
from users.models import User, Payments


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email',)


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date_payment', 'course', 'payment_method', 'amount')
    list_filter = ('user', 'course',)
    search_fields = ('user', 'course', 'payment_method',)
