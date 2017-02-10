import json

import falcon

from . import controller


class HealthCheckView(object):

    def on_get(self, req, resp, health_check_id):
        """
        Handler for GET requests to get health_check

        .. http:get:: /health_checks/(int:health_check_id)/

           Get all metadata for the specified health_check ID

           **Example request**:

           .. sourcecode:: http

              GET /health_checks/123/ HTTP/1.1

           **Example response**:

           .. sourcecode:: json

             { "id": 123,
               "status": 200,
               "message": "This is an example message."}

           :statuscode 200: Success
           :statuscode 404: Not Found
        """
        resp.content_type = "application/json"
        resp.status = falcon.HTTP_200

        health_check = controller.get(health_check_id)

        # if not health_check:
        #     resp.status = falcon.HTTP_404

        resp.body = json.dumps(self.get_metadata(health_check))

    def on_post(self, req, resp):
        """
        Handler for POST requests to add health checks

        .. http:post:: /health_checks/

           Add health check messages

           **Example request**:

           .. sourcecode:: http

              POST /health_checks/ HTTP/1.1
              Content-Type: application/json

              [ { "message": "Example message." } ]

           :reqheader Content-Type: application/json

           :statuscode 202: Success
           :statuscode 400: Malformed request
        """

        body = req.stream.read()
        payload = json.loads(body.decode('utf-8'))

        health_check = controller.create(payload['message'])

        resp.status = falcon.HTTP_201
        resp.body = json.dumps(self.get_metadata(health_check))

    def get_metadata(self, health_check):
        """Returns metadata for the specified health_check
        Args:
            health_check (models.HealthCheck): A HealthCheck instance
        Returns:
            dict
        """

        data = {}

        data["id"] = health_check.id
        data["message"] = health_check.message

        return data
