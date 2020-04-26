from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    username =models.CharField(max_length=200,blank=True)
    email =models.CharField(max_length=200,blank=True)
    address =models.CharField(max_length=300,blank=True)
    contact =models.CharField(max_length=30,blank=True)
    
    
    
    def _str_(self):
        return self.user.username
    
class Otpgenrate(models.Model):
    otp =models.CharField(max_length=100,blank=True)
      
class CoronaTracker(models.Model):
    countryCode =models.CharField(max_length=100,blank=True)
    country =models.CharField(max_length=200,blank=True)
    lat =models.FloatField()
    lng =models.FloatField()
    totalConfirmed =models.IntegerField()
    totalDeaths =models.IntegerField()
    totalRecovered =models.IntegerField()
    dailyConfirmed =models.IntegerField()
    dailyDeaths =models.IntegerField()
    activeCases =models.IntegerField()
    totalCritical =models.IntegerField()
    totalConfirmedPerMillionPopulation =models.IntegerField()
    totalDeathsPerMillionPopulation =models.IntegerField()
    FR =models.FloatField()
    PR =models.FloatField()
    lastUpdated =models.DateTimeField(auto_now_add=True)

class GlobalCoronatracker_Record(models.Model):
    totalConfirmed =models.IntegerField()
    totalDeaths =models.IntegerField()
    totalRecovered =models.IntegerField()
    totalNewCases =models.IntegerField()
    totalNewDeaths =models.IntegerField()
    totalActiveCases =models.IntegerField()
    totalCasesPerMillionPop =models.IntegerField()
    created =models.DateTimeField(auto_now_add=True)
    
class GlobalCtracker_Record(models.Model):
    totalConfirmed =models.IntegerField()
    totalDeaths =models.IntegerField()
    totalRecovered =models.IntegerField()
    totalNewCases =models.IntegerField()
    totalNewDeaths =models.IntegerField()
    totalActiveCases =models.IntegerField()
    totalCasesPerMillionPop =models.IntegerField()
    created =models.DateTimeField(auto_now_add=True)
    