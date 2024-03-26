from rest_framework import pagination

class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework_config.CustomPagination',
    'PAGE_SIZE': 10
}
