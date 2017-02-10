import json

import falcon

from managers import health_check_manager


class HealthCheck(object):

    def on_get(self, req, resp):
        resp.content_type = "application/json"
        resp.status = falcon.HTTP_200

        health_check = health_check_manager.get_health_check(1)

        resp.body = json.dumps(health_check_manager.get_metadata(health_check))
