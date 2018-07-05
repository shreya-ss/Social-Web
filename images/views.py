from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms importImageCreateForm

@login_required
def image_create(request):
	if request.method == 'POST':
		#form is sent
		form = ImageCreateForm(data=request.POST)
		if form.is_valid():
			#from data is valid
			cd = form.cleaned_data
			new_item = form.save(commit=False)

			#assign current user to the item
			new_item.user = request.user
			new_item.save()
			messages.success(request, 'Imae added successfully')

# Create your views here.
