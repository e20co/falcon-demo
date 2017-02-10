import json

import falcon

import controller


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

        if not health_check:
            resp.status = falcon.HTTP_404

        resp.body = json.dumps(self.get_metadata(health_check))

    def get_metadata(self, health_check):
        """Returns metadata for the specified health_check
        Args:
            health_check (models.HealthCheck): A HealthCheck instance
        Returns:
            dict
        """

        data = {}

        data["status"] = health_check.status
        data["message"] = health_check.message

        return data
