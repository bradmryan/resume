from rest_framework import serializers
from .models import Resume

class ResumeSerializer(serializers.Serializer):
    firstname = serializers.CharField(max_length=255)
    middleinitial = serializers.CharField(max_length=5)
    lastname = serializers.CharField(max_length=255)
    label = serializers.CharField(max_length=255)
    picture = serializers.ImageField(max_length=50, allow_empty_file=True, allow_null=True)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=14)
    website = serializers.URLField()
    summary = serializers.CharField()
    address = serializers.CharField(max_length=255)
    postalcode = serializers.CharField(max_length=9)
    city = serializers.CharField(max_length=255)
    countrycode = serializers.CharField(max_length=2)
    region = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Resume.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.firstname = validated_data.get('firstname', instance.firstname)
        instance.middleinitial = validated_data.get('middleinitial', instance.middleinitial)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.label = validated_data.get('label', instance.label)
        instance.picture = validated_data.get('picture', instance.picture)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.website = validated_data.get('website', instance.website)
        instance.summary = validated_data.get('summary', instance.summary)
        instance.address = validated_data.get('address', instance.address)
        instance.postalcode = validated_data.get('postalcode', instance.postalcode)
        instance.city = validated_data.get('city', instance.city)
        instance.countrycode = validated_data.get('countrycode', instance.countrycode)
        instance.region = validated_data.get('region', instance.region)
        return instance
