# 30. Login via django authentication form
# Import authenticationForm
# Here is the login_view in accounts.views.py
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username= username, password = password)
        if user is None:
            context = {"error": 'Invalid username or password.'}
            return render (request, 'accounts/login.html', context=context)
        login(request, user)
        return redirect('/')
    return render(request, 'accounts/login.html', {})

# Change the code like the following

def login_view(request):
    if request.method == 'POST':
        form = authenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user() #It's special for his particular form
            login(request, user)
            return redirect('/')
        else:
            form = authenticationForm(request)
        return render(request, 'accounts/login.html', {})

# Check! 
def login_view(request):
    if request.method == 'POST':
        form = authenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user() #It's special for his particular form
            login(request, user)
            return redirect('/')
        else:
            form = authenticationForm(request)
        context = {'form':form}
        return render(request, 'accounts/login.html', context =  context)
