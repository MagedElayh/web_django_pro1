from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import DoctorBook
from .forms import DoctorBookForm


def doctor_list(request):
    books = DoctorBook.objects.all()
    return render(request, 'doctor/book_list.html', {'books': books})


def save_doctor_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            books = Book.objects.all()
            data['html_book_list'] = render_to_string('doctor/includes/partial_book_list.html', {
                'books': books
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def doctor_create(request):
    if request.method == 'POST':
        form = DoctorBookForm(request.POST)
    else:
        form = DoctorBookForm()
    return save_book_form(request, form, 'doctor/includes/partial_book_create.html')


def doctor_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = DoctorBookForm(request.POST, instance=book)
    else:
        form = DoctorBookForm(instance=book)
    return save_book_form(request, form, 'doctor/includes/partial_book_update.html')


def doctor_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    data = dict()
    if request.method == 'POST':
        book.delete()
        data['form_is_valid'] = True
        books = DoctorBookBook.objects.all()
        data['html_book_list'] = render_to_string('doctor/includes/partial_book_list.html', {
            'books': books
        })
    else:
        context = {'book': book}
        data['html_form'] = render_to_string('doctor/includes/partial_book_delete.html', context, request=request)
    return JsonResponse(data)
