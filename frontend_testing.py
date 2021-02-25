from selenium import webdriver

from db_connector import get_all_user_id_from_db


def front_test(user_id):
    status = False
    driver = webdriver.Chrome(executable_path="/Users/udi.ofir/Downloads/chromedriver")
    url = "http://127.0.0.1:5001/users/get_user_data/%s" % user_id
    driver.get(url)
    try:
        user_name = driver.find_element_by_id('user').text
        # status = True
        print("result of the frontend testing for the given id:", user_id, "the user name is: ", user_name)
    except Exception as e:
        print("web element 'user' is not found")
    finally:
        driver.quit()
        return status


if __name__ == "__main__":
    # get_all_user_id_from_db()
    id = 3
    front_test(id)