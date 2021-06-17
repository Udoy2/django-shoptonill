from django.views import View
from django.shortcuts import render
from ..models import Gallery


class HomeView(View):
    def get(self, request):
        gallery_few_image = Gallery.objects.all()
        print(gallery_few_image)
        data = {'gallery_latest_preview': gallery_few_image}
        return render(request, 'pages/home.html', data)