# Real Python Building HTTP API with DRF

## Application List and Associated Lessons

### People
  - create project Fedora and people app
  - create the Person model
  - create the PersonSerializer
  - Add a function based views that uses a Response object and Use of @APIView decorator
    -- Response object is a serilized data of Person.objects.all() query set
  - import json data
  ```./manage.py loaddate people``` 
    -- from people/fixtures/people.json
  - 

### Artifacts
  - ViewSet is a class that encapsulates the common REST method calls
  - Router allows the the use of viewSet to declare a series of URLs
    -- six methods on the ViewSet class: 
        .list(), = GET for listing objects
        .create(), = POST
        .retrieve(), = GET for specific identifier, i.e get book id # 12
        .update(), = PUT
        .partial_update(), = PATCH
        .destroy() = DELETE

### Web interface
> This is the default settings -- best practice to remove the BrowseableAPIRenderer in Prod

- Reference: https://www.django-rest-framework.org/api-guide/renderers/

```python
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    )
}
```

### Books
> Demo app for user login and permissions

- created login page
  -- templates/registration/login.html
  -- urls "accounts/" in main Fedora.urls
- Permissions
  -- default permissions allow entry rather than deny
  -- permissions don't apply filters!


### Vehicles (and Tools)
> Demo for Alternative serializers
- Tools (list_tools)
  -- Serializer.serializer instead of Serializers.ModelSerializer
  -- Folder enclosure to accomodate multiple models, serializers, views
- Vehicles 
  -- url field in serializers instead of id
  -- Nested Serialization

- Parts
  -- to_representation method in  class SerialNumberField(serializers.Field):
    -- to_representation(self, value) # passes self and value
  -- again -- url field in serializers instead of id

### API
> app to demonstrate API that includes the whole data for SPA processing (think react, angular, vue, etc)
- `@api_view`
- doctor = filter query set
- context in VehicleSerializer
- `@view_set`
- `@action` viewset
- use of :  The mixins are CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin—which provides both .update() and .partial_update() methods—and DestroyModelMixin.
 

### Prepping for SPA lesson
#### Utilities:
- django-awl
-- Miscellaneous collections of utilities like RankedModel an abstract model that provides ordering
-- https://github.com/cltrudeau/django-awl

- django-bstrap-modals
-- Django templates for Bootstrap modal dialogs, include wrapper for Rest actions
-- https://github.com/cltrudeau/django-bstrap-modals 
