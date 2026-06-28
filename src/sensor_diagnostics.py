import numpy as np


class SensorDiagnostics:
    def __init__(self, temperature_limit=75, vibration_limit=2.5, current_limit=12):
        self.temperature_limit = temperature_limit
        self.vibration_limit = vibration_limit
        self.current_limit = current_limit

    def generate_sensor_data(self, time_steps=120, seed=42):
        np.random.seed(seed)

        time = np.arange(time_steps)

        temperature = 45 + 0.08 * time + np.random.normal(0, 1.2, time_steps)
        vibration = 1.0 + np.random.normal(0, 0.15, time_steps)
        current = 8.0 + np.random.normal(0, 0.4, time_steps)

        anomaly_points = [45, 80, 105]

        for point in anomaly_points:
            temperature[point] += 25
            vibration[point] += 2.0
            current[point] += 5.0

        return {
            "time": time,
            "temperature": temperature,
            "vibration": vibration,
            "current": current,
        }

    def detect_anomalies(self, sensor_data):
        anomalies = []

        for index in range(len(sensor_data["time"])):
            temperature = sensor_data["temperature"][index]
            vibration = sensor_data["vibration"][index]
            current = sensor_data["current"][index]

            triggered_sensors = []

            if temperature > self.temperature_limit:
                triggered_sensors.append("temperature")

            if vibration > self.vibration_limit:
                triggered_sensors.append("vibration")

            if current > self.current_limit:
                triggered_sensors.append("current")

            if triggered_sensors:
                anomalies.append(
                    {
                        "time_step": int(sensor_data["time"][index]),
                        "temperature": round(float(temperature), 2),
                        "vibration": round(float(vibration), 2),
                        "current": round(float(current), 2),
                        "triggered_sensors": triggered_sensors,
                    }
                )

        return anomalies
