lower_cyrillic = ''.join(map(chr, range(ord('а'), ord('я') + 1)))
upper_cyrillic = ''.join(map(chr, range(ord('А'), ord('Я') + 1)))

def alphabet(shift):
    return lower_cyrillic[shift:] + \
           lower_cyrillic[:shift] + \
           upper_cyrillic[shift:] + \
           upper_cyrillic[:shift] 
     
def coding(typ="enc",shift=3):
    a1 = lower_cyrillic + upper_cyrillic
    a2 = alphabet(shift)
    
    t = {
        "enc":str.maketrans(a1,a2),
        "dec":str.maketrans(a2,a1)
        }
        
    return t[typ]     
        
print("Да здравствует салат Цезарь!".translate(coding("enc")))
print("Зг кзугефхецих фгогх Щикгуя!".translate(coding("dec")))
#Зг кзугефхецих фгогх Щикгуя!
#Да здравствует салат Цезарь!