# encoding: utf-8
"""
API extension
=============
"""

from copy import deepcopy

from .api import Api
from .http_exceptions import abort
from .namespace import Namespace

api_v1 = Api(
    version='1.0',
    title="Catalog API",
    description=(
        "This is a catalog service of world-wide data sources.\n"
    ),
)


def init_app(app, **kwargs):
    """
    API extension initialization point.
    """
    # Prevent config variable modification with runtime changes
    api_v1.authorizations = deepcopy(app.config['AUTHORIZATIONS'])
