import random as rand

def bowling_random_game():
    result = []

    for frame in range(1, 11):

        # 1~9 프레임
        if frame < 10:
            if rand.random() < 0.3:
                result.append(10)
            else:
                first = rand.randint(0, 9)
                second = rand.randint(0, 10 - first)

                result.append(first)
                result.append(second)

        # 10 프레임
        else:
            first = rand.randint(0, 10)
            result.append(first)

            if first == 10:
                second = rand.randint(0, 10)
                result.append(second)

                if second == 10:
                    third = rand.randint(0, 10)
                else:
                    third = rand.randint(0, 10 - second)

                result.append(third)

            else:
                second = rand.randint(0, 10 - first)
                result.append(second)

                if first + second == 10:
                    third = rand.randint(0, 10)
                    result.append(third)

    return result


# 점수 계산
def score_bowling_random_game(result):
    score = 0
    i = 0
    frame_scores = []

    for frame in range(10):
        # 스트라이크
        if result[i] == 10:
            score = score + 10 + result[i+1] + result[i+2]
            frame_scores.append(score)
            i = i + 1

        # 스페어
        elif result[i] + result[i+1] == 10:
            score += 10 + result[i+2]
            frame_scores.append(score)
            i = i + 2

        # 오픈
        else:
            score += result[i] + result[i+1]
            frame_scores.append(score)
            i = i + 2

    return frame_scores

