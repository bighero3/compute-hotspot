import subprocess
import os
import uuid

import paramiko


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


def execute_file_on_remote_machine(filepath, runtime, username, hostname):
    ssh = paramiko.SSHClient()
    key = paramiko.RSAKey.from_private_key_file(
        "/home/zacharyvincze/.ssh/id_rsa")
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=username, pkey=key)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(
        "python3.8 programhandler.py " + runtime + " " + filepath)
    result = []
    for line in iter(ssh_stdout.readline, ""):
        result.append(line)
    return result
