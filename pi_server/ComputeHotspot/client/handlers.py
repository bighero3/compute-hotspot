import subprocess
import os
import uuid

import paramiko


def handle_uploaded_file(f, user_id):
    file_path = "files/" + user_id + ".py"
    with open(file_path, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_path


def copy_file_to_remote_machine(filepath, user_id, username, hostname):
    ssh = paramiko.SSHClient()
    key = paramiko.RSAKey.from_private_key_file(
        "/home/zacharyvincze/.ssh/id_rsa")
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=username, pkey=key)
    ssh.exec_command(
        "mkdir files/" + user_id)
    subprocess.run(
        ["scp", filepath, username + "@" + hostname + ":" + "~/files/" + user_id + "/" + user_id + ".py"])
    os.remove(filepath)


def execute_file_on_remote_machine(user_id, runtime, username, hostname):
    ssh = paramiko.SSHClient()
    key = paramiko.RSAKey.from_private_key_file(
        "/home/zacharyvincze/.ssh/id_rsa")
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=username, pkey=key)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(
        "python3.8 programhandler.py " + runtime + " " + "files/" + user_id + "/" + user_id + ".py")
    result = []
    for line in iter(ssh_stdout.readline, ""):
        result.append(line)
    return result
