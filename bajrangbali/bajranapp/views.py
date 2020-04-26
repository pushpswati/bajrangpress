from django.shortcuts import render
import random
from django.http import HttpResponse
from bajranapp.serializers import UserProfileSerializers,CoronaTrackerSerializers,CountryviewsSerializers,GlobalCoronatracker_RecordviewsSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from bajranapp.models import UserProfile,CoronaTracker,GlobalCoronatracker_Record


class UserProfileListviews(APIView):
    """
    list all the users profile ,and create the user profile
    """
    def get(self,request,format=None):
        bajrangbali=UserProfile.objects.all()
        serializer = UserProfileSerializers(bajrangbali,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = UserProfileSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def index(request):
    return HttpResponse("Hello, world. You're at the bagranapp index.")



class Login_generate_otpviews(APIView):

   

    def post(self,request,format=None):
        contact = request.data.get('contact', None)
        if contact:
            try:
                usr=UserProfile.objects.get(contact=contact)
            except:
                usr=None
            if usr:
                #GENRATE OTP CODE and sent you mobile
                if contact:
                    otp = random.randrange(999,9999 )
                    return otp
                else:
                    return false
                
                #code
                
                # Save oTP in DB (Otp model calss)
                #code
                otp.save()
                
                return Response({'success': True,"otp":otp})
            else:
                return Response({'success': False})
        else:
            return Response({'Authorization error': False})

class Login_verify_otpviews(APIView):

    def post(self,request,format=None):
        contact = ...
        otp = request.data.get('otp', None)
        if contact and otp:
            try:
                user = User.objects.get(contact=contact, otp=otp)
            except User.DoesNotExist:
                 return Response({'message': 'Invalid OTP'})

            token = Token.objects.create(user=user)
            return Response({'token': token})
        else:
             return Response({'login failed': False})
        




class CoronaTrackerListviews(APIView):
    """
    list all the users profile ,and create the CoronaTracker
    """
    def get(self,request,format=None):
        bajrangbali=CoronaTracker.objects.order_by('-id')[0]
        serializer = CoronaTrackerSerializers(bajrangbali)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = CoronaTrackerSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
def index(request):
    return HttpResponse("Hello, world. You're at the bagranapp index...covid-19.")


class Countryviews(APIView):
    
    def get(self,request,format=None):
       
        countryview=CoronaTracker.objects.filter(lastUpdated__hour__gte=12)
       # for i in countryview[len(countryview)-16:]:
            #print(i.country,i.lastUpdated,i.totalConfirmed)
        serializer = CountryviewsSerializers(countryview[len(countryview)-16:],many=True)
        return Response(serializer.data)
    
class GlobalCoronatracker_Recordviews(APIView):
    """
    list of global corona patient record
    """
    def get(self,request,format=None):
        globaldata=GlobalCoronatracker_Record.objects.all()
        serializer=GlobalCoronatracker_RecordviewsSerializers(globaldata,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = GlobalCoronatracker_RecordviewsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)(data=request.data)
        
    
    
    
    
    
    
    
    
    
    
    
    
    


