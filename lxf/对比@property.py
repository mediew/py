class Screen(object):
    

    def wh(self,width,height):
        if isinstance(width,int) and isinstance(height,int):
            self.width = width
            self.height = height
        else:
            raise ValueError('width or height must be an integer!')

    def Resolution(self):
        self.resolution = self.width * self.height

s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
