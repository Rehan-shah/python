class QuizBrain:
    def __init__(self,list):
        self.list = list
        self.current_idx = 0
        self.score = 0

    def still_has_question(self):
        if self.current_idx >= len(self.list):
            return False
        return True

    def next_question(self):
        self.current_idx += 1
        resp = input(f"Q.{self.current_idx}: {self.list[self.current_idx-1].text} (True/False)?: ")
        self.check_answer(resp,self.list[self.current_idx-1].answer )

    def check_answer(self, res,ans):
        if res.lower() == ans.lower():
            self.score += 1
            print("You got it right")
        else:
            print("You go it wrong")
        print(f"The correct ans : {ans}")
        print(f"Your score: {self.score}/{self.current_idx}")

