# wordcloud用法
from wordcloud import WordCloud
import jieba


def readFile(path):
    with open(path, 'r', encoding = 'utf-8') as f:
        return f.read()
        

def splitWord(str):
    jieba.suggest_freq('华氏老方', tune = True)    # 添加防拆分词
    wordLst = jieba.lcut(str)
    wordStr = '  '.join(wordLst)
    return wordStr

    
def genWordCloud(str, savepath):
    wc_settings = {
        'font_path': 'STXIHEI.TTF',
        'width': 800,
        'height': 600,
        'background_color': 'white',
        'max_words': 100,
    }
    # max_words数值越大显示词语越多，低频词越小而难以看清
    wc = WordCloud(**wc_settings).generate(str)
    wc.to_file(savepath)


def main():
    path = '487.txt'
    str = readFile(path)
    str = splitWord(str)
    savepath = 'file.png'
    genWordCloud(str, savepath)


if __name__ == '__main__':
    main()
    
