# using OOP. The details to receive are staff_id, basic_pay, years_of_experience, total_allowance and total_deduction with the help of Constructor. Using methods calculate net_pay
class staff:
def __init__(s, id, basicpay, experience, allowance, deduction):
    s.id = id
    s.basicpay = basicpay
    s.experience = experience
    s.allowance = allowance
    s.deduction = deduction
def calculate_netpay(s):
gross = s.basicpay + s.allowance
net = gross - s.deduction
return net

e = staff("S123", 50000, 5, 2000, 1000)
n = e.calculate_netpay()
print(f"Employee ID: {e.id}")
print(f"Net Salary: ${n}")

