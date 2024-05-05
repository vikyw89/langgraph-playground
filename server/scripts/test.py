def run():
    import subprocess

    subprocess.run(args="pytest -vv --ff -x", shell=True)