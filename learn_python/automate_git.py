import os

main_dir = 'learn_language'
cwd = os.getcwd()

print(cwd)

for x in os.listdir(cwd)[1::]:
    if os.path.isdir(f"{cwd}/{x}"):
        os.chdir(f"{cwd}/{x}")
        os.system(f"git remote add {main_dir} {cwd[:-12]}")
        os.system(f"git fetch {x} --tags")
        os.system(f"git merge --allow-unrelated-histories {main_dir}/main")
        os.system(f"git remote remove {cwd}/{x}")
        os.chdir(f"{cwd}")