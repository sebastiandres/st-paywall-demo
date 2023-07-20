import streamlit as st
from st_paywall.google_auth import login_button, logout_button, get_user_email

def authenticate():
    """
    Authenticates with the authentication method 
    specified in the ´AUTHENTICATION_METHOD´ secret.
    """
    check_required_secrets()
    login_button()
    logout_button()
    return

def check_required_secrets():
    """
    Check if all required secrets are set.
    """
    # The required secrets for the paywall
    required_secrets = ["AUTHENTICATION_METHOD", "CLIENT_ID", "CLIENT_SECRET", "REDIRECT_URL"]
    # Check that a PAYWALL section exists in the secrets.toml file
    if "PAYWALL" not in st.secrets:
        st.error(
            f"""
            Please add a PAYWALL section to ´.streamlit/secrets.toml´.
            """
        )
        st.stop()
    # Check that all required secrets are set
    paywall_secrets = st.secrets["PAYWALL"]
    for required_secret in required_secrets:
        if required_secret not in paywall_secrets:
            st.error(
                f"""
                Please add your {required_secret} secret to `.streamlit/secrets.toml`.
                """
            )
            st.stop()
    return