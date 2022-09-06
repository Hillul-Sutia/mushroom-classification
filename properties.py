# option list for all for properties of mushroom
m_classl = {"Edible":'e', "poisonous":'p'}
cap_shapel = {"bell":"b","conical":"c","convex":"x","flat":"f", "knobbed":"k","sunken":"s"}
cap_surfacel = {"fibrous":"f","grooves":"g","scaly":"y","smooth":"s"}
cap_colorl = {"brown":"n","buff":"b","cinnamon":"c","gray":"g","green":"r","pink":"p","purple":"u","red":"e","white":"w","yellow":"y"}
bruisesl = {"False":'f', "True":'t'}
odorl = {"almond":"a","anise":"l","creosote":"c","fishy":"y","foul":"f","musty":"m","none":"n","pungent":"p","spicy":"s"}
gill_attachmentl = {"attached":"a","descending":"d","free":"f","notched":"n"}
gill_spacingl = {"close":"c","crowded":"w","distant":"d"}
gill_sizel = {"broad":"b","narrow":"n"}
gill_colorl = {"black":"k","brown":"n","buff":"b","chocolate":"h","gray":"g", "green":"r","orange":"o","pink":"p","purple":"u","red":"e","white":"w","yellow":"y"}
stalk_shapel = {"enlarging":"e","tapering":"t"}
stalk_rootl = {"bulbous":"b","club":"c","cup":"u","equal":"e","rhizomorphs":"z","rooted":"r","missing":"?"}
stalk_surface_above_ringl = {"fibrous":"f","scaly":"y","silky":"k","smooth":"s"}
stalk_surface_below_ringl = {"fibrous":"f","scaly":"y","silky":"k","smooth":"s"}
stalk_color_above_ringl = {"brown":"n","buff":"b","cinnamon":"c","gray":"g","orange":"o","pink":"p","red":"e","white":"w","yellow":"y"}
stalk_color_below_ringl = {"brown":"n","buff":"b","cinnamon":"c","gray":"g","orange":"o","pink":"p","red":"e","white":"w","yellow":"y"}
veil_colorl = {"brown":"n","orange":"o","white":"w","yellow":"y"}
ring_numberl = {"none":"n","one":"o","two":"t"}
ring_typel = {"cobwebby":"c","evanescent":"e","flaring":"f","large":"l","none":"n","pendant":"p","sheathing":"s","zone":"z"}
spore_print_colorl = {"black":"k","brown":"n","buff":"b","chocolate":"h","green":"r","orange":"o","purple":"u","white":"w","yellow":"y"}
populationl = {"abundant":"a","clustered":"c","numerous":"n","scattered":"s","several":"v","solitary":"y"}
habitatl = {"grasses":"g","leaves":"l","meadows":"m","paths":"p","urban":"u","waste":"w","woods":"d"}

#Values of features with their encodings
m_class = ['e', 'p']
cap_shape = ['b', 'c', 'f', 'k', 's', 'x']
cap_surface = ['f', 'g', 's', 'y']
cap_color = ['b', 'c', 'e', 'g', 'n', 'p', 'r', 'u', 'w', 'y']
bruises = ['f', 't']
odor = ['a', 'c', 'f', 'l', 'm', 'n', 'p', 's', 'y']
gill_attachment = ['a','d', 'f','n']
gill_spacing = ['c','d', 'w']
gill_size = ['b', 'n']
gill_color = ['b', 'e', 'g', 'h', 'k', 'n', 'o', 'p', 'r', 'u', 'w', 'y']
stalk_shape = ['e', 't']
stalk_root = ['?', 'b', 'c', 'e', 'r','u','z']
stalk_surface_above_ring = ['f', 'k', 's', 'y']
stalk_surface_below_ring = ['f', 'k', 's', 'y']
stalk_color_above_ring = ['b', 'c', 'e', 'g', 'n', 'o', 'p', 'w', 'y']
stalk_color_below_ring = ['b', 'c', 'e', 'g', 'n', 'o', 'p', 'w', 'y']
veil_color = ['n', 'o', 'w', 'y']
ring_number = ['n', 'o', 't']
ring_type = ['c','e', 'f', 'l', 'n', 'p','s','z']
spore_print_color = ['b', 'h', 'k', 'n', 'o', 'r', 'u', 'w', 'y']
population = ['a', 'c', 'n', 's', 'v', 'y']
habitat = ['d', 'g', 'l', 'm', 'p', 'u', 'w']


# list of features
features = [
    'cap-shape', 'cap-surface',
    'cap-color', 'bruises', 'odor',
    'gill-attachment', 'gill-spacing',
    'gill-size', 'gill-color', 'stalk-shape',
    'stalk-root', 'stalk-surface-above-ring',
    'stalk-surface-below-ring', 'stalk-color-above-ring',
    'stalk-color-below-ring', 'veil-color', 'ring-number',
    'ring-type', 'spore-print-color', 'population', 'habitat'
]