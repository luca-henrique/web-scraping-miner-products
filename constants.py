
iphone5 = "iPhone 5|"
iphone6 = "iPhone 6|iphone 6s|IPhone 6S|IPhone 6s Plus|iphone 6s|"
iphone7 = "7 plus|iPhone 7|IPhone 7 Plus|7plus|iPhone 7 Plus|iphone 7 Plus|iphone 7|IPhone 7|I Phone 7 plus|"
iphone8 = "iPhone 8|IPhone 8|iPhone 8 Plus|Iphone 8 Plus|IPHONE 8|iPhone 8|iPhone 8|iPhone 8 Plus|IPHONE 8 PLUS|Iphone 8plus|iPhone 8|iPhone 8plus|iPhone 8 Plus|iPhone 8plus|Iphone xr|IPHONE 8|"
iphoneX = "iPhone X|Iphone X|iPhone XR|Iphone X|iPhone X|iPhone XR|Iphone xr|iphone x|"
iphoneSE = "iPhone SE|IPHONE SE|"

otherFilter = "Vitrine|Xaiomi|"

ipad = "Ipad Air|AirPod Apple|Airpods Pro|"
appleWatch = "Apple Watch|apple watch|APPLEWATCH 3|Apple watch"


minPricePhone = 1000
maxPricePhone = 2600


filterPhoneList = iphone5+iphone6+iphoneX+iphoneX + \
    iphone7+iphone8 + iphoneSE+ipad+otherFilter+appleWatch

filterPhoneList = filterPhoneList.split("|")
