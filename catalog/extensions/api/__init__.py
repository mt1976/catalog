# encoding: utf-8
"""
API extension
=============
"""
from copy import deepcopy

from catalog.extensions.flask_restplus import Api

api_v1 = Api(
    version='1.0',
    title="Catalog API",
    description="This is a catalog service of world-wide data sources."
)

current_api = api_v1


def serve_swaggerui_assets(path):
    """
    Swagger-UI assets serving route.
    """
    from flask import send_from_directory
    from flask import current_app as app
    if not app.debug:
        import warnings
        warnings.warn(
            "/swaggerui/ is recommended to be served by public-facing server (e.g. NGINX)"
        )
    return send_from_directory(app.config['STATIC_ROOT'], path)


def init_app(app, **kwargs):
    """
    API extension initialization point.
    """
    app.route('/swaggerui/<path:path>')(serve_swaggerui_assets)

    # Prevent config variable modification with runtime changes
    current_api.authorizations = deepcopy(app.config['AUTHORIZATIONS'])
