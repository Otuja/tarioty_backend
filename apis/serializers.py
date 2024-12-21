import base64
from rest_framework import serializers
from .models import Media

class MediaSerializer(serializers.ModelSerializer):
    file_content = serializers.FileField(write_only=True)  # We will handle this manually
    file_representation = serializers.SerializerMethodField(read_only=True)  # For output representation


    class Meta:
        model = Media
        fields = ['id', 'title', 'description', 'file_content', 'file_representation', 'media_type', 'is_tarioty_original', 'uploaded_at']

    # to receive file as media upload from user
    def create(self, validated_data):
        # Convert base64 file content to binary data
        uploaded_file = validated_data.pop('file_content')  # Extract the uploaded file
        file_content_binary = uploaded_file.read()
        
        # Create the Media instance
        media = Media.objects.create(file_content=file_content_binary, **validated_data)
        return media


    # to process the file in a representatble format
    def get_file_representation(self, obj):
        if obj.file_content:
            # Convert binary data to base64 and create a data URL
            base64_content = base64.b64encode(obj.file_content).decode('utf-8')
            media_type = 'image/jpeg' if obj.media_type == 'image' else 'video/mp4'  # Adjust based on file type
            return f"data:{media_type};base64,{base64_content}"
        return None