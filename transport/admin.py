
"""from django.contrib import admin

# Register your models here.
#from .models import Farmers, Vehicles,Route
from .models import Vehicle, Register
admin.site.register(Register)
admin.site.register(Vehicle)
#admin.site.register(Produce)
#admin.site.register(Route)"""


from django.contrib import admin

# Register your models here.
from .models import Vehicle , Payment

admin.site.register(Vehicle)
admin.site.register(Payment)