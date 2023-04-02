import random
from time import sleep

import requests

class DeviceStateMachine:
    def __init__(self):
        self.states = ["start", "check_device", "delete_device", "insert_device", "modify_device"]
        self.current_state = "start"
        self.devices = [112, 358, 132, 134]
        self.current_device = None

    def run(self):
        while True:
            if self.current_state == "start":
                print("check_device...")
                self.current_device = random.choice(self.devices)
                self.current_state = "check_device"
            elif self.current_state == "check_device":
                url = f"http://fleet:8000/fleet/{self.current_device}"
                response = requests.get(url)
                print(response.status_code)
                if response.status_code == 200:
                    self.current_state = "delete_device"
                    print("go to delete_device...")
                else:
                    self.current_state = "insert_device"
                    print("go to insert_device...")
            elif self.current_state == "delete_device":
                url = f"http://fleet:8000/fleet/{self.current_device}"
                response = requests.delete(url)
                print("delete_device...")
                if response.status_code == 204:
                    self.current_state = "stop"
            elif self.current_state == "insert_device":
                url = "http://fleet:8000/fleet/"
                data = {"deviceid": self.current_device, "description": "new"}
                response = requests.post(url, data=data)
                if response.status_code == 201:
                    self.current_state = "modify_device"
            elif self.current_state == "modify_device":
                url = f"http://fleet:8000/fleet/{self.current_device}"
                data = {"deviceid": self.current_device, "description": "update"}
                response = requests.put(url, data=data)
                if response.status_code == 200:
                    self.current_state = "stop"
                    break
            elif self.current_state == "stop":
                break

if __name__ == "__main__":
    print("Waiting 5 seconds to let the server start...")
    sleep(5)
    while True:
        state_machine = DeviceStateMachine()
        state_machine.run()
        sleep(5)
