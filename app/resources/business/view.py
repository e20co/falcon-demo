import json

import falcon

from . import controller


class BusinessView(object):

    def on_get(self, req, resp, business_id):
        """
        Handler for GET requests to get business

        .. http:get:: /businesss/(int:business_id)/

           Get all metadata for the specified business ID

           **Example request**:

           .. sourcecode:: http

              GET /businesss/123/ HTTP/1.1

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

        business = controller.get(business_id)

        # if not business:
        #     resp.status = falcon.HTTP_404

        resp.body = json.dumps(self.get_metadata(business))

    def on_post(self, req, resp):
        """
        Handler for POST requests to add health checks

        .. http:post:: /businesss/

           Add health check messages

           **Example request**:

           .. sourcecode:: http

              POST /businesss/ HTTP/1.1
              Content-Type: application/json

              [ { "message": "Example message." } ]

           :reqheader Content-Type: application/json

           :statuscode 202: Success
           :statuscode 400: Malformed request
        """

        body = req.stream.read()
        payload = body.decode('utf-8')
        print("utf-8 payload is "+payload)
        business = controller.create(payload)
        resp.status = falcon.HTTP_201
        resp.body = json.dumps(self.get_metadata(business))

    def get_metadata(self, business):
        """Returns metadata for the specified business
        Args:
            business (models.Business): A Business instance
        Returns:
            dict
        """

        data = {}

        print(str(business.fein))

        data["id"] = business.id
        data["fein"] = business.fein

        return data
