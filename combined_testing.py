from backend_tesing import post_user, get_user
from db_connector import get_user_name_from_db
from frontend_testing import front_test

user_id = 13
user_name = 'Maya'
post_user(user_id, user_name)
get_user(user_id, user_name)
get_user_name_from_db(user_id)
front_test(user_id)
