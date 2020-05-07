def DumbScoreFrame(frame):
    if 2 < len(frame):
        raise Exception("the frame is to long")
    result = 0
    for attempt in frame:
        result+=attempt
    return result

def IsStrike(frame):
    return 10 == frame[0]

def IsSpare(frame):
    if not IsStrike(frame):
        return 10 == frame[0] + frame[1]
    return False

def ScoreFrame(thisFrame, nextFrame, thirdFrame):
    if IsSpare(thisFrame):
        return 10 + nextFrame[0]
    if IsStrike(thisFrame):
        if 10 == nextFrame[0]:
            return 20 + thirdFrame[0]
        return 10 + nextFrame[0] + nextFrame[1]
    return DumbScoreFrame(thisFrame)

def ScoreFrameByIndex(index, frames):
    nextIndex = index + 1
    nextFrame = [0,0]
    thirdFrame = [0,0]
    thisFrame = frames[index]

    if nextIndex < 10:
        nextFrame = frames[nextIndex]
        thirdFrame = nextFrame
    else:
        nextFrame[0] = thisFrame[1]

    thirdIndex = nextIndex + 1
    if thirdIndex < len(frames):
        thirdFrame = frames[thirdIndex]
    else:
        if 3 == len(thisFrame):
            thirdFrame[0] = thisFrame[2]
    return ScoreFrame(thisFrame, nextFrame, thirdFrame)

def BowlingScore(frames):
    result = 0
    for i in range(10):
        result += ScoreFrameByIndex(i, frames)
    return result