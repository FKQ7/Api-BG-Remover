from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from io import BytesIO
from rembg import remove
import base64
from .models import ImageUpload

@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):

        image_upload, created = ImageUpload.objects.get_or_create(pk=1)
        
        image_upload.upload_count += 1
        image_upload.save()


        uploaded_image = request.FILES['image']
        input_image = Image.open(uploaded_image)
        output_image = remove(input_image)
        

        buffered_output = BytesIO()
        output_image.save(buffered_output, format="PNG")
        encoded_output = base64.b64encode(buffered_output.getvalue()).decode('utf-8')
        

        return JsonResponse({
            'image_data': encoded_output
        })
    else:
        return JsonResponse({'error': 'Image not uploaded'}, status=400)
