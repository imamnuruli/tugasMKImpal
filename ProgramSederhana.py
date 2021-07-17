computer_amount = int(input('Jumlah Komputer ke-1: '))
service_time = int(input('Jumlah Komputer ke-2: '))
drop_off = bool(input('Jumlah Komputer ke-3: '))
Pick_Up = bool(input('Jumlah Komputer ke-4: '))

if (computer_amount == 1 or computer_amount == 2):
    base_fee = 500
    additional_fee = 0
elif(computer_amount >= 3 and computer_amount <= 10):
    base_fee = 100
    additional_fee = 10
elif(computer_amount > 10):
    base_fee = 500
    additional_fee = 10

if (service_time < 9 or service_time > 21):
    base_fee = base_fee*2

if(drop_off == True and Pick_Up == True ):
    Total_Base_Fee = base_fee - (base_fee*0.015)

print(Total_Base_Fee)
