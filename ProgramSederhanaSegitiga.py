q = int(input('Masukkan angka ke-1  = '))
w = int(input('Masukkan angka ke-2  = '))
p = int(input('Masukkan angka ke-3  = '))

if q==w==p:
    print("Segitiga ini Segitiga Sama Sisi")
elif (q or w or p <= 0) and (q >= (w+p)) or (w >= q+p) or (p >= q+w):
    print ("Segitiga ini tidak dapat dibangun") 
elif (q==w or w==p or p==q):
    print("Segitiga ini Segitiga Sama Kaki")
elif (q*q == w*w + p*p or w*w == q*q + p*p or p*p == w*w + q*q):
    print("Segitiga ini Segitiga Siku-siku")
else :
    print("SEGITIGA BEBAS")
