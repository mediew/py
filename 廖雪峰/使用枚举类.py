from enum import  Enum, unique

@unique

class Gender(Enum):

    Male=0

    Female=1

class Student:

    def __init__(self,name, gender):

        self.name=name

        self.gender=gender

    @property

    def gender(self):

        return self._gender

    @gender.setter

    def gender(self,gender):

        if isinstance (gender, Gender):

            self._gender=gender

        if isinstance(gender,int):

            if gender==0:

                self._gender=Gender.Male

            elif gender==1:

                self._gender=Gender.Female

            else:

                raise ValueError ("The value of gender can only be '0' or '1'!")


bart = Student('Bart', 0)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
