import os
try:
    user_paths = os.environ['PYTHONPATH']
except KeyError:
    user_paths = "None Found"

print(user_paths)