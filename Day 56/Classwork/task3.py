3. #https://www.codewars.com/kata/56cd44e1aa4ac7879200010b

def is_uppercase(string):
    return string == string.upper()

#მაგალითი-)
print(is_uppercase("c")) #false
print(is_uppercase("C")) #true
print(is_uppercase("hello I AM DONALD")) #false
print(is_uppercase("HELLO I AM DONALD")) #true
print(is_uppercase("ACSKLDFJSgSKLDFJSKLDFJ")) #false
print(is_uppercase("ACSKLDFJSGSKLDFJSKLDFJ")) #true