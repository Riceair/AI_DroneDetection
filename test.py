# 給你一塊矩形土地的長寬，再依序給定每個機器人的初始位置狀況及一連串的指令集，你必須用你的程式求出每個機器人最後的位置狀況，並且判斷是否有機器人掉出土地外。
def main():
    print("Hello World!")
    # 土地的長寬
    land_width, land_height = map(int, input().split())
    # 機器人數量
    robot_count = int(input())
    # 機器人的初始位置狀況及一連串的指令集
    robot_list = []
    for _ in range(robot_count):
        x, y, direction, command = input().split()
        robot_list.append({
            'x': int(x),
            'y': int(y),
            'direction': direction,
            'command': command
        })
    # 計算每個機器人最後的位置狀況
    for robot in robot_list:
        for command in robot['command']:
            if command == 'F':
                if robot['direction'] == 'N':
                    robot['y'] += 1
                elif robot['direction'] == 'E':
                    robot['x'] += 1
                elif robot['direction'] == 'S':
                    robot['y'] -= 1
                elif robot['direction'] == 'W':
                    robot['x'] -= 1
            elif command == 'B':
                if robot['direction'] == 'N':
                    robot['y'] -= 1
                elif robot['direction'] == 'E':
                    robot['x'] -= 1
                elif robot['direction'] == 'S':
                    robot['y'] += 1
                elif robot['direction'] == 'W':
                    robot['x'] += 1
            elif command == 'L':
                if robot['direction'] == 'N':
                    robot['direction'] = 'W'
                elif robot['direction'] == 'E':
                    robot['direction'] = 'N'
                elif robot['direction'] == 'S':
                    robot['direction'] = 'E'
                elif robot['direction'] == 'W':
                    robot['direction'] = 'S'
            elif command == 'R':
                if robot['direction'] == 'N':
                    robot['direction'] = 'E'
                elif robot['direction'] == 'E':
                    robot['direction'] = 'S'
                elif robot['direction'] == 'S':
                    robot['direction'] = 'W'
                elif robot['direction'] == 'W':
                    robot['direction'] = 'N'
        # 判斷是否有機器人掉出土地外
        if robot['x'] < 0 or robot['x'] > land_width or robot['y'] < 0 or robot['y'] > land_height:
            print('Robot {} crashes into the wall'.format(robot_list.index(robot) + 1))
            return
        for other_robot in robot_list:
            if robot != other_robot and robot['x'] == other_robot['x'] and robot['y'] == other_robot['y']:
                print('Robot {} crashes into robot {}'.format(robot_list.index(robot) + 1, robot_list.index(other_robot) + 1))
                return

if __name__ == '__main__':
    main()