def computepay(h,r):
    if h > 40:
        p = 1.5* r * (h - 40) + (40 * r)
    else:
        p = h * r
    return p
hrs = input("Enter Hours:")
h = float(hrs)
rph = input("Enter rate per hour:")
r = float(rph) 
p = computepay(h,r)
print("Pay", p)