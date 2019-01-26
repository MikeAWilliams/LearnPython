class HighScores(object):
    def __init__(self, scores):
        self.scores = scores
        self.sorted_scores = None

    def __set_sorted_scores(self):
        self.sorted_scores = self.scores.copy()
        self.sorted_scores.sort(reverse = True)
        self.sorted_scores = self.sorted_scores[:3]

    def latest(self):
        if len(self.scores) == 0:
            return 0

        return self.scores[-1]
    
    def personal_best(self):
        if None == self.sorted_scores:
            self.__set_sorted_scores()

        if len(self.sorted_scores) == 0:
            return 0
        
        return self.sorted_scores[0]

    def personal_top(self):
        if None == self.sorted_scores:
            self.__set_sorted_scores()

        return self.sorted_scores

    def report(self):
        newest = self.latest()
        pbdif = self.personal_best() - newest
        message = str.format("That's {} short of your personal best!", pbdif)
        if 0 == pbdif:
            message = "That's your personal best!"
        
        return str.format("Your latest score was {}. {}", newest, message)
