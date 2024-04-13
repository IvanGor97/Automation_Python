from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Apple", "iPhone 12", "+79228888888")
phone2 = Smartphone("Samsung", "Galaxy S21", "+79119999999")
phone3 = Smartphone("Xiaomi", "Mi 11", "+79005555555")
phone4 = Smartphone("OnePlus", "8T", "+79336666666")
phone5 = Smartphone("Google", "Pixel 5", "+79777777777")

catalog.extend([phone1, phone2, phone3, phone4, phone5])

for phone in catalog:
    print(phone.brand_phone, "-", phone.model_phone, ".", phone.numder)
    



