# 4% rule
def calc_lump_sum(core):
    return 25 * 12 * core  

core = 1000 # assume core expenses 1000 a month
lump = calc_lump_sum(core) 
rate = 0.07

def compound_year (initial, monthly, rate):
    annual = 12 * monthly
    return (annual + initial) * (1 + rate)

def compound_years (initial, monthly, rate, years):
    sum = 0
    for y in range(0,years):
        sum = sum + compound_year(sum, monthly, rate)
    return sum    

def calc_years(target, monthly, rate):
    y = 1
    new = monthly * 12
    fv = new * (1 + rate)
    while fv < target:
        y = y + 1
        fv = (fv + new) * (1 + rate)
    return y
        
print("---\nCore: %d\nLump sum required: %d\nRate: %.2f\n---" % (core, lump, rate))
print("Gross\tMonthly\tNet\tSaving\tYears\tYears\tFireFactor")
for gross in range(23000, 80000, 4000):
    m_gross = gross / 12
    m_net = m_gross * 2/3
    m_saving = m_net - core
    print("%d\t%d\t%d\t%d\t%.1f\t%d\t%.1f" % (gross, m_gross, m_net, m_saving, lump/(m_saving * 12), calc_years(lump, m_saving, rate), m_gross/core))

print("---")

salary = 27000
core = 1000
for y in range(0, 20):
    salary = salary + (salary * 0.03)
    core = core + (core * 0.03)
    net = (salary / 12) * 2/3
    saving = net - core
    print("%.2f %.2f %.2f" % (salary, net, saving) )
