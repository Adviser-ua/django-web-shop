from django.shortcuts import render


# Страница с товарами
from contacts.models import Contact


def ContactsView(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contacts.html', {'contacts': contacts})


def PayShipment(request):
    return render(request, 'contacts/pay_ship.html')