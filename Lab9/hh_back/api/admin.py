from django.contrib import admin
from .models import *

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    pass

