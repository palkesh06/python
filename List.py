from typing import NewType


List = []
print(List)
List = [1,2,3,4,5]
print(List)
List =["hello", "world"]
print (List[0])
print (List[1])
List= [['hello', 'world'], "hello"]
print (List[0])
print(List[1])
print(List[0][1])
List.clear()
List.append(12)
List.append((7,8)) #list
List.append([2,3,4,5]) #list 
List.insert(0,"hello")
List.insert(2,37)
print(List)
print(List[-1])
print(List[-2][0])
List.remove(37)
List.append(23)
List.pop() 
print(List[:-1]) # negative slicing 
odd_square = [x ** 2 for x in range(1, 13) if x % 2 == 0] 
for k in List:
    print (k)
    k=0
while  k < len(odd_square) :
    print(odd_square[k])
    k= k+1 



    