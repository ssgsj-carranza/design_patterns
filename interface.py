from checkemail import check
import random
import string
from contestants import Contestant

registration_number = "".join([random.choice(string.ascii_letters+string.digits) for n in range(10)])


def interface():
