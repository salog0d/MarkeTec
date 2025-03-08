from django.views import View
from django.shortcuts import render

from .models import Products
# Create your views here.
class ProductView(View):

    def dashboard(request):
        products= Products.objesct.all()
        return render(request, "..templates/dashboard.html", {"products": products})
