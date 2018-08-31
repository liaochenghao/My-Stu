from rest_framework import routers

from common.views import CommonView

router = routers.SimpleRouter()
router.register('common', CommonView)
urlpatterns = router.urls