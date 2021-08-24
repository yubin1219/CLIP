import os

google_drive_paths = {
    "stylegan2-ffhq-config-f.pt": "https://drive.google.com/uc?id=1EM87UquaoQmk17Q8d5kYIAHqu0dkYqdT",

    "mapper/pretrained/afro.pt": "https://drive.google.com/uc?id=1i5vAqo4z0I-Yon3FNft_YZOq7ClWayQJ",
    "mapper/pretrained/angry.pt": "https://drive.google.com/uc?id=1g82HEH0jFDrcbCtn3M22gesWKfzWV_ma",
    "mapper/pretrained/beyonce.pt": "https://drive.google.com/uc?id=1KJTc-h02LXs4zqCyo7pzCp0iWeO6T9fz",
    "mapper/pretrained/bobcut.pt": "https://drive.google.com/uc?id=1IvyqjZzKS-vNdq_OhwapAcwrxgLAY8UF",
    "mapper/pretrained/bowlcut.pt": "https://drive.google.com/uc?id=1xwdxI2YCewSt05dEHgkpmmzoauPjEnnZ",
    "mapper/pretrained/curly_hair.pt": "https://drive.google.com/uc?id=1xZ7fFB12Ci6rUbUfaHPpo44xUFzpWQ6M",
    "mapper/pretrained/depp.pt": "https://drive.google.com/uc?id=1FPiJkvFPG_y-bFanxLLP91wUKuy-l3IV",
    "mapper/pretrained/hilary_clinton.pt": "https://drive.google.com/uc?id=1X7U2zj2lt0KFifIsTfOOzVZXqYyCWVll",
    "mapper/pretrained/mohawk.pt": "https://drive.google.com/uc?id=1oMMPc8iQZ7dhyWavZ7VNWLwzf9aX4C09",
    "mapper/pretrained/purple_hair.pt": "https://drive.google.com/uc?id=14H0CGXWxePrrKIYmZnDD2Ccs65EEww75",
    "mapper/pretrained/surprised.pt": "https://drive.google.com/uc?id=1F-mPrhO-UeWrV1QYMZck63R43aLtPChI",
    "mapper/pretrained/taylor_swift.pt": "https://drive.google.com/uc?id=10jHuHsKKJxuf3N0vgQbX_SMEQgFHDrZa",
    "mapper/pretrained/trump.pt": "https://drive.google.com/uc?id=14v8D0uzy4tOyfBU3ca9T0AzTt3v-dNyh",
    "mapper/pretrained/zuckerberg.pt": "https://drive.google.com/uc?id=1NjDcMUL8G-pO3i_9N6EPpQNXeMc3Ar1r",
    
    "mapper/pretrained/Anna.pt": "https://drive.google.com/file/d/1Vaw5GPEWlLn7DReu8lOfj4f3A_t-KHsl",
    "mapper/pretrained/Bangs.pt":"https://drive.google.com/file/d/1EaxNeAxC2_cPoI-QyL_VZNp-yg79xPw6",
    "mapper/pretrained/Blue_eyes_wavy.pt": "https://drive.google.com/file/d/14e0Uqe3CyDPY7nSU3iLweJwKj3EmltvF", # blue eyes & wavy hair
    "mapper/pretrained/blue_eyes.pt":"https://drive.google.com/file/d/1Z0s2iNaMlhm0CHjtGbvEL3kIdqF5Wq3e",
    "mapper/pretrained/Cold_face.pt": "https://drive.google.com/file/d/1sUAqfc-7Kxm7kQieMxq5eDfOSNsAwUzt",
    "mapper/pretrained/Elsa.pt": "https://drive.google.com/file/d/1YDyYL8katr6yvY_EDU14EOpE7Ay3i-83",
    "mapper/pretrained/Emma_Watson.pt":"https://drive.google.com/file/d/1LjlunghdYG91Z7XZiBEDeht1WTIAHGNO",
    "mapper/pretrained/IronMan.pt": "https://drive.google.com/file/d/1TLYiKHR3i0_W3uiQ6TqB2vggjn3Gzl6o",
    "mapper/pretrained/Moana.pt": "https://drive.google.com/file/d/1ZZJBI2qDRD5ZeA0QqPrzXChXNx9qT8RU",
    "mapper/pretrained/wavy.pt":"https://drive.google.com/file/d/1VEtSxJ8yu6PL-pwj5NOz3Q7VwUFtSZQe",

    "example_celebs.pt": "https://drive.google.com/uc?id=1VL3lP4avRhz75LxSza6jgDe-pHd2veQG"
}

def ensure_checkpoint_exists(model_weights_filename):
    if not os.path.isfile(model_weights_filename) and (
        model_weights_filename in google_drive_paths
    ):
        gdrive_url = google_drive_paths[model_weights_filename]
        try:
            from gdown import download as drive_download

            drive_download(gdrive_url, model_weights_filename, quiet=False)
        except ModuleNotFoundError:
            print(
                "gdown module not found.",
                "pip3 install gdown or, manually download the checkpoint file:",
                gdrive_url
            )

    if not os.path.isfile(model_weights_filename) and (
        model_weights_filename not in google_drive_paths
    ):
        print(
            model_weights_filename,
            " not found, you may need to manually download the model weights."
        )
