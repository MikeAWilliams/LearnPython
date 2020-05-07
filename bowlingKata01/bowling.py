def RequireSize(thisList, size):
    if size != len(thisList):
        raise Exception("the size of the list is wrong")

def ScoreSingleFrame(frame):
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

def ScoreFrameGeneral(thisFrame, nextFrame, thirdFrame, spareFunction, strikeFunction):
    if IsSpare(thisFrame):
        return spareFunction(thisFrame, nextFrame)
    if IsStrike(thisFrame):
        return strikeFunction(thisFrame, nextFrame, thirdFrame)
    return ScoreSingleFrame(thisFrame)

def ScoreSpareGeneral(thisFrame, nextFrame):
        return 10 + nextFrame[0]

def ScoreSpareFrameNine(thisFrame, nextFrame):
        return 10 + thisFrame[2]

def ScoreStrikeGeneral(thisFrame, nextFrame, thirdFrame):
    if 10 == nextFrame[0]:
        return 20 + thirdFrame[0]
    return 10 + nextFrame[0] + nextFrame[1]

def ScoreStrikeFrameEight(thisFrame, nextFrame, thirdFrame):
    return 10 + nextFrame[0] + nextFrame[1]

def ScoreStrikeFrameNine(thisFrame, nextFrame, thirdFrame):
    return ScoreSingleFrame(thisFrame)

def ScoreFrame(thisFrame, nextFrame, thirdFrame):
    RequireSize(thisFrame, 2)
    return ScoreFrameGeneral(thisFrame, nextFrame, thirdFrame, ScoreSpareGeneral, ScoreStrikeGeneral)

def ScoreFrameEight(thisFrame, nextFrame):
    RequireSize(thisFrame, 2)
    return ScoreFrameGeneral(thisFrame, nextFrame, [0, 0], ScoreSpareGeneral, ScoreStrikeFrameEight)

def ScoreFrameNine(thisFrame):
    RequireSize(thisFrame, 3)
    return ScoreFrameGeneral(thisFrame, [0, 0], [0, 0], ScoreSpareFrameNine, ScoreStrikeFrameNine)

def BowlingScore(frames):
    RequireSize(frames, 10)
    result = 0
    for i in range(8):
        result += ScoreFrame(frames[i], frames[i+ 1], frames[i+ 2])
    
    result += ScoreFrameEight(frames[8], frames[9])
    result += ScoreFrameNine(frames[9])
    return result