core = 1000 # assume core expenses 1000 a month
lump = 25 * core

def calc_gross_required (monthly):
    gross = monthly * 12
    gross = gross + (gross * 1/3) 
    return int(gross)

print("---\nCore: %d\nLump sum required: %d\n---" % (core, lump))
print("Gross\tNet\tSaving\tYears")
for m in range(1500, 6000, 500):
    saving = m - core
    print("%d\t%d\t%d\t%d" % (calc_gross_required(m), m, saving, int(300000/(saving * 12))))
