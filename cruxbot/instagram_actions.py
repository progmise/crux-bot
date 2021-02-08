from facebook import GraphAPI, GraphAPIError
from pyfacebook import IgProApi, PyFacebookException


def get_ig_user_info(api,  # type: IgProApi
                     username  # type: str
                     ):

    data = {}

    try:
        data = api.discovery_user(
            username = username,
            return_json = True
        )

    except PyFacebookException as error:
        data = { "error": error }

    return data
 

def get_ig_user_medias(api,  # type: IgProApi
                       username  # type: str
                       ):

    data = {}

    try:
        data = api.discovery_user_medias(
            username = username,
            return_json = True
        )

    except PyFacebookException as error:
        data = { "error": error }

    return data


def get_ig_media_info(api,  # type: IgProApi
                      media_id  # type: str
                      ):

    data = {}

    try:
        data = api.get_media_info(
            media_id = media_id,
            return_json = True
        )

    except PyFacebookException as error:
        data = { "error": error }

    return data


def post_ig_photo(api,  # type: GraphAPI
                  instagram_business_id,  # type: str
                  image_url  # type: str
                  ):

    response = {}
    data = {}

    try:
        response = api.request(
            path = "{0}/{1}/{2}".format("v9.0", instagram_business_id, "media"),
            args = {
                "image_url": image_url
            },
            post_args = {
                "access_token": api.access_token
            },
            method = "POST"
        )

    except GraphAPIError as error:
        response = { "error": error }

    try:
        data = api.request(
            path = "{0}/{1}/{2}".format("v9.0", instagram_business_id, "media_publish"),
            args = {
                "creation_id": response["id"]
            },
            post_args = {
                "access_token": api.access_token
            },
            method = "POST"
        )
        
    except (KeyError, GraphAPIError) as error:
        data = { "error": error }

    return data