class Screen(object):
    @property
    def wh(self):
        return self.width
        return self.height
    @wh.setter
    def wh(self,width,height):
        if isinstance(width,int) and isinstance(height,int):
            self.width = width
            self.height = height
        else:
            raise ValueError('width or height must be an integer!')
    @property
    def resolution(self):
        return self.width * self.height

s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
