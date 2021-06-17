from django.views import View
from django.shortcuts import render
from ..models import Shobhapoti, GroupCommitte


class AboutView(View):
    def get(self, request):
        committe_members = GroupCommitte.objects.all()
        shobhapoti = Shobhapoti.objects.first()
        data = {'committe_members': committe_members, 'shobhapoti': shobhapoti}
        return render(request, 'pages/about.html', data)