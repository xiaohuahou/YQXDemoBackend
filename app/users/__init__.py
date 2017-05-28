from flask import Blueprint

users = Blueprint('users', __name__)

from .teachers import *
from .students import *
from .parents import *