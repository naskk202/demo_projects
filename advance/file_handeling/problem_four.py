import os


def directory_traversal(cur_dir, all_files):

    for el in os.listdir(cur_dir):
        if os.path.isfile(el):
            ext = el.split(".")[-1]
            if ext not in all_files:
                all_files[ext] = []
            all_files[ext].append(os.path.join(cur_dir, el))
        if os.path.isdir(el):
            directory_traversal(el, all_files)



all_files = {}
directory_traversal(os.getcwd(), all_files)
for k, v in all_files.items():
    print(k)
    for el in v:
        print(f"---{el}")