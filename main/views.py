from django.shortcuts import render
from rest_framework.views import APIView
from . import models,serializers
from rest_framework.response import Response
from django.http import HttpResponse
import json,datetime,pytz
# Create your views here.
class insta_day(APIView):
    def get(self,request):
        day=list(models.insta_day.objects.all())
        if day==[]:
            return HttpResponse('no days present')
        return HttpResponse(day[0].lastday)
    def post(self,request):
        day=list(models.insta_day.objects.all())
        if day==[]:
            return HttpResponse('no days present')
        print(day[0])
        day=day[0]
        day.lastday=day.lastday+1
        day.save()
        return HttpResponse(day.lastday)
class get_replace_data(APIView):
    def get(self,replace):
        words=list(models.replace_letters.objects.all())
        result={}
        for i in words:
            result[i.word]=i.options.split(',')
        return Response(result)     
        #return Response(serializers.replace_letters(day,many=True).data)
class insta_msg(APIView):
    def get(self,replace):
        result=[]
        day=list(models.insta_msg.objects.all())
        for i in day:
            result.append(i.msg)
        return Response(result)    
class insta_time_counter(APIView):
    def get(self,request):
        op=list(models.insta_output.objects.all())
        date=list(models.instence_start_date.objects.all())
        day=list(models.insta_day.objects.all())
        error=list(models.instabot_error.objects.all())
        if op==[] or date==[]or day==[] or error==[]:
            return HttpResponse('error no instence found')
        op=op[0]
        date=date[0]
        day=day[0]
        error=error[0]
        print(date.date)
        html="""
        <!DOCTYPE html>
        <html>
        <head>
        <style>
        table {
          font-family: arial, sans-serif;
          border-collapse: collapse;
          width: 100%;
        }

        td, th {
          border: 1px solid #dddddd;
          text-align: left;
          padding: 8px;
        }

        tr:nth-child(even) {
          background-color: #dddddd;
        }
        .error{
        background-color:#FFCED0;
        }
        </style>
        </head>
        <body>

        <h2>OP for insta_bot</h2>

        <table>
          <tr>
            <th></th>
            <th></th>

          </tr>
          <tr>
            <td>number of days left to restart pythonanywhere </td>
            <td>"""+str((date.date+datetime.timedelta( days=90))-datetime.datetime.now().replace(tzinfo=pytz.UTC)).split(',')[0]+ """</td>

          </tr>
          
          <tr>
            <td>current day</td>
            <td>"""+str(day.lastday)+ """</td>

          </tr>
          
          <tr>
            <td>op </td>
            <td>"""+str(op.op)+ """</td>

          </tr>
          <tr class='error'>
            <td>error </td>
            <td>"""+str(error.error)+ """</td>

          </tr>

        </table>

        </body>
        </html>

"""
        return HttpResponse(html)
    def post(self,request):
        try:
            msg=request.POST['msg']
        except:
            return HttpResponse('')
        op=list(models.insta_output.objects.all())
        if op==[]:
            return HttpResponse('')
        op=op[0]
        op.op=msg
        op.save()
        return HttpResponse('')
class instabot_error(APIView):
    def post(self,request):
        try:
            msg=request.POST['msg']
        except:
            return HttpResponse('')
        op=list(models.instabot_error.objects.all())
        if op==[]:
            return HttpResponse('')
        op=op[0]
        op.error=msg
        op.save()
        return HttpResponse('')
