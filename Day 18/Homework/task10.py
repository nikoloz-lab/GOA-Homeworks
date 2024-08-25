#აიღეთ სამი სტრინგი და გააერთიანეთ ისინი ერთ წინადადებად. დაბეჭდეთ საბოლოო წინადადება.
 # აქ არის კიდევ 6 დავალება, რომლებიც ფოკუსირებულია შედარების ოპერატორებზე პირობითების გამოყენების გარეშე

yesterday_temp = int(input())
today_temp = int(input())
if today_temp > yesterday_temp:
    print("Today is warmer than yesterday.")
elif today_temp < yesterday_temp:
    print("Today is colder than yesterday.")
else:
    print("Today is the same temperature as yesterday.")