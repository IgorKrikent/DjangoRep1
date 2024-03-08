from django.urls import path
from .views import input_page_view, show_user_data_view, game_view

urlpatterns = [
    path('', input_page_view, name='user_input'),
    path('show-data/', show_user_data_view, name='show_data'),
    path('game-init/', game_view, name='game'),
    path('play-game/', game_view, name='play_game')
]
