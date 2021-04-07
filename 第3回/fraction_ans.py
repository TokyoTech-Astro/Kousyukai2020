from math import gcd


class frac:
    def __init__(self,bunsi:int,bunbo:int):
        if bunbo < 0:               # 分母を正にする
            bunsi,bunbo = -bunsi,-bunbo
        
        g = gcd(bunsi,bunbo)        # 約分する
        self.bunsi = bunsi // g
        self.bunbo = bunbo // g
    
    def __str__(self):              # print()やstr()で文字列に変換する特殊メソッド
        if self.bunbo == 1:
            return str(self.bunsi)
        return f"{self.bunsi}/{self.bunbo}"
    def __float__(self):            # float()で小数に変換する特殊メソッド
        return float(self.bunsi / self.bunbo)
    
    def __add__(a,b):
        return frac(a.bunsi*b.bunbo + a.bunbo*b.bunsi, a.bunbo*b.bunbo)
    def __sub__(a,b):
        return frac(a.bunsi*b.bunbo - a.bunbo*b.bunsi, a.bunbo*b.bunbo)
    def __mul__(a,b):
        return frac(a.bunsi*b.bunsi, a.bunbo*b.bunbo)
    def __truediv__(a,b):           # "/"で割り算できるようにする特殊メソッド
        return frac(a.bunsi*b.bunbo, a.bunbo*b.bunsi)
    def __pow__(a:"frac", b:int):   # "**"でべき演算できるようにする特殊メソッド
        return frac(a.bunsi**b, a.bunbo**b)


if __name__ == "__main__":
    a = frac(2,3)
    b = frac(15,60)
    print(a,b)
    print(float(a),float(b))
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a**3)