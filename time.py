import time

def focus_timer(work_minutes, break_minutes):
    while True:
        print(f"工作 {work_minutes} 分钟")
        time.sleep(work_minutes * 60)  # 将分钟转换为秒
        print("休息中...")
        time.sleep(break_minutes * 60)  # 将分钟转换为秒

if __name__ == "__main__":
    work_minutes = 25  # 设置工作时间为25分钟
    break_minutes = 5  # 设置休息时间为5分钟
    focus_timer(work_minutes, break_minutes)
