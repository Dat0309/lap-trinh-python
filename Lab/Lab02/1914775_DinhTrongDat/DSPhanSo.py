
from PhanSo import PhanSo


class DSPhanSo:
    def __init__(self):
        self.dsps= []
        
    def themPS(self, ps: PhanSo):
        self.dsps.append(ps)
        
    def xuat(self):
        for ps in self.dsps:
            print(ps)
    
    def countNegativeFraction(self):
        dem = 0
        for ps in self.dsps:
            if(int(ps.tu)<0 or int(ps.mau)<0):
                dem+=1
        return dem
    
    def comparisionFraction(self, a: PhanSo,b: PhanSo):
        if(a.mau == b.mau):
            return a.tu<b.tu
        else:
            return int(a.tu)*int(b.mau) < int(b.tu)*int(a.mau)
    
    def minFractions(self):
        min = self.dsps[0]
        for ps in self.dsps:
            if(int(ps.tu) > 0 and int(ps.mau) >0):
                if(dsps.comparisionFraction(ps,min)):
                   min = ps
        return min.xuat() 
    
    def compare(self, x: PhanSo, y: PhanSo):
        if(x.mau == y.mau and x.tu == y.tu):
            return True
        return False
    
    def findPos(self, x: PhanSo):
        pos = [p for p in range(0, len(self.dsps)) if self.compare(self.dsps[p],x)]
        return pos
    
    def sumNegative(self):
        for ps in self.dsps:
            if(int(ps.tu)<0 or int(ps.mau)<0):
                ps.__add__()
        
    
    def readFile(self, fileName: str):
        f = open(fileName, 'r', encoding="utf8")
        line = f.readline()
        sp = line.split(',')
        for i in sp:
            frac = i.split('/')
            ps = PhanSo()
            ps.tu = frac[0]
            ps.mau = frac[1]
            dsps.themPS(ps)
        return dsps.dsps

            
dsps = DSPhanSo()
ps = PhanSo()
ps.tu = 2
ps.mau = 3
dsps.readFile('phanso.txt')
print(f"Số lượng phân số âm có trong mảng là:  {dsps.countNegativeFraction()}")
dsps.minFractions()
print(*dsps.findPos(ps))
