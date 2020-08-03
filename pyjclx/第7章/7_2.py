from stock import stock
def test():
        symbol='INTC'
        name='Intel Corporation'
        pcp=20.5
        cp=20.35
        s1=stock(symbol,name,pcp,cp)
        print(s1.getChangePercent())
test()
