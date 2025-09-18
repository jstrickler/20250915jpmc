import logging
from functools import wraps

logging.basicConfig(
    filename="functions.log",
    level=logging.INFO,
    format="%(levelname)s %(asctime)s %(filename)s %(message)s",
)

def log_timestamp(func):
    @wraps(func)
    def _wrapper(*args, **kwargs):
        logging.info(func.__name__)
        return func(*args, **kwargs)
    return _wrapper


@log_timestamp
def spam(count):
    print("SPAM" * count)

@log_timestamp
def ham():
    print("HAM HAM HAM")

# spam = doit(spam)
# ham = doit(ham)

# eggs = log_timestamp(spam)

spam(3)
ham()
spam(10)
print(spam, ham)
