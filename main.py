from faker import Faker
import random
productData = [
  {
    "ProductID": 1,
    "ProductName": "AquaMist",
    "Price": 38834,
    "Description": "The water that hydrates and mystifies.",
    "Category": 5
  },
  {
    "ProductID": 2,
    "ProductName": "SwiftCharge",
    "Price": 10310,
    "Description": "The energy drink that gives you wings... and lightning bolts.",
    "Category": 1
  },
  {
    "ProductID": 3,
    "ProductName": "OnyxGlow",
    "Price": 30855,
    "Description": "The highlighter that illuminates your soul... and your cheekbones.",
    "Category": 2
  },
  {
    "ProductID": 4,
    "ProductName": "LunaScent",
    "Price": 20686,
    "Description": "The perfume that smells like moonbeams and stardust.",
    "Category": 3
  },
  {
    "ProductID": 5,
    "ProductName": "ChromaHue",
    "Price": 4038,
    "Description": "The paint that lets you hue you really are.",
    "Category": 5
  },
  {
    "ProductID": 6,
    "ProductName": "VaporBite",
    "Price": 34760,
    "Description": "The e-cigarette that's so cool, it's subzero.",
    "Category": 5
  },
  {
    "ProductID": 7,
    "ProductName": "BlazeBeam",
    "Price": 15856,
    "Description": "The flashlight that's so bright, it makes the sun jealous.",
    "Category": 5
  },
  {
    "ProductID": 8,
    "ProductName": "SolarSphere",
    "Price": 11354,
    "Description": "The beach ball that's out of this world... and into the sun.",
    "Category": 1
  },
  {
    "ProductID": 9,
    "ProductName": "SonicBoost",
    "Price": 8220,
    "Description": "The earbuds that make you feel like Sonic the Hedgehog.",
    "Category": 3
  },
  {
    "ProductID": 10,
    "ProductName": "NatureTonic",
    "Price": 29627,
    "Description": "The elixir that makes you feel one with the earth... and the plants.",
    "Category": 5
  },
  {
    "ProductID": 11,
    "ProductName": "MysticMist",
    "Price": 13050,
    "Description": "The fog machine that turns your living room into a mystical wonderland.",
    "Category": 2
  },
  {
    "ProductID": 12,
    "ProductName": "AlpineFrost",
    "Price": 33383,
    "Description": "The air freshener that smells like winter... in the Swiss Alps.",
    "Category": 5
  },
  {
    "ProductID": 13,
    "ProductName": "CrimsonCrush",
    "Price": 13634,
    "Description": "The lipstick that's so red, it crushes the competition.",
    "Category": 2
  },
  {
    "ProductID": 14,
    "ProductName": "EarthBlend",
    "Price": 12306,
    "Description": "The coffee that's made from dirt... and magic beans.",
    "Category": 2
  },
  {
    "ProductID": 15,
    "ProductName": "AuraGlow",
    "Price": 5418,
    "Description": "The toothpaste that brightens your smile... and your aura.",
    "Category": 3
  },
  {
    "ProductID": 16,
    "ProductName": "CrystalSpritz",
    "Price": 7531,
    "Description": "The air freshener that's so clean, it makes you want to lick the air.",
    "Category": 2
  },
  {
    "ProductID": 17,
    "ProductName": "SolarFrost",
    "Price": 13492,
    "Description": "The freezer that's powered by the sun... and the North Pole.",
    "Category": 2
  },
  {
    "ProductID": 18,
    "ProductName": "VitalWave",
    "Price": 17588,
    "Description": "The energy drink that's like a wave of vitality... with a splash of caffeine.",
    "Category": 5
  },
  {
    "ProductID": 19,
    "ProductName": "OceanicAura",
    "Price": 21726,
    "Description": "The body wash that smells like the sea... and a mermaid's perfume.",
    "Category": 3
  },
  {
    "ProductID": 20,
    "ProductName": "RadiantSpray",
    "Price": 7903,
    "Description": "The hairspray that makes your hair shine... like a disco ball.",
    "Category": 3
  },
  {
    "ProductID": 21,
    "ProductName": "TerraMist",
    "Price": 18572,
    "Description": "The air freshener that smells like freshly turned soil... and success.",
    "Category": 3
  },
  {
    "ProductID": 22,
    "ProductName": "FusionBrew",
    "Price": 9255,
    "Description": "The tea that's a fusion of flavors... and magic.",
    "Category": 1
  },
  {
    "ProductID": 23,
    "ProductName": "ArcticFlame",
    "Price": 33606,
    "Description": "The hot sauce that's so hot, it's like the Arctic... on fire.",
    "Category": 1
  },
  {
    "ProductID": 24,
    "ProductName": "StormSurge",
    "Price": 16606,
    "Description": "The surge protector that protects your electronics... from a storm of power surges.",
    "Category": 2
  },
  {
    "ProductID": 25,
    "ProductName": "SparklingSpritz",
    "Price": 2087,
    "Description": "The soda that's so fizzy, it makes your tongue sparkle... like a diamond.",
    "Category": 3
  },
  {
    "ProductID": 26,
    "ProductName": "SunburstBrew",
    "Price": 18530,
    "Description": "The beer that's like a burst of sunshine... and hops.",
    "Category": 4
  },
  {
    "ProductID": 27,
    "ProductName": "MysticMelody",
    "Price": 18660,
    "Description": "The music player that plays mystical melodies... and maybe some Britney Spears.",
    "Category": 4
  },
  {
    "ProductID": 28,
    "ProductName": "SolarSwirl",
    "Price": 27550,
    "Description": "The frozen yogurt that's swirled with sunshine... and rainbow sprinkles.",
    "Category": 1
  },
  {
    "ProductID": 29,
    "ProductName": "MysticMist",
    "Price": 39344,
    "Description": "The spray that's mystifying... and smells like a unicorn's breath.",
    "Category": 1
  },
  {
    "ProductID": 30,
    "ProductName": "SkySparkle",
    "Price": 11374,
    "Description": "The glitter that's as sparkly as the sky... on New Year's Eve.",
    "Category": 2
  },
  {
    "ProductID": 31,
    "ProductName": "AquaBurst",
    "Price": 22356,
    "Description": "The water balloon that bursts with so much force, it drenches your enemies... and your friends.",
    "Category": 4
  },
  {
    "ProductID": 32,
    "ProductName": "FireflyFizz",
    "Price": 6051,
    "Description": "The soda that fizzes like fireflies... and tickles your nose.",
    "Category": 4
  },
  {
    "ProductID": 33,
    "ProductName": "ZenBloom",
    "Price": 36125,
    "Description": "The flower that blooms with a sense of inner peace... and maybe some weed.",
    "Category": 1
  },
  {
    "ProductID": 34,
    "ProductName": "GoldenBurst",
    "Price": 5191,
    "Description": "The candy that's so golden, it bursts with flavor... and treasure.",
    "Category": 3
  },
  {
    "ProductID": 35,
    "ProductName": "EarthyScent",
    "Price": 39472,
    "Description": "The candle that smells like the earth... and a campfire.",
    "Category": 5
  },
  {
    "ProductID": 36,
    "ProductName": "OceanicSerenity",
    "Price": 26080,
    "Description": "The bath salts that make you feel serene",
    "Category": 4
  },
  {
    "ProductID": 37,
    "ProductName": "MoonlitMist",
    "Price": 12012,
    "Description": "The perfume that smells like a moonlit garden... and a werewolf's musk.",
    "Category": 3
  },
  {
    "ProductID": 38,
    "ProductName": "RainbowRush",
    "Price": 5449,
    "Description": "The energy drink that's like a rainbow of flavors... and sugar.",
    "Category": 4
  },
  {
    "ProductID": 39,
    "ProductName": "FrostyFiesta",
    "Price": 27178,
    "Description": "The frozen margarita that's so frosty, it's like a party in your mouth... and brain freeze.",
    "Category": 1
  },
  {
    "ProductID": 40,
    "ProductName": "StarlightSpray",
    "Price": 9802,
    "Description": "The body spray that smells like starlight... and hopes and dreams.",
    "Category": 2
  },
  {
    "ProductID": 41,
    "ProductName": "BerryBlaze",
    "Price": 7859,
    "Description": "The hot sauce that's so berrylicious, it's like a berry blaze in your mouth.",
    "Category": 1
  },
  {
    "ProductID": 42,
    "ProductName": "CosmicCotton",
    "Price": 2234,
    "Description": "The cotton candy that's out of this world... and maybe made of space dust.",
    "Category": 3
  },
  {
    "ProductID": 43,
    "ProductName": "RadiantRain",
    "Price": 17995,
    "Description": "The raincoat that's so radiant, it makes you feel like a superhero... and wet.",
    "Category": 2
  },
  {
    "ProductID": 44,
    "ProductName": "EmberEssence",
    "Price": 24082,
    "Description": "The cologne that smells like an ember in the wind... and a lumberjack's beard.",
    "Category": 2
  },
  {
    "ProductID": 45,
    "ProductName": "MysticMingle",
    "Price": 35396,
    "Description": "The dating app that's so mystical, it matches you with your soulmate... and maybe a mermaid.",
    "Category": 5
  },
  {
    "ProductID": 46,
    "ProductName": "SolarSizzle",
    "Price": 36167,
    "Description": "The grill that's powered by the sun... and a passion for barbecue.",
    "Category": 4
  },
  {
    "ProductID": 47,
    "ProductName": "OceanicOasis",
    "Price": 18098,
    "Description": "The beach towel that makes you feel like you're in an oceanic oasis... and maybe a mirage.",
    "Category": 2
  },
  {
    "ProductID": 48,
    "ProductName": "FlameFusion",
    "Price": 26260,
    "Description": "The candle that fuses different scents... and maybe some explosions.",
    "Category": 1
  },
  {
    "ProductID": 49,
    "ProductName": "ZenZone",
    "Price": 29602,
    "Description": "The meditation app that helps you find your zen... and your inner peace... and maybe some enlightenment.",
    "Category": 4
  },
  {
    "ProductID": 50,
    "ProductName": "LunarLullaby",
    "Price": 17208,
    "Description": "The music player that plays lullabies... and sounds of the moon... and maybe some Metallica.",
    "Category": 5
  },
  {
    "ProductID": 51,
    "ProductName": "AquaAdventures",
    "Price": 12606,
    "Description": "The snorkeling gear that makes you feel like you're on an underwater adventure... and maybe Finding Nemo.",
    "Category": 3
  },
  {
    "ProductID": 52,
    "ProductName": "CosmicCraze",
    "Price": 9545,
    "Description": "The popcorn that's out of this world... and maybe made of meteorites.",
    "Category": 3
  },
  {
    "ProductID": 53,
    "ProductName": "RadiantRelax",
    "Price": 1163,
    "Description": "The massage chair that relaxes your body... and radiates your aura... and maybe tickles your feet.",
    "Category": 3
  },
  {
    "ProductID": 54,
    "ProductName": "EmberEuphoria",
    "Price": 33701,
    "Description": "The fire pit that makes you feel euphoric... and maybe sets your hair on fire.",
    "Category": 1
  },
  {
    "ProductID": 55,
    "ProductName": "MysticMerch",
    "Price": 19269,
    "Description": "The online store that sells mystical merchandise... and maybe some unicorn onesies.",
    "Category": 2
  },
  {
    "ProductID": 56,
    "ProductName": "SolarSensation",
    "Price": 17485,
    "Description": "The sunglasses that make you feel the sensation of the sun... and maybe some temporary blindness.",
    "Category": 3
  },
  {
    "ProductID": 57,
    "ProductName": "OceanicOdyssey",
    "Price": 7266,
    "Description": "The cruise ship that takes you on an oceanic odyssey... and maybe a pirate adventure.",
    "Category": 1
  },
  {
    "ProductID": 58,
    "ProductName": "FlameFiesta",
    "Price": 21099,
    "Description": "The gas grill that makes you feel like you're having a flame fiesta... and maybe a trip to the ER.",
    "Category": 2
  },
  {
    "ProductID": 59,
    "ProductName": "ZenZest",
    "Price": 2919,
    "Description": "The diffuser that diffuses zen... and maybe some lavender essential oil.",
    "Category": 1
  },
  {
    "ProductID": 60,
    "ProductName": "LunarLounge",
    "Price": 37994,
    "Description": "The bean bag chair that's so comfortable, it makes you feel like you're lounging on the moon... and maybe some chips and dip.",
    "Category": 4
  },
  {
    "ProductID": 61,
    "ProductName": "AquaAttack",
    "Price": 20602,
    "Description": "The water gun that's so powerful, it attacks your enemies... and maybe your friends.",
    "Category": 3
  },
  {
    "ProductID": 62,
    "ProductName": "CosmicCrush",
    "Price": 7113,
    "Description": "The cereal that's so cosmic, it crushes your taste buds... and maybe some planets.",
    "Category": 1
  },
  {
    "ProductID": 63,
    "ProductName": "RadiantRetro",
    "Price": 14965,
    "Description": "The record player that plays radiant retro music... and maybe some ABBA.",
    "Category": 3
  },
  {
    "ProductID": 64,
    "ProductName": "EmberElegance",
    "Price": 29586,
    "Description": "The fireplace that adds elegance to your home... and maybe sets your drapes on fire.",
    "Category": 5
  },
  {
    "ProductID": 65,
    "ProductName": "MysticMood",
    "Price": 21411,
    "Description": "The smart lightbulbs that create a mystical mood... and maybe a seance.",
    "Category": 5
  },
  {
    "ProductID": 66,
    "ProductName": "SolarSerenade",
    "Price": 25895,
    "Description": "The outdoor speaker that serenades you with solar-powered music... and maybe some birds chirping.",
    "Category": 2
  },
  {
    "ProductID": 67,
    "ProductName": "OceanicOpulence",
    "Price": 7408,
    "Description": "The yacht that takes you on an oceanic journey of opulence... and maybe a game of yacht polo.",
    "Category": 4
  },
  {
    "ProductID": 68,
    "ProductName": "FlameFrenzy",
    "Price": 14731,
    "Description": "The hot sauce that creates a frenzy in your mouth... and maybe some tears.",
    "Category": 3
  },
  {
    "ProductID": 69,
    "ProductName": "ZenZoo",
    "Price": 6884,
    "Description": "The zoo that's so zen, it's like a meditation session with animals... and maybe some koala cuddling.",
    "Category": 3
  },
  {
    "ProductID": 70,
    "ProductName": "LunarLustre",
    "Price": 1058,
    "Description": "The jewelry that's so shiny, it looks like it's made of lunar dust... and maybe some moon rocks.",
    "Category": 5
  },
  {
    "ProductID": 71,
    "ProductName": "AquaAdventure",
    "Price": 17999,
    "Description": "The inflatable water park that creates an aqua adventure... and maybe some belly flops.",
    "Category": 4
  },
  {
    "ProductID": 72,
    "ProductName": "CosmicCrisp",
    "Price": 16476,
    "Description": "The apple that's so cosmic, it's out of this world... and maybe a supernova explosion.",
    "Category": 2
  },
  {
    "ProductID": 73,
    "ProductName": "RadiantRendezvous",
    "Price": 9410,
    "Description": "The dating service that connects you with radiant people... and maybe a romantic rendezvous.",
    "Category": 2
  },
  {
    "ProductID": 74,
    "ProductName": "EmberEnchantment",
    "Price": 38804,
    "Description": "The magic wand that creates an ember enchantment... and maybe some dragon fire.",
    "Category": 3
  },
  {
    "ProductID": 75,
    "ProductName": "MysticMuse",
    "Price": 6251,
    "Description": "The writing software that inspires you with mystical musings... and maybe a bestseller.",
    "Category": 3
  },
  {
    "ProductID": 76,
    "ProductName": "SolarSparkle",
    "Price": 38572,
    "Description": "The glitter that sparkles like the sun... and maybe some glitter in your eyes.",
    "Category": 4
  },
  {
    "ProductID": 77,
    "ProductName": "OceanicOyster",
    "Price": 5991,
    "Description": "The seafood restaurant that specializes in oceanic oysters... and maybe some pearl diving.",
    "Category": 1
  },
  {
    "ProductID": 78,
    "ProductName": "FlameFlair",
    "Price": 25772,
    "Description": "The flamethrower that adds some flair to your life... and maybe a firework display.",
    "Category": 5
  },
  {
    "ProductID": 79,
    "ProductName": "ZenZip",
    "Price": 26918,
    "Description": "The zipline that takes you on a zen adventure... and maybe some screaming.",
    "Category": 4
  },
  {
    "ProductID": 80,
    "ProductName": "LunarLuscious",
    "Price": 38550,
    "Description": "The ice cream that's so luscious, it tastes like it's made of lunar cream... and maybe some moon pies.",
    "Category": 2
  },
  {
    "ProductID": 81,
    "ProductName": "AquaAroma",
    "Price": 11704,
    "Description": "The shower gel that smells like a refreshing aqua aroma... and maybe some salty sea breeze.",
    "Category": 3
  },
  {
    "ProductID": 82,
    "ProductName": "CosmicCandies",
    "Price": 34401,
    "Description": "The candies that are so cosmic, they taste like they're made of stardust... and maybe some sugar rush.",
    "Category": 3
  },
  {
    "ProductID": 83,
    "ProductName": "RadiantRetrograde",
    "Price": 16523,
    "Description": "The astrology app that predicts your radiant retrograde... and maybe some mercury in retrograde.",
    "Category": 3
  },
  {
    "ProductID": 84,
    "ProductName": "EmberEcstasy",
    "Price": 19578,
    "Description": "The bonfire that creates an ember ecstasy... and maybe some marshmallow roasting.",
    "Category": 5
  },
  {
    "ProductID": 85,
    "ProductName": "MysticMastery",
    "Price": 2896,
    "Description": "The online course that teaches you mystical mastery... and maybe some spells.",
    "Category": 2
  },
  {
    "ProductID": 86,
    "ProductName": "SolarSustain",
    "Price": 1855,
    "Description": "The solar panel that creates sustainable energy... and maybe some savings on your electricity bill.",
    "Category": 5
  },
  {
    "ProductID": 87,
    "ProductName": "OceanicOdor",
    "Price": 30756,
    "Description": "The air freshener that smells like a refreshing oceanic odor... and maybe some seaweed.",
    "Category": 1
  },
  {
    "ProductID": 88,
    "ProductName": "FlameFlicker",
    "Price": 6885,
    "Description": "The candle that flickers like a flame... and maybe some romantic ambiance.",
    "Category": 2
  },
  {
    "ProductID": 89,
    "ProductName": "ZenZone-out",
    "Price": 22758,
    "Description": "The meditation class that takes you on a zen zone-out... and maybe some snoring.",
    "Category": 3
  },
  {
    "ProductID": 90,
    "ProductName": "LunarLounge-wear",
    "Price": 19266,
    "Description": "The pajamas that are so comfortable, they make you feel like you're lounging on the moon... and maybe some Netflix.",
    "Category": 1
  },
  {
    "ProductID": 91,
    "ProductName": "AquaAdventure-parka",
    "Price": 3099,
    "Description": "The parka that keeps you warm on your aqua adventure... and maybe some iceberg spotting.",
    "Category": 4
  },
  {
    "ProductID": 92,
    "ProductName": "CosmicCuisine",
    "Price": 17301,
    "Description": "The restaurant that serves cosmic cuisine... and maybe some alien delicacies.",
    "Category": 2
  },
  {
    "ProductID": 93,
    "ProductName": "RadiantRunway",
    "Price": 32123,
    "Description": "The fashion show that showcases radiant runway looks... and maybe some paparazzi.",
    "Category": 3
  },
  {
    "ProductID": 94,
    "ProductName": "EmberExtinguisher",
    "Price": 691,
    "Description": "The fire extinguisher that puts out your ember ecstasy... and maybe some disappointment.",
    "Category": 1
  },
  {
    "ProductID": 95,
    "ProductName": "MysticMantra",
    "Price": 30537,
    "Description": "The mantra that unlocks your mystical potential... and maybe some enlightenment.",
    "Category": 1
  },
  {
    "ProductID": 96,
    "ProductName": "SolarSpectacle",
    "Price": 21562,
    "Description": "The solar eclipse glasses that turn the spectacle into a solar spectacle... and maybe some sunburn.",
    "Category": 5
  },
  {
    "ProductID": 97,
    "ProductName": "OceanicOasis",
    "Price": 9990,
    "Description": "The beach resort that's an oceanic oasis... and maybe some coconut drinks.",
    "Category": 1
  },
  {
    "ProductID": 98,
    "ProductName": "FlameFreeze",
    "Price": 15889,
    "Description": "The freeze-dried ice cream that cools down your flame frenzy... and maybe some astronaut nostalgia.",
    "Category": 4
  },
  {
    "ProductID": 99,
    "ProductName": "ZenZinger",
    "Price": 10073,
    "Description": "The mindfulness coach that's a real zen zinger... and maybe some life-changing epiphanies.",
    "Category": 5
  }
]
productNamesAndDesc = ['ZenBlend - The tea that makes you go "ohmmm".', "AquaMist - The water that hydrates and mystifies.", "SwiftCharge - The energy drink that gives you wings... and lightning bolts.", "OnyxGlow - The highlighter that illuminates your soul... and your cheekbones.", "LunaScent - The perfume that smells like moonbeams and stardust.", 'ChromaHue - The paint that lets you hue you really are.', "VaporBite - The e-cigarette that's so cool, it's subzero.", "BlazeBeam - The flashlight that's so bright, it makes the sun jealous.", "SolarSphere - The beach ball that's out of this world... and into the sun.", "SonicBoost - The earbuds that make you feel like Sonic the Hedgehog.", "NatureTonic - The elixir that makes you feel one with the earth... and the plants.", "MysticMist - The fog machine that turns your living room into a mystical wonderland.", "AlpineFrost - The air freshener that smells like winter... in the Swiss Alps.", "CrimsonCrush - The lipstick that's so red, it crushes the competition.", "EarthBlend - The coffee that's made from dirt... and magic beans.", "AuraGlow - The toothpaste that brightens your smile... and your aura.", "CrystalSpritz - The air freshener that's so clean, it makes you want to lick the air.", "SolarFrost - The freezer that's powered by the sun... and the North Pole.", "VitalWave - The energy drink that's like a wave of vitality... with a splash of caffeine.", "OceanicAura - The body wash that smells like the sea... and a mermaid's perfume.", "RadiantSpray - The hairspray that makes your hair shine... like a disco ball.", "TerraMist - The air freshener that smells like freshly turned soil... and success.", "FusionBrew - The tea that's a fusion of flavors... and magic.", "ArcticFlame - The hot sauce that's so hot, it's like the Arctic... on fire.", "StormSurge - The surge protector that protects your electronics... from a storm of power surges.", "SparklingSpritz - The soda that's so fizzy, it makes your tongue sparkle... like a diamond.", "SunburstBrew - The beer that's like a burst of sunshine... and hops.", "MysticMelody - The music player that plays mystical melodies... and maybe some Britney Spears.", "SolarSwirl - The frozen yogurt that's swirled with sunshine... and rainbow sprinkles.", "MysticMist - The spray that's mystifying... and smells like a unicorn's breath.", "SkySparkle - The glitter that's as sparkly as the sky... on New Year's Eve.", "AquaBurst - The water balloon that bursts with so much force, it drenches your enemies... and your friends.", "FireflyFizz - The soda that fizzes like fireflies... and tickles your nose.", "ZenBloom - The flower that blooms with a sense of inner peace... and maybe some weed.", "GoldenBurst - The candy that's so golden, it bursts with flavor... and treasure.", "EarthyScent - The candle that smells like the earth... and a campfire.", "OceanicSerenity - The bath salts that make you feel serene", "MoonlitMist - The perfume that smells like a moonlit garden... and a werewolf's musk.", "RainbowRush - The energy drink that's like a rainbow of flavors... and sugar.", "FrostyFiesta - The frozen margarita that's so frosty, it's like a party in your mouth... and brain freeze.", "StarlightSpray - The body spray that smells like starlight... and hopes and dreams.", "BerryBlaze - The hot sauce that's so berrylicious, it's like a berry blaze in your mouth.", "CosmicCotton - The cotton candy that's out of this world... and maybe made of space dust.", "RadiantRain - The raincoat that's so radiant, it makes you feel like a superhero... and wet.", "EmberEssence - The cologne that smells like an ember in the wind... and a lumberjack's beard.", "MysticMingle - The dating app that's so mystical, it matches you with your soulmate... and maybe a mermaid.", "SolarSizzle - The grill that's powered by the sun... and a passion for barbecue.", "OceanicOasis - The beach towel that makes you feel like you're in an oceanic oasis... and maybe a mirage.", "FlameFusion - The candle that fuses different scents... and maybe some explosions.", "ZenZone - The meditation app that helps you find your zen... and your inner peace... and maybe some enlightenment.", "LunarLullaby - The music player that plays lullabies... and sounds of the moon... and maybe some Metallica.", "AquaAdventures - The snorkeling gear that makes you feel like you're on an underwater adventure... and maybe Finding Nemo.", "CosmicCraze - The popcorn that's out of this world... and maybe made of meteorites.", "RadiantRelax - The massage chair that relaxes your body... and radiates your aura... and maybe tickles your feet.", "EmberEuphoria - The fire pit that makes you feel euphoric... and maybe sets your hair on fire.", "MysticMerch - The online store that sells mystical merchandise... and maybe some unicorn onesies.", "SolarSensation - The sunglasses that make you feel the sensation of the sun... and maybe some temporary blindness.", "OceanicOdyssey - The cruise ship that takes you on an oceanic odyssey... and maybe a pirate adventure.", "FlameFiesta - The gas grill that makes you feel like you're having a flame fiesta... and maybe a trip to the ER.", "ZenZest - The diffuser that diffuses zen... and maybe some lavender essential oil.", "LunarLounge - The bean bag chair that's so comfortable, it makes you feel like you're lounging on the moon... and maybe some chips and dip.", "AquaAttack - The water gun that's so powerful, it attacks your enemies... and maybe your friends.", "CosmicCrush - The cereal that's so cosmic, it crushes your taste buds... and maybe some planets.", "RadiantRetro - The record player that plays radiant retro music... and maybe some ABBA.", "EmberElegance - The fireplace that adds elegance to your home... and maybe sets your drapes on fire.", "MysticMood - The smart lightbulbs that create a mystical mood... and maybe a seance.", "SolarSerenade - The outdoor speaker that serenades you with solar-powered music... and maybe some birds chirping.", "OceanicOpulence - The yacht that takes you on an oceanic journey of opulence... and maybe a game of yacht polo.", "FlameFrenzy - The hot sauce that creates a frenzy in your mouth... and maybe some tears.", "ZenZoo - The zoo that's so zen, it's like a meditation session with animals... and maybe some koala cuddling.", "LunarLustre - The jewelry that's so shiny, it looks like it's made of lunar dust... and maybe some moon rocks.", "AquaAdventure - The inflatable water park that creates an aqua adventure... and maybe some belly flops.", "CosmicCrisp - The apple that's so cosmic, it's out of this world... and maybe a supernova explosion.", "RadiantRendezvous - The dating service that connects you with radiant people... and maybe a romantic rendezvous.", "EmberEnchantment - The magic wand that creates an ember enchantment... and maybe some dragon fire.", "MysticMuse - The writing software that inspires you with mystical musings... and maybe a bestseller.", "SolarSparkle - The glitter that sparkles like the sun... and maybe some glitter in your eyes.", "OceanicOyster - The seafood restaurant that specializes in oceanic oysters... and maybe some pearl diving.", "FlameFlair - The flamethrower that adds some flair to your life... and maybe a firework display.", "ZenZip - The zipline that takes you on a zen adventure... and maybe some screaming.", "LunarLuscious - The ice cream that's so luscious, it tastes like it's made of lunar cream... and maybe some moon pies.", "AquaAroma - The shower gel that smells like a refreshing aqua aroma... and maybe some salty sea breeze.", "CosmicCandies - The candies that are so cosmic, they taste like they're made of stardust... and maybe some sugar rush.", "RadiantRetrograde - The astrology app that predicts your radiant retrograde... and maybe some mercury in retrograde.", "EmberEcstasy - The bonfire that creates an ember ecstasy... and maybe some marshmallow roasting.", "MysticMastery - The online course that teaches you mystical mastery... and maybe some spells.", "SolarSustain - The solar panel that creates sustainable energy... and maybe some savings on your electricity bill.", "OceanicOdor - The air freshener that smells like a refreshing oceanic odor... and maybe some seaweed.", "FlameFlicker - The candle that flickers like a flame... and maybe some romantic ambiance.", "ZenZone-out - The meditation class that takes you on a zen zone-out... and maybe some snoring.", "LunarLounge-wear - The pajamas that are so comfortable, they make you feel like you're lounging on the moon... and maybe some Netflix.", "AquaAdventure-parka - The parka that keeps you warm on your aqua adventure... and maybe some iceberg spotting.", "CosmicCuisine - The restaurant that serves cosmic cuisine... and maybe some alien delicacies.", "RadiantRunway - The fashion show that showcases radiant runway looks... and maybe some paparazzi.", "EmberExtinguisher - The fire extinguisher that puts out your ember ecstasy... and maybe some disappointment.", "MysticMantra - The mantra that unlocks your mystical potential... and maybe some enlightenment.", "SolarSpectacle - The solar eclipse glasses that turn the spectacle into a solar spectacle... and maybe some sunburn.", "OceanicOasis - The beach resort that's an oceanic oasis... and maybe some coconut drinks.", "FlameFreeze - The freeze-dried ice cream that cools down your flame frenzy... and maybe some astronaut nostalgia.", "ZenZinger - The mindfulness coach that's a real zen zinger... and maybe some life-changing epiphanies."]
fake = Faker()
#fill products
# with open("dummydata/products.csv", "w") as file:
#     for i in range(100):
#         if i==0:
#             file.write('"ProductID","ProductName","Price","Description","Category"'+'\n')
#         else:
#             product_id = i
#             product_name = productNamesAndDesc[i].split(' - ')[0]
#             # product_name = fake.company()
#             price = random.randint(100, 40000)
#             description = productNamesAndDesc[i].split(' - ')[1]
#             print(product_name, description)
#             category = random.randint(1, 5)
#             file.write('"{}","{}","{}","{}","{}"'.format(product_id, product_name,price,description, category)+'\n')

