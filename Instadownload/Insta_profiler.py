import instaloader
dp = instaloader.Instaloader()
id = input('Give the Insta_id: ')
print('Processing..../')
dp.download_profile(id, profile_pic_only=True)