# hill_climbing

## 簡介

這是啟發式演算法的練習，該程式是以hill_climbing演算法處裡 one max 問題。

## hill_climbing

一種模擬爬山的啟發式演算法，原理是最開始隨機找一個起始解決方案，之後靠鄰居演算法找出一個鄰近的解，如果這個解比之前的好，那就將解決方案改為後者，不斷迭代並在最後回傳這之中的最佳解。

## one max

在一個只能放入1，0的陣列中，找出有最多1的組合，最佳解就是陣列裡全是1。

### 演算法細節

#### initial

初始化一個一維陣列，裡面會隨機的放入0跟1。

#### evalution

計算陣列中有幾個1，該問題中一越多分數越好。

#### transition

挑選隨機陣列中的一個元素 XOR 1 也就是說讓0變1，1變0。