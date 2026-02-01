from app.models.schemas import Location
from urllib.parse import quote_plus
from typing import Literal


def _search_url(name: str) -> str:
    """Generate AllTrails search URL for a location."""
    query = quote_plus(f"{name} circular walk")
    return f"https://www.alltrails.com/search?q={query}"


Mode = Literal["callum", "robert"]

# All hiking locations with user flag
ALL_LOCATIONS: list[Location] = [
    # ============ CALLUM LOCATIONS (E7 0AR - East London) ============
    # Forest Hikes
    Location(
        id=1, name="Epping Forest", latitude=51.6571, longitude=0.0413,
        type="forest", description="Ancient woodland with diverse wildlife and varied trails through beech and oak trees.",
        drive_time="30 min", walk_url=_search_url("Epping Forest"), user="callum"
    ),
    Location(
        id=2, name="Hainault Forest", latitude=51.6197, longitude=0.1242,
        type="forest", description="Country park with woodland walks, lake, and open grassland areas.",
        drive_time="25 min", walk_url=_search_url("Hainault Forest"), user="callum"
    ),
    Location(
        id=3, name="Burnham Beeches", latitude=51.5561, longitude=-0.6455,
        type="forest", description="National Nature Reserve with ancient pollarded beech trees and peaceful woodland paths.",
        drive_time="1hr 15min", walk_url=_search_url("Burnham Beeches"), user="callum"
    ),
    Location(
        id=4, name="Ashdown Forest", latitude=51.0410, longitude=0.0755,
        type="forest", description="Inspiration for Hundred Acre Wood, featuring heathland and woodland trails.",
        drive_time="1hr 30min", walk_url=_search_url("Ashdown Forest"), user="callum"
    ),
    Location(
        id=5, name="Box Hill", latitude=51.2487, longitude=-0.3136,
        type="forest", description="Surrey Hills beauty spot with stunning viewpoints and chalk downland walks.",
        drive_time="1hr 15min", walk_url=_search_url("Box Hill Surrey"), user="callum"
    ),
    Location(
        id=6, name="Leith Hill", latitude=51.1769, longitude=-0.3697,
        type="forest", description="Highest point in Southeast England with a Victorian tower and woodland trails.",
        drive_time="1hr 20min", walk_url=_search_url("Leith Hill"), user="callum"
    ),
    Location(
        id=7, name="Wendover Woods", latitude=51.7717, longitude=-0.7115,
        type="forest", description="Chiltern Hills forest with waymarked trails, Go Ape, and scenic viewpoints.",
        drive_time="1hr 30min", walk_url=_search_url("Wendover Woods"), user="callum"
    ),
    Location(
        id=8, name="Chess Valley", latitude=51.7040, longitude=-0.6122,
        type="forest", description="Picturesque Chilterns valley with riverside walks and charming villages.",
        drive_time="1hr 20min", walk_url=_search_url("Chess Valley Chilterns"), user="callum"
    ),
    Location(
        id=9, name="Bedgebury Pinetum", latitude=51.0706, longitude=0.4536,
        type="forest", description="National Pinetum with world-class conifer collection and family-friendly trails.",
        drive_time="1hr 30min", walk_url=_search_url("Bedgebury Pinetum"), user="callum"
    ),
    Location(
        id=10, name="Holmwood Common", latitude=51.1805, longitude=-0.3210,
        type="forest", description="Surrey woodland common with peaceful paths through oak and birch trees.",
        drive_time="1hr 20min", walk_url=_search_url("Holmwood Common Surrey"), user="callum"
    ),
    # Coastal Hikes
    Location(
        id=11, name="White Cliffs of Dover", latitude=51.1370, longitude=1.3657,
        type="coastal", description="Iconic chalk cliffs with spectacular sea views and clifftop walking paths.",
        drive_time="1hr 45min", walk_url=_search_url("White Cliffs Dover"), user="callum"
    ),
    Location(
        id=12, name="Seven Sisters", latitude=50.7743, longitude=0.1530,
        type="coastal", description="Dramatic chalk cliffs along the South Downs Way with sweeping coastal views.",
        drive_time="1hr 45min", walk_url=_search_url("Seven Sisters Cliffs"), user="callum"
    ),
    Location(
        id=13, name="Beachy Head", latitude=50.7374, longitude=0.2477,
        type="coastal", description="England's highest chalk sea cliff with panoramic views and lighthouse below.",
        drive_time="1hr 50min", walk_url=_search_url("Beachy Head"), user="callum"
    ),
    Location(
        id=14, name="Thanet Coast", latitude=51.3355, longitude=1.4199,
        type="coastal", description="Coastal path through seaside towns with sandy bays and chalk stacks.",
        drive_time="1hr 40min", walk_url=_search_url("Thanet Coast Broadstairs"), user="callum"
    ),
    Location(
        id=15, name="Whitstable Coastal Path", latitude=51.3610, longitude=1.0243,
        type="coastal", description="Seaside walk past oyster beds, beach huts, and the famous harbour.",
        drive_time="1hr 30min", walk_url=_search_url("Whitstable"), user="callum"
    ),
    Location(
        id=16, name="Leigh-on-Sea Estuary", latitude=51.5500, longitude=0.6460,
        type="coastal", description="Thames estuary walks with mudflats, cockle sheds, and birdwatching.",
        drive_time="50 min", walk_url=_search_url("Leigh-on-Sea Two Tree Island"), user="callum"
    ),
    Location(
        id=17, name="Southend-on-Sea", latitude=51.5378, longitude=0.7143,
        type="coastal", description="Classic seaside resort with the world's longest pleasure pier and esplanade walks.",
        drive_time="55 min", walk_url=_search_url("Southend-on-Sea"), user="callum"
    ),
    Location(
        id=18, name="Wivenhoe Trail", latitude=51.8580, longitude=0.9653,
        type="coastal", description="Riverside walk along the Colne estuary with boats, wildlife, and historic quay.",
        drive_time="1hr 20min", walk_url=_search_url("Wivenhoe Essex"), user="callum"
    ),
    Location(
        id=19, name="Devil's Dyke", latitude=50.8828, longitude=-0.2146,
        type="coastal", description="South Downs valley with far-reaching views to the sea and rolling hills.",
        drive_time="1hr 40min", walk_url=_search_url("Devil's Dyke Brighton"), user="callum"
    ),
    Location(
        id=20, name="Ditchling Beacon", latitude=50.9019, longitude=-0.1074,
        type="coastal", description="South Downs summit with expansive views over the Weald and towards the coast.",
        drive_time="1hr 45min", walk_url=_search_url("Ditchling Beacon"), user="callum"
    ),

    # ============ ROBERT LOCATIONS (WA12 9US - Newton-le-Willows) ============
    # Forest/Woodland Hikes
    Location(
        id=21, name="Delamere Forest", latitude=53.2283, longitude=-2.6842,
        type="forest", description="Cheshire's largest woodland with waymarked trails through pine and broadleaf trees.",
        drive_time="30 min", walk_url=_search_url("Delamere Forest"), user="robert"
    ),
    Location(
        id=22, name="Rivington Pike", latitude=53.6267, longitude=-2.5525,
        type="forest", description="Historic pike tower atop West Pennine Moors with stunning views over Lancashire.",
        drive_time="25 min", walk_url=_search_url("Rivington Pike"), user="robert"
    ),
    Location(
        id=23, name="Alderley Edge", latitude=53.2980, longitude=-2.2280,
        type="forest", description="Dramatic red sandstone escarpment with woodland trails and legends of wizards.",
        drive_time="40 min", walk_url=_search_url("Alderley Edge"), user="robert"
    ),
    Location(
        id=24, name="Lyme Park", latitude=53.3385, longitude=-2.0548,
        type="forest", description="National Trust estate with deer park, woodland walks, and Pemberley from Pride and Prejudice.",
        drive_time="50 min", walk_url=_search_url("Lyme Park Disley"), user="robert"
    ),
    Location(
        id=25, name="Macclesfield Forest", latitude=53.2600, longitude=-2.0150,
        type="forest", description="Peaceful conifer forest on the edge of the Peak District with reservoir views.",
        drive_time="55 min", walk_url=_search_url("Macclesfield Forest"), user="robert"
    ),
    Location(
        id=26, name="Tegg's Nose", latitude=53.2544, longitude=-2.0790,
        type="forest", description="Country park with panoramic Peak District views and old quarry workings to explore.",
        drive_time="50 min", walk_url=_search_url("Tegg's Nose Macclesfield"), user="robert"
    ),
    Location(
        id=27, name="Beacon Fell", latitude=53.8520, longitude=-2.5810,
        type="forest", description="Lancashire country park with forest trails and sweeping views to the Lake District.",
        drive_time="45 min", walk_url=_search_url("Beacon Fell Lancashire"), user="robert"
    ),
    Location(
        id=28, name="Grizedale Forest", latitude=54.3500, longitude=-2.9840,
        type="forest", description="Lake District forest with sculpture trails, wildlife, and mountain bike routes.",
        drive_time="1hr 30min", walk_url=_search_url("Grizedale Forest"), user="robert"
    ),
    Location(
        id=29, name="The Cloud", latitude=53.1612, longitude=-2.1988,
        type="forest", description="Distinctive gritstone hill with heathland summit and views across Cheshire Plain.",
        drive_time="45 min", walk_url=_search_url("The Cloud Congleton"), user="robert"
    ),
    Location(
        id=30, name="Helsby Hill", latitude=53.2742, longitude=-2.7750,
        type="forest", description="Sandstone crag with woodland trails and spectacular views over the Mersey estuary.",
        drive_time="25 min", walk_url=_search_url("Helsby Hill"), user="robert"
    ),
    # Coastal/Moorland/Hills
    Location(
        id=31, name="Formby Beach & Pinewoods", latitude=53.5630, longitude=-3.0870,
        type="coastal", description="Red squirrel reserve with pine forests leading to vast sandy beaches and dunes.",
        drive_time="35 min", walk_url=_search_url("Formby Beach National Trust"), user="robert"
    ),
    Location(
        id=32, name="Crosby Beach", latitude=53.4752, longitude=-3.0392,
        type="coastal", description="Home to Antony Gormley's 'Another Place' iron men sculptures along the shoreline.",
        drive_time="25 min", walk_url=_search_url("Crosby Beach Another Place"), user="robert"
    ),
    Location(
        id=33, name="West Kirby & Hilbre Island", latitude=53.3735, longitude=-3.1830,
        type="coastal", description="Tidal walk across the sands to Hilbre Island with seals and spectacular sunsets.",
        drive_time="40 min", walk_url=_search_url("Hilbre Island West Kirby"), user="robert"
    ),
    Location(
        id=34, name="Arnside Knott", latitude=54.1957, longitude=-2.8407,
        type="coastal", description="Limestone hill with views over Morecambe Bay and the Lake District fells.",
        drive_time="1hr 15min", walk_url=_search_url("Arnside Knott"), user="robert"
    ),
    Location(
        id=35, name="Silverdale", latitude=54.1700, longitude=-2.8230,
        type="coastal", description="AONB with limestone pavements, woodland, and stunning Morecambe Bay views.",
        drive_time="1hr 10min", walk_url=_search_url("Silverdale Lancashire"), user="robert"
    ),
    Location(
        id=36, name="Mam Tor", latitude=53.3490, longitude=-1.8098,
        type="coastal", description="The 'Shivering Mountain' with ridge walks and spectacular Peak District panoramas.",
        drive_time="1hr 10min", walk_url=_search_url("Mam Tor Peak District"), user="robert"
    ),
    Location(
        id=37, name="Kinder Scout", latitude=53.3870, longitude=-1.8760,
        type="coastal", description="Highest point in the Peak District with moorland plateau and historic mass trespass route.",
        drive_time="1hr 15min", walk_url=_search_url("Kinder Scout"), user="robert"
    ),
    Location(
        id=38, name="Stanage Edge", latitude=53.3486, longitude=-1.6315,
        type="coastal", description="Dramatic gritstone edge popular with climbers, with sweeping moorland views.",
        drive_time="1hr 20min", walk_url=_search_url("Stanage Edge"), user="robert"
    ),
    Location(
        id=39, name="Malham Cove", latitude=54.0720, longitude=-2.1566,
        type="coastal", description="Stunning curved limestone cliff with pavement on top and waterfall after rain.",
        drive_time="1hr 30min", walk_url=_search_url("Malham Cove Yorkshire"), user="robert"
    ),
    Location(
        id=40, name="Ingleton Waterfalls", latitude=54.1560, longitude=-2.4650,
        type="coastal", description="Classic waterfall trail through ancient woodland in the Yorkshire Dales.",
        drive_time="1hr 20min", walk_url=_search_url("Ingleton Waterfalls Trail"), user="robert"
    ),
]


def get_all_locations(mode: Mode = "callum") -> list[Location]:
    """Get all locations for the specified user."""
    return [loc for loc in ALL_LOCATIONS if loc.user == mode]


def get_location_by_id(location_id: int, mode: Mode = "callum") -> Location | None:
    """Get a specific location by ID for the specified user."""
    locations = get_all_locations(mode)
    for loc in locations:
        if loc.id == location_id:
            return loc
    return None
