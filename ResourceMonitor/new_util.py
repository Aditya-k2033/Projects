import psutil
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk


def monitor_resources(interval=1, duration=60):
    # Initialize lists to store data for plotting
    time_points = []
    cpu_usage = []
    memory_usage = []
    disk_usage = []

    start_time = time.time()
    end_time = start_time + duration

    root = tk.Tk()
    root.title('Resource Monitor')

    fig, ax = plt.subplots(figsize=(10, 6))
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    while time.time() < end_time:
        # Get CPU usage
        cpu_percent = psutil.cpu_percent(interval=interval)

        # Get memory usage
        memory_info = psutil.virtual_memory()

        # Get disk usage
        disk_info = psutil.disk_usage('/')

        # Store data for plotting
        time_points.append(time.time() - start_time)
        cpu_usage.append(cpu_percent)
        memory_usage.append(memory_info.percent)
        disk_usage.append(disk_info.percent)

        # Print the resource usage
        print(f"Time: {time.time() - start_time:.1f}s")
        print(f"CPU Usage: {cpu_percent}%")
        print(f"Memory Usage: {memory_info.percent}%")
        print(f"Disk Usage: {disk_info.percent}%")

        ax.clear()
        ax.plot(time_points, cpu_usage, label='CPU Usage', marker='o')
        ax.plot(time_points, memory_usage, label='Memory Usage', marker='o')
        ax.plot(time_points, disk_usage, label='Disk Usage', marker='o')
        ax.set_xlabel('Time (s)')
        ax.set_ylabel('Usage (%)')
        ax.set_title('Resource Usage Over Time')
        ax.legend()
        ax.grid()

        canvas.draw()
        root.update()

        time.sleep(interval)

    root.mainloop()


if __name__ == "__main__":
    monitor_resources()
