import matplotlib.pyplot as plt

from src.sensor_diagnostics import SensorDiagnostics


def plot_sensor_data(sensor_data, anomalies):
    time = sensor_data["time"]

    plt.figure()

    plt.plot(time, sensor_data["temperature"], label="Temperature")
    plt.plot(time, sensor_data["vibration"], label="Vibration")
    plt.plot(time, sensor_data["current"], label="Current")

    anomaly_times = [item["time_step"] for item in anomalies]

    for anomaly_time in anomaly_times:
        plt.axvline(anomaly_time, linestyle="--", alpha=0.5)

    plt.title("Actuator Sensor Diagnostics")
    plt.xlabel("Time Step")
    plt.ylabel("Sensor Reading")
    plt.grid(True)
    plt.legend()
    plt.show()


def main():
    diagnostics = SensorDiagnostics()

    sensor_data = diagnostics.generate_sensor_data()
    anomalies = diagnostics.detect_anomalies(sensor_data)

    print("Detected anomalies:")
    print("-------------------")

    for anomaly in anomalies:
        print(anomaly)

    plot_sensor_data(sensor_data, anomalies)


if __name__ == "__main__":
    main()
