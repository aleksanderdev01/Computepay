#Definuje funkcję "computepay"
def computepay(h,r):
    #Pokazuje kiedy zwiększyć stawkę za nadgodziny
    if h > 40:
        p = 1.5* r * (h - 40) + (40 * r)
    #A kiedy pozostać przy stałej stawce godzinowej
    else:
        p = h * r
    return p
#Pyta o liczbę przepracowanych godzin
hrs = input("Enter Hours:")
#Wczytuje wartość jako liczbę zmiennoprzecinkową
h = float(hrs)
#Pyta o stawkę godzinową
rph = input("Enter rate per hour:")
#Wczytuje wartość jako liczbę zmiennoprzecinkową
r = float(rph) 
#przywołuje funkcję zdefinowaną powyżej
p = computepay(h,r)
#Drukuje wyliczoną wartość wypłaty
print("Pay", p)