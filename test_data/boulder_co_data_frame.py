"""Test data for climbing_data_provider tests"""
import pandas

url = "https://www.mountainproject.com/data/get-routes-for-lat-lon?lat=40.03&lon=-105.25&maxDistance=10&maxResults=20" \
      "&minDiff=5.1&maxDiff=5.15&key=test_key"

json_response = """{
    "routes": [
        {
            "id": 105748490,
            "name": "The Bastille Crack",
            "type": "Trad",
            "rating": "5.7",
            "stars": 4.5,
            "starVotes": 1777,
            "pitches": 5,
            "location": [
                "Colorado",
                "Boulder",
                "Eldorado Canyon SP",
                "The Bastille",
                "The Bastille - N Face"
            ],
            "url": "https:\/\/www.mountainproject.com\/route\/105748490\/the-bastille-crack",
            "imgSqSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/108995841_sqsmall_1494302324.jpg",
            "imgSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/108995841_small_1494302324.jpg",
            "imgSmallMed": "https:\/\/cdn2.apstatic.com\/photos\/climb\/108995841_smallMed_1494302324.jpg",
            "imgMedium": "https:\/\/cdn2.apstatic.com\/photos\/climb\/108995841_medium_1494302324.jpg",
            "longitude": -105.283,
            "latitude": 39.9307
        },
        {
            "id": 105748268,
            "name": "Direct Route",
            "type": "Trad",
            "rating": "5.6 R",
            "stars": 4.5,
            "starVotes": 1057,
            "pitches": 10,
            "location": [
                "Colorado",
                "Boulder",
                "Flatirons",
                "North",
                "First Flatiron"
            ],
            "url": "https:\/\/www.mountainproject.com\/route\/105748268\/direct-route",
            "imgSqSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/1301163_sqsmall_1557850417.jpg",
            "imgSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/1301163_small_1557850417.jpg",
            "imgSmallMed": "https:\/\/cdn2.apstatic.com\/photos\/climb\/1301163_smallMed_1557850417.jpg",
            "imgMedium": "https:\/\/cdn2.apstatic.com\/photos\/climb\/1301163_medium_1557850417.jpg",
            "longitude": -105.2928,
            "latitude": 39.9908
        },
        {
            "id": 105748777,
            "name": "Rosy Crucifixion",
            "type": "Trad",
            "rating": "5.10a\/b PG13",
            "stars": 4.8,
            "starVotes": 401,
            "pitches": 3,
            "location": [
                "Colorado",
                "Boulder",
                "Eldorado Canyon SP",
                "Redgarden Wall",
                "Redgarden - Tower Two"
            ],
            "url": "https:\/\/www.mountainproject.com\/route\/105748777\/rosy-crucifixion",
            "imgSqSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/108271333_sqsmall_1494273144.jpg",
            "imgSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/108271333_small_1494273144.jpg",
            "imgSmallMed": "https:\/\/cdn2.apstatic.com\/photos\/climb\/108271333_smallMed_1494273144.jpg",
            "imgMedium": "https:\/\/cdn2.apstatic.com\/photos\/climb\/108271333_medium_1494273144.jpg",
            "longitude": -105.2852,
            "latitude": 39.9312
        },
        {
            "id": 108095626,
            "name": "Rebuffat's Arete",
            "type": "Trad",
            "rating": "5.7",
            "stars": 4.7,
            "starVotes": 426,
            "pitches": 1,
            "location": [
                "Colorado",
                "Boulder",
                "Eldorado Canyon SP",
                "Redgarden Wall",
                "Redgarden - Lumpe to the top"
            ],
            "url": "https:\/\/www.mountainproject.com\/route\/108095626\/rebuffats-arete",
            "imgSqSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/117244156_sqsmall_1561133998.jpg",
            "imgSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/117244156_small_1561133998.jpg",
            "imgSmallMed": "https:\/\/cdn2.apstatic.com\/photos\/climb\/117244156_smallMed_1561133998.jpg",
            "imgMedium": "https:\/\/cdn2.apstatic.com\/photos\/climb\/117244156_medium_1561133998.jpg",
            "longitude": -105.2867,
            "latitude": 39.9323
        },
        {
            "id": 105756796,
            "name": "Over the Hill",
            "type": "Trad",
            "rating": "5.10b",
            "stars": 4.7,
            "starVotes": 383,
            "pitches": 2,
            "location": [
                "Colorado",
                "Boulder",
                "Eldorado Canyon SP",
                "Rincon",
                "Rincon - L of Center Route"
            ],
            "url": "https:\/\/www.mountainproject.com\/route\/105756796\/over-the-hill",
            "imgSqSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/1201436_sqsmall_1557524924.jpg",
            "imgSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/1201436_small_1557524924.jpg",
            "imgSmallMed": "https:\/\/cdn2.apstatic.com\/photos\/climb\/1201436_smallMed_1557524924.jpg",
            "imgMedium": "https:\/\/cdn2.apstatic.com\/photos\/climb\/1201436_medium_1557524924.jpg",
            "longitude": -105.2899,
            "latitude": 39.9344
        },
        {
            "id": 105749599,
            "name": "Handcracker Direct",
            "type": "Trad",
            "rating": "5.10a",
            "stars": 4.6,
            "starVotes": 513,
            "pitches": 5,
            "location": [
                "Colorado",
                "Boulder",
                "Eldorado Canyon SP",
                "The West Ridge",
                "West Ridge - part C - Pony Express to Long John"
            ],
            "url": "https:\/\/www.mountainproject.com\/route\/105749599\/handcracker-direct",
            "imgSqSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/108599432_sqsmall_1494290177.jpg",
            "imgSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/108599432_small_1494290177.jpg",
            "imgSmallMed": "https:\/\/cdn2.apstatic.com\/photos\/climb\/108599432_smallMed_1494290177.jpg",
            "imgMedium": "https:\/\/cdn2.apstatic.com\/photos\/climb\/108599432_medium_1494290177.jpg",
            "longitude": -105.2885,
            "latitude": 39.932
        },
        {
            "id": 105751960,
            "name": "Gambit",
            "type": "Trad",
            "rating": "5.8",
            "stars": 4.5,
            "starVotes": 572,
            "pitches": 5,
            "location": [
                "Colorado",
                "Boulder",
                "Eldorado Canyon SP",
                "Shirt Tail Peak"
            ],
            "url": "https:\/\/www.mountainproject.com\/route\/105751960\/gambit",
            "imgSqSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/106602420_sqsmall_1494124248.jpg",
            "imgSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/106602420_small_1494124248.jpg",
            "imgSmallMed": "https:\/\/cdn2.apstatic.com\/photos\/climb\/106602420_smallMed_1494124248.jpg",
            "imgMedium": "https:\/\/cdn2.apstatic.com\/photos\/climb\/106602420_medium_1494124248.jpg",
            "longitude": -105.2884,
            "latitude": 39.9343
        },
        {
            "id": 105750457,
            "name": "Cosmosis",
            "type": "Trad",
            "rating": "5.10a",
            "stars": 4.6,
            "starVotes": 269,
            "pitches": 2,
            "location": [
                "Colorado",
                "Boulder",
                "Boulder Canyon",
                "Bell Buttress Massif",
                "Bell Buttress - Main Crag"
            ],
            "url": "https:\/\/www.mountainproject.com\/route\/105750457\/cosmosis",
            "imgSqSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/114266043_sqsmall_1523878109.jpg",
            "imgSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/114266043_small_1523878109.jpg",
            "imgSmallMed": "https:\/\/cdn2.apstatic.com\/photos\/climb\/114266043_smallMed_1523878109.jpg",
            "imgMedium": "https:\/\/cdn2.apstatic.com\/photos\/climb\/114266043_medium_1523878109.jpg",
            "longitude": -105.413,
            "latitude": 40.0011
        },
        {
            "id": 105750565,
            "name": "Darkness 'til Dawn",
            "type": "Trad",
            "rating": "5.10a",
            "stars": 4.6,
            "starVotes": 365,
            "pitches": 1,
            "location": [
                "Colorado",
                "Boulder",
                "Eldorado Canyon SP",
                "Redgarden Wall",
                "Redgarden - Lumpe to the top"
            ],
            "url": "https:\/\/www.mountainproject.com\/route\/105750565\/darkness-til-dawn",
            "imgSqSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/106249144_sqsmall_1494091427.jpg",
            "imgSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/106249144_small_1494091427.jpg",
            "imgSmallMed": "https:\/\/cdn2.apstatic.com\/photos\/climb\/106249144_smallMed_1494091427.jpg",
            "imgMedium": "https:\/\/cdn2.apstatic.com\/photos\/climb\/106249144_medium_1494091427.jpg",
            "longitude": -105.2867,
            "latitude": 39.9323
        },
        {
            "id": 105764211,
            "name": "The Metamorphosis",
            "type": "Trad",
            "rating": "5.10-",
            "stars": 4.6,
            "starVotes": 142,
            "pitches": 1,
            "location": [
                "Colorado",
                "Boulder",
                "Eldorado Canyon SP",
                "The Wind Tower",
                "Wind Tower - S Face"
            ],
            "url": "https:\/\/www.mountainproject.com\/route\/105764211\/the-metamorphosis",
            "imgSqSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/1205755_sqsmall_1557848867.jpg",
            "imgSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/1205755_small_1557848867.jpg",
            "imgSmallMed": "https:\/\/cdn2.apstatic.com\/photos\/climb\/1205755_smallMed_1557848867.jpg",
            "imgMedium": "https:\/\/cdn2.apstatic.com\/photos\/climb\/1205755_medium_1557848867.jpg",
            "longitude": -105.283,
            "latitude": 39.9314
        },
        {
            "id": 105748645,
            "name": "The Green Spur",
            "type": "Trad",
            "rating": "5.9+",
            "stars": 4.5,
            "starVotes": 509,
            "pitches": 2,
            "location": [
                "Colorado",
                "Boulder",
                "Eldorado Canyon SP",
                "Redgarden Wall",
                "Redgarden - Lumpe to the top"
            ],
            "url": "https:\/\/www.mountainproject.com\/route\/105748645\/the-green-spur",
            "imgSqSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/1203187_sqsmall_1557526346.jpg",
            "imgSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/1203187_small_1557526346.jpg",
            "imgSmallMed": "https:\/\/cdn2.apstatic.com\/photos\/climb\/1203187_smallMed_1557526346.jpg",
            "imgMedium": "https:\/\/cdn2.apstatic.com\/photos\/climb\/1203187_medium_1557526346.jpg",
            "longitude": -105.2867,
            "latitude": 39.9323
        },
        {
            "id": 105762483,
            "name": "Alice in Bucketland",
            "type": "Trad",
            "rating": "5.8+ R",
            "stars": 4.6,
            "starVotes": 183,
            "pitches": 2,
            "location": [
                "Colorado",
                "Boulder",
                "Eldorado Canyon SP",
                "Redgarden Wall",
                "Redgarden - Tower One"
            ],
            "url": "https:\/\/www.mountainproject.com\/route\/105762483\/alice-in-bucketland",
            "imgSqSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/106354949_sqsmall_1494100995.jpg",
            "imgSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/106354949_small_1494100995.jpg",
            "imgSmallMed": "https:\/\/cdn2.apstatic.com\/photos\/climb\/106354949_smallMed_1494100995.jpg",
            "imgMedium": "https:\/\/cdn2.apstatic.com\/photos\/climb\/106354949_medium_1494100995.jpg",
            "longitude": -105.286,
            "latitude": 39.9319
        },
        {
            "id": 105748627,
            "name": "Hair City",
            "type": "Trad",
            "rating": "5.9+ R",
            "stars": 4.6,
            "starVotes": 411,
            "pitches": 3,
            "location": [
                "Colorado",
                "Boulder",
                "Eldorado Canyon SP",
                "The Bastille",
                "The Bastille - W Face"
            ],
            "url": "https:\/\/www.mountainproject.com\/route\/105748627\/hair-city",
            "imgSqSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/1203651_sqsmall_1557526857.jpg",
            "imgSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/1203651_small_1557526857.jpg",
            "imgSmallMed": "https:\/\/cdn2.apstatic.com\/photos\/climb\/1203651_smallMed_1557526857.jpg",
            "imgMedium": "https:\/\/cdn2.apstatic.com\/photos\/climb\/1203651_medium_1557526857.jpg",
            "longitude": -105.283,
            "latitude": 39.9304
        },
        {
            "id": 105748639,
            "name": "Blind Faith",
            "type": "Trad",
            "rating": "5.10a",
            "stars": 4.5,
            "starVotes": 659,
            "pitches": 2,
            "location": [
                "Colorado",
                "Boulder",
                "Eldorado Canyon SP",
                "The Bastille",
                "The Bastille - W Face"
            ],
            "url": "https:\/\/www.mountainproject.com\/route\/105748639\/blind-faith",
            "imgSqSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/106416404_sqsmall_1494106828.jpg",
            "imgSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/106416404_small_1494106828.jpg",
            "imgSmallMed": "https:\/\/cdn2.apstatic.com\/photos\/climb\/106416404_smallMed_1494106828.jpg",
            "imgMedium": "https:\/\/cdn2.apstatic.com\/photos\/climb\/106416404_medium_1494106828.jpg",
            "longitude": -105.283,
            "latitude": 39.9304
        },
        {
            "id": 105750577,
            "name": "Perversion",
            "type": "Trad",
            "rating": "5.9",
            "stars": 4.5,
            "starVotes": 184,
            "pitches": 3,
            "location": [
                "Colorado",
                "Boulder",
                "Eldorado Mountain",
                "Mickey Mouse Wall"
            ],
            "url": "https:\/\/www.mountainproject.com\/route\/105750577\/perversion",
            "imgSqSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/105997383_sqsmall_1558388974.jpg",
            "imgSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/105997383_small_1558388974.jpg",
            "imgSmallMed": "https:\/\/cdn2.apstatic.com\/photos\/climb\/105997383_smallMed_1558388974.jpg",
            "imgMedium": "https:\/\/cdn2.apstatic.com\/photos\/climb\/105997383_medium_1558388974.jpg",
            "longitude": -105.2853,
            "latitude": 39.9198
        },
        {
            "id": 105748924,
            "name": "Long John Wall",
            "type": "Trad",
            "rating": "5.8",
            "stars": 4.4,
            "starVotes": 546,
            "pitches": 4,
            "location": [
                "Colorado",
                "Boulder",
                "Eldorado Canyon SP",
                "The West Ridge",
                "West Ridge - part B - Long John to Verschneidung"
            ],
            "url": "https:\/\/www.mountainproject.com\/route\/105748924\/long-john-wall",
            "imgSqSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/105953077_sqsmall_1558029292.jpg",
            "imgSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/105953077_small_1558029292.jpg",
            "imgSmallMed": "https:\/\/cdn2.apstatic.com\/photos\/climb\/105953077_smallMed_1558029292.jpg",
            "imgMedium": "https:\/\/cdn2.apstatic.com\/photos\/climb\/105953077_medium_1558029292.jpg",
            "longitude": -105.2879,
            "latitude": 39.9314
        },
        {
            "id": 105750454,
            "name": "North Face",
            "type": "Trad",
            "rating": "5.6 R",
            "stars": 4.4,
            "starVotes": 184,
            "pitches": 5,
            "location": [
                "Colorado",
                "Boulder",
                "Flatirons",
                "South",
                "The Maiden"
            ],
            "url": "https:\/\/www.mountainproject.com\/route\/105750454\/north-face",
            "imgSqSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/107342922_sqsmall_1494182976.jpg",
            "imgSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/107342922_small_1494182976.jpg",
            "imgSmallMed": "https:\/\/cdn2.apstatic.com\/photos\/climb\/107342922_smallMed_1494182976.jpg",
            "imgMedium": "https:\/\/cdn2.apstatic.com\/photos\/climb\/107342922_medium_1494182976.jpg",
            "longitude": -105.2872,
            "latitude": 39.95
        },
        {
            "id": 105749029,
            "name": "Xanadu",
            "type": "Trad",
            "rating": "5.10a",
            "stars": 4.5,
            "starVotes": 293,
            "pitches": 1,
            "location": [
                "Colorado",
                "Boulder",
                "Eldorado Canyon SP",
                "The West Ridge",
                "West Ridge - part D - Xanadu to Pony Express"
            ],
            "url": "https:\/\/www.mountainproject.com\/route\/105749029\/xanadu",
            "imgSqSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/119092848_sqsmall_1592887223.jpg",
            "imgSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/119092848_small_1592887223.jpg",
            "imgSmallMed": "https:\/\/cdn2.apstatic.com\/photos\/climb\/119092848_smallMed_1592887223.jpg",
            "imgMedium": "https:\/\/cdn2.apstatic.com\/photos\/climb\/119092848_medium_1592887223.jpg",
            "longitude": -105.2887,
            "latitude": 39.9324
        },
        {
            "id": 105749890,
            "name": "Werk Supp",
            "type": "Trad",
            "rating": "5.9",
            "stars": 4.4,
            "starVotes": 676,
            "pitches": 2,
            "location": [
                "Colorado",
                "Boulder",
                "Eldorado Canyon SP",
                "The Bastille",
                "The Bastille - N Face"
            ],
            "url": "https:\/\/www.mountainproject.com\/route\/105749890\/werk-supp",
            "imgSqSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/105910940_sqsmall_1557940890.jpg",
            "imgSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/105910940_small_1557940890.jpg",
            "imgSmallMed": "https:\/\/cdn2.apstatic.com\/photos\/climb\/105910940_smallMed_1557940890.jpg",
            "imgMedium": "https:\/\/cdn2.apstatic.com\/photos\/climb\/105910940_medium_1557940890.jpg",
            "longitude": -105.283,
            "latitude": 39.9307
        },
        {
            "id": 105751315,
            "name": "Grand Giraffe",
            "type": "Trad",
            "rating": "5.10a",
            "stars": 4.4,
            "starVotes": 226,
            "pitches": 5,
            "location": [
                "Colorado",
                "Boulder",
                "Eldorado Canyon SP",
                "Redgarden Wall",
                "Redgarden - Tower One"
            ],
            "url": "https:\/\/www.mountainproject.com\/route\/105751315\/grand-giraffe",
            "imgSqSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/111767568_sqsmall_1494303412.jpg",
            "imgSmall": "https:\/\/cdn2.apstatic.com\/photos\/climb\/111767568_small_1494303412.jpg",
            "imgSmallMed": "https:\/\/cdn2.apstatic.com\/photos\/climb\/111767568_smallMed_1494303412.jpg",
            "imgMedium": "https:\/\/cdn2.apstatic.com\/photos\/climb\/111767568_medium_1494303412.jpg",
            "longitude": -105.286,
            "latitude": 39.9319
        }
    ],
    "success": 1
}
"""

expected_state_series = pandas.Series(["Colorado"] * 20, name="state")
