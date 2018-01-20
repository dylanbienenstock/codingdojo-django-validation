# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import User

def index(request):
	return render(request, "index.html")

def register(request):
	if request.method == "POST":
		response = User.objects.register(request.POST)

		if not response["success"]:
			return render(request, "index.html", response)

	return HttpResponse("<h1><a href='/'>Successful registration. Click me to go back</a></h1>")

def login(request):
	if request.method == "POST":
		response = User.objects.login(request.POST)

		if not response["success"]:
			return render(request, "index.html", response)

	return HttpResponse("<h1><a href='/'>Successful login. Click me to go back</a></h1>")