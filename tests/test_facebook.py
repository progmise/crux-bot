import sys
sys.path.append("path-project")

from pyfacebook import Api
from facebook import GraphAPI
from cruxbot.cruxbot import APP_ID, APP_SECRET, PAGE_ACCESS_TOKEN, PAGE_ID, USER_ID

import cruxbot.facebook_actions as fb


def testGetPosts():
    data = fb.get_posts(
        api = api,
        page_id = page_id
    )

    assert isinstance(data, list) and len(data) != 0


def testGetComments():
    data = fb.get_comments(
        api = api,
        object_id = object_id
    )

    assert "total_count" in data[1]


def testGetPageConversations():
    data = fb.get_page_conversations(
        api = api,
        page_id = page_id
    )

    assert isinstance(data, list) and len(data) != 0


def testGetConversationMessages():
    data = fb.get_conversation_messages(
        api = api,
        conversation_id = conversation_id
    )

    assert isinstance(data, list) and len(data) != 0


def testPostComment():
    data = fb.post_comment(
        api = api,
        post_id = post_id,
        message = "Un mensaje de test desde Python"
    )

    assert "id" in data


def testPostPublication():
    data = fb.post_publication(
        api = api,
        page_id = page_id,
        message = "Una nueva publicación desde Python"
    )

    assert "id" in data


def testPutPublication():
    data = fb.put_publication(
        api = api,
        post_id = post_id_to_manipulate,
        message = "Un mensaje modificado"
    )

    assert "id" in data


def testDeletePublication():
    data = fb.delete_publication(
        api = api,
        post_id = post_id_to_manipulate
    )

    assert data["success"]


def testPostLike():
    data = fb.post_like(
        api = api,
        object_id = object_id
    )

    assert data["success"]


def testPostPhoto():
    data = fb.post_photo(
        api = graphApi,
        page_id = page_id,
        image = image
    )

    assert "post_id" in data


def testPostProfilePhoto():
    data = fb.post_profile_photo(
        api = graphApi,
        page_id = page_id,
        image = image
    )

    assert data["error"].code == 100


def testListFriends():
    data = fb.list_friends(
        api = api,
        user_id = user_id
    )

    assert isinstance(data, list) and len(data) != 0


def testGetPageInformation():
    data = fb.get_page_information(
        api = api,
        page_id = page_id
    )

    assert "id" in data


if __name__ == "__main__":

    page_id = PAGE_ID
    user_id = USER_ID
    object_id = "102579945106245_118113996886173"
    conversation_id = "t_10224843694505732"
    post_id = "102579945106245_118113650219541"
    post_id_to_manipulate = "102579945106245_117924853571754"
    image = open("images\\image.jpg", "rb")

    api = Api(
        app_id = APP_ID,
        app_secret = APP_SECRET,
        long_term_token = PAGE_ACCESS_TOKEN,
    )

    graphApi = GraphAPI(
        access_token = PAGE_ACCESS_TOKEN
    )

    testGetPosts()
    testGetComments()
    testGetPageConversations()
    testGetConversationMessages()
    testPostComment()
    testPostPublication()
    testPutPublication()
    testDeletePublication()
    testPostLike()
    testPostPhoto()
    testPostProfilePhoto()
    testListFriends()
    testGetPageInformation()