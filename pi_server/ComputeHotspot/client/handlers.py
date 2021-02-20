import uuid
import subprocess
import os


def handle_uploaded_file(f):
    file_path = "files/" + str(uuid.uuid4()) + ".py"
    with open(file_path, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_path


def copy_file_to_remote_machine(filepath, remote_filepath, hostname):
    subprocess.run(
        ["scp", filepath, hostname + ":" + remote_filepath])
    os.remove(filepath)
