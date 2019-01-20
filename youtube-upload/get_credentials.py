# import google.oauth2.credentials
# import google_auth_oauthlib.flow
from google_auth_oauthlib.flow import Flow


SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

VALID_PRIVACY_STATUSES = ('public', 'private', 'unlisted')





def get_credentials(config):
    flow = Flow.from_client_config(
        config,
        scopes=SCOPES,
        redirect_uri='urn:ietf:wg:oauth:2.0:oob')

    # Tell the user to go to the authorization URL.
    auth_url, _ = flow.authorization_url(prompt='consent')

    print('Please go to this URL: {}'.format(auth_url))

    # The user will get an authorization code. This code is used to get the
    # access token.
    code = input('Enter the authorization code: ')
    flow.fetch_token(code=code)

    return flow.credentials

    # using flow.authorized_session.
    # session = flow.authorized_session()
    # print(session.get('https://www.googleapis.com/userinfo/v2/me').json())