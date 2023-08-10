from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from accountapp.models import HelloWorld
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accountapp.forms import AccountUpdateForm

# Create your views here.
def test(request):

    if request.method == "POST":

        temp = request.POST.get('test_input')

        test_text = HelloWorld()
        test_text.text = temp
        test_text.save()
        
        return HttpResponseRedirect(reverse('accountapp:test'))
    
    else:
        new_text_list = HelloWorld.objects.all()

        return render(request, 'accountapp/test.html', context={'new_text_list':new_text_list})
    


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:test') # reverse와 reverse_lazy의 차이점? => reverse_lazy는 class형 view에서 사용한다(class에서는 reverse를 사용할 수 없음)
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp/update')
    template_name = 'accountapp/update.html'