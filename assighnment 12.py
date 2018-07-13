#Q1
#Accesstoken: An Evidence that can be used by an application to access an api
#Access token:Generated

#Q2
#www.google.com ww.google.com./172.217.9.164

#Q3
'''
from keys import consumer_key,consumer_secret,access_token,access_secret
import tweepy

oauth=tweepy.OAuthHandler(consumer_key,consumer_secret)
oauth.set_access_token(access_token,access_secret)
api=tweepy.API(oauth)
tweets = api.user_timeline(screen_name="LeoDiCaprio")
tweets_for_csv = [tweet.text for tweet in tweets]  # CSV file created
for j in tweets_for_csv:
    print(j)'''

'''
TWEETS:
RT @ClimateReality: Sign our #ClimateMajority pledge and let the @WhiteHouse know that Americans support commonsense solutions to the clima…
RT @ozy: A 17-year-old activist is not uncommon these days. But @NalleliCobo has been challenging the oil industry since age 9 when toxic c…
RT @EURACTIV: EU strikes deal on 32% renewable energy target and palm oil ban after all-night session https://t.co/8vZfvIZdvm
RT @NewsHour: Antarctica is losing ice twice as fast as anyone thought https://t.co/5yd87lw9gp
Great news from @DiCaprioFdn and @TompkinsConserv’s rewilding project. Learn more. https://t.co/tSnZvWZLM0
RT @oceana: An estimated 8 million metric tons of plastic is dumped into the ocean each year.
It's time to #BreakFreeFromPlastic. https://…
A great read on the always inspiring @laurenepowell. cc: @EmCollective https://t.co/2HFLr653dq
.@DiCaprioFdn is partnering w/ Porky Hefer on this project that uses eco-friendly art to bring attention to the iss… https://t.co/8sE26gVwR9
RT @RubiconGlobal: .@J_WintersLDF of the @dicapriofdn joins us on the Town Haul for a #WorldOceansDay celebration! Tune in here: https://t.…
RT @nytimesworld: Executives from the world’s biggest oil companies and money managers were summoned to the Vatican for a two-day conferenc…
RT @NatGeoMaps: This refuge may be the most contested land in the U.S. https://t.co/qweg7rbxvy https://t.co/Hjvmx7DYLe
Learn about @OnlythismuchSA, a new campaign advancing the protection of the oceans around South Africa.… https://t.co/ymEcnU1zyA
RT @RobertKennedyJr: Defending CA’s coast &amp; rivers against pollution, trash &amp; oil spills is a tough job, especially with #Trump &amp; #Pruitt w…
This #WorldOceansDay, @DiCaprioFdn partner @GlobalFishWatch is helping to bring transparency to global fishing, sup… https://t.co/nisro3yi7s
RT @dicapriofdn: Half the world’s population depends on mountain ecosystems, yet climate change is threatening their continued existence. I…
RT @NG_PristineSeas: Our new @NG_PristineSeas study with @sfgucsb @GlobalFishWatch @UBC @SeaAroundUs @UWAnews reveals that without large go…
RT @GlblCtzn: The Great Pacific Garbage Patch is about to get cleaned up – thanks to one ambitious 23-year-old! https://t.co/6XYjoX0r9q
RT @antonioguterres: Our world is swamped by harmful plastic waste. By 2050, there could be more plastic in the ocean than fish. On World E…
RT @voxdotcom: If Democrats have any chance of winning back the majority in the House of Representatives, they’ll have to make huge gains i…
RT @business: Carmakers in letter to Trump's White House: “Climate change is real” https://t.co/eRTp8UCcGb https://t.co/B5JA83dV3z
'''
#Q4: A library is a collection of classes, while API is an application programming interface
# We may change our library, but we cannot change our API , abstraction is done in an API too.

#Q5:
from keys import consumer_key,consumer_secret,access_token,access_secret
import tweepy

oauth=tweepy.OAuthHandler(consumer_key,consumer_secret)
oauth.set_access_token(access_token,access_secret)
api=tweepy.API(oauth)
user=api.get_user("LeoDiCaprio")
print(user.screen_name)
print(user.followers_count)