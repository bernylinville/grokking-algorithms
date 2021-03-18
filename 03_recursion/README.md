# 递归

假设你在祖母的阁楼中翻箱倒柜，发现了一个上锁的神秘手提箱。祖母告诉你，钥匙很可能在下面这个盒子里。这个盒子里有盒子，而盒子里的盒子又有盒子。钥匙就在某个盒子中。为找到钥匙，你将使用什么算法?

第一种方法使用的是while循环:只要盒子堆不空，就从中取一个盒子，并在其中仔细查找。

1. 创建一个要查找的盒子堆。
2. 从盒子堆取出一个盒子，在里面找。
3. 如果找到的是盒子，就将其加入盒子堆中，以便以后再查找。
4. 如果找到钥匙，则大功告成!
5. 回到第二步。

```python
def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print('Found the key!')
```

第二种方法使用递归——函数调用自己

1. 检查盒子中的每样东西。
2. 如果是盒子，就回到第一步。
3. 如果是钥匙，就大功告成!

这种方法的伪代码如下：

```python
def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item)
        elif item.is_a_key():
            print('Found the key!')
```

这两种方法的作用相同，但在我看来，第二种方法更清晰。递归只是让解决方案更清晰，并没有性能上的优势。实际上，在有些情况下，使用循环的性能更好。

> 如果使用循环，程序的性能可能更高;如果使用递归，程序可能更容易理解。如何选择要看什么对你来说更重要。
> Loops may achieve a performance gain for your program. Recursion may achieve a performance gain for your programmer. Choose which is more important in your situation! Leigh Caldwell [Recursion or Iteration?](https://stackoverflow.com/questions/72209/recursion-or-iteration/72694#72694)

## 基线条件和递归条件

编写递归函数时，必须告诉它何时停止递归。正因为如此，每个递归函数都有两部分：基线条件(base case)和递归条件(recursive case)。

```python
def countdown(i):
    print i
    countdown(i-1)
```

上述代码会无限执行下去

```python
def countdown(i):
    print i
    # base case
    if i <= 1:
        return
    # recursive case
    else:
        countdown(i-1)
```

## 栈

### 调用栈 call stack

计算机在内部使用被称为调用栈的栈

```python
def greet(name):
    print("hello, " + name + "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()


def greet2(name):
print("how are you, " + name + "?")


def bye():
print("ok bye!")
```

* 首先调用了函数greet，并将参数name的值指定为maggie。
* 接下来，函数greet调用了函数greet2，并将参数name的值指定为maggie。
* 此时函数greet处于未完成(挂起)状态。
* 当前的函数调用为函数greet2。
* 这个函数执行完毕后，从函数调用返回。此时，栈顶的内存块被弹出。
* 首先打印getting ready to say bye...，再调用 函数bye。
* 在栈顶添加了函数bye的内存块。然后，你打印ok bye!，并从这个函数返回
* 现在你又回到了函数greet。由于没有别的事情要做，你就从函数greet返回

这个栈用于存储多个函数的变量，被称为调用栈。

### 递归调用栈

使用栈虽然很方便，但是也要付出代价:存储详尽的信息可能占用大量的内存。每个函数调用都要占用一定的内存，如果栈很高，就意味着计算机存储了大量函数调用的信息。在这种情况下，你有两种选择。

* 重新编写代码，转而使用循环。
* 使用尾递归。这是一个高级递归主题，不在本书的讨论范围内。另外，并非所有的语言都支持尾递归。

## 小结

* 递归指的是调用自己的函数。
* 每个递归函数都有两个条件:基线条件和递归条件。
* 栈有两种操作:压入和弹出。
* 所有函数调用都进入调用栈。
* 调用栈可能很长，这将占用大量的内存。
