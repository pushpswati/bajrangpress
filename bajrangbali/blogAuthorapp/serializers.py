from rest_framework import serializers
from blogAuthorapp.models import Blog,Author,Entry


class BlogSerializers(serializers.ModelSerializer):
    blogserialize=serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model=Blog
        fields='__all__'
        
class AuthorSerializers(serializers.ModelSerializer):
    authorserializer=serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model=Author
        fields='__all__'
        
        
        
class EntrySerializers(serializers.ModelSerializer):
    entryserializer=serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model=Entry
        fields='__all__'