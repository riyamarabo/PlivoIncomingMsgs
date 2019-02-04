from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import plivo
from datetime import datetime
from plivoterminal.models import Incoming


def post(request):
    #store request POST into a var and record timestamp
    # data = request.POST
    #     # timestamp = datetime.now()
    #     #
    #     #
    #     # #now retrieve data individually
    #     # phone_number = data.get('From')
    #     # content = data.get('Text')

    #saving into database
    phone_number = "619" #request.POST.get('From')
    contents = "hello" #request.POST.get('Text')
    dbsave = Incoming(phone_number=phone_number, date_time=datetime.now(), contents=contents)
    dbsave.save()


    #post data into database
    html = "<html><body> phone number:{} <br>content:{} <br>timestamp:{} </body></html>".format(phone_number, contents, datetime.now())

    #testing posting data to a page

    return HttpResponse(html)







