from cgitb import html, reset
from distutils.log import info
from multiprocessing import context
from tracemalloc import start
from unittest import result
from django import http
from django.http import HttpResponse
from django.shortcuts import render
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views import View
from qr_code.qrcode.utils import QRCodeOptions
from qr_code.qrcode.utils import MeCard, VCard, EpcData, WifiConfig, Coordinates, QRCodeOptions
from datetime import date
from io import BytesIO
from django.core.files import File
from django_xhtml2pdf.utils import generate_pdf


from . models import *


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result =  BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)

    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
  

def pdf(request, pk):
    student = Student.objects.get(id=pk)
    info = " Name: {name} \n Passport No {passport} \n Trade: {trade} \n Training Center: {center}\n Website: {website} ".format(name = student.name, passport = '123B234', trade = "6G", center="JTC Training Center", website="https://jtcbd.net")

    context = {
            'my_options': QRCodeOptions(size='t', border=6, error_correction='L'),
            'info': info,
            'student': student
    }
    # resp = HttpResponse(content_type='application/pdf')
    # result = generate_pdf('my_template.html', file_object=resp)
    # return result

    pdf = render_to_pdf('core/certificate.html', context)
    #receipt_file = File(BytesIO(pdf.content))

    #print('apel',pdf)
    return HttpResponse(pdf, content_type='application/pdf')

def pdfTest(request):

    return render(request, 'core/pdf-test.html')





class ViewPDF(View):

    def get(self, request, *args, **kwargs):
        person = Student.objects.get(id=1)
        print(person.name)
        context = {
            'person': person
        }
        pdf = render_to_pdf('core/certificate.html', context)

        return HttpResponse(pdf, content_type='application/pdf')



def allStudent(request):

    students = Student.objects.all()

    context = {
        'students': students,
    }

    return render(request, 'core/all-student.html', context)

def qr(request):
    students = Student.objects.all()[0:2]

    start = 1
    end = 3

    vcard_contact = VCard(
        name='Doe; John',
        phone='+41769998877',
        email='j.doe@company.com',
        url='http://www.company.com',
        street='Cras des Fourches 987',
        city='Delémont',
        zipcode=2800,
        region='Jura',
        country='Switzerland',
        memo='Development Manager',
        org='Company Ltd'
    )


    context = {
        'my_options': QRCodeOptions(size='t', border=6, error_correction='L'),
        'url': 'http://127.0.0.1:8000/range/'+str(start) + '/' + str(end),
        'vcard_contact': vcard_contact,

    }

    return render(request, 'core/test.html', context=context)


def queryRange(request, start, end):

    students = Student.objects.all()[start-1:end]
    context = {
        'students': students,
    }
    return render(request, 'core/range.html', context)
