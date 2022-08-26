from rest_framework import routers

from .views import SummarizerViewset

router = routers.SimpleRouter()
router.register("", SummarizerViewset)


urlpatterns = router.urls
