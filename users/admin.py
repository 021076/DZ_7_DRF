from django.contrib import admin
from users.models import User, Payments


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email',)


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date_payment', 'course_paid', 'payment_method',)
    list_filter = ('user', 'course_paid',)
    search_fields = ('user', 'course_paid', 'payment_method',)
