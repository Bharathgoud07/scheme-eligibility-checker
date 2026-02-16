from django.shortcuts import render, redirect
from .models import Document, UserDocument
from collections import defaultdict


def documents_form(request):

    profile_id = request.session.get('profile_id')
    if not profile_id:
        return redirect('/profile/')

    documents = Document.objects.exclude(category__isnull=True).order_by('category', 'name')

    grouped_docs = defaultdict(list)

    for doc in documents:
        grouped_docs[doc.category].append(doc)

    if request.method == 'POST':
        UserDocument.objects.filter(profile_id=profile_id).delete()

        for doc in documents:
            if str(doc.id) in request.POST:
                UserDocument.objects.create(
                    profile_id=profile_id,
                    document=doc
                )

        return redirect('/eligibility/results/')

    return render(request, "documents/documents.html", {
        "grouped_docs": dict(grouped_docs)   # IMPORTANT
    })
