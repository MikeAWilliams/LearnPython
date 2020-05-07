def DumbScoreFrame(frame):
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

def RequireSize(thisFrame, size):
    if size != len(thisFrame):
        raise Exception("the frame is to long")

def ScoreFrame(thisFrame, nextFrame, thirdFrame):
    RequireSize(thisFrame, 2)

    if IsSpare(thisFrame):
        return 10 + nextFrame[0]
    if IsStrike(thisFrame):
        if 10 == nextFrame[0]:
            return 20 + thirdFrame[0]
        return 10 + nextFrame[0] + nextFrame[1]
    return DumbScoreFrame(thisFrame)

def ScoreFrameEight(frames):
    thisFrame = frames[8]
    RequireSize(thisFrame, 2)

    nextFrame = frames[9]
    if IsSpare(thisFrame):
        return 10 + nextFrame[0]
    if IsStrike(thisFrame):
        return 10 + nextFrame[0] + nextFrame[1]
    return DumbScoreFrame(thisFrame)

def ScoreFrameNine(frames):
    thisFrame = frames[9]
    RequireSize(thisFrame, 3)

    if IsSpare(thisFrame):
        return 10 + thisFrame[2]
    if IsStrike(thisFrame):
        return 10 + thisFrame[1] + thisFrame[2]
    return DumbScoreFrame(thisFrame)

def BowlingScore(frames):
    result = 0
    for i in range(8):
        result += ScoreFrame(frames[i], frames[i+ 1], frames[i+ 2])
    
    result += ScoreFrameEight(frames)
    result += ScoreFrameNine(frames)
    return result