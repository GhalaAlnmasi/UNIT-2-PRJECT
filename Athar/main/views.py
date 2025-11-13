from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.utils.translation import gettext_lazy as _

REGIONS_LIST = [
    ('riyadh', _('Riyadh'), 'riyadh_view'),
    ('ash_sharqiyah', _('Ash-Sharqiyah'), 'ash_sharqiyah_view'),
    ('qassim', _('Qassim'), 'qassim_view'),
    ('makkah', _('Makkah'), 'makkah_view'),
    ('madinah', _('Madinah'), 'madinah_view'),
    ('tabuk', _('Tabuk'), 'tabuk_view'),
    ('jouf', _('Al-Jouf'), 'jouf_view'),
    ('hail', _('Hail'), 'hail_view'),
    ('ash_shamaliyah', _('Al-Hudud Ash-Shamaliyah'), 'ash_shamaliyah_view'),
    ('asir', _('Asir'), 'asir_view'),
    ('bahah', _('Al-Baha'), 'bahah_view'),
    ('jizan', _('Jazan'), 'jizan_view'),
    ('najran', _('Najran'), 'najran_view'),
]


REGIONS_DATA = {
    "riyadh": {
        "title": _("Riyadh"),
        "subtitle": _("A city that started from clay, then became a full horizon."),
        "locations": [
            {"name": _("Al-Masmak Palace"), "description": _("A clay fortress with sharp lines resembling the first words of a long novel. Here the unification began, and here the moment of Riyadh’s recapture in 1902 occurred. Every wall looks like an open historical page."),"image": "https://d.top4top.io/p_36037gjaq2.jpg"},
            {"name": _("Al-Turaif District - Diriyah (UNESCO site)"), "description": _("A clay city on the slopes of Wadi Hanifah. Narrow alleys, but vast memory. From here the first Saudi state arose, and the Najdis’ voices rose in architecture, jurisprudence, and politics."),"image": "https://i.top4top.io/p_3603vdmya1.jpg"},
            {"name": _("Wadi Hanifah"), "description": _("A green strip cutting through the desert. It was a caravan route and a center of settlement; today it’s an extended oasis combining the city with its natural history."),"image": "https://i.top4top.io/p_3603oei3m3.jpg"},
        ],
    },
    "makkah": {
        "title": _("Makkah"),
        "subtitle": _("A heart where people walk from all directions."),
        "locations": [
            {"name": _("Jabal Noor – Hira Cave"), "description": _("The mountain that witnessed the start of revelation. The mountain does not comment on history, but it remains standing as if it knows more than it says."),"image": "https://e.top4top.io/p_3604rasyr3.jpg"},
            {"name": _("Al-Bay’ah Mosque"), "description": _("Site of the pledge of allegiance of the Ansar to the Prophet ﷺ. Simple in form, heavy in symbolism. Here, words were not mere words, they were the foundation of destiny."),"image": "https://d.top4top.io/p_3603u40hc1.jpg"},
            {"name": _("Makkah Museum of Heritage and Antiquities"), "description": _("An old Ottoman house turned into an open memory: tools, manuscripts, old mosque doors, and pilgrims’ clothes from centuries past."),"image": "https://e.top4top.io/p_3604r65rt1.jpg"},
        ],
    },
    "madinah": {
        "title": _("Madinah"),
        "subtitle": _("Peace walks on the ground here."),
        "locations": [
            {"name": _("Al-Hijr (Madain Saleh / UNESCO)"), "description": _("A rock city carved 2000 years ago. The facades look like hanging doors waiting for someone to open them. Every tomb carries a name and a hand-etched story."),"image": "https://e.top4top.io/p_3604ge4o41.jpg"},
            {"name": _("Dadan"), "description": _("Capital of the Dadan and Lihyan kingdoms. The rock tombs are high as if windows overlooking a bygone time. A key trading station on the incense route."),"image": "https://i.top4top.io/p_3603p6h5o2.jpeg"},
            {"name": _("Quba Mosque"), "description": _("The first mosque in Islam. The place relies not on the beauty of details but on the beauty of history. It’s the beginning of the community before it was a building."),"image": "https://c.top4top.io/p_36043qact1.jpeg"},
        ],
    },
    "ash_sharqiyah": {
        "title": _("Ash-Sharqiyah"),
        "subtitle": _("Where the sea meets the palm trees and the old salt."),
        "locations": [
            {"name": _("Al-Ahsa Oasis (UNESCO)"), "description": _("Seas of palm trees. Water here is not just a river, but memory. The greatest continuously inhabited oasis in the world."),"image": "https://i.top4top.io/p_36034204t1.jpg"},
            {"name": _("Ibrahim Palace (Al-Hofuf)"), "description": _("An Ottoman fortress combining Najdi and Ottoman styles. Its walls are like layers of accumulated history."),"image": "https://f.top4top.io/p_36049c0h42.jpg"},
            {"name": _("Historical Port of Al-Aqeer"), "description": _("An old gateway to the Gulf; ships from India and East Africa anchored here. A place resembling an open door to maritime history."),"image": "https://c.top4top.io/p_3603g12661.jpg"},
        ],
    },
    "qassim": {
        "title": _("Qassim"),
        "subtitle": _("The heart of hot Najd… and the warmth of heritage."),
        "locations": [
            {"name": _("Al-Shanna Tower"), "description": _("An archaeological edifice that tells the story of the heroism shown by the people of Al-Ras and the strength of Bass in confronting aggression. It was a witness to their courage and sacrifice in defending their town."),"image": "https://j.top4top.io/p_3603eg7x82.jpg"},
            {"name": _("Al Musawkaf Traditional Market"), "description": _("A market that was a meeting point for traders, agriculture, and horses. Its scent is a mix of dates, coffee, and sun."),"image": "https://a.top4top.io/p_3604noe841.jpg"},
            {"name": _("Antarah's Palace and Rock"), "description": _("A rock are two archaeological sites associated with the pre-Islamic poet Antarah Ibn Shaddad, who resided between the town of Qusayba and the Uyun al-Jiwa Governorate, within Qassim Province at the heart of the Kingdom of Saudi Arabia."),"image": "https://f.top4top.io/p_3603kmv6h2.jpg"},
        ],
    },
    "tabuk": {
        "title": _("Tabuk"),
        "subtitle": _("Here’s the north that keeps its shadow long… a calm desert, and valleys that whisper."),
        "locations": [
            {"name": _("Tabuk Castle"), "description": _("A fortress guarded by silent stone walls, a station for caravans and pilgrims. Armies, travelers, and worshippers passed, yet it remains… only watching."),"image": "https://g.top4top.io/p_3604v1r3u1.jpg"},
            {"name": _("Ain Al-Sukkar (Ancient Springs)"), "description": _("Flowing water since ancient times; humans carved life and agriculture around it. Water here is not ordinary; it is a sign of survival."),"image": "https://b.top4top.io/p_36046aktz2.jpeg"},
            {"name": _("Wadi Al-Dissa"), "description": _("A green mountain canyon in the middle of the desert. Its rocky walls look like gates to an ancient city forgotten by time."),"image": "https://h.top4top.io/p_3604cgaw82.jpg"},
        ],
    },
    "hail": {
        "title": _("Hail"),
        "subtitle": _("Black mountains, red inscriptions, and silence filled with stories of those who passed before us."),
        "locations": [
            {"name": _("Jubbah (Rock Art / UNESCO)"), "description": _("Drawings of humans and animals thousands of years old. Ancestors drew their daily life on stone instead of paper."),"image": "https://d.top4top.io/p_3604t5nr61.jpeg"},
            {"name": _("Barzan Tower"), "description": _("A watchtower built in the late 19th century and renovated in 1910 by Muhammad bin Qasim Al Thani."),"image": "https://b.top4top.io/p_3603s2jwm1.jpg"},
            {"name": _("Al-Qishlah Palace"), "description": _("An old Ottoman administrative building. Its square, strong shape resembles the idea of “order” as cities learned early organization."),"image": "https://d.top4top.io/p_36049yn1n3.jpg"},
        ],
    },
    "jouf": {
        "title": _("Al-Jouf"),
        "subtitle": _("A region that knows the value of water in the desert… thus becoming an oasis of civilizations."),
        "locations": [
            {"name": _("Marid Castle – Dumat Al-Jandal"), "description": _("A tall stone castle standing proudly. Said “Marid rebelled against whoever tried to break it,” and it still supports this saying."),"image": "https://f.top4top.io/p_3604ouh7u2.jpg"},
            {"name": _("Omar Ibn Al-Khattab Mosque in Dumat Al-Jandal"), "description": _("One of the oldest surviving mosques. Simple stone construction, preserving centuries of impact as if breathing quietly."),"image": "https://b.top4top.io/p_36046iofm1.jpeg"},
            {"name": _("Dumat Al-Jandal Lake"), "description": _("Water surprises you in the desert depths. Not just an irrigation source, but a full-life hub."),"image": "https://c.top4top.io/p_36036t72a2.jpeg"},
        ],
    },
    "ash_shamaliyah": {
        "title": _("Al-Hudud Ash-Shamaliyah"),
        "subtitle": _("Vast land, low sky, and ruins standing as markers of the old passage."),
        "locations": [
            {"name": _("King Abdulaziz Palace in Linah"), "description": _("A royal palaces ordered to be built by the Founding King Abdulaziz Bin Abdulrahman Al Saud in various regions of the Kingdom of Saudi Arabia after its unification in 1932."),"image": "https://d.top4top.io/p_3604q2cwr2.jpg"},
            {"name": _("The Emirate Palace in Ar'ar"), "description": _("It is considered one of the oldest palaces in the Kingdom. The palace is divided into several rooms with different uses, and specific types of mountain stones were used in its construction."),"image": "https://c.top4top.io/p_3604ix3ev1.jpg"},
            {"name": _("Linah Heritage Village"), "description": _("A Village built during the reign of the Founding King Abdulaziz Bin Abdulrahman Al Saud during the unification of the Kingdom, the village is distinguished by its market where various goods and products were displayed."),"image": "https://e.top4top.io/p_3604s1tn52.png"},
        ],
    },
    "bahah": {
        "title": _("Al-Baha"),
        "subtitle": _("Wet mountains, suspended villages, and fog walking like a visitor who knows the way."),
        "locations": [
            {"name": _("Dhi Ayn Heritage Village"), "description": _("Built of white stone on a green hill. Looks like a painted canvas, yet very real."),"image": "https://b.top4top.io/p_3603ahd2t1.jpeg"},
            {"name": _("Matair Al-Aish Archaeological Village"), "description": _("The historic village of Mutair Al-Aish is rich in many historical and archaeological monuments, which are part of the barren Bani Assem region and surrounded by mountainous areas that reflect the beauty of nature."),"image": "https://g.top4top.io/p_36048lwfz3.jpg"},
            {"name": _("Bani Kabir"), "description": _("A large building center is located in the northern part of Beljarshi Governorate and is 12 km² from the headquarters of the governorate, and in the southeast of the city of Al-Baha."),"image": "https://h.top4top.io/p_3603b40yq1.jpeg"},
        ],
    },
    "asir": {
        "title": _("Asir"),
        "subtitle": _("The south that resembles no one… colored stones, and fog touching the mountains like a greeting."),
        "locations": [
            {"name": _("Rijal Almaa Village (UNESCO candidate)"), "description": _("Stone houses with colored windows, as if walls wear jewelry. The village is a stone poem."),"image": "https://d.top4top.io/p_3604vufs82.jpg"},
            {"name": _("Jabal Al-Souda"), "description": _("The highest mountains in the kingdom. Clouds here are not above you, but around you."),"image": "https://j.top4top.io/p_3604zzml72.png"},
            {"name": _("Hanging Al-Habla Village"), "description": _("Built on a steep cliff, as if a brave decision against gravity."),"image": "https://h.top4top.io/p_36033dku52.jpeg"},
        ],
    },
    "jizan": {
        "title": _("Jazan"),
        "subtitle": _("Warm sea, coral islands, and a maritime culture that never stops singing."),
        "locations": [
            {"name": _("Farasan Island"), "description": _("Marine reserve with coral beaches. Water here is like glass."),"image": "https://g.top4top.io/p_3603p4cx71.jpg"},
            {"name": _("Luqman Castle"), "description": _("An old stone fortress on a hill overlooking the sea."),"image": "https://f.top4top.io/p_3604i7xfv3.jpeg"},
            {"name": _("Al-Darb Archaeological Road"), "description": _("An old route linking coastal villages, still walking lightly through history."),"image": "https://h.top4top.io/p_3603kj9lw1.jpg"},
        ],
    },
    "najran": {
        "title": _("Najran"),
        "subtitle": _("South with the taste of dark coffee… civilizations crossed from Yemen to the peninsula."),
        "locations": [
            {"name": _("Aba Al-Saud Heritage District"), "description": _("Tall clay houses with small windows. Like towers made of clay."),"image": "https://g.top4top.io/p_3604jjl6r3.jpeg"},
            {"name": _("Najran Rock Inscriptions"), "description": _("Ancient southern Arabic writings. Every symbol looks like a pre-language word."),"image": "https://c.top4top.io/p_3604bl36w2.jpg"},
            {"name": _("Al-Okhdood Archaeological City"), "description": _("It consists of a surrounding wall, remnants of buildings, artifacts, tombs, inscriptions, and drawings. Its oldest artifacts date back to the Stone Age, while its most recent ones belong to the Islamic period, including artifacts from the Umayyad and Abbasid eras."),"image": "https://e.top4top.io/p_360320h051.jpg"},
        ],
    },
}




