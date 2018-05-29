class Rectangle:
    def __init__(self):
        self.Name = ["矩形","正方形"]
    def enter(self):
        self.a = True
        x = input("请输入x1,y1,x2,y2,以空格为间隔：")
        while self.a:
            self.data = []
            self.D = []
            try:
                for a in x:
                    if a != " ":
                        self.D.append(float(a))
                if self.D[0] == self.D[2] or self.D[1] == self.D[3]:
                    raise Datawrong
            except Datawrong:
                print("数据错误！")
                x = input("请输入x1,y1,x2,y2,以空格为间隔：")
            else:
                self.data = self.D
                self.a = False
    def width(self):
        self.w = abs(self.data[0]-self.data[2])
        print("矩形的宽度为:%f"% self.w)
    def height(self):
        self.h = abs(self.data[1]-self.data[3])
        print("矩形的长度为:%f"% self.h)
    def area(self):
        s = self.w * self.h
        if self.w == self.h:
            n = str(self.Name[1])
        else:
            n = str(self.Name[0])
        print("%s面积为：%f"%(n,s))
    def circumference(self):
        c = 2*(self.w + self.h)
        if self.w == self.h:
            n = str(self.Name[1])
        else:
            n = str(self.Name[0])
        print("%s的周长为%f"%(n,c))
class Datawrong(Exception):
    pass
class Square(Rectangle):
    def side_length(self):
        self.w = abs(self.data[0]-self.data[2])
        self.h = self.w
        print("正方形边长为%f."% self.w)
if __name__ == "__main__":
    S = Square()
    S.enter()
    S.side_length()
    S.circumference()
    S.area()
