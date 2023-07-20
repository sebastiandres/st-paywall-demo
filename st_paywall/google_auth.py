import asyncio

import jwt
import streamlit as st
from httpx_oauth.clients.google import GoogleOAuth2
from httpx_oauth.clients.github import GitHubOAuth2

provider = st.secrets["PAYWALL"]["AUTHENTICATION_METHOD"]
redirect_url = st.secrets["PAYWALL"]["REDIRECT_URL"]

if provider == "github":
    client = GitHubOAuth2(
                        client_id=st.secrets["PAYWALL"]["CLIENT_ID"], 
                        client_secret=st.secrets["PAYWALL"]["CLIENT_SECRET"]
                        )
elif provider == "google":
    client = GoogleOAuth2(
                        client_id=st.secrets["PAYWALL"]["CLIENT_ID"], 
                        client_secret=st.secrets["PAYWALL"]["CLIENT_SECRET"]
                        )

# Public methods
## These are the methods that can be called from the main app
def login_button():
    user_email = get_logged_in_user_email()
    if "email" not in st.session_state:
        show_login_button()
        st.stop()

def get_user_email():
    return st.session_state.email

def logout_button():
    if st.button("Logout", type="primary"):
        del st.session_state.email
        st.experimental_rerun()

# Private methods
## This are internal methods to make public methods work
def decode_user(token: str):
    """
    :param token: jwt token
    :return:
    """
    decoded_data = jwt.decode(jwt=token, options={"verify_signature": False})
    return decoded_data


async def get_authorization_url(client: GoogleOAuth2, redirect_url: str):
    authorization_url = await client.get_authorization_url(
        redirect_url,
        scope=["email"],
        extras_params={"access_type": "offline"},
    )
    return authorization_url


def markdown_button(
    url: str, text: str | None = None, color="#FD504D", sidebar: bool = True
):
    markdown = st.markdown if sidebar else st.markdown

    markdown(
        f"""
    <a href="{url}" target="_self">
        <div style="
            display: inline-flex;
            -webkit-box-align: center;
            align-items: center;
            -webkit-box-pack: center;
            justify-content: center;
            font-weight: 400;
            padding: 0.25rem 0.75rem;
            border-radius: 0.25rem;
            margin: 0px;
            line-height: 1.6;
            width: auto;
            user-select: none;
            background-color: {color};
            color: rgb(255, 255, 255);
            border: 1px solid rgb(255, 75, 75);
            text-decoration: none;
            ">
            {text}
        </div>
    </a>
    """,
        unsafe_allow_html=True,
    )


async def get_access_token(client: GoogleOAuth2, redirect_url: str, code: str):
    token = await client.get_access_token(code, redirect_url)
    return token


def get_access_token_from_query_params(client: GoogleOAuth2, redirect_url: str) -> str:
    query_params = st.experimental_get_query_params()
    code = query_params["code"]
    token = asyncio.run(
        get_access_token(client=client, redirect_url=redirect_url, code=code)
    )
    # Clear query params
    st.experimental_set_query_params(query_params)
    return token


def show_login_button():
    authorization_url = asyncio.run(
        get_authorization_url(client=client, redirect_url=redirect_url)
    )
    markdown_button(authorization_url, f"Login with {provider}")


def get_logged_in_user_email() -> str | None:
    if "email" in st.session_state:
        return st.session_state.email

    if provider == "google":
        try:
            token_from_params = get_access_token_from_query_params(client, redirect_url)
        except KeyError:
            return None
        user_info = decode_user(token=token_from_params["id_token"])
        st.session_state["email"] = user_info["email"]
    elif provider == "github":
        st.session_state["email"] = "sebastiandres (not email, account/username)"
    else:
        st.error("Unknown provider. Check st.secrets configuration")
        raise ValueError("Unknown provider")

    return st.session_state["email"]

