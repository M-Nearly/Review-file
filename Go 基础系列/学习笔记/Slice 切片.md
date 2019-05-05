## Slice 切片

- slice 概述

  > 切片本身不是数组，它只想底层的数组

- 创建slice

  > 一般使用make()创建 `make([]type,len,cap)`
  >
  > 其中cap可以省略，则和len的值相同
  >
  > len 表示存在的元素个数，cap表示容量

- 作为可边长数组的替代方案，可以关联底层数组局部或全部

- 可以直接创建或从底层数组获取生成

  ![image-20190502002207853](/Users/garry/Library/Application Support/typora-user-images/image-20190502002207853.png)

----



## Reslice

1. Reslice 按索引取值
2. 索引不可以超过被slice的切片的容量cap()值
3. 索引越界不会导致底层数组的重新分配，而是引发错误



## append

1. 开业在slice尾部追加元素
2. 可以将一个slice追加在另一个slice尾部
3. 如果最终长度未超过追加到slice的容量则返回原始slice
4. 如果超过追加到的slice的容量则将重新分配数组并拷贝原始数据



## copy

