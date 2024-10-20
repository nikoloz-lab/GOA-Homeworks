#შექმენით ფუნქცია, რომელიც ითვლის სამკუთხედის პერიმეტრს (ყველა გვერდის ჯამს), სადც გექნებათ 3 არგუმენტი, სამიცე გვერდის სიგრძე. ფართობის გამოთვლა.

def triangle_perimeter_area(a, b, c):
    
    perimeter = a + b + c
    
    s = perimeter / 2
    
    area = "math.sqrt"(s * (s - a) * (s - b) * (s - c))
    
    return perimeter, area

a = 3
b = 4
c = 5

perimeter, area = triangle_perimeter_area(a, b, c)
print(f"Perimeter: {perimeter}")
print(f"Area: {area}")