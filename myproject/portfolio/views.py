from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        
        subject = f"Portfolio Contact from {name}"
        email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        
        try:
            send_mail(
                subject,
                email_message,
                email,  
                ['joelsalazarqt@gmail.com'],  
                fail_silently=False,
            )
            messages.success(request, "Thank you for contacting me! Your message has been sent successfully.")
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")

        return redirect("portfolio:index")

    return render(request, "pages/portfolio.html")