#fill customers
# with open("dummydata/customers.csv", "w") as file:
#     for i in range(20000):
#         if i==0:
#             file.write('"CustomerID","FirstName","LastName","Email","Phone"'+'\n')
#         else:
#             customer_id = i
#             profile = fake.simple_profile()
#             phone = fake.phone_number()
#             # print(fake.simple_profile(), fake.phone_number())
#             file.write('"{}","{}","{}","{}","{}"'.format(customer_id, profile['name'].split(' ')[0],profile['name'].split(' ')[1],profile['mail'], phone )+'\n')

#fill employees
# with open("dummydata/employees.csv", "w") as file:
#     jobs = ['Junior seller','Seller', 'Manager']
#     for i in range(100):
#         if i==0:
#             file.write('"EmployeeID","FirstName","LastName","Email","Phone","JobTitle"'+'\n')
#         else:
#             employee_id = i
#             profile = fake.simple_profile()
#             phone = fake.phone_number()
#             job = jobs[random.randint(0,2)]
#             print(profile, fake.phone_number())
#             file.write('"{}","{}","{}","{}","{}","{}"'.format(employee_id, profile['name'].split(' ')[0],profile['name'].split(' ')[1],profile['mail'], phone, job )+'\n')

#fill orders
def findPrice(product_id):
    for product in productData:
        print(product['ProductName'])
        if product["ProductID"]==product_id:
            return product["Price"]
with open("dummydata/orders.csv", "w") as file:
    for i in range(50000):
        if i==0:
            file.write('"OrderID","OrderDate","CustomerID","ProductID","Quantity","EmployeeID","Price"'+'\n')
        else:
            order_id = i
            order_date = fake.date_time_this_decade()
            customer_id = random.randint(1, 19999)
            product_id = random.randint(1, 99)
            quantity = random.randint(1, 20)
            employee_id = random.randint(1, 99)
            price = int(findPrice(product_id)) * quantity
            file.write('"{}","{}","{}","{}","{}","{}","{}"'.format(order_id, order_date,customer_id,product_id, quantity, employee_id, price )+'\n')