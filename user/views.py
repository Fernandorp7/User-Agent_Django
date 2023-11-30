from django.shortcuts import render
from django_user_agents.utils import get_user_agent


def index(request):
    return render(request, 'user/index.html', {})


def info(request):
    user_agent = get_user_agent(request)
    return render(request, 'user/info.html', {'user_agent': user_agent})


def sobreMi(request):
    user_agent = get_user_agent(request)
    data = ""
    host = request.META.get("HTTP_HOST")
    ip = request.META.get('REMOTE_ADDR')
    tactil = "No táctil"

    if user_agent.is_mobile:
        data = "Móvil"
        if user_agent.is_touch_capable:
            tactil = "Táctil"
    elif user_agent.is_tablet:
        data = "Tablet"
        tactil = "Táctil"
    elif user_agent.is_pc:
        data = "PC"
    elif user_agent.is_bot:
        data = "BOT"

    return render(request, 'user/sobreMi.html', {'data': data, 'host': host, 'ip': ip, 'tactil': tactil})
