import shutil
import os


def generate_public_files(public_path, static_path):
    if os.path.exists(public_path):
        print(f"Removing files in {public_path} - {os.listdir(public_path)}")
        shutil.rmtree(public_path)
    os.mkdir(public_path)
    print(f"Creating dir {public_path}")

    copy_source_files(static_path, public_path)


def copy_source_files(source_path, target_path):
    dir = os.listdir(source_path)

    for item in dir:
        path = os.path.join(source_path, item)
        if os.path.isfile(path):
            shutil.copy(path, target_path)
            print(f"Copying files from {path} to {target_path}")
        elif os.path.isdir(path):
            new_path = os.path.join(target_path, item)
            os.mkdir(new_path)
            print(f"Creating dir {new_path}")
            copy_source_files(path, new_path)
