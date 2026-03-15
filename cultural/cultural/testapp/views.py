from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Yoga
from .forms import YogaForm, UserUpdateForm, CustomPasswordChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout


def user_register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("login")   # ✅ after signup → login page
    return render(request, "testapp/register.html", {"form": form})

# Home page
def home(request):
    return render(request, 'testapp/home.html')

# Yoga list
@login_required(login_url='login')
def yoga(request):
    yogas = Yoga.objects.all()
    return render(request, 'testapp/yoga.html', {'yogas': yogas})

# Meditation page
@login_required(login_url='login')
def meditation(request):
    return render(request, 'testapp/meditation.html')

# Festival page
@login_required(login_url='login')
def festival(request):
    return render(request, 'testapp/festival.html')

# Agriculture page
@login_required(login_url='login')
def agriculture(request):
    """Simple informational page about agriculture."""
    return render(request, 'testapp/agriculture.html')

# Food page
@login_required(login_url='login')
def food(request):
    """Simple informational page about cultural cuisine and food."""
    return render(request, 'testapp/food.html')

# Login
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # ✅ Correct login → open home page
            login(request, user)
            return redirect('home')
        else:
            # ❌ Wrong login → stay on login page
            return render(
                request,
                'testapp/login.html',
                {'error': 'Invalid username or password'}
            )

    # Normal GET request → open login page
    return render(request, 'testapp/login.html')
# Logout
def user_logout(request):
    logout(request)
    return redirect('home')

# Add yoga (login required)
@login_required
def add_yoga(request):
    form = YogaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('yoga')
    return render(request, 'testapp/add_yoga.html', {'form': form})

# Edit yoga
@login_required

@login_required(login_url='login')
def profile(request):
    """Display user profile information."""
    # the template can access the user via request.user
    return render(request, 'testapp/profile.html')


@login_required(login_url='login')
def edit_profile(request):
    """Allow the logged-in user to update their own details."""
    user = request.user
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=user)
    return render(request, 'testapp/profile_edit.html', {'form': form})


@login_required(login_url='login')
def change_password(request):
    """Let user change their password."""
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('profile')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'testapp/change_password.html', {'form': form})


@login_required(login_url='login')
def view_activity(request):
    """Display simple activity info for the user."""
    # expand later with real activity logs
    return render(request, 'testapp/activity.html')


# Edit yoga
@login_required
def edit_yoga(request, id):
    yoga = get_object_or_404(Yoga, id=id)
    form = YogaForm(request.POST or None, instance=yoga)
    if form.is_valid():
        form.save()
        return redirect('yoga')
    return render(request, 'testapp/edit_yoga.html', {'form': form})

def surya_detail(request):
    steps = [
        {"name": "Pranamasana", "desc": "Stand at the edge of your mat, feet together, palms joined.", "breath": "Exhale", "icon": "🧘", "color": "warning"},
        {"name": "Hastauttanasana", "desc": "Inhale, lift the arms up and back, keeping the biceps close to the ears.", "breath": "Inhale", "icon": "🙌", "color": "primary"},
        {"name": "Hastapadasana", "desc": "Exhale, bend forward from the waist, keeping the spine erect.", "breath": "Exhale", "icon": "🤸", "color": "danger"},
        {"name": "Ashwa Sanchalanasana", "desc": "Inhale, push your right leg back as far as possible. Look up.", "breath": "Inhale", "icon": "🏇", "color": "success"},
        {"name": "Dandasana", "desc": "Bring the left leg back. Keep the body in a straight line.", "breath": "Retain", "icon": "📏", "color": "info"},
        {"name": "Ashtanga Namaskara", "desc": "Gently bring knees, chest, and chin to the floor.", "breath": "Exhale", "icon": "🙇", "color": "secondary"},
        {"name": "Bhujangasana", "desc": "Slide forward and raise the chest into the Cobra pose.", "breath": "Inhale", "icon": "🐍", "color": "warning"},
        {"name": "Adho Mukha Svanasana", "desc": "Lift the hips and the tailbone up to form an 'V' pose.", "breath": "Exhale", "icon": "🐕", "color": "primary"},
        {"name": "Ashwa Sanchalanasana", "desc": "Inhale, bring the right foot forward between the two hands.", "breath": "Inhale", "icon": "🏇", "color": "success"},
        {"name": "Hastapadasana", "desc": "Exhale, bring the left foot forward. Keep palms on the floor.", "breath": "Exhale", "icon": "🤸", "color": "danger"},
        {"name": "Hastauttanasana", "desc": "Inhale, roll the spine up. Raise the hands and bend backward.", "breath": "Inhale", "icon": "🙌", "color": "warning"},
        {"name": "Tadasana", "desc": "Exhale, first straighten the body, then bring the arms down.", "breath": "Exhale", "icon": "🏔️", "color": "success"},
    ]
    # template file uses plural name
    return render(request, 'testapp/surya_details.html', {'steps': steps})