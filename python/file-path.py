import os

print("This file: --> ", __file__)
dir_name = os.path.dirname(__file__)
print("This dir: --> ", dir_name)

abs_path = os.path.abspath(dir_name)
print("Abs path: --> ", abs_path)

