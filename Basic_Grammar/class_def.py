#创建类和对象
class Liner:
    def __init__(self,w,b):
        self.w = w;
        self.b = b;
    def forward(self,x):
        y = self.w*x+self.b
        return y;
#先实例化对象
model = Liner(2,1)
#调用forward方法
result = model.forward(3)
print(result)


#继承
class BaseLayer:
    def __init__(self):
        self.device = "cpu";

class CustomLinear(BaseLayer):
    
    def __init__(self,w,b):
        super().__init__();
        self.w = w;
        self.b = b;
    def forward(self,x):
        m = self.w*x + self.b;
        return m;
model = CustomLinear(3,2);
print(model.device);
result = model.forward(4);
print(result);
