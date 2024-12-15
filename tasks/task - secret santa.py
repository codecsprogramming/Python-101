# 5 nefer
# Heresi ucun 1 nefer sec
import random
sinif = {
        "Nuraya": None,
        "Gunel": None,
        "Nicat": None,
        "Amiray": None,
        "Ismayil": None,
        "Nasiba": None
}
def run():
    adlar = list(sinif.keys())
    for adam in sinif.keys():
        alacagi_adam = random.choice(adlar)
        while alacagi_adam == adam:
            if len(adlar) == 1 and adlar[0] == adam:
                raise Exception("Infinite loop")
            alacagi_adam = random.choice(adlar)
        adlar.remove(alacagi_adam)
        sinif[adam] = alacagi_adam

while True:
    try:
        run()
        for adam, alacagi_adam in sinif.items():
            print(f"{adam} hediye alir -> {alacagi_adam}")
        break
    except:
        run()