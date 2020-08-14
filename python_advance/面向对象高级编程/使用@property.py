# 使用@property，把一个方法变成属性调用，这样既可以像访问属性一样赋值，又可以检查有效性

class Student():

    @property
    def score(self):
        return self._score

    @score.setter           # 定义setter方法为属性添加合法性检查
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError('Please input int value!')
        if score < 0 or score > 100:
            raise ValueError('Please input value between 0 & 100!')
        self._score = score

    @ property
    def grade(self):        # 只定义property，不定义setter表示此属性只读！
        if 0 <= self._score < 60:
            return '不及格'
        elif 60 <= self._score < 90:
            return '良好'
        else:
            return '优秀'


s = Student()
s.score = 90
print(s.score, s.grade)