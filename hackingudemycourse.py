
# Foundations of Hacking and Pentesting Android Apps
import requests

def download_lecture(urls):
    
    for index ,url in enumerate(urls,start=1):
        response = requests.get(url)
    
    with open(f"video{index}.mp4", 'wb') as f:
        
        f.write(response.content)
        
    print('all lecture  downloaded successfully')

urls= [
'https://mp4-c.udemycdn.com/2020-04-21_00-08-25-c6cf95b334aa6bb13487ec0aa7993b5d/WebHD_720p.mp4?Expires=1707900457&Signature=k2QT3IwFtAz0~n-vqkCuZDQzQWFJQ4dBJmFOpl0gK6FRf4QMleCu39ra2SyM1h-qlzys9IGRWHT2OuYf-XfPd6rAnmB3lYDuwEK0BJAAXeFJilHfsmeV60rKij03TzMWxwtIRsOrTsNw3nK-RqOcRqo6KTBEgcDcff19B~iFZ0AvH1fYSeuowcn0eJQXl6YG7~YtfsphBhFHV-GTzbsnpym5Eozi5~q6ftO31Rqwjz4kE42OW7FSmNhgNYFcPUBmpBKOYMoGcKlvtM8u-jEdBfqN2cj84Y-DW2BwESPUMGIm3Tj4cwQINx1P-zWmL-Eqx31K3Fq-3Jaz2oxx6TV02Q__&Key-Pair-Id=K3MG148K9RIRF4',
"https://mp4-c.udemycdn.com/2020-04-21_00-13-24-09c97883630f51d9db59f5cb74be6c2b/WebHD_480.mp4?Expires=1707900785&Signature=HTAnoBF5zKCtCNoFNVmFexukz9CfwF6eL8jmvMKJnkhnXEY9EKws3jv88CiQulX0KZM3G0gF6nmARjD6slcIab7RhoZ7PoUd66K2aScQfTjQ2PpYtN-Ct-NQOmlDwPjb7Z4RRnBsUe1AExvYAQOZKaAzwmpYmcDZtgVP7h6wIQbOlLZ~jiL2K9RSzFHcWzABCoA5ni5BK~QJqUuu~xBYnTROPeLXpWV7Ch-julrzntu-0320YCEzvQ~fzSfVtwU6A5SH8-8OEWrkjkZCT1r7V1VMxE8m1nbNwTR0SFdbKTvs26jYegO0lW70Dcc0VkTT6XJn8MjtT9iJbd2XSH4btA__&Key-Pair-Id=K3MG148K9RIRF4",
"https://mp4-c.udemycdn.com/2020-04-21_00-13-24-a62c7f7b327032389dc2e36a39105601/WebHD_720p.mp4?Expires=1707901448&Signature=d332p-TFVfYr5nNJmAJUFMb5-2SG3i9Si3nZ8~59kD51fZdGSWWsntI1zMvA7Qwa10atwq-DnsIp9pkaA3NeA9IZfTNnifJm25XbnO5WCBUgoWwgILdt6hq0UEP9AuAg1NMqWhH1ZrbjDMWmlDvUtOX9URhQ02LrHEoopNcUpNVpIZzoVFdtDRXyV4pHMxL6mpuSBBbpOk8v72Zuds6VerMKfs6w3duzWbbHcbL2nYMeLjaiuLmr6F6RIG7vfVSG7WwlPypP3~k7IggnsFEGEWQ91j9xvZb40-F4Bg4KPSfwSEyzKDHuCJGIS2tlf3Da4HU5Vu6nfrqEnLATDmKhPA__&Key-Pair-Id=K3MG148K9RIRF4",
"https://mp4-c.udemycdn.com/2020-04-21_00-24-08-1159a568a2e210630c4d3717987be793/WebHD_720p.mp4?Expires=1707901676&Signature=C3XkxE~fmrwqlidFR1-y83ycUR5q0acEAZRsQr0Xx2hdtHI8IesGTNyQsrv1mEaRTGWQqcPMSZjJaWou5MA1WYpLP7CILqWGzxjzAJhVDdLpuXhF~tGHa~va0Oh3KJAgQ1Pmrd~StDoAPI76X4kpkBL34zBy00fUTpkrjKTHBPCxLdG015Ox9DIo~Ytz9V4dkAOJoyQjGf0IuU3lMRRfEGaVVpifU635OaUUCE5sYDUVBn7Y5iygcDXHJw2YFGYBfWumVZu8DktNy4-L6qmKOkVhNQWJ3rLtwn0ad4gX-b95o1L~ntsItYnIUfBfkUi~eRgUpC3ylf5IkYT00dq3Mw__&Key-Pair-Id=K3MG148K9RIRF4",
"https://mp4-c.udemycdn.com/2020-04-21_00-25-02-aa93474ba38ac90df1af40f92b93c550/WebHD_720p.mp4?Expires=1707901738&Signature=PH0VrxSiP~cebFk1XB8WgkFkFVvBCnmaY5gZRb5vivtlNqonbuya9kL4RGAgOpmJ-8QsRRBzGOtaFCycglDPSBgVQPyCNB2X8QcLHgapJfIebUdw4vtUkmaY1iZYXoM-mc3m5rTFNP2WyvpDVFzzuE0Ye1wPkofAFahdWwFSqCw6qYdYpcqo9ekIeqD04NSY~aLA1mDAy5cq3-FOulMnZIQCv2PgI855sKPNk7TuDEKNbe0piBy0f-xhn52CjF6fBs045eMOMj5WL8V2KWNoehCICHBs0W6Ek1OUTKtKZirwEBEbg3crp8wCtlTX1n3RNB~tKlUhqsqurWmxM8Jhzg__&Key-Pair-Id=K3MG148K9R",
"https://mp4-c.udemycdn.com/2020-04-21_00-26-01-5e51d5f0a794bc6e235585f708b2d134/WebHD_720p.mp4?Expires=1707901806&Signature=5VEg--dRaurE--34TbCVBVtfK-vGL2uIQym8stFw1KFvXGe8~jBHzlUK51plt5SxhqQ6PdQPOf3xsCaLBI0kGhyW7aqc3cZpK4STPH7orjAiTJ35vpr8yr0jUwIpMhjqnoADY2FfWrcRXJcZY1vc71dbUYxo8smYpdyhNQPwr37B5dzBvaUFplWFJo6~VjlU2HSMqL07svOW76-TatStTSauwsTIcNaxpHJcdWi5nCFY~vRJgfiMFOhhoQWx2cta7J4bFYLSmatxIKf5nTTl0Q0UtRb4354FVffCCfjQQZYM3tDhViJhYBaIy~18s2h1sq75ZV6esD30oqBYxRnLXg__&Key-Pair-Id=K3MG148K9RIRF4",
"https://mp4-c.udemycdn.com/2020-04-21_00-27-39-c93b75db5fcda23a01155b6ab8dc5ca0/WebHD_720p.mp4?Expires=1707901890&Signature=gpr9VI~~nlbfwgkKrwTxNm49mPwU2cy-CWATi9U3PWdQ-orXozcZGKLjXK1lM-TX80pZnQbCqzZDw2HVAHOB~d4c9NlpC3dsLlqzQ4OHXvNGSbTlJTPqI45ltaSzilMvKj5o2vqR0eDDK2bzwS~97~aAbue4MefUwvrF1txIypvbW9Zye0MKULOFWeOyh3nWc35VuwVYMNoNz25lAm6JGPdWU7FFVeV1i1cQRELMWxgGCO6VH11z-qaLHjcrjxMg7AZstBCvV2DgP-BAc8FGF3Fu6pvgdHwFQsI9LG-GsGdPBW8lPKUkTbDRLnEw-2TtEobYTx39pgZ5mjdTM--FPw__&Key-Pair-Id=K3MG148K9RIRF4",
"https://mp4-c.udemycdn.com/2020-04-21_00-26-01-5e51d5f0a794bc6e235585f708b2d134/WebHD_720p.mp4?Expires=1707902006&Signature=lVVzaqeS0Oe81PJeuvyeXD~62da7K810asgYd92ME3nFnTS321cyAHszwP3zZlZDvRHrGG9szmJrpF8XxlTNLB9sH9WELGsFRBjv1ESc4SCgo7V~CfDHCHRG5mxwWBPy0vukTy92jXpmu~68dL9pDeoW0wzrB7WCxQKcDuDd-Nh1iNAgA5M39QlmAyR7lFQIjqNsviC3prBLliWrf8umzkFsvh49BawvOcDLz5rlxn1cjBlXdD8Ompd-8cV6zRsjVLc~zKZpgumrtCbpgl3TyEpNmogEmC3qYs1E7RZBlUmlRGMCclpN76F-fHO0cT5i82OjLQPChNoJ09tG2ZAvFQ__&Key-Pair-Id=K3MG148K9RIRF4",
"https://mp4-c.udemycdn.com/2020-04-21_00-27-39-c93b75db5fcda23a01155b6ab8dc5ca0/WebHD_720p.mp4?Expires=1707902213&Signature=1lUhLANNxg3tWgbK8VFTnbKdIlIpPSMYHVRwvG4KGra2xxpZXXSmm-ofvsvVMfpHWODNHS8sgGDuZVHiCmMQcgHeRZ5zQ6Q0EMBt~GM5IbPeaAecZDuCxfv4CyOaczuC6G7PDlBuqulcRL0-oaOa-nlByiUS8eXHU65PzORTJtrntRug~~10JYsrEagLu4NfMDAT7WvMIkTWwXeuEZMLl9L7rz5zNEACI0VCMNoeFjIFFgFikPMG6uWVpAVV7ULUZEEniceLvkMPrparj5e-HtvLn174hCR0Gdxvu1o8QxZCk-6q19G1haHcm9y-tUBwvN~~2rHXTnmh~At4fVTMDA__&Key-Pair-Id=K3MG148K9RIRF4",
"https://mp4-c.udemycdn.com/2020-04-21_00-32-51-f3bb124ef302f861a517545dd140004c/WebHD_720p.mp4?Expires=1707902246&Signature=xAyXRbdxpDzPQiKZoY5cKEhbGFl5jHacsz9HAyhYviYKcJCRNRAAlJsm3j4Jobdnn4J23igpDKgtzducNeIdxGLgzrjSoF0XFXwAkiASl293tRD5ENAb4ETgIXOUkvbvXJhvqxWi15MSyJ11c3RHh3uSic-xemTZbKxl~FO93LUDTD7oD5TnuCGLGcLrbEGAlRip-p1dzYLv6lZcYmZnU45alaLj9ZeDRgiQsdt-14h~54-tQ1v1e-yyuP2skeK28~I9sIvw-vaX7BtSBjL8e9cM6ji7W9z~piqwJAN6OyXrc2ehsI6SxgvTm1cX7BJsVbHzOWt9OZ8JHfB~S6H3Jg__&Key-Pair-Id=K3MG148K9RIRF4",
"https://mp4-c.udemycdn.com/2020-04-21_00-32-51-daf195eb1d727f9d66f3a22cb45b8eb8/WebHD_720p.mp4?Expires=1707902298&Signature=CGWUF4nwPWscpFrFsBlV2SrmnBjV6AT4P47jIwY6WJOSvavjZH5L-3gT75ncmJEF-OOm8u5o~AYXnxLNpa1kO~Zx-K9y4PHRDECSDhu9uZi1iwTedZF6jw3xGOf5WHiLw58MCGjnvbtjIdfklbMCSwZYp-fA~pQlhX6kg9bsNFYbn1uNkDHMMCeqHwp3qx8LBvF7av-JLl6jnDblikltnlzO0lkqeLFAyl0~BSDwC0lZKSEW72qOfjSfZE~Fq6vefUFKwZILYlJFtu5X-EcXy8PboNuWC-LStNzOX-DCgxvoHRxmJCgNv21PbGJghASV3EbdSEKSQX5ETUkhOgPArg__&Key-Pair-Id=K3MG148K9RIRF4",
"https://mp4-c.udemycdn.com/2020-04-21_00-37-48-84caa20226cbd03f7f84e50cb1e31530/WebHD_720p.mp4?Expires=1707902325&Signature=xVSXhr5pttT1jo1TltvaHm3oilRVsF0IEgEywpzjHvpG-ngX2KoYRwhVIrA5avvV9Q3eCcsYY47Mq6fAJKHTizgSphzV-YLLSzwE9bVasDeKwxK3SM5TFMnCJQisabUV8prXwVD58Ub-R5VrSKn-fKtzlzDOZViBQLczq1CuSnAlegFGnu5L179i~U5rUpDovnSSpBB6f4Lgpl1eLWV1bB5rU4nHhwGJHL1SgYFk5w8e53Q-SxaSvzw6by687wCt-mJrCyh1dasqLZl08qUXUUR-AYfkcVwq8FUkfYg5Arid6v0GCVEuihACt08WglgLcbx-c~EaZqv81UeqqUUPAg__&Key-Pair-Id=K3MG148K9RIRF4",
"https://mp4-c.udemycdn.com/2020-04-21_00-39-59-9d1bc34dca17675cf244454ea178e475/WebHD_720p.mp4?Expires=1707902352&Signature=mam14tfJ3JDPppFX~jyFwjQz6P4-dgEYSr3HxdvmmC5qhzWfdqnX0Q2ZSe9~wPGHQCORzYAkbfFk8eoUhDLkIP8ac5ZPfnzHjJLdBZTzzbfLR5zPUKzOzaFfYj74GwIV6Bgalhh2e0~xLEirDFu8eWZmxmpeMdK-4O7t-xfeb2CQT8qprvSdBEwCMfNY4O3tQIOH8baBkTfVFSZeNiL-rzkV8sZMw-UewPZs4ecZbBED2QVvKnu1i7ICeoMco0ecWq9XsbmZ1xI-m1RbQtPIpOL~gnQeLZJACUi-MzzLaSetq1PjhUBT2bZQ6QFPkqAzIm-Qs4J7wJKDAZxTuUbSDg__&Key-Pair-Id=K3MG148K9RIRF4",
"https://mp4-c.udemycdn.com/2020-04-21_00-45-50-5355f83302ad122340c97f2bffce9578/WebHD_720p.mp4?Expires=1707902373&Signature=d6Kj5qQIyLV237vYaVju4ufCwEyY5BhGn8X3VyjFkBIkC0pE5vPmAA~kOZPvYZ7fpF~coiYaHx77QdgwK-6MNRHa1KumElDbGSS~aiBVgVMORKen1dE-8ihML0-c1tt4pZ12TzQkjt0TFGphjvlmgcTPGrSwOosVgg63wVxkBUd6909Ond4T6FTAZdjAdUych1Rx~dOsasJ2ru97VZltaBfRLjdW8ei5891piHBFWGOMRiQv6AzwzAPJOKsIsJJsHyH6ZEqM3uOkHPfdHCTeVVwcZsQULcZWN48P1DyBVEY1ZACPSju-5gbpmoc5C25HrjNwK56YlWAt67Uk8OiXog__&Key-Pair-Id=K3MG148K9RIRF4",
"https://mp4-c.udemycdn.com/2020-04-21_00-49-43-4bb641b31e737c6c3c49ced9d4cdf5d1/WebHD_720p.mp4?Expires=1707902394&Signature=d4JUtxI2qe2K8TFsUroia7nwjVSQo1KwZ-pRa-R-2B1OvbhIWzcGy2lEnN7uQFAQUB0C5rBPfEsENZWpi1Nuu9VYTrwUDiSbMBMUrTBPvQoj4ga9myT4TO9g9o6ZDtN~ziQBiwb7MnBCnQelcqC4ZNJLy99f4~HVNv~T2zlNHjkuRmGhlobCFFv5RSblGoC3mqpV~KrNo05S5~5wTvXt5UXwTPGBOovbZ8xUra0ooqyFAIV98Gq4QEsJKspVeTrgg3nhsCM~dr4-XqIQaWyTm5nPxcvomOZix0VMisHEkc1WR32n~q6drede1Tmbf0p9HmaqmpBVkxahNgDwDIaXcA__&Key-Pair-Id=K3MG148K9RIRF4"
]
download_lecture(urls)

"""Learn More For Free!
Want to learn more about programming, security, and low level programming? Check out our free resources!

YouTube Channel: https://www.youtube.com/channel/UC7KBXRtv-EkiOFsRtpBxIbg

Our Technical Tutorials: https://olivestem.net/home

Download Links
Drozer: https://labs.f-secure.com/tools/drozer/

Insecure Banking App v2: https://github.com/dineshshetty/Android-InsecureBankv2

Diva apk: http://www.payatu.com/wp-content/uploads/2016/01/diva-beta.tar.gz

Python 2.7.18: https://www.python.org/downloads/release/python-2718/

jadx: https://github.com/skylot/jadx

Strings: https://docs.microsoft.com/en-us/sysinternals/downloads/strings"""
