import os
from glob import iglob

root_dir = os.path.dirname(os.path.realpath(__file__))+"/**"

file_list = [f for f in iglob(root_dir, recursive=True) if os.path.isfile(f)&("."in f)]

print(list(set(map(lambda x:x.split(".")[-1],file_list))))
