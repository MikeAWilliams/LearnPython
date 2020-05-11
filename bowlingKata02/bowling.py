def IsStrike(frame):
    return 10 == frame[0]


def IsSpare(frame):
    return 10 == SumFrame(frame) and 10 != frame[0]


def ScoreStrikeFramesZeroToSeven(nextFrame, thirdFrame):
    if IsStrike(nextFrame):
        return 20 + thirdFrame[0]
    return 10 + nextFrame[0] + nextFrame[1]


def ScoreStrikeFrameEight(frameNine, notUsed):
    return 10 + frameNine[0] + frameNine[1]


def ScoreStrikeFrameNine(frameNine):
    return SumFrame(frameNine)


def ScoreSpareFramesZeroToEight(nextFrame):
    return 10 + nextFrame[0]


def SumFrame(frame):
    result = 0
    for bowl in frame:
        result += bowl
    return result


def ScoreFrameByFunction(thisFrame, nextFrame, thirdFrame, strikeFunction,
                         spareFunction):
    if IsStrike(thisFrame):
        return strikeFunction(nextFrame, thirdFrame)
    if IsSpare(thisFrame):
        return spareFunction(nextFrame)
    return SumFrame(thisFrame)


def ScoreFramesZeroToSeven(thisFrame, nextFrame, thirdFrame):
    return ScoreFrameByFunction(thisFrame, nextFrame, thirdFrame,
                                ScoreStrikeFramesZeroToSeven,
                                ScoreSpareFramesZeroToEight)


def ScoreFrameEight(frameEight, frameNine):
    return ScoreFrameByFunction(frameEight, frameNine, [0, 0],
                                ScoreStrikeFrameEight,
                                ScoreSpareFramesZeroToEight)


def ScoreFrameNine(frameNine):
    if IsStrike(frameNine):
        return ScoreStrikeFrameNine(frameNine)
    return SumFrame(frameNine)


def CalculateScore(frames):
    result = 0
    for index in range(8):
        result += ScoreFramesZeroToSeven(frames[index],
                                         frames[index + 1], frames[index + 2])

    result += ScoreFrameEight(frames[8], frames[9])
    result += ScoreFrameNine(frames[9])
    return result
