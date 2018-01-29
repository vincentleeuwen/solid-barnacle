

class BowlingGame(object):
    def __init__(self):
        self.frames = []

    def roll(self, pins):
        if pins < 0 or pins > 10:
            raise ValueError('Invalid score')
        if len(self.frames) % 2 == 1:
            if pins + self.frames[-1] > 10 and self.frames[-1] != 10:
                raise ValueError('Too high')

        if len(self.frames) == 20 and pins == 10:
            if self.frames[-1] == 10:
                pass
            elif self.frames[-2] + self.frames[-1] == 10:
                pass
            elif self.frames[-2] + self.frames[-1] == 20:
                pass
            else:
                raise ValueError('Too many items')
        elif len(self.frames) == 20:
            if self.frames[-2] + self.frames[-1] == 10:
                pass
            elif 10 in self.frames[-3:]:
                pass
            else:
                raise IndexError()

        self.frames.append(pins)

    def score(self):
        if len(self.frames) < 10:
            raise IndexError()
        elif len(self.frames) == 19:
            if self.frames[-1] == 10:
                raise IndexError()
        elif len(self.frames) == 20:
            if self.frames[-1] == 10 and self.frames[-2] == 10:
                raise IndexError()
            if self.frames[-1] + self.frames[-2] == 10:
                raise IndexError()

        score = 0
        frame_score = 0
        for index, frame in enumerate(self.frames):
            frame_score += frame
            if frame_score == 10 and index < len(self.frames) - 3:
                try:
                    frame_score += self.frames[index + 1]
                    if frame == 10:
                        # strike
                        frame_score += self.frames[index + 2]
                    score += frame_score
                    frame_score = 0
                except IndexError:
                    raise IndexError()

            if (index + 1) % 2 == 0 or (index + 1) == len(self.frames):
                score += frame_score
                frame_score = 0

        return score
