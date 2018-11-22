import os


def check_user_id(userid):
    def decorator(func):
        def check_user_id(*args, **kwargs):
            if userid == os.geteuid():  # who is currently logged on (geteuid)
                return func(*args, **kwargs)
            else:
                raise OSError("Invalid userid: {}".format(os.geteuid()))
        return check_user_id
    return decorator


@check_user_id(502)
def sqr(x):
    return x*x

print(sqr(10))
