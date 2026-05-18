class smartphone:
    def __init__(self , merk , model , ram):
        self .merk = merk
        self .model = model
        self .ram = ram

hp_reza = smartphone("oppo" , "oppo f1 pro" , "4gb")

hp_andi = smartphone("xiaomi" , " redmi 14 c" , "8gb")

print(f"smartphone 1  hp reza bermerk {hp_reza .merk} series {hp_reza .model} dan dengan penyimpanan {hp_reza .ram}")

print(f"smartphone 2  hp andi bermerk {hp_andi .merk} series {hp_andi .model} dan dengan penyimpanan {hp_andi .ram}")


    