from speedtest import InterentSpeed
from tweet import TwittManger
from util import SpeedData

speedTester = InterentSpeed(up_speed=10 , down_speed=100)
current_speed = speedTester.get_speed()

should_i_tweet = speedTester.is_speed_lower(up_speed=current_speed[1] , down_speed=current_speed[0])

print(current_speed)

if should_i_tweet: 
    twitManger = TwittManger()
    twitManger.send_tweet(SpeedData(
        promised_down = 40,
        promised_up= 10,
        actuall_up= current_speed[0],
        actuall_down=current_speed[1]
    ))
else:
    print("no complains")
