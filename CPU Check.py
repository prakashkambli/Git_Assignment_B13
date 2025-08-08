import psutil

def monitor_cpu(threshold=80.0, interval=1):
    """Optimized CPU monitor with configurable parameters"""
    print(f"CPU Monitor (threshold: {threshold}%) - Press Ctrl+C to stop\n")
    
    try:
        # Pre-calculate format string for efficiency
        fmt = "CPU: {:5.1f}% {}"
        alert_msg = "⚠️ ALERT!"
        normal_msg = "✅ OK   "
        
        while True:
            usage = psutil.cpu_percent(interval)
            msg = alert_msg if usage > threshold else normal_msg
            print(fmt.format(usage, msg))
            
    except KeyboardInterrupt:
        print("\n🛑 Stopped")
    except Exception as e:
        print(f"❌ {e}")

if __name__ == "__main__":
    monitor_cpu()