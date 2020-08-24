import ffmpy3


name = './test.mp4'
link = 'https://daqqzz.com/20200527/eec17eb73eba3ee8cf227271a89c4f6c.mp4/index.m3u8?ts=1598248865000&token=74332d603a40447ab8e78387db50eb55'
ffmpy3.FFmpeg(inputs={link: None}, outputs={name:None}).run()