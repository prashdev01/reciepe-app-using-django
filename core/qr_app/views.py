# qr_app/views.py
from django.shortcuts import render,redirect
import qrcode
import os
from django.conf import settings

def qr_gen(request):
    if request.method == 'POST':
        url = request.POST.get('url')

        if not url:
            return render(request, 'qr_form.html', {'error': 'Please enter a URL.'})

        # Generate the QR code
        
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        
        # Create an image from the QR code
        img = qr.make_image(fill='black', back_color='white')

        # Define the path to save the image
        file_name = "qrcode.png"
        file_path = os.path.join(settings.MEDIA_ROOT, 'qr_codes', file_name)

        # Save the image
        if not os.path.exists(os.path.dirname(file_path)):
            os.makedirs(os.path.dirname(file_path))

        img.save(file_path)

        # Pass the file path to the template
        context = {
            'qr_code_image': os.path.join('media', 'qr_codes', file_name),
            'download_url': file_path,
        }

        return redirect( '/qr_gen/', context)

    return render(request, 'qr_gen.html')
