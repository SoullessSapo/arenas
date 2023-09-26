
import math


def can_pop_balloons(n, balloons):
    distances = [math.sqrt(x ** 2 + y ** 2) for x, y in balloons]
    balloons_sorted_by_distance = sorted(zip(balloons, distances), key=lambda x: x[1])

    for i in range(n):
        x1, y1 = balloons_sorted_by_distance[i][0]
        angle1 = math.atan2(y1, x1)

        balloons_sorted_by_angle = sorted(balloons_sorted_by_distance[i + 1:],
                                          key=lambda x: math.atan2(x[0][1], x[0][0]))

        for j in range(len(balloons_sorted_by_angle)):
            x2, y2 = balloons_sorted_by_angle[j][0]
            angle2 = math.atan2(y2, x2)

            remaining_balloons = balloons_sorted_by_angle[j + 1:]

            third_dart_needed = True
            for k in range(len(remaining_balloons)):
                x3, y3 = remaining_balloons[k][0]
                angle3 = math.atan2(y3, x3)
                if not (angle1 <= angle3 <= angle2):
                    third_dart_needed = False
                    break

            if not third_dart_needed:
                break
        if not third_dart_needed:
            break

    return "possible" if not third_dart_needed else "impossible"


# Read input
n = int(input())
balloons = []
for _ in range(n):
    x, y = map(int, input().split())
    balloons.append((x, y))

# Check if it's possible to pop all balloons
result = can_pop_balloons(n, balloons)
print(result)