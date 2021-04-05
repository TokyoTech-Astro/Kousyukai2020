from math import gcd


class frac:
    def __init__(self, n:int, d:int):
        
        # TODO
        
        self.bunsi = 
        self.bunbo = 
    

    def __str__(self):      # print()やstr()で文字列に変換する特殊メソッド
        if self.bunbo == 1:
            return str(self.bunsi)
        return f"{self.bunsi}/{self.bunbo}"
    
    def __float__(self):    # float()で小数に変換する特殊メソッド
        return float(self.bunsi / self.bunbo)
    
    # TODO: