import psutil
import time
import os

THRESHOLD_UP = 75
THRESHOLD_DOWN = 30

vm_created = False

def scale_up():
    print("Scaling UP → Launching VM")
    os.system("gcloud compute instances create autoscale-vm-3 --machine-type=e2-micro --image-family=ubuntu-2204-lts --image-project=ubuntu-os-cloud --metadata-from-file startup-script=startup.sh")

def scale_down():
    print("Scaling DOWN → Deleting VM")
    os.system("gcloud compute instances delete autoscale-vm-3 --zone=asia-south1-a --quiet")

while True:
    cpu = psutil.cpu_percent(interval=5)
    print(f"CPU Usage: {cpu}%")

    if cpu > THRESHOLD_UP and not vm_created:
        scale_up()
        vm_created = True

    elif cpu < THRESHOLD_DOWN and vm_created:
        scale_down()
        vm_created = False

    time.sleep(5)