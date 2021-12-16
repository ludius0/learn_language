import os

main_dir = 'learn_language'
second_dir = 'learn_python'
path = "/Users/ludius/MEGAsync/CODES"
#cwd = os.getcwd()
#print(cwd)

print(os.listdir(f"{path}/{main_dir}"))

for x in os.listdir(f"{path}/{main_dir}/{second_dir}"):
    if os.path.isdir(f"{path}/{main_dir}/{second_dir}/{x}"):
        #os.chdir(f"{path}/{main_dir}/{x}")
        os.system(f"git remote add {x} {path}/{main_dir}/{second_dir}/{x}")
        os.system(f"git fetch {x} --tags")
        os.system(f"git merge --allow-unrelated-histories {x}/main")
        #os.system(f"git remote remove {cwd}/{x}")
        #os.chdir(f"{path}/{main_dir}")