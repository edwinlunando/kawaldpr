from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import SetPasswordForm
from django.core.urlresolvers import reverse_lazy
from django.db import transaction
from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, View
from django.views.generic.edit import FormMixin
from .forms import SignUpForm, SignInForm, ContactForm, ForgotPasswordForm
from .mailers import ForgotPasswordEmail
from .models import ForgotPassword, User


# Create your views here.
class SignUpPage(FormMixin, TemplateView):
    """
    The sign up page for kuliahkita.com. There need to be forgot password link in this page.
    """

    template_name = "core/sign-up.html"
    form_class = SignUpForm
    success_url = reverse_lazy('sign-up-success')

    def get_context_data(self, **kwargs):
        context = super(SignUpPage, self).get_context_data(**kwargs)
        form_class = self.get_form_class()
        context['form'] = self.get_form(form_class)
        return context

    def post(self, request):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(SignUpPage, self).form_valid(form)


class SignInPage(FormMixin, TemplateView):
    """
    The sign in page for kuliahkita.com
    """

    template_name = "core/sign-in.html"
    form_class = SignInForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(SignInPage, self).get_context_data(**kwargs)
        form_class = self.get_form_class()
        context['form'] = self.get_form(form_class)
        return context

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        username_or_email = form.cleaned_data['username_or_email']
        password = form.cleaned_data['password']
        user = authenticate(username=username_or_email, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                messages.success(self.request, 'Berhasil masuk!')
                if self.request.GET.get('next'):
                    return redirect(self.request.GET.get('next'))
                return redirect('home')
            else:
                messages.error(self.request, 'Akun sudah tidak aktif!')
        else:
            messages.error(self.request, 'Kombinasi pengguna tidak dapat ditemukan!')
        context = super(SignInPage, self).get_context_data()
        context['form'] = form
        return render(self.request, self.template_name, context)


class ContactPage(FormMixin, TemplateView):
    """
    Contact page to let User communicate to the kuliahkita.com admin
    """
    template_name = "core/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def post(self, request):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(ContactPage, self).get_context_data(**kwargs)
        form_class = self.get_form_class()
        context['form'] = self.get_form(form_class)
        return context

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Pesan berhasil terkirim!")
        return super(ContactPage, self).form_valid(form)


class ForgotPasswordPage(FormMixin, TemplateView):
    """
    Forgot Password page to let User reset their password through the link send by email
    """
    template_name = "core/forgot-password.html"
    form_class = ForgotPasswordForm
    success_url = reverse_lazy('home')

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(ForgotPasswordPage, self).get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context

    def form_valid(self, form):
        email_address = form.cleaned_data['email']
        user = get_object_or_404(User, email=email_address)
        token = ForgotPassword(user=user)
        token.save()
        email = ForgotPasswordEmail([token.user.email], token.guid, self.request.get_host())
        email.send()
        messages.success(self.request, "Password berhasil direset!")
        return super(ForgotPasswordPage, self).form_valid(form)


class ResetPasswordPage(FormMixin, View):
    """
    Page to reset user password from the given link. After reset, the link must be made expired.
    """
    template_name = "core/reset-password.html"
    data = {}
    form_class = SetPasswordForm
    success_url = reverse_lazy('home')

    @method_decorator(transaction.atomic)
    def post(self, request, guid):
        token = get_object_or_404(ForgotPassword, guid=guid)
        self.data['form'] = form = self.form_class(data=request.POST, user=token.user)
        if form.is_valid():
            token.delete()
            return self.form_valid(form)
        return render(request, self.template_name, self.data)

    def get(self, request, guid):
        token = get_object_or_404(ForgotPassword, guid=guid)
        if token.is_valid():
            token.delete()
            raise Http404
        self.data['form'] = self.form_class(user=token.user)
        return render(request, self.template_name, self.data)

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Password berhasil direset!")
        return redirect('home')