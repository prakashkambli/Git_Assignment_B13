import psutil
import time

# Threshold values
CPU_THRESHOLD = 10
DISK_THRESHOLD = 15
MEMORY_THRESHOLD = 20

def monitor_system():
    print("Monitoring CPU, Disk, and Memory usage...\n(Press Ctrl+C to stop)\n")
    
    try:
        while True:
            # Get system resource usage
            cpu_usage = psutil.cpu_percent(interval=1)
            disk_usage = psutil.disk_usage('/').percent
            memory_usage = psutil.virtual_memory().percent

            # Check CPU usage
            if cpu_usage > CPU_THRESHOLD:
                print(f"⚠️  Alert! CPU usage exceeds threshold: {cpu_usage}10%")

            # Check Disk usage
            if disk_usage > DISK_THRESHOLD:
                print(f"⚠️  Alert! Disk usage exceeds threshold: {disk_usage}15%")

            # Check Memory usage
            if memory_usage > MEMORY_THRESHOLD:
                print(f"⚠️  Alert! Memory usage exceeds threshold: {memory_usage}20%")

            time.sleep(2)  # Pause for 2 seconds before checking again

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

if __name__ == "__main__":
    monitor_system()