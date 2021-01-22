import os
path= '../../photos'
files = os.listdir(path)
files = [os.path.join(path, file) for file in files]
files = [file for file in files if os.path.isfile(file)]
print(max(files, key=os.path.getctime))
# print(open('../../data/users_ids.txt').read())