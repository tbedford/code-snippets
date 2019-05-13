core = 1000 # assume core expenses 1000 a month
lump = 25 * 12 * core # 4% rule
rate = 0.07

def calc_years(lump, saving):
    y = 1
    fv = (saving * 12) * (1 + rate)
    while fv < lump:
        y = y + 1
        fv = (fv + (saving * 12)) * (1 + rate)
    return y
        
print("---\nCore: %d\nLump sum required: %d\n---" % (core, lump))
print("Gross\tMonthly\tNet\tSaving\tYears\tYears\tFireFactor")
for gross in range(23000, 80000, 4000):
    m_gross = gross / 12
    m_net = m_gross * 2/3
    m_saving = m_net - core
    print("%d\t%d\t%d\t%d\t%.1f\t%d\t%.1f" % (gross, m_gross, m_net, m_saving, lump/(m_saving * 12), calc_years(lump, m_saving), m_gross/core))
