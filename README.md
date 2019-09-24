# NFC-Handoff - Hand your Music to an Amazon Echo

## Showcase
https://photos.app.goo.gl/g2zqJhHCFPAALcW69
## Introduction
The idea of this project is to imitate the new feature of iOS 13 which is used to hand your Music from your Apple device to a HomePod. I personally own an Amazon Echo Dot, so I tried to create my own "Handoff-System".
I will share multiple versions of this script depending on which Streaming-Provider you prefer. You also have to know that this project mostly depends other great projects - you can find all of them below. 

## Credits and dependencies

 - [Mike Brady´s](https://github.com/mikebrady) incredible [AirPlay Server (shairport-sync)](https://github.com/mikebrady/shairport-sync) and his [Metadata-Reader](https://github.com/mikebrady/shairport-sync-metadata-reader)
 - [Paul Lamere´s](https://github.com/plamere) Python implementation of the Spotify WEB-API

## Prerequisites

 - An Amazon Echo that supports the streaming of music
 - An Spotify Premium Account that is connected to that Echo
 - An Apple Device with the latest [Shortcuts App](https://apps.apple.com/de/app/shortcuts/id915249334?l=en) installed
 - Any kind of Linux based system that can be accesed via SSH  e.g an Raspberry Pi
 
 Unfortunately Apple Music is currently not supported for the use on our Amazon Echo because of its missing API. Nevertheless we can use it on our iOS device to synchronize our music from Apple Music with our Amazon Echo. But you need to know that in this case you would need an Apple Music subscription for your iOS device AND a subscription to Spotify Premium for your Echo. If you just want to synchronize the Spotify Music of your iOS device with your Echo via NFC you ONLY need to own Spotify Premium.

**As a result there are two different use cases:**

 - **Method 1**: You want to use Apple Music on your iOS device e and transfer that music to your Echo which is running Spotify
 - **Method 2**: You want to use Spotify on your iOS device and transfer that music to your Echo which is also running Spotify
## Method 1: Apple Music → Amazon Echo

 - [Download](https://github.com/EvilShark25/NFCHandoff/archive/master.zip) this repository and navigate to the "Apple Music" folder.
 - Upload the "nfc-handoff" folder to your Linux Server and note down the location
 
 
**I. First we install [shairport-sync](https://github.com/mikebrady/shairport-sync):**

    # sudo apt update && sudo apt upgrade -y
    # sudo apt install build-essential git xmltoman autoconf automake libtool libpopt-dev libconfig-dev libasound2-dev avahi-daemon libavahi-client-dev libssl-dev libsoxr-dev screen
    # git clone https://github.com/mikebrady/shairport-sync.git
    # cd shairport-sync
    # autoreconf -fi
    # ./configure --sysconfdir=/etc --with-alsa --with-soxr --with-avahi --with-ssl=openssl --with-systemd --with-metadata
    # make
    # sudo make install
After the installation is completed we have to edit the configuration of shairport:

    
    /etc/shairport-sync.conf

![config](https://lh3.googleusercontent.com/U2o5TuAFDDtjxZ8CAGfb5ig0ADhSeddh-EZwHgx1hsp5ilIa8E8wRXA07ToKJTCr8ccsEEKOxgVfOkNXiRFEIIaJRmiKKejGeCPcJ86SGAjTa9T8fmMY7Q8M1HBKe3bSrv-txVUVuKKVkY2NW7KIYo8q91q_OnMYO4FRNB7MkwZ3hCw9AwIq7NdVuzHTt_uaZyyNsxglSyx7h9RYS9LoSwnXVvJtBwbO4VVlHjOrvsJWcQfbjOF_guV-OWrOAzXcfWyh6SaGETrx8WVqQR7IVJ_MSyGygEuUq74lEQTUoFm7aq0FGXsrBLcL3-mWriZoGtqck6-6tJlVbegq2o5ar0rQnEEe0AVU7ZMOCTrHiiVgg-KtqZH30mC3Ki81GOUpRjLu30oaDpuGk2vH6iaYiq9gIKtfX8rU4e7lDHOFmiCCkCo0YBxWr5SF5IE8ImD9wRROAiynRd8dRDgeL_21TBMG5shWZ0IhO0u8Rp5-b8vR2gpcqR4qFUG7rlmY4LsC5wgh5bMzakjmE0dZB8EJee4SX3flee8RIgnIDOwBSIzYndK2Xmvlw0NK14JpkKXLnI1QzSGbV9mP__eiqGS7nY2QuKNDRRvoiHUaMpHyQdm1SBK1t8iAigP9iJVgbKgjUUAThWDKJoCZ7zK1QiLSjiJLpx73No_FdmcBSYocTAHH4bkcd5R7fQ=w1388-h233-no)
Just copy that part of the config

**II. After that we install the [shairport-sync-metadata-reader](https://github.com/mikebrady/shairport-sync-metadata-reader) and start the AirPlay Server:**

    # git clone https://github.com/mikebrady/shairport-sync-metadata-reader.git
    # cd shairport-sync-metadata-reader
    # autoreconf -i -f
    # ./configure
    # make
    # sudo make install
    # systemctl enable shairport-sync
    # systemctl start shairport-sync
**III. Now we install Python and the required libaries:**

    # sudo apt install python python-pip
    # pip install spotipy
    # pip install git+https://github.com/plamere/spotipy.git --upgrade

**IV. We will now proceed in the [Shortcuts App](https://apps.apple.com/de/app/shortcuts/id915249334?l=en) on our iOS-Device:**

![enter image description here](https://lh3.googleusercontent.com/4zd6GpqONkC2CIocQjtBiMZTb-M65tnS3V0cCUcOwCsRev5bpIJ4jv10Rtr0N1oIe1z24mIpRX7B79mODCmH-7-T6F_xLVH18TQt5ycoQ6yor-zDZOy0ZwGQmk5fvRjYJz3hSjdRu4aBRf4xRfielM2aZnSA2_1izTva20EWUfurGuhhc77ia78hT0uRXF0aDB-oU6w75pf_XBFKa0he4pwd8sIF4WcY19n0GA4n_o-Gl9KY9N7mhruubZQlgohg9C6wxX8v9a84Sl1V_95AQYn2PFAMYbOKTEhJIB-RBuCoIosL4BNhMALh-HG2RV67nMjwToXJdrKOdQ1JYVgLkQfcbOW4ySwJ9Qr_XCl4SllqC0upCt637gbUSbGA85rVAOaufvXPnPCyv76JTVNWu5BV4ONSJVRyCgEOKOwsIYNRcPyBmh1nXJRQhQecvjkNTd86wx5TFxoJJyYqpyanUfYsf3jP7nZ1mrypsGjtkwvDrBbaG_999s3ApYcITtEUumf8L63892HL02qYglBQnzqKDfTTq7CKMxeiFDmkq2J104O6QFBMmqWKRAnntLW2xLrOr-hZ49XZJnknlV9KxNiznfVr2ZBXMol4_Kpk7PWm6wWblcunBG4xMGVwyhUwrDFdkf2Stvdt8u2TmzMR_aV-sN8_Fl-BHPBXLVUpkeG2fVjelW_h7sHQFzy5qk-kr6G9hSuxvOtRQhj5zUOruLY2X17FBEtdKmeuQFhWhXogezI=w437-h944-no)

**First open the App and create a new Shortcut** 

![enter image description here](https://lh3.googleusercontent.com/Sjkuct_1WJSYIHBtZZzDhsLNuNLk-j55G9kWKb6psNHrth-FWr9ZAFOYrRsRkbsoQaxuJ2nCGMbvIh_EEpRtBSr5Bdci6ZWo8-ln7N3Qww8ZgKfEPuW84LMHEvCR8d518sSL3W3iH_LYTN79EtyUqJbC1HgzM8gscRAkVhTfP1IqoHSgmDlmRyvn9CEcBS1MNdm5K22CF6SF7tEG7dE1j-FposQGCZ_-C6Jds7crtJ6qRVRj0c_xoVMvLp99PZortgsyXLSwFfJmz1TlTpq7zUt705hcQd16CuhyzWa3Q9exqjcT0Wi7vC0Ojwt68e0AoQGD4UqZzEaHMl6zSUFjcZM-uOvwmBMbXdCSg5gGaQNnXgb9ShtsD69pDl7n_QiQz-b8egSzyIagTUN6zV7A8OW-7WpxjNFxwtNA0HoRsDebISo2cXIgZjNgm0iPelFgZWLWwj_JVz6XElDhjdDe05Ck5uY2T9bsgAdJnZXAIMrIT1bV0LLw0aCf7NL_jgSSHYRBFabEAw2kILs56l-CTVReiDPS5veaPpICTWUrkoAkygxrBVdGo4Buu2rFUJTZJDmzTsMIFJLSpJ4xelA5cbkNLg76n6pb8GaeWxJrfNdnVLCZKPxjYvRW3aCX5ZKS3EUJAvpLJqxHfhq4FKrK3NF-iI_gp8pIT2t_nSXOyx2k76vac6bsRpMzPXCLKTw8cY9Y44beJc-PviIE2nhCh_eFxm2Qljh0E5pAcUUDg1zOJyk=w437-h944-no)

**Click "Add Action"**

![enter image description here](https://lh3.googleusercontent.com/KLyEuFbVXGjBF03RYtGvRP8Og4DcX1vAwIRpt-WdJGCYE79Ot1cPqEhH3vT16SwZU4T7sK5arQ1k8AS3A8QFJco2E1xUaSZoK9bogLNWk74lwJKekzMUvH-jzZrUm1tieelFTE4NZw5zwHj9gDk2X5ypibnqNZN_Ocvfq9O5G8GxEjwQSaSxdLoJzex9mbguq4FnaxRsCBNyuay7WghdwVKeKirr_szra7Z0HXXd0TXRsSPd59EDIGKmDtvsMQXMZjkKaJPPHGiB2t2qQy0kE7Zf5JvcgKvst2qsLcUf4RkK_rDMwyTWiDVVzJ8v9g6ZBE8HmHJviL6z9VF7wAX6EMHfG9gsDzq_3P0VGNRT-vL5ZNCgnfN8DAHHpLe9Ua6_4viZnw7SKxnChyWlB4T__vFKfbjJXQ84uBfJzcfqzuKoYMm17KyfeYFPgWM81H3k3wa_6HMkrCAZcgPv55kvEVr6zGfkqod_c23o783NWZ0cVIbUIRBMmDt3dmP4tpZK23yEAdlneGKw9j5w6nfS_oGOn6r2Wj0BTg-iRbR4Z1nVvv1RR-Lsisi7B0wwM0speW_JZejzVVRoCDr-ic36Xz0SLU8nuEgfJc8tC4oGb7bsbZSv142590WCl2GmDXVc4ZjTQRg6dAyJ9udOlwycI_JY0oiQlfa7yKZYTllU1GzfC_7PYaJU-75CyicICslPHKQ5Mn-T3pGeLk3s08baKZn7dv6f7lWeGVgPmG3d2R873WU=w437-h944-no)

**Search for SSH and add the shown action**

![enter image description here](https://lh3.googleusercontent.com/pf6Ba4nCgLsWyR0st5a-LYHLSFzP5TMgZfBe-Z6EP0vl5L-i-5zMCiCYCfAVkH3tRLQPSdR5hcSR2JFMgZ0p3-GH_wFY6uG5jBu9ZadrFHWHhHRIlS9kdxeaH6D6iTaWHhsnogdKelh85r_j4P6f_7MetK1saesKAzuGSQXTvK0PGGhh_jdKL0Ss8NBBhXxWUIKgQojxgJT-ScxO_qz44Sm0jzO8YGLOAGAM18WynBz0pBGj6zhFXQ0tsWL9pRkNTKasdyN6D_tjQ8R8TcpLF_6T3eK3bBpUZ14HgLa8MaBs48nE1ed7A8OivJMfbt3HzrfSNuv2esx3wCtGAWMk2E6nBBn-H_0bfmw6f9EJJlMiQFhUFHBhjHizb2LsFBVpMKpIPKmG5bxYMeen0ZB6Fjc_KTpeY8FiIyBBkjb2kOpMb_G7yhzJqaDIUYCeBqvIJs2pNgauE549ijRP-gk5FNnYmA8Of9kpsSZaVJOoT4PpaVBRj--cPRrbJ-dg8c-_CfBt_76BFhMPtY0P2KESWyDaxTj-0_mzwcpJa25klEcNsS2AgSICA5TAKn6MlI7n7ecEI7NCID20C8ahTZpkjOJDkkA3-xM0Yk79DGKGZxLcXA-1cuxupKrUqegWyN-xiGV6IdrA9JrZjS6jOK01hQRx0mu9uir5pu3E0PiQdnJcQj-d4VDiLOP4Xigi4rtxyEhIhoVzace2Se0qtrMSaKTS9cP22nib4fA1jd4EVf5nJgk=w437-h944-no)

**1. Enter the IP, the username and the password for your user account choose noting for "Input".
2. Enter the command you can see in the picture and adjust the path according to the location you have chosen for the "nfc-handoff" folder at the beginning - DO NOT change the file airplay.txt, only adjust the folder location!**

**Example: You installed the folder under /opt/nfc-handoff/ so you have to change the path to /opt/nfc-handoff/airplay.txt**

![enter image description here](https://lh3.googleusercontent.com/n5fWrglTDCnwRg464GRh5L1kzDUwEnxguR2ejdGdskersz4PjjDQhbEXN5Yw7cJ4t_rSVkBlSdnYJL5mzuahlY99R7h4i6hvClZEAOJu2zT6-ddiqWkRtm-Y6HUmSWAGjE9vWtLJJaFHeXSfAZQ1PE7i2IDqlVOV87UvePlyCE20INXpuHgGmpZnZ6RClya79rtisKQYPgPecxQw2FDEpWzSpcUa1MIwr6P5rNiB8Zz1gaDamjYmZNB1RHHSQpaWiqEK1Fzjjszp0bqZj7HNgt7KIxTXtNdoomFdBe7uDICupqnMBmhmEOIQdIB6dWRFSoXNuOlZoBIKfwfHiwmGsOMww9Zd1ej17SRRE0n1cWFNXCW_Zq2okz0_s3eZKQh-bwN8uV_vGty2Qm_g32C1s6XT3OxLO6eWQQI_FVO0FRb29hH0V59I7bg2IXQEvZilwozJR1IjN4gVvZm9AbWjEfZRSJeg-vlxX03j5QAaaYAff0KXHhVv_A-HZNSbUlqZ3MQrMrfY0eA5-0e825xDVqiqZpElebQmPcWtu7SADLoVOECdYrre3bOeu0Uya7lYWD8yaHgPMhaqllf5SCiNvyz6GqME3kAzpgCSiGWu-2G3ceWY8bJLZQoRhUXvnX1TdPQUftEI4pVDPFAvRMHShuCZ63pOCoZQ3gKytRI9VIXrLRTC7fCy7AkezwqS3VLpA9M6TmpgV4iSe6vmiaufHqkR0EV459bzHN38edQ3jWVMfnw=w437-h944-no)



![enter image description here](https://lh3.googleusercontent.com/eXekDfAOv7AMKn89ph0dqXsMJlL1VEgxdSg9intxQx3rpvkCA0urdutGXyonCUyrtSqfI0eSV0BwEPrR0W6ZJUAErFuw7BKskC9HoFQZ6ivdLxFAYIxGrYEUUx2eWD2E2pWyDPydfZCQ0xHD4mWklTIwWpr3-xiXDFP4FMrw2QuN9cymYA9AMJoVf5MJXRDvGsG0Rxry4WgB903hPs9DuKDKv9pQGx9Vh56dB5niwwCfNELZVcJDL74xl9nEpbsZTIQU3g1MvfclZERpE7YjBQ0RLxtHejDmrLQ9z1cgmdfiF2oIOJq8lOistsy49mxWwvZVY_R9nlsW5fj6DSmuJ_rZbyawWi5W9wfZwkaz7VXnTN4hfTutvePVef3ncsk6_iYn3FJ-htC9vt2fMCR-8Ls3Vfx9pCj9xOWkTKS-4CQtidi7ZwAbQKR8IFpYyrMEJbOsj3oka-FH1pNYASHao_2_ilCblzoCKo8xmQqywFveHpLSi27qIHzZLutuVdcLI1_9zpxy4i-PxD4gQzVSZoiYeyxeTemYctw8xpSu1ppkJwQrABXlAb4oIrayoOzB4nBhBsYRlA6DR85aSgxVXPdia1g1Ksqw1gHgJ35d7hfLFHgP6FOk7Bg90l4UR0IOWAz5NWOi-HdFhU-LiFYSbaMz-dma2rFdnnwBNuy9A8h4ahUzrADAuJauwxOq2U06vqY6OIZEi7MLQBT119Zp1S7QB9gNxa_QQZr4LCuSf0N1A-o=w437-h944-no)


**After that you add the two actions you can see in the picture. For the second action you have to choose your Server as device for AirPlay (Second Picture)**

![enter image description here](https://lh3.googleusercontent.com/Erahui3lTu6tgQ19n9Ktt5YL4xWp8S8gZlXIv0FWDOtwrCDvuph5Vpu-cH36m_jcivzmU8vSk9JrKvVEmcbDdfZrzomUmMrZ_bqgWU_YczbyiQZQYrVCyBr5KIYxaTnTf84iytRngSX5-U4FrF6fFBpunxoJIbTAcWkoCCU525JHL0pP6uOhXqJ5IUaEw4kGeBNEmyIbTU9KEpaB2Ea0_bmaDt5nHvm_AgY_Rngug3QYQ498eUmElCNNGSYGHDZNx-17_lwntGUzJWiQW5_eosPUEcP4oGZD933-fQVCbG5YKjenOns77hI0zk8tGSjJ52xJW5zLyrNhmLRe9cGqiNjeVYFithzH6ay_-ZgNNaew_bzkxKO-IqB7zFDTxtpj908TFV9yt2wothcKpAtIzeBXRG44u5xgv25LTOAw2SfNAw9Ug4NsJoqkXjDbBXt2UVvKEqsoRx5YPT1tLH7ol_szzNvIDkqA-htCngdnSxAtfKknwDMD3rfp--6Ys_qLqSK9kCsBuuQl5RMnbLfjnQVv16YFMJo8wHh7ngBRNTidVmzGFrWFMd1ef0NQ_9NrkOkGi_6oM31axFo0t7dwJZ_Ns6JGLX8b0RMewDlpJ00UaB_RNjbB0TRKnCZ79GCJjZv8CRpXjh_mhzeJtguJ-eKJwUFMEcCy5PgUn6yYLSioEasQ42jyXQJmfMlzpjKGvI8c6VBS0FwK7apdlPX4mhWpm_jZaP7Eacqp8su3c7d59xM=w437-h944-no)
**Then you add "Wait" for 2 seconds and another SSH script
Here you again have to adjust the path to the folder but DO NOT modify the start.sh file**

![enter image description here](https://lh3.googleusercontent.com/Gi3Uu_VAgRCGKJJWaoDOmyZdUGqT_z-T2g0MU_dtHlyTVC_0kd5aH2NPHchY_ZU798WxaSVXPhwoELwZsc_vG5jhwPkrEmxNHzES9ezcJazJf3zaEvB6Op24M-GmpnRtJ6v9LoInZpR12bVr-j6U0FrzYnvq0SeuOA3kh_4WyAHz4w_gd0pcxxKS8Sm2NLusxOJ-0BzmqaEnZXRYhJWT7ES3iIpJaWqQ6-NfcclS0HawjRoI2HN8bm4NpLh2WN_IlDvfMaHPIsV5u0lEio2U3yWf4D9p18FOvDJUST2d10st3e4kkAqnsM5HQkOxI7IcYYuP39cisZGCM8kL9uwRKGgYrRntoqqobWCkDjiPPQ_EsTwogd8TdQsjhVqYCcLtke_dOVblnxqr66BcMuqD0LsTng1bVGDY9xWpcOrxWYikGi4jf6a2ghQiG0MZkt-ZcOz3qiB1idJSLTMXBI1UsoAU0o353NT4ioFMPB1L3i0f19o33jDoUrl2eOheel0yGaCLL9TE8Dfuz8XO8OaxZpzOkreJiLn0g5GNYG-CRGsfsBSBOGMrOxoN_AnEJY_itu4rXixLjnl2rjnvjhI0VsGcoMdS_7jkDxNPRaVI0AFMxLOpJRcRm-xGJ-HbhR6g27iq7uJuDVtUX4nfnHJjQiTVqa5SpkqurFrXbGakmOWbpQbh0pOO5OorqToL5byr8_hEykEAGJWf3JvUlSa2mfkglTodU5mNLNQRVergVQ-4LcQ=w437-h944-no)


**To end your shortcut just add these two actions, click "Next", enter a name and save it**

**V. After we created the shortcut on our device we start configuring the script:**

 - Navigate to your "nfc-handoff" folder and open config.txt with any text editor
 - There you will find the following settings:
		 - ClientID: ID of your Spotify Developer App (see below)
		 - ClientSecret: Secret of your Spotify App (see below)
		 - Username: Your Spotify Username
		 - Country: Your two-letter country-code e.g. DE for Germany
		 - Device: Not important for now, we will configure that later on

 To obtain the username of your Spotify Account open your [Account Page](https://www.spotify.com/de/account/overview/)

**How to create an Spotify Developer App:**

 - Open the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/login) and login to your normal Spotify Account

	![enter image description here](https://lh3.googleusercontent.com/pIwbLEp_ooZzjklnE8c8nDbXwRqgkt3OtqBgZgxKvlIQfrj8NItSqH8MQWL2c2oAAGLwfYt98Qygn3J1AviOdUfLL65vOB0ncrI6Fb1Z1ETgj_TGtCXh4i9YbZipq4GiUVgkVWdsQFkOWwz3gkblvCKtSUe3gYfhBzwcqq0wTa5wxg93kIA6ZTW6_kN790gVelufZUn3-OOqn_gQk2Ww8NEtTt-E8YqQ6iQoNQcdhqKAtDwWWZLJsGyWSuadOvPA2dD1xVdNidBfi-K3ftFJpe9Y3fWkoolrq1GLYMpzbuKkVe6FjHTfCp0Rml0LbQH7MrTb0nUYKwofmBdzqnbx-QbqE4q1raD5Hmj1FpYlSJ-MR_B3SFhB2hVaF30gA17qmGICLbMRlITwjQqlgkqLJ4PHSZW92Vn95Tod_kLM1n6_zbcOSG6r9DoB3My66jYwGszdUCP4yUHsbyR2-swLFAtX_Y8_8HU3bz0XQwMrayRyJlf57Q2TOPRl8cFEQCnJy547xSVAfcocy1BavpfJ6PWESDFS6hv0zq2M5_aVpIh0ZiMUXa1-qdvCuJ89yuQveGAL-5nWVFomT273IBr_1YnXZJuS-3q0C-6UPJVZmhRSVWQPAXSATdWpZqG5J1LVXM01d939xKUN_VqC2y6U66cWL4ireI3CLgurfYoVVC-YHSJdp_8Kl4Pd29caaUm91xt2HnXDXaCzGAsUzzpqChygtsvhT5X-tN3lfJKB6Ai9XM0=w1560-h764-no)

 - Create a new app 

	![enter image description here](https://lh3.googleusercontent.com/ViH3GJ_-yweLglsW_1Gq7mO-DBSqFmoKQJXI0ywzEhcrteGCury0CMvUlw25rPPP8sPsffx5cym7D4TR_U5fXb90uJdxWTwdhOUU3az6wp-bQWkDGV1sed_ypalkuycdzbUYcsRD8rw1AMo2FRxgUe8harrKVNXt4EcR3IG0gtmGKrdS_oImqHlzOaJn8hAUbzPxDZbvjq2yIaa79rJoZXo4-baxuc0u5VryiJfybafQbHeFw7TTNxq-DPLWSgSF1rGQ4QOqGw84mnYU7q3bIZvzz2j8BoFPOhELdWY1g_UW6xJb5vBsCdM-zIvjw92RvoLdyAU6fyPhArCagKkx-6s5Bnb0Au2s4ylUIgGO7lumHRcujZkVKRjE8tuwXACmzf8ZKqI563p4Ut0Ful8tABDNJWp7bIMOdubQLgQfGzT6YeBsjXT7GHHZHGM3D8RwHwZ3GvjROwtH9-YKKf_19dnUZvofkz0Ifv3CrNvjT3Nm_9WQup5aYH0EwEyBnu0SMegmDAG0DIuoPmAqxP5QBorZsFqpQVHgNOiZXjFCg6aUNvIHO8B4tUV38lQ0Hag7Z5K1dwz7J6An6EHVUuH5rUIp_mLPmBzenkLQjXIl1ee-lR_aIHed9tMruKb5QLi6D1P4kvNMp3RekuZGcu7ublGQlMli75mZgpEPxTJE4zwAAexG_rFdaACO59Bs0NrfrA5vUp-Hz7tBfDbykD95wqEb5vs0cZu47qBf0AWm6lWT-Js=w498-h819-no)

 - Enter a name and a description, select a project type and click next
 - After that you will be asked if your App is intended for commercial use, just click no, check the three boxes on the next page and click submit.
 
	 ![enter image description here](https://lh3.googleusercontent.com/k1YTFEpVAPilpVddFaebg-06KsIvvNjZ_TjTmG_0xvDpISqs9M3FuJGLzIlMcTU3SMOXMz0ewfmkRhAMkmJeUr1crqOnPfyKAi5tu3gXY_-MgUGtNktDhg3zE2BuWjEuZ6z9eewjef6MHzQ23UDjnBrAxvNDq432lxEveNo1sftBlxrVg5qHav-EPTWhhKMliN5OlP9guy6L8E9Oao3Mpkr5xbvRAQf0qET37q-RTU6iqbvfFUWcYrTQrT00GpnSEWDp4vB4Ajxc8lE_FWBA4cOyctjfVpQyDLZVUhmj8BPfJ2jpjkNOSuySGg4xMuGizEzWGzF1qYRnVI0Ae3rTHV_cex7nxqdPb-4D7EUNIkHJ85HDxFvHe4NNabgzxjZ3LOxe8zOPsyDPfEf1JSNMb3ItbOvYDyaxRWIh_jw51SMhJXvYgH_M3sPiH0ez5OlsfdCcvhSYBa9ljlBpK2yDLnQ7u8lDXPfqc1nCJeqSfSTxB2p41eBlYVPMTdny5zRLQ5xUZ40OdE4rvyrIejIwq_sm4WCkX6jY5u1SyU2KPMLz2nNG534sks_YJqQogfP3bSR5aPcfzKjbdKTHyuuuA6GcJ3k6rYpsgllyrYHaPzXJwqDnmd68U2wQ-8IN6Tte72F60b5LzRso6co-a91_raA5N95pkSgyDG6UiMI1DBZBxH9aNZqSHkLeddxJIfGBIvgnHzJH9vwqhcUBxar4vHporgY1UBpSwCwXzCcMzi0drnc=w1560-h650-no)

 - You can find your ID and Secret on the App´s page
 - Click edit settings and add `http://localhost/` to the Redirect URLs and save:
 
 ![enter image description here](https://lh3.googleusercontent.com/j2c_TpGgBzlOSwsY4Z0K5TlQ5Vx8bvtK-p3AjacXvJ_AFbJy6YcAZH09l60BhyQbxPQfSAhSTyYs4gcGDz5MFrL3AR51ZAG2K2XdnAa2pYpzDsuM44WCLmtJ16CrKrGMYcJTGMV_0RryIAnoS3VbNZgf6feRhFdStbx8m3wL9SNtlGBPxu8attwAaMc9Iw75-I9SJyyiKGqOlkm8i-0n2WLt8wwFNMsoltCxao9e3Naz9MIxdETrMGRCVVjbjDX0tBYs7Snma7zhN8tO3jjB2Pe6CaLD7JMQ0CbhQsqhMZdln74DHS-8PxPkhnB4cVYOpCDQxqR2E9MsetizI-Fv-hsGVRfDs92gd3a3FJt4XkZtj4A-Kn11q9F8FviCBxnLzxtHSVjmZCpmYAxuDZNwA2yJ1FFIpFqCMhuDgVIAbrnML9rUo_LE-DrILbNRl4izKbl1w4duFLJRUB4N2HHIngRXPmUIAuLdPglZcuotVKbzJOT2FF0lbO_ixXT6M44Y29Us4CgH5GK11kmXlBAg0_z--kiHyswnk6MmDECWAMje-cMfmj2MAgLRvIq7PbDnO6zxBqyu4aAJru3pdB-ZdTq2oOSbnb3F1_6wbHLFX3VSe7GAvLr-iLg81PiulczAe0eMxxoNu1wNVIAzKYgwAhbSCwqMwHmOaB3ex3dRLG7N7Ujedi-B1Q=w526-h937-no)

**Now you can fill in your data like that:**
	
	
![enter image description here](https://lh3.googleusercontent.com/839i4UVwhf4-rpZz0KGYCY3j6eNX8E7nQYGZKwMZO5WvvT_G4MngH24WPKx7aqawtw7_fADGWermBNLDv3dDQkfLIDBaLOiweDvCLi4RHy9IJuv9Pe0xbVwnq_lIG-l_ha_TRnfl8q-73MchM7hWdC286GVprDsgYKlESW3yIRUnaI4oXc8BLNd1exdrrsrkuUpnrYC9W2oXxYPzPdPqJ0LtAq2E1goTaGqRaP5Bz1uAZ9hKAimMuIElz7YSHjzDCr5YD1_SDLuMgwpcNxzJUabdGAO2wlJYbMC9GkpK3aKj_N_1FF-1FRvdj1-oFb3Dc1lUMD1OSS9eaIpQsthE680AhG3Yej6DPwJfDVxTwwhSCUqov_v16fbB6V7pDAygW6S8BRe5qEUqsc2q4Vnuj6ckTdeLIgeCutt1Evss0GD0aYR_T0d98Z9OM5nlrKuHPx4Kn7b-plaYkXev0pzQpcI-biYFyMwQ7Rc5zVQPODKJva9zzz5GtF7xN27NgI03J36obaxzDR_SNoHrme1AyUxV48wJ5ObGjg7IF9_XccL-oB54UBWs4Kk6Px558ZwxIU8u-Ok55QWALmbhwbyOHqRzcHNSYBFwIEYMF2W0rfwkTErvJ0X0gnl7DHClETutUi9PfFQwZ0GoK3WF2CL980_9INlchsubHg3l5DKBODPDmvcReKdXgde8Nb32KnmkNKTEa2k07yv6lVFOWkvMIxk3ymiqd-qVWmWeMCcTjxadaM0=w396-h81-no)

**VI. Initialisation:**

 - Execute `bash getKey.sh`
 - If you filled in the config correctly the script will show a URL starting with "`https://accounts.spotify.com/authorize?scope=..."`
 - You have to copy that URL and open it in your browser
 - Enter your Spotify E-Mail and Password to authorize the Application
 - After that Spotify will redirect you to `"http://localhost/?code=..."`
 You will get an error because localhost is not the valid domain of our server, just copy the link paste it into the terminal running the `getKey.sh` script and hit enter
 

 - After that you will get back to the command line and a new file named `".cache-..."` will get created
 That file contains the so called Authorization code for the user you logged in with

**VII. Get your DeviceID:**

- Execute the following command: `# python getDevices.py`
- The script will output a json object that contains the devices that are connected to the user you selected in the config.txt
- You have to look for the name of your Amazon Echo to get its id
- Add the obtained ID in config.txt under `Device: ""`

Example:
The name of my Echo Dot is "Davids Echo Dot"
After I executed the command I got the following output:

    {u'devices': [{u'name': u'Davids Echo Dot', u'volume_percent': 36, u'is_private_session': False, u'is_active': False, u'is_restricted': False, u'type': u'Speaker', u'id': u'27aXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX7213'}

 You can see the name of the device, its volume level and much more but you just need the ID.
 The ID in this case would be: `27aXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX7213`.


**VIII. Finalization:**

Now you should be able to "handoff" your music to your Amazon Echo by simply starting the shortcut on your phone. Try it by playing a song from Apple Music and starting the shortcut in the meantime. The music should pause on your phone and continue to play on your Amazon Echo at the same position. If you encounter any errors review the Troubleshooting and Known Bugs section down below before opening an issue. 

##  How this script works
This project is based on 3 different systems that are combined in a Python script - `nfc.py`

**Part 1: Apple´s Shortcut App on your iOS device.**
This section is the trigger of the script. If the shortcut is started different SSH commands are sent to our server. The server will start the required applications and the Python script. The Shortcut App also takes care of all the things we have to do on our iOS device (e.g. play/pause playback, set up AirPlay, ...).

**Part 2: [Shairport-sync](https://github.com/mikebrady/shairport-sync) and [the corresponding reader for metadata](https://github.com/mikebrady/shairport-sync-metadata-reader):**
[Shairport-sync](https://github.com/mikebrady/shairport-sync)  is used to emulate an AirPlay Server. At the beginning I tried to transfer the required information of the song (Songname, current postion, ...) over the Shortcut App. Unfortunately the data that is accesed by Shortcuts is not updated in real time so I searched for an alternative method of transmission and chose AirPlay for this project. If we choose our server as AirPlay-Reciever our iOS device transfers the information of the current playback to that reciever. We use this [ reader for metadata](https://github.com/mikebrady/shairport-sync-metadata-reader) to access that data and save it for the Python script.

**Part 3: The script itself with the [WEB-API of Spotify](https://github.com/plamere/spotipy):**
Part 3 controls the final playback on the Amazon Echo. It uses the WEB-API of Spotify to search for the songname we got through AirPlay and skips to the position in the song at which we stoped listening with Apple Music.

# Known bugs and limitations

 - Problems with selecting the correct playback device inside the Shortcuts App (Missing options inside the App itself)
 - The music does not get resumed at the exact same location at which it was stoped because of some inaccuracies using AirPlay
 - Error when no music or other content than music is played and the shortcut gets activated (tried to fix that by forcing the phone to start music but sometimes it still results in errors because of song´s progress time)

# Troubleshooting

 - Check if the paths you entered in the Shortcuts App match the path of the `"nfc-handoff"` folder
 - Check if [shairport-sync](https://github.com/mikebrady/shairport-sync) is running and configured correctly (`# service shairport-sync status`)
 - Check if the needed Python libary is installed
 - Check the syntax of `config.txt`
 - Try restarting your server

If the problem still persists feel free to open an issue containing your error.

# Implementation of NFC
In theory you can start the shortcut via NFC with the coming update of iOS 13.1.
You will find a tutorial on how to do that shortly after iOS 13.1 is released.

# Security
Please be aware of the fact that you are dealing with sensitive data. I do not recommend running this script in an unsecure network or on a server that is directly accesible through the internet. Only use it in safe enviroments because the script itself is NOT secure. All tokens that are needed for the API are stored in form of clear text, so everybody that has access to this data could take control over your Premium or Developer Account at Spotify. Keep that in mind!