def home_view(request:HttpRequest):
    return render(request,"main/index.html", {"regions_list": REGIONS_LIST})



def riyadh_view(request:HttpRequest):
    region = REGIONS_DATA['riyadh']
    return render(request, "main/riyadh.html", {"region": region, "regions_list": REGIONS_LIST})

def makkah_view(request:HttpRequest):
    region = REGIONS_DATA['makkah']
    return render(request, "main/makkah.html", {"region": region, "regions_list": REGIONS_LIST})

def madinah_view(request:HttpRequest):
    region = REGIONS_DATA['madinah']
    return render(request, "main/madinah.html", {"region": region, "regions_list": REGIONS_LIST})

def ash_sharqiyah_view(request:HttpRequest):
    region = REGIONS_DATA['ash_sharqiyah']
    return render(request, "main/ash-sharqiyah.html", {"region": region, "regions_list": REGIONS_LIST})

def qassim_view(request:HttpRequest):
    region = REGIONS_DATA['qassim']
    return render(request, "main/qassim.html", {"region": region, "regions_list": REGIONS_LIST})

def tabuk_view(request:HttpRequest):
    region = REGIONS_DATA['tabuk']
    return render(request, "main/tabuk.html",{"region": region, "regions_list": REGIONS_LIST} )

def hail_view(request:HttpRequest):
    region = REGIONS_DATA['hail']
    return render(request, "main/hail.html", {"region": region, "regions_list": REGIONS_LIST})

