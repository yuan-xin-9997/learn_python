from datetime import datetime
import multiprocessing
import time

def wait_for_event(e):
    """Wait for the event to be set before doing anything"""
    print(f'{datetime.now()} wait_for_event: starting')
    e.wait()
    print(f'{datetime.now()} wait_for_event: e.is_set()->', e.is_set())


def wait_for_event_timeout(e, t):
    """Wait t seconds and then timeout"""
    print(f'{datetime.now()} wait_for_event_timeout: starting')
    e.wait(t)
    print(f'{datetime.now()} wait_for_event_timeout: e.is_set()->', e.is_set())


if __name__ == '__main__':
    e = multiprocessing.Event()
    w1 = multiprocessing.Process(
        name='block',
        target=wait_for_event,
        args=(e,),
    )
    w1.start()

    w2 = multiprocessing.Process(
        name='nonblock',
        target=wait_for_event_timeout,
        args=(e, 2),
    )

    w2.start()
    print(f'{datetime.now()} main: waiting before calling Event.set()')
    time.sleep(3)
    e.set()
    print(f'{datetime.now()} main: event is set')