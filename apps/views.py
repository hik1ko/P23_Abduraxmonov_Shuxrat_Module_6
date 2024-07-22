import re

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, FormView, DetailView

from apps.forms import ProfileForm
from apps.models import User, Product, Category


class RegistrationView(TemplateView):
    template_name = 'apps/register.html'

    def post(self, request, *args, **kwargs):
        phone_number = re.sub(r'\D', '', request.POST.get('phone_number'))
        user = User.objects.create_user(phone_number=phone_number, password=request.POST['password'],
                                        email=request.POST['email'], name=request.POST['name'])
        login(request, user)
        return redirect('login')


class CustomLoginView(TemplateView):
    template_name = 'apps/login.html'

    def post(self, request, *args, **kwargs):
        phone_number = re.sub(r'\D', '', request.POST.get('phone_number'))
        user = User.objects.filter(phone_number=phone_number).first()
        if not user:
            return redirect('register')
        else:
            user = authenticate(request, username=user.phone_number, password=request.POST['password'])
            if user:
                login(request, user)
                return redirect('home')

            else:
                context = {
                    "messages_error": ["Invalid password"]
                }
                return render(request, template_name='apps/login.html', context=context)


class CategoryListView(ListView):
    queryset = Product.objects.all()
    template_name = 'apps/home_page.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        data['categories'] = Category.objects.all()
        return data


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'apps/product_list.html'
    context_object_name = 'products'
    paginate_by = 3


class ProductDetailView(DetailView):
    model = Product
    template_name = 'apps/product_detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'


class ProfileFormView(FormView):
    form_class = ProfileForm
    template_name = 'apps/profile.html'

    def form_valid(self, form):
        data = form.save(commit=False)
        print(data)

    def form_invalid(self, form):
        data = form.errors
        print(data)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
        return redirect('profile')
