#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File: ponies.py
# by Arzaroth Lekva
# lekva@arzaroth.com
#

from collections import OrderedDict

PONY_LIST = OrderedDict([
    ('Pony_Ace', 'Ace'),
    ('Pony_AKYearling', 'AKYearling'),
    ('Pony_Aloe', 'Aloe'),
    ('Pony_Apple_Bloom', 'Apple Bloom'),
    ('Pony_Apple_Bottoms', 'Apple Bottoms'),
    ('Pony_Apple_Bumpkin', 'Apple Bumpkin'),
    ('Pony_Apple_Cider', 'Apple Cider'),
    ('Pony_Apple_Cinnamon', 'Apple Cinnamon'),
    ('Pony_Apple_Cobbler', 'Apple Cobbler'),
    ('Pony_Apple_Dumpling', 'Apple Dumpling'),
    ('Pony_Apple_Honey', 'Apple Honey'),
    ('Pony_Apple_Leaves', 'Apple Leaves'),
    ('Pony_Apple_Pie', 'Apple Pie'),
    ('Pony_Apple_Rose', 'Apple Rose'),
    ('Pony_Apple_Stars', 'Apple Stars'),
    ('Pony_Apple_Strudel', 'Apple Strudel'),
    ('Pony_Applefritter', 'Apple Fritter'),
    ('Pony_Applejack', 'Applejack'),
    ('Pony_Architecture_Unicorn', 'Architecture Unicorn'),
    ('Pony_Aunt_Applesauce', 'Aunt Applesauce'),
    ('Pony_Aunt_Orange', 'Aunt Orange'),
    ('Pony_Babs_Seed', 'Babs Seed'),
    ('Pony_Banana_Bliss', 'Banana Bliss'),
    ('Pony_Beauty_Brass', 'Beauty Brass'),
    ('Pony_Berry_Punch', 'Berry Punch'),
    ('Pony_Big_Mac', 'Big Macintosh'),
    ('Pony_Blue_moon', 'Blue Moon'),
    ('Pony_Bon_Bon', 'Bon Bon'),
    ('Pony_Braeburn', 'Braeburn'),
    ('Pony_Bright_Unicorn', 'Bright Unicorn'),
    ('Pony_Bulk_Biceps', 'Bulk Biceps'),
    ('Pony_Candy_Apples', 'Candy Apples'),
    ('Pony_Caramel', 'Caramel'),
    ('Pony_Caramel_Apple', 'Caramel Apple'),
    ('Pony_Cheerilee', 'Cheerilee'),
    ('Pony_Cheese_Sandwich', 'Cheese Sandwich'),
    ('Pony_Cherry_Fizzy', 'Cherry Fizzy'),
    ('Pony_Cherry_Jubilee', 'Cherry Jubilee'),
    ('Pony_CherryBerry', 'Cherry Berry'),
    ('Pony_Claude_the_Puppeteer', 'Claude the Puppeteer'),
    ('Pony_Clear_Skies', 'Clear Skies'),
    ('Pony_Clumsy_Clownspony', 'Clumsy Clownspony'),
    ('Pony_Coco_Pommel', 'Coco Pommel'),
    ('Pony_Comet_Tail', 'Comet Tail'),
    ('Pony_Compass_Star', 'Compass Star'),
    ('Pony_Conductor', 'Conductor'),
    ('Pony_Crescent_Moon', 'Crescent Moon'),
    ('Pony_Curio_Shopkeeper', 'Curio Shopkeeper'),
    ('Pony_Daisy', 'Daisy'),
    ('Pony_Dancing_Clownspony', 'Dancing Clownspony'),
    ('Pony_Daring', 'Daring Do'),
    ('Pony_Diamond_Tiara', 'Diamond Tiara'),
    ('Pony_Discord', 'Discord'),
    ('Pony_Dj_Pon3', 'Dj Pon3 (Ponyville)'),
    ('Pony_Dj_Pon3_Canterlot', 'Dj Pon3 (Canterlot)'),
    ('Pony_Double_Diamond', 'Double Diamond'),
    ('Pony_DrWhooves', 'Dr. Hooves'),
    ('Pony_Eclaire_Creme', 'Eclaire Creme'),
    ('Pony_Elite_Male', 'Elite Pony'),
    ('Pony_Emerald_Gem', 'Emerald Gem'),
    ('Pony_Emerald_Green', 'Emerald Green'),
    ('Pony_Fancypants', 'Fancypants'),
    ('Pony_Fashion_Plate', 'Fashion Plate'),
    ('Pony_Fashionable_Unicorn', 'Fashionable Unicorn'),
    ('Pony_Featherweight', 'Featherweight'),
    ('Pony_Filthy_Rich', 'Filthy Rich'),
    ('Pony_Fine_Line', 'Fine Line'),
    ('Pony_FireChief', 'Dinky Doo (Fire Chief)'),
    ('Pony_Flam', 'Flam'),
    ('Pony_Flash_Sentry', 'Flash Sentry'),
    ('Pony_Flashy_Pony', 'Flashy Pony'),
    ('Pony_Fleetfoot', 'Fleetfoot'),
    ('Pony_Fleur_Dis_Lee', 'Fleur Dis Lee'),
    ('Pony_Flim', 'Flim'),
    ('Pony_Fluttershy', 'Fluttershy'),
    ('Pony_Forsythia', 'Forsythia'),
    ('Pony_Four_Step', 'Four Step'),
    ('Pony_Frederic', 'Frederic'),
    ('Pony_Gala_Appleby', 'Gala Appleby'),
    ('Pony_Gilda', 'Gilda'),
    ('Pony_Gleeful_Clownspony', 'Gleeful Clownspony'),
    ('Pony_Golden_Delicious', 'Golden Delicious'),
    ('Pony_Golden_Harvest', 'Golden Harvest'),
    ('Pony_Goldie_Delicious', 'Goldie Delicious'),
    ('Pony_Goth_Unicorn', 'Goth Unicorn'),
    ('Pony_Grampa_Gruff', 'Grampa Gruff'),
    ('Pony_Granny_Smith', 'Granny Smith'),
    ('Pony_Green_Jewel', 'Green Jewel'),
    ('Pony_Greta', 'Greta'),
    ('Pony_Griffon_Shopkeeper', 'Griffon Shopkeeper'),
    ('Pony_Half_Baked_Apple', 'Half Baked Apple'),
    ('Pony_Hayseed_Turnip_Truck', 'Hayseed Turnip Truck'),
    ('Pony_Hoity_Toity', 'Hoity Toity'),
    ('Pony_Jeff_Letrotski', 'Jeff Letrotski'),
    ('Pony_Jet_Set', 'Jet Set'),
    ('Pony_Jigging_Clownspony', 'Jigging Clownspony'),
    ('Pony_Joe', 'Joe'),
    ('Pony_Jokester_Clownspony', 'Jokester Clownspony'),
    ('Pony_Junebug', 'Junebug'),
    ('Pony_Junior_Deputy', 'Junior Deputy'),
    ('Pony_King_Sombra', 'King Sombra'),
    ('Pony_Lassoing_Clownspony', 'Lassoing Clownspony'),
    ('Pony_Lemon_Hearts', 'Lemon Hearts'),
    ('Pony_Lemony_Gem', 'Lemony Gem'),
    ('Pony_Li_I_Griffon', 'Li\'l Griffon'),
    ('Pony_Lightning_Dust', 'Lightning Dust'),
    ('Pony_Lily_Valley', 'Lily Valley'),
    ('Pony_Limestone_Pie', 'Limestone Pie'),
    ('Pony_Lotus_Blossom', 'Lotus Blossom'),
    ('Pony_Lovestruck', 'Lovestruck'),
    ('Pony_Lucky_Clover', 'Lucky Clover'),
    ('Pony_Lucky_Dreams', 'Lucky Dreams'),
    ('Pony_Luna_Guard', 'Luna Guard'),
    ('Pony_Lyra', 'Lyra'),
    ('Pony_Lyrica', 'Lyrica'),
    ('Pony_Magnum', 'Hondo Flanks (Magnum)'),
    ('Pony_Mane_iac', 'Mane-iac'),
    ('Pony_Manehattan_Delegate', 'Manehattan Delegate'),
    ('Pony_Marble_Pie', 'Marble Pie'),
    ('Pony_Maud_Pie', 'Maud Pie'),
    ('Pony_Mayor', 'Mayor'),
    ('Pony_Minuette', 'Minuette'),
    ('Pony_Moondancer', 'Moondancer'),
    ('Pony_Mr_Breezy', 'Mr. Breezy'),
    ('Pony_Mr_Cake', 'Mr. Cake'),
    ('Pony_Mrs_Cake', 'Mrs. Cake'),
    ('Pony_MsHarshwhinny', 'Ms. Harshwhinny'),
    ('Pony_Musical_Clownspony', 'Musical Clownspony'),
    ('Pony_Neon_Lights', 'Neon Lights'),
    ('Pony_Nerdpony', 'Nerdpony'),
    ('Pony_Night_Glider', 'Night Glider'),
    ('Pony_Noteworthy', 'Noteworthy'),
    ('Pony_Nurse_Redheart', 'Nurse Redheart'),
    ('Pony_Octavia', 'Octavia'),
    ('Pony_Open_Skies', 'Open Skies'),
    ('Pony_Parish', 'Parish'),
    ('Pony_Party_Favor', 'Party Favor'),
    ('Pony_Peachy_Pie', 'Peachy Pie'),
    ('Pony_Peachy_Sweet', 'Peachy Sweet'),
    ('Pony_Pearl', 'Cookie Crumbles (Betty Bouffant)'),
    ('Pony_Perfect_Pace', 'Perfect Pace'),
    ('Pony_Pest_Control_Pony', 'Pest Control Pony'),
    ('Pony_Photofinish', 'Photo Finish'),
    ('Pony_Pinkie_Pie', 'Pinkie Pie'),
    ('Pony_Pinkiepies_Dad', 'Igneous Rock'),
    ('Pony_Pinkiepies_Mom', 'Cloudy Quartz'),
    ('Pony_Pipsqueak', 'Pipsqueak'),
    ('Pony_Posh_Unicorn', 'Posh Unicorn'),
    ('Pony_Prim_Hemline', 'Prim Hemline'),
    ('Pony_Prince_Blueblood', 'Prince Blueblood'),
    ('Pony_Princess_Cadence', 'Princess Cadence'),
    ('Pony_Princess_Celestia', 'Princess Celestia'),
    ('Pony_Princess_Luna', 'Princess Luna'),
    ('Pony_Professor', 'Bill Neigh (Professor)'),
    ('Pony_Purple_Wave', 'Purple Wave'),
    ('Pony_Quake', 'Quake'),
    ('Pony_Rainbow_Dash', 'Rainbow Dash'),
    ('Pony_Randolph', 'Randolph the Butler'),
    ('Pony_Rarity', 'Rarity'),
    ('Pony_Red_Delicious', 'Red Delicious'),
    ('Pony_Red_Gala', 'Red Gala'),
    ('Pony_Renfairpony', 'Richard (the) Hoovenheart'),
    ('Pony_Royal_Guard', 'Royal Guard'),
    ('Pony_Royal_Pin', 'Royal Pin'),
    ('Pony_Royal_Ribbon', 'Royal Ribbon'),
    ('Pony_Rumble', 'Rumble'),
    ('Pony_Sapphire_Shores', 'Sapphire Shores'),
    ('Pony_Sassy_Saddles', 'Sassy Saddles'),
    ('Pony_Savoir_Fare', 'Savoir Fare'),
    ('Pony_Scootaloo', 'Scootaloo'),
    ('Pony_Senior_Deputy', 'Senior Deputy'),
    ('Pony_Shadow_Surprise', 'The Shadowbolts'),
    ('Pony_Sheriff_Silverstar', 'Sheriff Silverstar'),
    ('Pony_Shining_Armour', 'Shining Armour'),
    ('Pony_Shooting_Star', 'Shooting Star'),
    ('Pony_Silver_Shill', 'Silver Shill'),
    ('Pony_Silver_Spoon', 'Silver Spoon'),
    ('Pony_Snails', 'Snails'),
    ('Pony_Snips', 'Snips'),
    ('Pony_Soarin', 'Soarin'),
    ('Pony_Spitfire', 'Spitfire'),
    ('Pony_Sprinkle_Stripe', 'Sprinkle Stripe'),
    ('Pony_Starlight_Glimmer', 'Starlight Glimmer'),
    ('Pony_Studious_Delegate', 'Studious Delegate'),
    ('Pony_Sugar_Belle', 'Sugar Belle'),
    ('Pony_Sunny_Daze', 'Sunny Daze'),
    ('Pony_Sunsetshimmer', 'Sunset Shimmer'),
    ('Pony_Sunshower', 'Sunshower'),
    ('Pony_Suri_Polomare', 'Suri Polomare'),
    ('Pony_Swan_Song', 'Swan Song'),
    ('Pony_Sweetiebelle', 'Sweetie Belle'),
    ('Pony_Thunderlane', 'Thunderlane'),
    ('Pony_Toe_Tapper', 'Toe Tapper'),
    ('Pony_Torch_Song', 'Torch Song'),
    ('Pony_Traveling_Gentlecolt', 'Traveling Gentlecolt'),
    ('Pony_Traveling_Mare', 'Traveling Mare'),
    ('Pony_Traveling_Pony', 'Traveling Pony'),
    ('Pony_Tree_Hugger', 'Tree Hugger'),
    ('Pony_Trenderhoof', 'Trenderhoof'),
    ('Pony_Trixie', 'Trixie'),
    ('Pony_Trouble_Shoes', 'Trouble Shoes'),
    ('Pony_Truffle', "Teacher's Pet"),
    ('Pony_Twilight_Sparkle', 'Twilight Sparkle'),
    ('Pony_Twilight_Velvet', 'Twilight Velvet'),
    ('Pony_Twilights_Dad', "Night Light (Twilight's Dad)"),
    ('Pony_Twinkleshine', 'Twinkleshine'),
    ('Pony_Twist', 'Twist'),
    ('Pony_Uncle_Orange', 'Uncle Orange'),
    ('Pony_Unicorn_Guard', 'Unicorn Guard'),
    ('Pony_Unicorn_Painter', 'Unicorn Painter'),
    ('Pony_Uppercrust', 'Upper Crust'),
    ('Pony_Walter', 'Walter (Bowling Pony)'),
    ('Pony_Wensley', 'Wensley'),
    ('Pony_Whinnyapolis_Delegate', 'Whinnyapolis Delegate'),
    ('Pony_Wild_Fire', 'Wild Fire'),
    ('Pony_Zecora', 'Zecora'),
    ('Pony_Zipporwhill', 'Zipporwhill')
])
