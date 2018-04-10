int = 100 #赋值整形
float = 1000.0 #浮点型
string = "john" #字符串
print(int);print(float);print(string);print("---------------------")

#为多个变量赋相同值
int = float = string = 1
print(int) ;print(float);print(string);print("---------------------")

#为多个变量赋不同值
int,float,string = 1,2,"c"
print(int) ;print(float);print(string);print("---------------------")
