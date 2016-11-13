from django.shortcuts import render, redirect
from book.forms import LoginForm, bookEntryForm
from book.models import bookEntryModel
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import csv

def user_filter(user):
	return bookEntryModel.objects.filter(user=user)

# Create your views here.
def log_in(request):
	if not request.user.is_authenticated():
		if request.method == 'POST':
			form = LoginForm(request.POST)
			if form.is_valid():
				if form.get_user():
					login(request, form.get_user())
					return HttpResponseRedirect('/')
		else:
			form = LoginForm()
		return render(request, 'login.html', {'form': form})
	else:
		return HttpResponseRedirect('/')

def log_out(request):
	logout(request)
	return redirect('login')

@login_required(login_url='/login/')
def main_page_render(request):
	if request.user.is_authenticated():
		user = request.user.username
		entryAll = user_filter(user)
		form = bookEntryForm
		return render(request, "main.html", {'form': form, 'entryAll':entryAll})
	else:
		return redirect('login')

def submit(request):
	if request.method == 'POST':
		user = request.user.username
		book_user = bookEntryModel(user=user)
		entry = bookEntryForm(request.POST, instance=book_user)
		if entry.is_valid():
			entry.save()
	return redirect('/')

def remove(request):
	entry_num = request.GET['entry_num']
	if entry_num is not None:
		input_remove = bookEntryModel.objects.get(pk = entry_num)
		input_remove.delete()
		return redirect('/')
	else:
		return redirect('/')

@login_required(login_url='/login/')
def edit(request):
	entryAll = bookEntryModel.objects.all()
	entry_num = request.GET['entry_num']
	entry_edit = bookEntryModel.objects.get(pk = entry_num)
	if entry_num is not None:
		if request.method == 'POST':
			form = bookEntryForm(request.POST, instance=entry_edit)
			if form.is_valid():
				form.save()
				return redirect('/')
	form = bookEntryForm(instance=entry_edit)
	return render(request, 'edit.html', {'form': form, 'entryAll': entryAll, 'InputEdit': entry_edit, 'Input': entry_num})

@csrf_exempt
def make_csv(request):
	if request.is_ajax() and request.method == 'POST':
		global entryAll
		user = request.user.username
		entryAll = user_filter(user)

	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="address_book.csv"'

	writer = csv.writer(response)
	writer.writerow(['Name', 'Birth Date', 'Address', 'Phone', 'Email'])
	for i in entryAll:
		writer.writerow([i.name, i.birth_date, i.address, i.phone, i.email])

	return response