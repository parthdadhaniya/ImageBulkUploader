from django.shortcuts import render
from .models import Document
from django.contrib import messages

# Create your views here.


def index(request):
    try:
        if request.method == "POST":
            document_name = request.POST.get("document_name")
            document_file = request.FILES.getlist("document")
            documents_data = [
                Document(name=document_name, document=document)
                for document in document_file
            ]
            Document.objects.bulk_create(documents_data)
            messages.success(request, "Documents upload successfully")
        return render(request, "index.html")
    except Exception as e:
        print(e)
