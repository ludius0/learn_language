import os

main_dir = 'learn_language'
cwd = os.getcwd()

print(cwd)

for x in os.listdir(cwd)[1::]:
    if os.path.isdir(f"{cwd}/{x}"):
        os.chdir(f"{cwd}/{x}")
        os.system(f"git remote add {x} {cwd}/{x}")
        os.system(f"git fetch {x} --tags")
        os.system(f"git merge --allow-unrelated-histories {x}/main")
        os.system(f"git remote remove {cwd}/{x}")
        os.chdir(f"{cwd}")

a = ['calculator', 'Bitcoin-price-tracker', 'simple_time_program', 'login_system', 'simple_deep_learning', 'Chess-GUI', 'Conway-s-game-of-life', 'simple_hangman_game', 'CartPole_Gym', '2048-game', 'login_data', 'simple_database', 'pixel-painter', 'simulations', 'sorting_algorithm', 'face-recognition', 'Path-finding-algorithm-GUI', 'weather_app', 'automate_git.py', 'sudoku-solver', 'Sorting-visualiser', 'snake']