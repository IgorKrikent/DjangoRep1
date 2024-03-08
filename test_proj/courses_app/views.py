from django.shortcuts import render


def courses_authorize_view(request):

    is_user = request.session.get('user_input')

    return render(request, 'courses_authorize.HTML', {'is_user': is_user})
