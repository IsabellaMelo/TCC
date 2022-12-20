IDHM_MUNICIPALITIES = ['group1', 'group6', 'group11', 'group16', 'group21', 'group26', 'group2', 'group7', 'group12', 'group17', 'group22', 'group27','group3', 'group8', 'group13', 'group18', 'group23', 'group28','group4', 'group9', 'group14', 'group19', 'group24', 'group29', 'group5', 'group10', 'group15', 'group20', 'group25', 'group30']


# _SURVEY_NAMES_IDHM = {
#   'train': ['REGISTRO','RIO BRANCO DO SUL', 'IGUAPE','APIAI','JUQUITIBA', 'ITARIRI','MIRACATU',
#             'CERRO AZUL', 'CAJATI','JUQUIA','ITAPERUCU', 'DOUTOR ULYSSES'],
#   'val': ['ADRIANOPOLIS', 'IPORANGA', 'PEDRO DE TOLEDO', 'TAPIRAI', 'BARRA DO TURVO', 'TUNAS DO PARANA',
#            'BARRA DO CHAPEU', 'ITAPIRAPUA PAULISTA', 'ITAOCA', 'RIBEIRA'],
#   'test': ['ELDORADO', 'PARIQUERA-ACU', 'SAO LOURENCO DA SERRA', 'ILHA COMPRIDA', 'SETE BARRAS', 'JACUPIRANGA', 
#           'BOCAIUVA DO SUL', 'CANANEIA']        
# }


# A ['group1_2010', 'group6_2010', 'group11_2010', 'group16_2010', 'group21_2010', 'group26_2010'] - 1944
# B ['group2_2010', 'group7_2010', 'group12_2010', 'group17_2010', 'group22_2010', 'group27_2010'] - 1944
# C ['group3_2010', 'group8_2010', 'group13_2010', 'group18_2010', 'group23_2010', 'group28_2010'] - 1944
# D ['group4_2010', 'group9_2010', 'group14_2010', 'group19_2010', 'group24_2010', 'group29_2010'] - 1944
# E ['group5_2010', 'group10_2010', 'group15_2010', 'group20_2010', 'group25_2010', 'group30_2010'] - 1972


#train:C, D, E - 5860
#val:B - 1944
#test:A - 1944

_SURVEY_NAMES_IDHM_OOC_A = {
  'train':  ['group3_2010', 'group8_2010', 'group13_2010', 'group18_2010', 'group23_2010', 'group28_2010','group4_2010', 'group9_2010', 'group14_2010', 'group19_2010', 'group24_2010', 'group29_2010', 'group5_2010', 'group10_2010', 'group15_2010', 'group20_2010', 'group25_2010', 'group30_2010'],
  'val': ['group2_2010', 'group7_2010', 'group12_2010', 'group17_2010', 'group22_2010', 'group27_2010'],
  'test': ['group1_2010', 'group6_2010', 'group11_2010', 'group16_2010', 'group21_2010', 'group26_2010']
}

#A, D, E - 5860
#C - 1944
#B - 1944

_SURVEY_NAMES_IDHM_OOC_B = {
  'train':  ['group1_2010', 'group6_2010', 'group11_2010', 'group16_2010', 'group21_2010', 'group26_2010', 'group4_2010', 'group9_2010', 'group14_2010', 'group19_2010', 'group24_2010', 'group29_2010', 'group5_2010', 'group10_2010', 'group15_2010', 'group20_2010', 'group25_2010', 'group30_2010'],
  'val': ['group3_2010', 'group8_2010', 'group13_2010', 'group18_2010', 'group23_2010', 'group28_2010'],
  'test': ['group2_2010', 'group7_2010', 'group12_2010', 'group17_2010', 'group22_2010', 'group27_2010']
}

#A, B, E - 5860
#D - 1944
#C - 1944


_SURVEY_NAMES_IDHM_OOC_C = {
  'train':  ['group1_2010', 'group6_2010', 'group11_2010', 'group16_2010', 'group21_2010', 'group26_2010','group2_2010', 'group7_2010', 'group12_2010', 'group17_2010', 'group22_2010', 'group27_2010', 'group5_2010', 'group10_2010', 'group15_2010', 'group20_2010', 'group25_2010', 'group30_2010' ],
  'val': ['group4_2010', 'group9_2010', 'group14_2010', 'group19_2010', 'group24_2010', 'group29_2010'],
  'test': ['group3_2010', 'group8_2010', 'group13_2010', 'group18_2010', 'group23_2010', 'group28_2010']
}


