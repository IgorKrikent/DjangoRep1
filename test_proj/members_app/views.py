from django.shortcuts import render, redirect
from .my_forms import MyInputForm, MyConfirmForm


def input_page_view(request):

    if request.method == "POST":

        form = MyInputForm(request.POST)

        if form.is_valid():

            request.session['user_input'] = form.cleaned_data

        return redirect('show-data/')

    return render(request, 'input_page.HTML', {'form': MyInputForm})


def show_user_data_view(request):

    user_data = request.session.get('user_input', {})

    return render(request, 'display_page.HTML', {'user_data': user_data})


def game_view(request):

    if request.method == "POST":

        confirm = MyConfirmForm(request.POST)

        if confirm.is_valid():

            request.session['game']['try'] = confirm.cleaned_data['confirm']

        print(request.session['game'])

        if not request.session['game']['try'] == '3':

            if request.session['game']['try'] == '1':

                request.session['game']['interval']['max'] = request.session['game']['last_number']

            else:

                request.session['game']['interval']['min'] = request.session['game']['last_number']

            print(request.session['game'])

            number = round((request.session['game']['interval']['min'] +
                            request.session['game']['interval']['max'])/2)

            request.session['game']['last_number'] = number

            print(request.session['game'])

            return render(request, 'game.HTML',
                          {'number': number, 'confirm': MyConfirmForm})

    else:

        request.session['game'] = {'interval': {'min': 1, 'max': 100}, 'try': None, 'last_number': 1}

        print(request.session['game'])

        return render(request, 'game_init.HTML')

    return redirect('/show-data/')
