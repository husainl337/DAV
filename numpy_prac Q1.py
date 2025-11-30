import numpy as np


# n = int(input("give num for n cols: "))
# m = int(input("give num for m rows: "))
d2 = np.array([[1,2,3,4,5],
               [6,7,8,9,10]])
ria = np.random.randint(0,100, size=(4,5))
# print(ria)
print(np.mean(ria, axis=1))
print(np.var(ria, axis=1))
print(np.std(ria, axis=1))


# print(d2.shape)
# print(d2.ndim)
# print(d2.dtype)
# d2 = d2.reshape(m,n)
# print(d2)

d1 = np.array([1,2,3,4,5,0,6])
allzero = d1[d1 <= 0]
allnonzero = d1[d1 > 0]
nAn = d1[d1 == np.nan]
# print(allzero)
# print(allnonzero)
# print(nAn)




array1 = np.array([[1,2,3],[4,5,6]])
array2 = np.array([[7,8,9],[6,5,4]])
array3 = np.array([[5,6,8],[4,7,9]])

array4 = array2 - array3
array5 = array1 * 2
# print(array4)
# print(array5)
# print(np.cov(array1,array4))
# print(np.corrcoef(array1,array4))
# print(np.cov(array1,array5))
# print(np.corrcoef(array1,array5))

a1 = np.array([1,2,3,4,5,6,7,8,9,10])
a2 = np.array([10,9,8,7,6,5,4,3,2,1])
# print(a1[0:5] + a2[0:5])
# print(a1[5:] * a2[5:])

array = np.array([1,2,3,4])
# print(np.sum(array))
# print(np.square(array))
# print(np.sqrt(array))

dd = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
dd = dd.reshape(3,4)
# print(dd)

rarr = np.random.default_rng(seed=1)
rarr = rarr.integers(low= 0 , high= 1, size=(2,3))
# print(rarr)

aaa = np.array([1.2, 2.3, 3.5])
# print(aaa.dtype)
aaa = aaa.astype('int64')
# print(aaa)

strr = np.array(['1','2','5'])
# print(strr.dtype)
strr = strr.astype('float64')
# print(strr)


d = np.array([1,2,3])
d3 = np.array([[[1,1,1],
               [1,1,1],
               [1,1,1]]])
# print(d+d3)

d22 = np.array([[1,2,3],[4,5,6]])
# print(np.sum(d22))
# print(np.mean(d22[:, :1]) , np.mean(d22[:, 1:2]))

