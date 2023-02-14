def choose_coffee(*preference):
    global ingredients
    for pref in preference:
        if pref == 'Эспрессо':
            if ingredients[0] >= 1:
                ingredients[0] -= 1
                return pref
        if pref == 'Капучино':
            if ingredients[0] >= 1 and ingredients[1] >= 3:
                ingredients[0] -= 1
                ingredients[1] -= 3
                return pref
        if pref == 'Маккиато':
            if ingredients[0] >= 2 and ingredients[1] >= 1:
                ingredients[0] -= 2
                ingredients[1] -= 1
                return pref
        if pref == 'Кофе по-венски':
            if ingredients[0] >= 1 and ingredients[2] >= 2:
                ingredients[0] -= 1
                ingredients[2] -= 2
                return pref
        if pref == 'Латте Маккиато':
            if ingredients[0] >= 1 and ingredients[1] >= 2 and ingredients[2] >= 1:
                ingredients[0] -= 1
                ingredients[1] -= 2
                ingredients[2] -= 1
                return pref
        if pref == 'Кон Панна':
            if ingredients[0] >= 1 and ingredients[2] >= 1:
                ingredients[0] -= 1
                ingredients[2] -= 1
                return pref
    return 'К сожалению, не можем предложить Вам напиток'

ingredients = [9, 4, 5]
print(choose_coffee("Эспрессо", "Маккиато", "Латте Маккиато"))
print(choose_coffee("Кофе по-венски", "Эспрессо", "Кон Панна"))
print(choose_coffee("Кофе по-венски", "Эспрессо", "Кон Панна"))
print(choose_coffee("Кофе по-венски", "Эспрессо", "Кон Панна"))
print(choose_coffee("Латте Маккиато", "Капучино", "Маккиато", "Кофе по-венски"))
print(choose_coffee("Латте Маккиато", "Капучино", "Маккиато", "Кофе по-венски"))
print(choose_coffee("Латте Маккиато", "Капучино", "Маккиато", "Кофе по-венски"))
print(choose_coffee("Латте Маккиато", "Капучино", "Маккиато", "Кофе по-венски"))
