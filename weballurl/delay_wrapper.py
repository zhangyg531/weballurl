# 异步下载视频
from threading import Timer


def delayed(seconds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            a_timer = Timer(seconds, func, args=args, kwargs=kwargs)
            a_timer.start()

        return wrapper

    return decorator
