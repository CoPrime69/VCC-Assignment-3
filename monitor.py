import psutil
import time
import os

THRESHOLD_UP = 75
THRESHOLD_DOWN = 30

VM_NAME = "autoscale-vm-3"
ZONE = "asia-south1-a"

vm_created = False

def scale_up():
    print("Scaling UP → Launching VM")
    os.system(f"""
    gcloud compute instances create {VM_NAME} \
    --machine-type=e2-micro \
    --image-family=ubuntu-2204-lts \
    --image-project=ubuntu-os-cloud \
    --zone={ZONE} \
    --tags=http-server \
    --metadata-from-file startup-script=startup.sh
    """)

def scale_down():
    print("Scaling DOWN → Deleting VM")
    os.system(f"""
    gcloud compute instances delete {VM_NAME} \
    --zone={ZONE} \
    --quiet
    """)

while True:
    cpu = psutil.cpu_percent(interval=5)
    print(f"CPU Usage: {cpu}%")

    if cpu > THRESHOLD_UP and not vm_created:
        scale_up()
        vm_created = True
        time.sleep(30)  # wait for VM creation

    elif cpu < THRESHOLD_DOWN and vm_created:
        scale_down()
        vm_created = False
        time.sleep(20)  # avoid rapid delete/recreate

    time.sleep(5)