def jouf_view(request:HttpRequest):
    region = REGIONS_DATA['jouf']
    return render(request, "main/jouf.html", {"region": region, "regions_list": REGIONS_LIST})

def ash_shamaliyah_view(request:HttpRequest):
    region =REGIONS_DATA['ash_shamaliyah']
    return render(request, "main/al-hudud-ash-shamaliyah.html", {"region": region, "regions_list": REGIONS_LIST})

def bahah_view(request:HttpRequest):
    region =REGIONS_DATA['bahah']
    return render(request, "main/bahah.html", {"region": region, "regions_list": REGIONS_LIST})

def asir_view(request:HttpRequest):
    region =REGIONS_DATA['asir']
    return render(request, "main/asir.html", {"region": region, "regions_list": REGIONS_LIST})

def jizan_view(request:HttpRequest):
    region =REGIONS_DATA['jizan']
    return render(request, "main/jizan.html", {"region": region, "regions_list": REGIONS_LIST})

def najran_view(request:HttpRequest):
    region =REGIONS_DATA['najran']
    return render(request, "main/najran.html", {"region": region, "regions_list": REGIONS_LIST})



def about_view(request:HttpRequest):
    return render(request, "main/about.html", {"regions_list": REGIONS_LIST})






def set_theme(request:HttpRequest, mode):
    response = redirect(request.GET.get('HTTP_REFERER', '/'))
    if mode in ['dark', 'light']:
        response.set_cookie('theme', mode, max_age=60*60*24) 
    return response


def set_language(request: HttpRequest, lang):
    referer = request.GET.get('HTTP_REFERER', request.META.get('HTTP_REFERER', '/'))
    response = redirect(referer)
    if lang in ['en', 'ar']:
        response.set_cookie('django_language', lang, max_age=60*60*24*30)
    return response