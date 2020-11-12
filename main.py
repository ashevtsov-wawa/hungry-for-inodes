import math
import os
import uuid


def create_dirs(base_dir: str, recurse: bool):
    for i in range(0, 256):
        child_dir = '{0:0{1}x}'.format(i, 2)
        dir_path = os.path.join(base_dir, child_dir)
        try:
            os.mkdir(dir_path)
        except FileExistsError:
            print(f'{dir_path} directory already exists')
        if recurse:
            # Do not print out child directories to speed up execution
            print(f'Creating child directories in {dir_path} directory')
            create_dirs(dir_path, False)


def create_dummy_files(base_dir: str, max_files: int):
    # Pre-create directories to avoid checking whether they exist inside the infinite loop
    try:
        os.mkdir(base_dir)
    except FileExistsError:
        print(f'{base_dir} directory already exists')
    create_dirs(base_dir, True)

    i = 0
    progress_increment = math.ceil(max_files/500)
    while i < max_files:
        unique_id = str(uuid.uuid4())
        top_dir = unique_id[0:2]
        child_dir = unique_id[2:4]
        filepath = os.path.join(base_dir, top_dir, child_dir, unique_id)
        # Print out every hundred's file to speed up execution
        if i % progress_increment == 0:
            print(f'Creating {filepath} file - {i}')
        with open(filepath, 'w') as fd:
            fd.write(unique_id)
        i += 1


if __name__ == '__main__':
    create_dummy_files(os.environ.get('BASE_DIR', 'tmp'), int(os.environ.get('MAX_FILES', '100')))
