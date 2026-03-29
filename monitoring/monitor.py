import psutil
import time
import os

THRESHOLD = 75

def scale_to_gcp():
    print("Scaling triggered! Launching VM on GCP")

    command = "gcloud compute instances create autoscale-vm-3 --machine-type=e2-micro --image-family=ubuntu-2204-lts --image-project=ubuntu-os-cloud --metadata-from-file startup-script=startup.sh"

    os.system(command)

while True:
    cpu_usage = psutil.cpu_percent(interval=5)
    print(f"CPU Usage: {cpu_usage}%")

    if cpu_usage > THRESHOLD:
        print("CPU exceeded threshold!")
        scale_to_gcp()
        break

    time.sleep(5)