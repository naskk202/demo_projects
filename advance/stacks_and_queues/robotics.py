from collections import deque


def from_time_to_seconds(time):
    hh, mm, ss = time
    return (hh * 3600) + (mm * 60) + ss


def from_sec_to_hours(time):
        time %= 24 * 3600
        hh = time // 3600
        mm = (time % 3600) // 60
        ss = (time % 3600) % 60
        return f"[{hh:02d}:{mm:02d}:{ss:02d}]"


class Robot:
    def __init__(self, name, time_processing):
        self.name = name
        self.time_processing = time_processing
        self.busy = 0


robots_input = input().split(";")
robots = []
for i in robots_input:
    robot_name, processing = i.split("-")
    robots.append(Robot(robot_name, int(processing)))

time_input = [int(i) for i in input().split(":")]
time = from_time_to_seconds(time_input)

collection = deque()
while True:
    item = input()
    if item == "End":
        break
    collection.append(item)

while collection:
    time += 1
    item = collection.popleft()
    found = False
    for robot in robots:
        if time >= robot.busy:
            robot.busy = time + robot.time_processing
            print(f"{robot.name} - {item} {from_sec_to_hours(time)}")
            found = True
            break
    if not found:
        collection.append(item)
