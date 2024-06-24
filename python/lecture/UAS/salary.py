class Salary:
    def __init__(self, division):
        self.division=division
    
    def SetDivision(self, division):
        self.division=division
    
    def GetDivision(self):
        return self.division
    
    def cekSalary(self):
        paycheck=''
        if self.division=='1':
            paycheck='Rp. 5.000.000'
        elif self.division=='2':
            paycheck='Rp. 6.000.000'
        elif self.division=='3':
            paycheck='Rp. 4.500.000'
        elif self.division=='4':
            paycheck='Rp. 5.000.000'
        else: paycheck='input salah'

        return paycheck