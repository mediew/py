print("---------------------")
print("  ",format("公斤","4s"),"|   ",format("磅","2s"))
for i in range(1,200,2):
        print("---------------------")
        kg=i
        po=i*2.2
        print("   ",format(kg,">3d"),"  |  ",format(po,">5.1f"),)
print("---------------------")
