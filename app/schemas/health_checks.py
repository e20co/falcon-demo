import marshmallow


class HealthCheckRequestSchema(marshmallow.Schema):
    """Schema for payload to add health checks"""
    status = marshmallow.fields.Int()
    message = marshmallow.fields.Str()
