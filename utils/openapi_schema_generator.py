from drf_yasg.generators import OpenAPISchemaGenerator


class SightIntegratedAPISchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request=request, public=public)
        schema.base_path = "/api/"
        schema.schemes = ["http", "https"]

        return schema
