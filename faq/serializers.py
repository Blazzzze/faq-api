from rest_framework import serializers
from faq.models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    """
    Serializer class for the FAQ model.

    This serializer is used to convert FAQ model instances into JSON format and vice versa.
    It automatically includes all fields from the FAQ model in the serialized output.
    """
    class Meta:
        # Specify the model that this serializer works with
        model = FAQ
        
        # Include all fields from the FAQ model in the serialized output
        fields = "__all__"
