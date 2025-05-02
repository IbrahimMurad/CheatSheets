# Available Fonts

## Usage Example

```typescript
import { ABeeZee } from "next/font/google";

const abeeZee = ABeeZee({
  weight: "400",
  style: "normal",
  subsets: ["latin"],
});

// Use in your component
function MyComponent() {
  return (
    <div className={abeeZee.className}>This text will use the ABeeZee font</div>
  );
}
```

## Font Options

Most fonts support the following options:

- `weight`: Font weight (varies by font)
- `style`: Font style (normal, italic)
- `subsets`: Character subsets to load
- `display`: Font display strategy
- `variable`: CSS variable name for variable fonts
- `preload`: Whether to preload the font
- `fallback`: Fallback font stack
- `adjustFontFallback`: Whether to adjust the fallback font

Check individual font declarations for specific supported options.

## Available Fonts

- ABeeZee - ADLaM_Display - AR_One_Sans - Abel - Abhaya_Libre - Abril_Fatface - Aclonica - Acme - Actor - Adamina - Advent_Pro - Aguafina_Script Akaya_Kanadaka - Akaya_Telivigala - Akronim - Aladin - Alata - Alatsi - Aldrich - Alef - Alegreya - Alegreya_SC - Alegreya_Sans Alegreya_Sans_SC - Aleo - Alex_Brush - Alfa_Slab_One - Alice - Alike - Alike_Angular - Allan - Allerta - Allerta_Stencil - Allura - Almarai - Almendra Almendra_Display - Almendra_SC - Amarante - Amaranth - Amatic_SC - Amethysta - Amiko - Amiri - Amita - Anaheim - Andada - Andika Angkor - Annie_Use_Your_Telescope - Anonymous_Pro - Antic - Antic_Didone - Antic_Slab - Anton - Arapey - Arbutus - Arbutus_Slab - Architects_Daughter Archivo - Archivo_Black - Archivo_Narrow - Arima_Madurai - Arimo - Arizonia - Armata - Arsenal - Artifika - Arvo - Arya - Asap - Asap_Condensed - Asar - Asset - Assistant - Astloch - Asul - Athiti - Atma - Atomic_Age - Aubrey - Audiowide - Autour_One Average - Average_Sans - Averia_Gruesa_Libre - Averia_Libre - Averia_Sans_Libre - Averia_Serif_Libre
- B612 - B612_Mono - Bad_Script - Bahiana - Bahianita - Bai_Jamjuree - Baloo - Baloo_Bhai - Baloo_Bhaina - Baloo_Chettan - Baloo_Da - Baloo_Paaji - Baloo_Tamma - Baloo_Tammudu - Baloo_Thambi - Balsamiq_Sans
- Balthazar - Bangers - Barlow - Barlow_Condensed - Barlow_Semi_Condensed - Barriecito - Barrio - Basic - Baskervville - Baumans - Bayon - Be_Vietnam - Bebas_Neue - Belgrano - Bellefair - Belleza - BenchNine - Bentham - Berkshire_Swash - Beth_Ellen - Bevan - Big_Shoulders_Display - Big_Shoulders_Text - Bigelow_Rules - Bigshot_One - Bilbo - Bilbo_Swash_Caps - BioRhyme - BioRhyme_Expanded - Biryani - Bitter - Black_And_White_Picture - Black_Han_Sans - Black_Han_Serif - Blacker_One - Bokor - Bonbon - Boogaloo - Bowlby_One - Bowlby_One_SC - Brawler - Bree_Serif - Bubblegum_Sans - Bubbler_One - Buda - Buenard - Bungee - Bungee_Hairline - Bungee_Inline - Bungee_Outline - Bungee_Shade - Butcherman - Butterfly_Kids
- Cabin - Cabin_Condensed - Cabin_Sketch - Caesar_Dressing - Cagliostro - Cairo - Calligraffitti - Cambay - Cambo - Candal - Cantarell - Cantata_One - Cantora_One - Capriola - Cardo - Carme - Carrois_Gothic - Carrois_Gothic_SC - Carter_One - Catamaran - Caudex - Caveat - Caveat_Brush - Cedarville_Cursive - Ceviche_One - Chakra_Petch - Changa - Changa_One - Chango - Charm - Charmonman - Chathura - Chau_Philomene_One - Chela_One - Chelsea_Market - Chenla - Cherry_Cream_Soda - Cherry_Swash - Chewy - Chicle - Chilanka - Chivo - Chonburi - Cinzel - Cinzel_Decorative - Clicker_Script - Coda - Coda_Caption - Codystar - Coiny - Combo - Comfortaa - Comic_Neue - Coming_Soon - Commissioner - Concert_One - Condiment - Content - Contrail_One - Convergence - Cookie - Copse - Corben - Cormorant - Cormorant_Garamond
- Cormorant_Infant - Cormorant_SC - Cormorant_Unicase - Cormorant_Upright - Courgette - Cousine - Coustard - Covered_By_Your_Grace - Crafty_G - Creepster - Crete_Round - Crimson_Pro_Text - Crimson_Text - Croissant_One - Crushed - Cuprum - Cute_Font - Cutive - Cutive_Mono
- DM_Mono - DM_Sans - DM_Serif_Display - Damion - Dancing_Script - Dangrek - Darker_Grotesque - David_Libre - Dawning_of_a_New_Day - Days_One - Dekko - Delius - Delius_Swash_Caps - Delius_Unicase - Della_Respira - Denk_One - Devonshire - Dhurjati - Didact_Gothic - Diplomata - Diplomata_SC - Do_Hyeon - Dokdo - Domine - Donegal_One - Doppio_One - Dorsa - Dosis - Dr_Sugiyama - Duru_Sans - Dynalight
- EB_Garamond - Eagle_Lake - East_Sea_Dokdo - Eater - Economica - Eczar - El_Messiri - Electrolize - Elsie - Elsie_Swash_Caps - Emblema_One - Emilys_Candy - Encode_Sans - Encode_Sans_Condensed - Encode_Sans_Expanded - Encode_Sans_Semi_Condensed - Encode_Sans_Semi_Expanded - Engagement - Englebert - Enriqueta - Erica_One - Esteban - Euphoria_Script - Ewert - Exo - Exo_2 - Expletus_Sans
- Fahkwang - Fanwood_Text - Farro - Fascinate - Fascinate_Inline - Faster_One - Fasthand - Fauna_One - Faustina - Federant - Federo - Felipa - Fenix - Finger_Paint - Fira_Code - Fira_Mono - Fira_Sans - Fira_Sans_Condensed - Fira_Sans_Extra_Condensed - Fjalla_One - Fjord_One - Flamenco - Flavors - Fondamento - Fontdiner_Swanky - Forum - Francois_One - Frank_Ruhl_Libre - Fraunces - Freckle_Face - Fredericka_the_Great - Fredoka_One - Freehand - Fresca - Frijole - Fruktur - Fugaz_One - GFS_Didot
- GFS_Neohellenic - Gabriela - Gaegu - Gafata - Galada - Galdeano - Galindo - Gamja_Flower - Gayathri - Gelasio - Gentium_Basic - Gentium_Book_Basic
- Geo - Geostar - Geostar_Fill - Germania_One - Gidugu - Gilda_Display - Girassol - Give_You_Glory - Glass_Antiqua - Glegoo - Gloria_Hallelujah - Goblin_One
- Gochi_Hand - Gorditas - Gothic_A1 - Gotu - Goudy_Bookletter_1911 - Graduate - Grand_Hotel - Gravitas_One - Great_Vibes - Grenze - Griffy - Gruppo
- Gudea - Gugi - Gupter - Gurajada - Habibi - Hachi_Maru_Pop - Halant - Hammersmith_One - Hanalei - Hanalei_Fill - Handlee - Hanuman
- Happy_Monkey - Harmattan - Headland_One - Heebo - Henny_Penny - Hepta_Slab - Herr_Von_Muellerhoff - Hi_Melody - Hind - Hind_Guntur - Hind_Madurai - Hind_Siliguri
- Hind_Vadodara - Holtwood_One_SC - Homemade_Apple - Homenaje - IBM_Plex_Mono - IBM_Plex_Sans - IBM_Plex_Sans_Condensed - IBM_Plex_Serif - IM_Fell_Double_Pica - IM_Fell_Double_Pica_SC - IM_Fell_English
- IM_Fell_English_SC - IM_Fell_French_Canon - IM_Fell_French_Canon_SC - IM_Fell_Great_Primer - IM_Fell_Great_Primer_SC - Ibrik - Iceberg - Iceland - Imprima - Inconsolata - Inder
- Indie_Flower - Inika - Inknut_Antiqua - Irish_Grover - Istok_Web - Italiana - Italianno - Itim - Jacques_Francois - Jacques_Francois_Shadow - Jaldi - Jim_Nightshade
- Jockey_One - Jolly_Lodger - Jomhuria - Jomolhari - Josefin_Sans - Josefin_Slab - Jost - Joti_One - Jua - Judson - Julee
- Julius_Sans_One - Junge - Jura - Just_Another_Hand - Just_Me_Again_Down_Here - K2D - Kadwa - Kalam - Kameron - Kanit - Kantumruy - Karla
- Karma - Katibeh - Kaushan_Script - Kavivanar - Kavoon - Kdam_Thmor - Keania_One - Kelly_Slab - Kenia - Khand - Khmer - Khula
- Kirang_Haerang - Kite_One - Knewave - KoHo - Kodchasan - Kosugi - Kosugi_Maru - Kotta_One - Koulen - Kranky - Kreon - Kristi
- Krona_One - Krub - Kulim_Park - Kumar_One - Kumar_One_Outline - Kurale - La_Belle_Aurore - Laila - Lakki_Reddy - Lalezar - Lancelot - Langar
- Lateef - Lato - League_Script - Leckerli_One - Ledger - Lekton - Lemon - Lemonada - Lexend - Lexend_Deca - Lexend_Exa - Lexend_Giga
- Lexend_Mega - Lexend_Peta - Lexend_Tera - Lexend_Zetta - Libre_Baskerville - Libre_Caslon_Display - Libre_Caslon_Text - Libre_Franklin - Life_Savers - Lilita_One - Lily_Pond_Scenario
- Limelight - Linden_Hill - Literata - Liu_Jian_Mao_Cao - Livvic - Lobster - Lobster_Two - Londrina_Outline - Londrina_Shadow - Londrina_Solid - Long_Cang - Lora
- Love_Ya_Like_A_Sister - Loved_by_the_King - Lovers_Quarrel - Luckiest_Guy - Lusitana - Lustria - M_PLUS_1p - M_PLUS_Rounded_1c - Ma_Shan_Zheng - Macondo - Macondo_Swash_Caps
- Mada - Magra - Maiden_Orange - Maitree - Major_Mono_Display - Mako - Mali - Mall
- Mandali - Marcellus - Marcellus_SC - Marck_Script - Margarine - Markazi_Text - Marko_One - Marmelad - Martel - Martel_Sans - Marvel - Mate
- Mate_SC - Maven_Pro - McLaren - Meddon - MedievalSharp - Medula_One - Meera_Inimai - Megrim - Meie_Script - Merienda - Merienda_One - Merriweather
- Merriweather_Sans - Metal - Metal_Mania - Metamorphous - Metrophobic - Michroma - Milonga - Miltonian - Miltonian_Tattoo - Mina - Miniver - Miriam_Libre
- Mirza - Miss_Fajardose - Mitr - Modak - Modern_Antiqua - Mogra - Molengo - Molle - Monda - Monofett - Monoton - Monsieur_La_Doulaise
- Montaga - Montez - Montserrat - Montserrat_Alternates - Montserrat_Subrayada - Moul - Moulpali - Mountains_of_Christmas - Mouse_Memoirs - Mr_Bedfort - Mr_Dafoe - Mr_De_Haviland
- Mrs_Saint_Delafield - Mrs_Sheppards - Mukta - Mukta_Mahee - Mukta_Malar - Mukta_Vaani - Mulish - Muli - Mystery_Quest - NTR - Nanum_Brush_Script - Nanum_Gothic
- Nanum_Gothic_Coding - Nanum_Myungjo - Nanum_Pen_Script - Nerko_One - Neucha - Neuton - New_Rocker - News_Cycle - Niconne - Niramit - Nixie_One - Nobile - Nokora
- Norican - Nosifer - Notable - Nothing_You_Could_Do - Noticia_Text - Noto_Sans - Noto_Sans_Display - Noto_Sans_JP - Noto_Sans_KR - Noto_Sans_SC - Noto_Sans_TC
- Noto_Serif - Noto_Serif_JP - Noto_Serif_KR - Noto_Serif_SC - Noto_Serif_TC - Nova_Cut - Nova_Flat - Nova_Mono - Nova_Oval - Nova_Round - Nova_Slim
- Nova_Square - Numans - Nunito - Nunito_Sans - Odibee_Sans - Odor_Mean_Chey - Offside - Old_Standard_TT - Oldenburg - Oleo_Script - Oleo_Script_Swash_Caps - Open_Sans
- Open_Sans_Condensed - Oranienbaum - Orbitron - Oregano - Orienta - Original_Surfer - Oswald - Over_the_Rainbow - Overlock - Overlock_SC - Overpass - Overpass_Mono
- Ovo - Oxygen - Oxygen_Mono - PT_Mono - PT_Sans - PT_Sans_Caption - PT_Sans_Narrow - PT_Serif - PT_Serif_Caption - Pacifico - Padauk - Palanquin
- Palanquin_Dark - Pangolin - Paprika - Parisienne - Passero_One - Passion_One - Pathway_Gothic_One - Patrick_Hand - Patrick_Hand_SC - Pattaya - Patua_One - Pavanam
- Paytone_One - Peddana - Peralta - Permanent_Marker - Petit_Formal_Script - Petrona - Philosopher - Piazzolla - Piedra - Pinyon_Script - Pirata_One - Plaster
- Play - Playball - Playfair_Display - Playfair_Display_SC - Podkova - Poiret_One - Poller_One - Poly - Pompiere - Pontano_Sans - Poor_Story - Poppins
- Port_Lligat_Sans - Port_Lligat_Slab - Pragati_Narrow - Prata - Preahvihear - Press_Start_2P - Pridi - Princess_Sofia - Prociono - Prompt - Prosto_One - Proza_Libre
- Public_Sans - Puritan - Purple_Purse - Quando - Quantico - Quattrocento - Quattrocento_Sans - Questrial - Quicksand - Quintessential - Qwigley - Racing_Sans_One
- Radley - Raghu_Malayalam - Raghu_Tamil - Rajdhani - Rakkas - Raleway - Raleway_Dots - Ramabhadra - Ramaraja - Rambla - Rammetto_One - Ranchers
- Rancho - Ranga - Rasa - Rationale - Ravi_Prakash - Recursive - Red_Hat_Display - Red_Hat_Text - Red_Rose - Redressed - Reem_Kufi - Reenie_Beanie
- Revalia - Rhodium_Libre - Ribeye - Ribeye_Marrow - Righteous - Risque - Roboto - Roboto_Condensed - Roboto_Mono - Roboto_Slab - Rochester - Rock_Salt
- RocknRoll_One - Rokkitt - Romanesco - Ropa_Sans - Rosario - Rosarivo - Rouge_Script - Rowdies - Rozha_One - Rubik - Rubik_Mono_One - Ruda
- Rufina - Ruge_Boogie - Ruluko - Rum_Raisin - Ruslan_Display - Russo_One - Ruthie - Rye - Sacramento - Sahitya - Sail - Saira
- Saira_Condensed - Saira_Extra_Condensed - Saira_Semi_Condensed - Saira_Stencil_One - Salsa - Sanchez - Sancreek - Sansita - Sarabun - Sarala - Sarina - Sarpanch
- Satisfy - Sawarabi_Gothic - Sawarabi_Mincho - Scada - Scheherazade - Schoolbell - Scope_One - Seaweed_Script - Secular_One - Sedgwick_Ave - Sedgwick_Ave_Display - Sen
- Sevillana - Seymour_One - Shadows_Into_Light - Shadows_Into_Light_Two - Shanti - Share - Share_Tech - Share_Tech_Mono - Shojumaru - Short_Paragraph - Shrikhand - Siemreap
- Sigmar_One - Signika - Signika_Negative - Simonetta - Single_Day - Sintony - Sirin_Stencil - Six_Caps - Skranji - Slabo_13px - Slabo_27px - Slackey
- Smokum - Smythe - Sniglet - Snippet - Snowburst_One - Sofadi_One - Sofia - Solway - Song_Myung - Sonsie_One - Sorts_Mill_Goudy - Source_Code_Pro
- Source_Sans_Pro - Source_Serif_Pro - Space_Grotesk - Space_Mono - Spartan - Special_Elite - Spectral - Spectral_SC - Spicy_Rice - Spinnaker - Spirax - Squada_One
- Sree_Krushnadevaraya - Sriracha - Srisakdi - Staatliches - Stalemate - Stalinist_One - Stardos_Stencil - Stick_No_Bills - Stint_Ultra_Condensed - Stint_Ultra_Expanded - Stoke
- Strait - Stylish - Sue_Ellen_Francisco - Suez_One - Sulphur_Point - Sumana - Sunflower - Sunshiney - Supermercado_One - Sura - Suranna - Suravaram
- Suwannaphum - Swanky_and_Moo_Moo - Syncopate - Tajawal - Tangerine - Taprom - Tauri - Taviraj - Teko - Telex - Tenali_Ramakrishna - Tenor_Sans
- Text_Me_One
- Texturina
- Thasadith - The_Girl_Next_Door - Tienne - Tillana - Timmana - Tinos - Titan_One - Titillium_Web - Tomorrow - Trade_Winds - Trirong - Trispace
- Trocchi - Trochut - Trykker - Tulpen_One - Turret_Road - Ubuntu - Ubuntu_Condensed - Ubuntu_Mono - Ultra - Uncial_Antiqua - Underdog - Unica_One
- UnifrakturCook - UnifrakturMaguntia - Unkempt - Unlock - Unna - VT323 - Vampiro_One - Varela - Varela_Round - Varta - Vast_Shadow - Vesper_Libre
- Viaoda_Libre - Vibes - Vibur - Vidaloka - Viga - Voces - Volkhov - Vollkorn - Vollkorn_SC - Voltaire - Waiting_for_the_Sunrise - Wallpoet
- Walter_Turncoat - Warnes - Wellfleet - Wendy_One - Wire_One - Work_Sans - Xanh_Mono - Yanone_Kaffeesatz - Yantramanav - Yatra_One - Yellowtail
- Yeon_Sung - Yeseva_One - Yesteryear - Yrsa - ZCOOL_KuaiLe - ZCOOL_QingKe_HuangYou - ZCOOL_XiaoWei - Zeyada - Zhi_Mang_Xing - Zilla_Slab
- Zilla_Slab_Highlight
