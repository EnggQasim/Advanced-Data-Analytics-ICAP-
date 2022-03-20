
print("Module Starts here..............") 

def tax_calculator(annual_income):
    if annual_income <=600000:
        taxable_income = annual_income-600000
        tax = 0
    elif (annual_income>600000) and (annual_income<=700000):
        taxable_income = annual_income-600000
        tax =5
        
        
    elif (annual_income>700000) and (annual_income<=1000000):
        taxable_income = annual_income-700000
        tax  = 10
    else:
        taxable_income  = annual_income - 1000000
        tax  = 20
    return (taxable_income*tax/100)/12
    
        

def netSalary(gross):
    annual_income = gross *12
    
    

    
    netSalary = gross-tax_calculator(annual_income)
    return netSalary   



def name():
    print("Nasir")
    
    
    
    
print("module ended here......")