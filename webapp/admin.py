from django.contrib import admin
from .models import Employee, Client, Group, Contract, EmployeeContractStatus

admin.site.register(Employee)
admin.site.register(Client)
admin.site.register(Group)
admin.site.register(Contract)
admin.site.register(EmployeeContractStatus)


  