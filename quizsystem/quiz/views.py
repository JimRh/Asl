
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from .models import *
@api_view(['GET','POST'])
def home(request):

    if request.method=='GET':
        payload={}
        question=Question.objects.all()
        data=[]
        for qs in question:
            data.append({
                'id':qs.id,
                'question':qs.question,
                'marks':qs.marks,
                 'ans':qs.getanswer()
            },
            )
            payload={'status':True,'Data':data}
        return Response (payload)
    elif request.method=='POST':
        score=0
        data=request.data['data']
        res=[]
        for i in range(len(data)):
            ques = data[i]['ques']
            given_ans=data[i]['ans']
            answer=Answer.objects.filter(question=ques)
            cor_ans=''
            for ans in answer:
                if ans.iscorrect==True:
                    cor_ans=ans.answer

                    break
            if cor_ans==given_ans:
                res.append(cor_ans)
                score+=2
            else:
                res.append('wrong')
        data={'res':res,"score":score}
        return Response (data)





        return Response(data)
from django.contrib.auth.models import User
@api_view(['POST'])

def register(request):
    try:
        username=request.data['username']
        email=request.data['email']
        first_name=request.data['first_name']
        last_name=request.data['last_name']
        password1=request.data['password']
        password2=request.data['password']

        if User.objects.filter(username=username).exists():
            return Response({"error":"username exists"})
        user=User()
        user.username=username
        user.email=email
        user.first_name=first_name
        user.last_name=last_name
        user.is_active=True
        user.set_password(raw_password=password1)
        user.save()
        return Response({"Success":"User has been created"})
    except:
         return Response({"Error":"Something went wrong"})
