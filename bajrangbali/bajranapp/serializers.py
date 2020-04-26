from rest_framework import serializers
from bajranapp.models import UserProfile,CoronaTracker,GlobalCoronatracker_Record

class UserProfileSerializers(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model=UserProfile
        fields='__all__'
        
class Login_generate_otpSerializers(serializers.ModelSerializer):
    login=serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model=UserProfile
        fields='__all__'
        
class Login_verify_otpSerializers(serializers.ModelSerializer):
    login=serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model=UserProfile
        fields='__all__'
        
class CoronaTrackerSerializers(serializers.ModelSerializer):
    coronatracker=serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model=CoronaTracker
        fields='__all__'
        
class CountryviewsSerializers(serializers.ModelSerializer):
    countryviews=serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model=CoronaTracker
        fields='__all__'
        
class GlobalCoronatracker_RecordviewsSerializers(serializers.ModelSerializer):
    globaldata=serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model=GlobalCoronatracker_Record
        fields='__all__'
        