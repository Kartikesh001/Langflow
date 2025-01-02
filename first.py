# Required modules
# Install them using: pip install instaloader requests
import instaloader
import requests

# Input username
username = input("Enter Your Username: ")
instagram = instaloader.Instaloader()
profile = instaloader.Profile.from_username(instagram.context, username)

# Download profile picture
r = requests.get(profile.profile_pic_url)
with open(f"{username}.jpg", "wb") as photo:
    photo.write(r.content)
    photo.close()

# Display profile details
print(f"""
Username: {username}
Followers: {profile.followers}
Following: {profile.followees}
Posts: {profile.mediacount}
Bio: {profile.biography}
External URL: {profile.external_url}
Full Name: {profile.full_name}
Username: {profile.username}
Is Private: {profile.is_private}
Is Verified: {profile.is_verified}
Is Business Account: {profile.is_business_account}
""")
