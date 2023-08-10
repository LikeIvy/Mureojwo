from django.urls import path
from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView, test
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accountapp'

urlpatterns = [
    path('test/', test, name='test'),                           # 두 번째 인자 test는 함수형 view => 이 경우에는 해당 함수이름을 바로 써서 넣어주면 되지만
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', AccountCreateView.as_view(), name='create'),  # class based view는 as_view()를 적어줘야 한다
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]