#! /usr/bin/env python
#! -*- encoding: utf-8 -*-

def echo(value=None):
    print "Execution starts when 'next()' is called for the time."
    try:
        while True:
            try:
                print type(value)
                value = (yield value)
                print type(value)

            except Exception, e:
                value = e

    finally:
        print "Don't forget to clean up when 'close()' is called."

def echo2():
    print 1
    yield
    print 2

def echo3(value):
    for i in range(0,3):
        value = yield (i + value)

if __name__ == "__main__":
    generator = echo(1)
    print generator.next() #输出：Execution starts when 'next()' is called for the time.
                              #执行到了value = (yield 1)
                              #返回1，挂起。value = (yield 1)没有执行完，此时左值的value仍然是None

    print "="*3
    print generator.next() #接着value = (yield 1)开始执行。左值value这时是None
                              #执行到value = (yield None)
                              #返回None
    print "="*3
    print generator.send(2) #先执行value = (yield None)。因为是send(2),所以此时左值value的值为2
                              #然后继续执行循环value = (yield 2)。
                              #因为send()返回下一个yield表达式中的表达式（expression_list）的值，所以此时返回2，挂起。此时左值value的值为None。
    print "="*3
    generator.throw(TypeError, "spam") #先执行value = (yield 2)
                                          #然后抛出异常，这个异常被"except Exception, e:"捕捉，并处理，这时value是TypeError
                                          #然后继续循环到value = (yield TypeError)，返回yield表达式，也就是TypeError这个异常。然后挂起。
    print "="*3
    print generator.close() #继续执行value = (yield TypeError)，抛出GeneratorExit异常。
                               #这个异常被"except Exception, e:"捕获，并处理，这时value为GeneratorExit。
                               #继续执行循环，执行到value = (yield GeneratorExit)，返回GeneratorExit。
                               #这相当于generator产生了一个值，所以就会抛出一个RuntimeError异常。


    print "~" * 20
    echo2().next() # 1

    print "~" * 20
    gen = echo3(1)
    print gen.next()
    while(True):
        try:
            print gen.send(2)
        except:
            break