#A, B, C - 5832
#E - 1972
#D - 1944


_SURVEY_NAMES_IDHM_OOC_D = {
  'train':  ['group1_2010', 'group6_2010', 'group11_2010', 'group16_2010', 'group21_2010', 'group26_2010', 'group2_2010', 'group7_2010', 'group12_2010', 'group17_2010', 'group22_2010', 'group27_2010', 'group3_2010', 'group8_2010', 'group13_2010', 'group18_2010', 'group23_2010', 'group28_2010'],
  'val': ['group5_2010', 'group10_2010', 'group15_2010', 'group20_2010', 'group25_2010', 'group30_2010'],
  'test': ['group4_2010', 'group9_2010', 'group14_2010', 'group19_2010', 'group24_2010', 'group29_2010']
}


#B, C, D - 5832
#A - 1944
#E - 1972


_SURVEY_NAMES_IDHM_OOC_E = {
  'train':  ['group2_2010', 'group7_2010', 'group12_2010', 'group17_2010', 'group22_2010', 'group27_2010', 'group3_2010', 'group8_2010', 'group13_2010', 'group18_2010', 'group23_2010', 'group28_2010', 'group4_2010', 'group9_2010', 'group14_2010', 'group19_2010', 'group24_2010', 'group29_2010'],
  'val': ['group1_2010', 'group6_2010', 'group11_2010', 'group16_2010', 'group21_2010', 'group26_2010'],
  'test': ['group5_2010', 'group10_2010', 'group15_2010', 'group20_2010', 'group25_2010', 'group30_2010']
}

########## PROPORTION ###########
# train: 60%
# val: 20% 
# test: 20%
#################################

TOTAL_SIZE = 9748

#B, C, D - 5832
#A - 1944
#E - 1972

SIZES = {
    #'IDHM':{'train': 544, 'val': 133, 'test': 203, 'all': 880},
    'IDHM_OOC_A':{'train': 5860, 'val': 1944, 'test': 1944, 'all': 9748},
    'IDHM_OOC_B':{'train': 5860, 'val': 1944, 'test': 1944, 'all': 9748},
    'IDHM_OOC_C':{'train': 5860, 'val': 1944, 'test': 1944, 'all': 9748},
    'IDHM_OOC_D':{'train': 5832, 'val': 1972, 'test': 1944, 'all': 9748},
    'IDHM_OOC_E':{'train': 5832, 'val': 1944, 'test': 1972, 'all': 9748},
}

# means and standard deviations calculated over the entire dataset (train + val + test),
# with negative values set to 0, and ignoring any pixel that is 0 across all bands

_MEANS_IDHM = {
 'BLUE': 0.03881422822285812,
 'DMSP': 7.254336855539441,
 'GREEN': 0.06383289865527494,
 'NIR': 0.26814197654255334,
 'RED': 0.06558464949683206,
 'SWIR1': 0.19413160058809623,
 'SWIR2': 0.10481595546673592,
 'TEMP1': 294.6163774331654,
 'VIIRS': 0.0}

_STD_DEVS_IDHM = {
 'BLUE': 0.011899925054510829,
 'DMSP': 28.398516118991267,
 'GREEN': 0.01873605479881772,
 'NIR': 0.052359457445103896,
 'RED': 0.027800201975011242,
 'SWIR1': 0.06201829995803823,
 'SWIR2': 0.04676775561198121,
 'TEMP1': 2.2825123328058714,
 'VIIRS': 0.0}

 
MEANS_DICT = {
    'IDHM': _MEANS_IDHM,
}

STD_DEVS_DICT = {
    'IDHM': _STD_DEVS_IDHM,
}

###################



SURVEY_NAMES = {
    #'IDHM': _SURVEY_NAMES_IDHM,
    'IDHM_OOC_A': _SURVEY_NAMES_IDHM_OOC_A,
    'IDHM_OOC_B': _SURVEY_NAMES_IDHM_OOC_B,
    'IDHM_OOC_C': _SURVEY_NAMES_IDHM_OOC_C,
    'IDHM_OOC_D': _SURVEY_NAMES_IDHM_OOC_D,
    'IDHM_OOC_E': _SURVEY_NAMES_IDHM_OOC_E,
}