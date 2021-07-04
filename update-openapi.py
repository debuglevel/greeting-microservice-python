from app.rest.main import fastapi
openapi = fastapi.openapi()

# with open('openapi.json', 'w') as openapi_file:
#     import json
#     json.dump(openapi, openapi_file, indent=4)

with open('openapi.yaml', 'w') as openapi_file:
    import yaml
    yaml.dump(openapi, openapi_file)
