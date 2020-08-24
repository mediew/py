import ffmpy3
from multiprocessing import Pool


def main(name, link):
    ffmpy3.FFmpeg(inputs={link: None}, outputs={name: None}).run()


if __name__ == '__main__':
    name = './test.mp4'
    link = 'https://daqqzz.com/20200118/a187bf139b8fe6452130d28921c4b5cf.mp4/index.m3u8?ts=1598258626000&token=1ccf90cce80953842dc75a60f865a0ba'
    p = Pool(8)
    p.apply_async(main, args=(name, link))
    p.close()
    p.join()