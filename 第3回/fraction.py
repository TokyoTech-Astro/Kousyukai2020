from math import gcd


class frac:
    def __init__(self, n:int, d:int):
        
        # TODO
        
        self.bunsi = 
        self.bunbo = 
    

    def __str__(self):      # 文字列に変換する関数
        if self.bunbo == 1:
            return str(self.bunsi)
        return f"{self.bunsi}/{self.bunbo}"
    
    def __float__(self):    # 小数に変換する関数
        return float(self.bunsi / self.bunbo)
    
    # TODO: