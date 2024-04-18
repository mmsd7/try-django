# 29. Register a user via built-in model form
# In accounts.views.py impoft UserCreationForm

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj= form.save()
        return redirect('/login')
    context['form'] = {'form': form}

    return render (request, 'accounts/register.html', context = context)



# Add url

# remote the register_view functio

# Is the user already registerd
# Create the register.html like below
{% extends 'base.html' %}


{% block content %}

{% if request.user.is_authenticated %}
<div>
    <form action="" method="POST"> {% csrf_token %}
        {{ form.as_p }}
        <p>Already have an account? Please <a href="/login"> login </a></p>
        <button type="submit">Yes, Log out.</button>
    </form>


</div>
{% else %}
    <p> You are already logged in. Would you like to <a href="/logout/"> logout? </a> </p>
{% endif %}


{% endblock content %}


# Change the login.html like below
{% extends 'base.html' %}


{% block content %}

{% if not request.user.is_authenticated %}
<div>
    <form action="" method="POST"> {% csrf_token %}
        {% if error %}
            <p style="color: red;">{{ error }}</p>
        {% endif %}

        <input type="text" name="username" placeholder="username">
        <input type="password" name="password">
        <button type="submit">Login</button>
        
        
        
    </form>

    <p>Need an account? Please <a href="/register"></a> Register</a></p>

</div>
{% else %}
    <p> You are already logged in. Would you like to <a href="/logout/"> logout? </a> </p>
{% endif %}


{% endblock content %}




