from backend_tesing import post_user, get_user
from db_connector import get_user_name_from_db
from frontend_testing import front_test

post_user(1, 'lihi ofir')
get_user(1, 'lihi ofir')
get_user_name_from_db(1)
front_test(1)
