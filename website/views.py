from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AddRecordForm, SignUpForm
from .models import Record


def home(request):
    records = Record.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have been successfuly logged in!")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in, please try again!")
            return redirect('home')
    else:
        return render(request, "home.html", {"records": records})
        

def logout_user(request):
    logout(request)
    messages.success(request, "You have been successfully logged out!")

    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and Login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have been successfully registered! Welcome!")

            return redirect('home')

    else:
        form = SignUpForm()

        return render(request, "account/register.html", {"form": form})
    
    return render(request, "account/register.html", {"form": form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)

        return render(request, "record/record.html", {"record": customer_record})
    else:
        return redirect("login")


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_staff:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()

                messages.success(request, "Record has been successfully added! Congratulations!")
                return redirect("home")

        return render(request, "record/add-record.html", {"form": form})


def delete_redord(request, pk):
    delete_record = Record.objects.get(id=pk)
    delete_record.delete()

    messages.success(request, "Record has been successfully deleted! Congratulations!")
    return redirect("home")


def update_redord(request, pk):
    if request.user.is_staff:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()

            messages.success(request, "Record has been successfully updated! Congratulations!")
            return redirect("home")
        
        return render(request, "record/update.html", {"form": form})
    else:
        messages.success(request, "You must be Logged in...")
        return redirect("home")

