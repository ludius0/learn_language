import os

a = ['calculator', 'Bitcoin-price-tracker', 'simple_time_program', 'login_system', 'simple_deep_learning', 'Chess-GUI', 'Conway-s-game-of-life', 'simple_hangman_game', 'CartPole_Gym', '2048-game', 'login_data', 'simple_database', 'pixel-painter', 'simulations', 'sorting_algorithm', 'face-recognition', 'Path-finding-algorithm-GUI', 'weather_app', 'sudoku-solver', 'Sorting-visualiser', 'snake']

main_dir = 'learn'
second_dir = 'learn_python'
path = "/Users/ludius/MEGAsync/CODES"

for i in a:
    os.chdir(f"{path}/{main_dir}/{second_dir}/{i}")
    os.system("rm -rf .git")