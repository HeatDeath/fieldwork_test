# -*- coding:utf-8 -*-
from multiprocessing import Process, Pipe


def f(conn):
    conn.send([42, None, 'hello'])
    while True:
        print(conn.recv())

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print parent_conn.recv()   # prints "[42, None, 'hello']"
    parent_conn.send('666')
    p.terminate()




