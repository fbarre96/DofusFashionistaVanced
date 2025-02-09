# Copyright (C) 2020 The Dofus Fashionista
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from copy import copy


CHARACTER_CLASSES = sorted(['Eniripsa', 'Iop', 'Xelor', 'Osamodas', 'Feca',
                     'Sacrier', 'Ecaflip', 'Enutrof', 'Sram', 'Sadida',
                     'Cra', 'Pandawa', 'Rogue', 'Masqueraider', 'Foggernaut',
                     'Eliotrope', 'Huppermage', 'Ouginak', 'Forgelance'])

TYPE_NAME_TO_SLOT = {
    'Weapon': 'weapon',
    'Shield': 'shield',
    'Hat': 'hat',
    'Cloak': 'cloak',
    'Amulet': 'amulet',
    'Ring': 'ring',
    'Belt': 'belt',
    'Boots': 'boots',
    'Dofus': 'dofus',
    'Pet': 'pet',
}

SLOT_NAME_TO_TYPE = {
    'weapon': 'Weapon',
    'shield': 'Shield',
    'hat': 'Hat',
    'cloak': 'Cloak',
    'amulet': 'Amulet',
    'ring1': 'Ring',
    'ring2': 'Ring',
    'belt': 'Belt',
    'boots': 'Boots',
    'dofus1': 'Dofus',
    'dofus2': 'Dofus',
    'dofus3': 'Dofus',
    'dofus4': 'Dofus',
    'dofus5': 'Dofus',
    'dofus6': 'Dofus',
    'pet': 'Pet',
}

TYPE_NAME_TO_SLOT_NUMBER = {
    'Weapon': 1,
    'Shield': 1,
    'Hat': 1,
    'Cloak': 1,
    'Amulet': 1,
    'Ring': 2,
    'Belt': 1,
    'Boots': 1,
    'Dofus': 6,
    'Pet': 1,
}

TYPE_NAMES = list(TYPE_NAME_TO_SLOT.keys())

SLOTS = []
for type_name in TYPE_NAMES:
    slot_number = TYPE_NAME_TO_SLOT_NUMBER[type_name]
    slot_name = TYPE_NAME_TO_SLOT[type_name]
    if slot_number > 1:
        for i in range(1, slot_number + 1):
            SLOTS.append("%s%d" % (slot_name, i))
    else:
        SLOTS.append(slot_name)
        
STAT_NAME_TO_KEY = {
    'Power': 'pow',
    'Damage': 'dam',
    'Heals': 'heals',
    'AP': 'ap',
    'MP': 'mp',
    'Critical Hits': 'ch',
    'Agility': 'agi',
    'Strength': 'str',
    'Neutral Damage': 'neutdam',
    'Earth Damage': 'earthdam',
    'Intelligence': 'int',
    'Fire Damage': 'firedam',
    'Air Damage': 'airdam',
    'Chance': 'cha',
    'Water Damage': 'waterdam',
    'Vitality': 'vit',
    'Initiative': 'init',
    'Summon': 'summon',
    'Range': 'range',
    'Wisdom': 'wis',
    'Neutral Resist': 'neutres',
    'Water Resist': 'waterres',
    'Air Resist': 'airres',
    'Fire Resist': 'fireres',
    'Earth Resist': 'earthres',
    '% Neutral Resist': 'neutresper',
    '% Air Resist': 'airresper',
    '% Fire Resist': 'fireresper',
    '% Water Resist': 'waterresper',
    '% Earth Resist': 'earthresper',
    'Neutral Resist in PVP': 'pvpneutres',
    'Water Resist in PVP': 'pvpwaterres',
    'Air Resist in PVP': 'pvpairres',
    'Fire Resist in PVP': 'pvpfireres',
    'Earth Resist in PVP': 'pvpearthres',
    '% Neutral Resist in PVP': 'pvpneutresper',
    '% Air Resist in PVP': 'pvpairresper',
    '% Fire Resist in PVP': 'pvpfireresper',
    '% Water Resist in PVP': 'pvpwaterresper',
    '% Earth Resist in PVP': 'pvpearthresper',
    'Prospecting': 'pp',
    'Pods': 'pod',
    'AP Reduction': 'apred',
    'MP Reduction': 'mpred',
    'Lock': 'lock',
    'Dodge': 'dodge',
    'Reflects': 'ref',
    'Pushback Damage': 'pshdam',
    'Trap Damage': 'trapdam',
    '% Trap Damage': 'trapdamper',
    'Critical Resist': 'crires',
    'Pushback Resist': 'pshres',
    'MP Loss Resist': 'mpres',
    'AP Loss Resist': 'apres',
    'Critical Damage': 'cridam',
    'Critical Failure': 'cf',
    '% Melee Damage': 'permedam',
    '% Ranged Damage': 'perrandam',
    '% Weapon Damage': 'perweadam',
    '% Spell Damage': 'perspedam',
    '% Melee Resist': 'respermee',
    '% Ranged Resist': 'resperran',
    'HP': 'hp',
    '% Weapon Resist': 'resperwea'
}

STAT_ORDER = {
    'hp': 0,
    'vit': 1,
    'str': 2,
    'int': 3,
    'cha': 4,
    'agi': 5,
    'wis': 6,
    'pow': 7,
    
    'ch': 11,
    'ap': 12,
    'mp': 13,
    'range': 14,
    'summon': 15,
    'init': 16,
    'pod': 17,
    'pp': 18,
    
    'dam': 21,
    'neutdam': 22,
    'earthdam': 23,
    'firedam': 24,
    'waterdam': 25,
    'airdam': 26,
    
    'heals': 31,
    
    'neutres': 71,
    'earthres': 72,
    'fireres': 73,
    'waterres': 74,
    'airres': 75,
    'crires': 76,
    'pshres': 77,
    'neutresper': 81,
    'earthresper': 82,
    'fireresper': 83,
    'waterresper': 84,
    'airresper': 85,
    
    'pvpneutres': 133,
    'pvpearthres': 134,
    'pvpfireres': 135,
    'pvpwaterres': 136,
    'pvpairres': 137,
    'pvpneutresper': 138,
    'pvpearthresper': 139,
    'pvpfireresper': 140,
    'pvpwaterresper': 141,
    'pvpairresper': 142,
    
    'lock': 91,
    'dodge': 92,
    'apred': 93,
    'mpred': 94,
    'apres': 95,
    'mpres': 96,
    
    'pshdam': 101,
    'cridam': 102,   
    'trapdam': 103,
    'trapdamper': 104, 
    'cf': 111,
    'ref': 112,
    
    'pvpcrires': 120,
    'pvppshres': 121,
    
    'permedam': 127,
    'perrandam': 128,
    'perweadam': 129,
    'perspedam': 130,
    'respermee': 131,
    'resperran': 132,
    'resperwea': 133,
}

STAT_MAXIMUM = {
    'AP': 12,
    'MP': 6,
    'Range': 6,
    '% Neutral Resist': 53,
    '% Air Resist': 53,
    '% Fire Resist': 53,
    '% Water Resist': 53,
    '% Earth Resist': 53,
}

STAT_KEY_TO_NAME = {v: k for k, v in STAT_NAME_TO_KEY.items()}

# Stats still in projects (weights, minimums) but not used anymore.
# Adding them here prevents crashes with legacy projects that still have them.
# If a migration is done to remove them from all projects, they can be cleaned
# up from DEPRECATED_STATS.
DEPRECATED_STATS = {
#     'Neutral Resist in PVP': 'pvpneutres',
#     'Water Resist in PVP': 'pvpwaterres',
#     'Air Resist in PVP': 'pvpairres',
#     'Fire Resist in PVP': 'pvpfireres',
#     'Earth Resist in PVP': 'pvpearthres',
#     '% Neutral Resist in PVP': 'pvpneutresper',
#     '% Air Resist in PVP': 'pvpairresper',
#     '% Fire Resist in PVP': 'pvpfireresper',
#     '% Water Resist in PVP': 'pvpwaterresper',
#     '% Earth Resist in PVP': 'pvpearthresper',
#    'pvpneutres',
#    'pvpearthres',
#    'pvpfireres',
#    'pvpwaterres',
#    'pvpairres',
#    'pvpneutresper',
#    'pvpearthresper',
#    'pvpfireresper',
#    'pvpwaterresper',
#    'pvpairresper',
}

AGI_TARGETS = [
    (0, 2),
    (8, 3),
    (42, 4),
    (134, 5),
    (384, 6),
    (1060, 7),
]

MIN_AGI_FOR_BONUS = dict((e[1], e[0]) for e in AGI_TARGETS)

CRIT_TARGETS = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]

BASE_STATS = ['vit', 'wis', 'str', 'int', 'cha', 'agi']
MAIN_STATS = ['str', 'int', 'cha', 'agi']

STATS_NAMES = [(STAT_KEY_TO_NAME[stat_key], stat_key) for stat_key in BASE_STATS]

AIR = 'air'
FIRE = 'fire'
WATER = 'water'
NEUTRAL = 'neut'
EARTH = 'earth'
DAMAGE_TYPE_TO_MAIN_STAT = {
    NEUTRAL: 'str',
    EARTH: 'str',
    FIRE: 'int',
    WATER: 'cha',
    AIR: 'agi'
}
DAMAGE_TYPES = [NEUTRAL, EARTH, FIRE, WATER, AIR]
ELEMENT_KEY_TO_NAME = {
    'neut': 'Neutral',
    'earth': 'Earth',
    'fire': 'Fire',
    'water': 'Water',
    'air': 'Air'
}
ELEMENT_NAME_TO_KEY = {v: k for k, v in ELEMENT_KEY_TO_NAME.items()}

WEIRD_CONDITION_FROM_ID = {1: 'light_set', 2: 'prysmaradite'}
WEIRD_CONDITION_TO_ID = {v: k for k, v in WEIRD_CONDITION_FROM_ID.items()}
WEIRD_CONDITIONS = list(WEIRD_CONDITION_TO_ID.keys()) 

class Spell:
    def __init__(self, name, level_req, effects, aggregates=[], 
                 is_linked=None, stacks=1, special=None):
        self.name = name
        self.level_req = level_req
        self.effects = effects
        self.aggregates = aggregates
        self.stacks = stacks
        self.digest = None
        self.is_linked = is_linked
        self.special = special

    def get_effects_digest(self):
        if self.digest is None:
            self.digest = self.build_effects_digest()
        return self.digest
        
    def build_effects_digest(self):
        levels = len(self.level_req)
        e = self.effects
        non_crit = [[] for _ in range(levels)]
        for dam_entry in range(len(e.elements)):
            non_crit_range = (e.non_crit_ranges[dam_entry]
                              if (e.non_crit_ranges is not None
                                  and len(e.non_crit_ranges) > dam_entry)
                              else None)
            if non_crit_range:
                element = e.elements[dam_entry]
                steals = (e.steals[dam_entry] if e.steals is not None else False)
                heals = (e.heals[dam_entry] if e.heals is not None else False)
                for level in range(levels):
                    non_crit[level].append(DamageDigest(non_crit_range[level].min_dam,
                                                        non_crit_range[level].max_dam,
                                                        element,
                                                        steals,
                                                        heals))
        crit = [[] for _ in range(levels)]
        for dam_entry in range(len(e.crit_elements)):
            crit_range = (e.crit_ranges[dam_entry]
                          if (e.crit_ranges is not None
                              and len(e.crit_ranges) > dam_entry)
                          else None)
            if crit_range:
                element = e.crit_elements[dam_entry]
                steals = (e.steals[dam_entry] if e.steals is not None else False)
                heals = (e.heals[dam_entry] if e.heals is not None else False)
                for level in range(levels):
                    crit[level].append(DamageDigest(crit_range[level].min_dam,
                                                  crit_range[level].max_dam,
                                                  element,
                                                  steals,
                                                  heals))
        
        return EffectsDigest(non_crit, crit, self.aggregates)

class Effects:
    def __init__(self, non_crit_ranges, crit_ranges, elements, crit_elements=None, 
                 steals=None, heals=None):
        self.non_crit_ranges = [[Range(r) for r in l] for l in non_crit_ranges]
        self.crit_ranges = ([[Range(r) for r in l] for l in crit_ranges]
                            if crit_ranges is not None
                            else None)
        self.elements = elements
        self.crit_elements = crit_elements if crit_elements else elements
        self.steals = steals
        self.heals = heals

class Range:
    def __init__(self, min_max_dam):
        min_max_dam_string = min_max_dam.split('-')
        if len(min_max_dam_string) == 1:
            self.min_dam = self.max_dam = int(min_max_dam_string[0])
        else:
            self.min_dam = int(min_max_dam_string[0])
            self.max_dam = int(min_max_dam_string[1])

class EffectsDigest:
    def __init__(self, non_crit_dams, crit_dams, aggregates=[]):
        self.hit_number = len(non_crit_dams[0])
        self.non_crit_dams = non_crit_dams
        self.crit_dams = crit_dams
        self.aggregates = aggregates

class BaseDamage:
    def __init__(self, min_dam, max_dam, element, steals=False, heals=False):
        self.min_dam = min_dam
        self.max_dam = max_dam
        self.element = element
        self.steals = steals
        self.heals = heals

    def __repr__(self):
        return '%d-%d (%s)' % (self.min_dam,
                               self.max_dam,
                               self.element)    
        #return '%s%d-%d (%s)' % (('%s ' % self.hit_name) if self.hit_name else '',
        #                           self.min_dam,
        #                           self.max_dam,
        #                           self.element)  
                                            
    def average(self):
        return (self.min_dam + self.max_dam) / 2.0
        
    def copy_with_element(self, element):
        new_instance = copy(self)
        new_instance.element = element
        return new_instance

class DamageDigest(BaseDamage):
    pass

def create_duster_values(base, base_per_tofu, max_tofus):
    spell = []
    for i in range(max_tofus + 1):
        inner_spell = []
        for values in base:
            dam = '%d-%d' % (values[0] + base_per_tofu * i, 
                             values[1] + base_per_tofu * i)
            inner_spell.append(dam)
        spell.append(inner_spell)
    return spell

def create_stacking_values(base, bonus, times):
    spell = []
    for i in range(times):
        inner_spell = []
        for values in base:
            dam = '%d-%d' % (values[0] + bonus * i, 
                             values[1] + bonus * i)
            inner_spell.append(dam)
        spell.append(inner_spell)
    return spell

def create_level_based_stacking_values(base, bonus, times):
    spell = []
    for i in range(times):
        inner_spell = []
        for j in range(len(base)):
            dam = '%d-%d' % (base[j][0] + bonus[j] * i, 
                             base[j][1] + bonus[j] * i)
            inner_spell.append(dam)
        spell.append(inner_spell)
    return spell

CHARGED_LABELS = [
    'Not charged',
    'Charged once',
    'Charged twice',
] + ['Charged %d times' % n for n in range(3, 20)]

BOMB_LABELS = [
    '',
    '1 bomb',
] + ['%d bombs' % n for n in range(2, 20)]

TREE_LABELS = [
    '',
    '1 tree',
] + ['%d trees' % n for n in range(2, 20)]

TRAP_LABELS = [
    '',
    '1 trap',
] + ['%d traps' % n for n in range(2, 20)]

REBOUND_LABELS = [
    '',
    '1 rebound',
] + ['%d rebounds' % n for n in range(2, 20)]


DAMAGE_SPELLS = {
    'default': [
        Spell("Grunob's Lightning Strike", [20, 87, 154], Effects(
            [['13-16', '17-21', '21-26']],
            [['16-22', '20-25', '25-31']],
            [FIRE]
        ), is_linked=(1, "Grunob's Lesson")),
        Spell("Grunob's Lesson", [87, 154], Effects(
            [['19-22', '23-37']],
            None,
            [FIRE]
        ), is_linked=(2, "Grunob's Lightning Strike")),
        Spell('Burnt Pie', [30, 97, 164], Effects(
            [['5-7', '6-8', '8-10']] * 5,
            [['6-8', '8-10', '10-12']] * 5,
            [EARTH, FIRE, WATER, AIR]
        ), aggregates=[("Hit in worst element", [0]),
                       ('', [1]),
                        ('', [2]),
                        ('', [3])],
        is_linked=(1, 'Leek Pie')),
        Spell('Leek Pie', [97, 164], Effects(
            [['6-8', '8-10']] * 5,
            [['8-10', '10-12']] * 5,
            [EARTH, FIRE, WATER, AIR]
        ), aggregates=[("Hit in best element", [0]),
                       ('', [1]),
                        ('', [2]),
                        ('', [3])],
        is_linked=(2, 'Burnt Pie')),
        Spell('Kannibubble', [40, 107, 174], Effects(
            [['12-15', '15-19', '19-23']],
            [['14-17', '18-22', '23-28']],
            [WATER]
        ), is_linked=(1, 'Kanniboil')),
        Spell('Kanniboil', [107, 174], Effects(
            [['21-24', '26-30']],
            [['25-29', '31-36']],
            [WATER]
        ), is_linked=(2, 'Kannibubble')),
        Spell('Mantiscroc', [60, 127, 194], Effects(
            [['14-17', '18-22', '20-24']],
            [['17-21', '21-26', '24-29']],
            [EARTH]
        ), is_linked=(1, 'Dart Mocles')),
        Spell('Dart Mocles', [127, 194], Effects(
            [['22-27', '25-30']],
            [['27-32', '30-36']],
            [EARTH]
        ), is_linked=(2, 'Mantiscroc')),
        Spell('Moon Hammer', [80, 147], Effects(
            [['15-19', '19-24']],
            [['19-24', '23-29']],
            [AIR]
        ), is_linked=(1, 'Darkli Moon Hammer')),
        Spell('Darkli Moon Hammer', [80, 147], Effects(
            [['21-26', '26-33']],
            [['25-32', '31-40']],
            [AIR]
        ), is_linked=(2, 'Moon Hammer')),
        Spell('Perfidious Boomerang', [100, 200], Effects(
            [['21-23', '26-29'] for i in range(4)],
            [['25-28', '31-35'] for i in range(4)],
            [EARTH, FIRE, WATER, AIR],
            steals=[True for i in range(4)],
        ), aggregates=[("25% chance of", [0]),
                       ("25% chance of", [1]),
                       ("25% chance of", [2]),
                       ("25% chance of", [3])],
        is_linked=(1, 'Diamondine Boomerang')),
        Spell('Diamondine Boomerang', [100, 200], Effects(
            [['21-23', '26-29'] for i in range(4)],
            [['25-28', '31-35'] for i in range(4)],
            [EARTH, FIRE, WATER, AIR],
        ), aggregates=[("25% chance of", [0]),
                       ("25% chance of", [1]),
                       ("25% chance of", [2]),
                       ("25% chance of", [3])],
        is_linked=(2, 'Perfidious Boomerang')),
        Spell('Weapon Skill', [1], Effects(
            [['300']],
            [['350']],
            ['buff_pow_weapon']
        )),
        Spell('Ebony Dofus', [180], Effects(
            [['14-16']] * 4,
            None,
            [EARTH, FIRE, WATER, AIR]
        )),
        Spell("Crocobur's Appetite", [200], Effects(
            [['11-15']] * 5,
            None,
            [NEUTRAL, EARTH, FIRE, WATER, AIR], steals=[True, True, True, True, True]
        ), aggregates=[("Steals in best element", [0]),
                    ('', [1]),
                    ('', [2]),
                    ('', [3]),
                    ('', [4])]),
        Spell('Pestilential Fog', [200], Effects(
            [['16-18']] * 5,
            None,
            [NEUTRAL, EARTH, FIRE, WATER, AIR]
        ), aggregates=[("Hit in best element", [0]),
                    ('', [1]),
                    ('', [2]),
                    ('', [3]),
                    ('', [4])]),
        Spell('Scurvion Toxicity', [200], Effects(
            [['6-8']] * 5,
            None,
            [NEUTRAL, EARTH, FIRE, WATER, AIR]
        ), aggregates=[("Hit in best element", [0]),
                    ('', [1]),
                    ('', [2]),
                    ('', [3]),
                    ('', [4])]),
    ],
    'Cra': [
        Spell('Optical Arrow', [1, 66, 132], Effects(
            [['14-16', '18-21', '23-27']],
            [['16-19', '21-25', '28-32']],
            [AIR]
        ), is_linked=(1, 'Raining Arrows')),
        Spell('Raining Arrows', [95, 162], Effects(
            [['19-21', '24-26']],
            [['23-25', '29-31']],
            [AIR]
        ), is_linked=(2, 'Optical Arrow')),
        Spell('Frozen Arrow', [1, 67, 133], Effects(
            [['14-17', '19-22', '24-28']],
            [['28-21', '23-26', '29-34']],
            [WATER]
        ), is_linked=(1, 'Slow Down Arrow')),
        Spell('Slow Down Arrow', [100, 167], Effects(
            [['27-29', '34-36']],
            [['33-35', '41-43']],
            [WATER]
        ), is_linked=(2, 'Frozen Arrow')),
        Spell('Repulsive Shot', [3, 69, 136], Effects(
            [['17-19', '22-25', '28-32']],
            [['20-23', '26-30', '34-38']],
            [FIRE]
        ), is_linked=(1, 'Burning Arrows')),
        Spell('Burning Arrows', [110, 177], Effects(
            [['27-29', '33-36']],
            [['32-35', '40-43']],
            [FIRE]
        ), is_linked=(2, 'Repulsive Shot')),
        Spell('Erosive Arrow', [6, 71, 138], Effects(
            [['15-17', '20-23', '25-29']],
            [['18-21', '24-28', '30-35']],
            [EARTH]
        ), is_linked=(1, 'Covering Fire')),
        Spell('Covering Fire', [115, 182], Effects(
            [['32-36', '38-42']],
            [['39-43', '46-50']],
            [EARTH]
        ), is_linked=(2, 'Erosive Arrow')),
        Spell('Immobilising Arrow', [15, 82, 149], Effects(
            [['7-9', '9-11', '11-13']],
            [['8-10', '10-12', '13-16']],
            [WATER]
        ), is_linked=(1, 'Assailing Arrow')),
        Spell('Assailing Arrow', [125, 192], Effects(
            [['29-32', '33-37'], ['100', '100']],
            [['35-39', '40-44'], ['100', '100']],
            [FIRE, 'buff_pow']
        ), stacks=3, is_linked=(2, 'Immobilising Arrow')),
        Spell('Retreating Shot', [20, 87, 154], Effects(
            [['15-17', '20-22', '25-28']],
            [['18-20', '23-26', '30-34']],
            [AIR]
        ), is_linked=(1, 'Barricade Shot')),
        Spell('Barricade Shot', [130, 197], Effects(
            [['23-27', '26-30']],
            [['28-32', '31-36']],
            [EARTH]
        ), is_linked=(2, 'Retreating Shot')),
        Spell('Piercing Shots', [25, 92, 159], Effects(
            [['10', '40', '60']],
            [['15', '50', '70']],
            ['buff_dam']
        )),
        Spell('Exploding Arrow', [30, 97, 164], Effects(
            [['4-6', '6-8', '7-10'], ['12-13', '14-16', '19-23']],
            [['7-9', '9-11', '11-14'], ['14-16', '17-20', '24-28']],
            [FIRE, FIRE]
        ), is_linked=(1, 'Tormenting Arrow 1')),
        Spell('Tormenting Arrow 1', [140], Effects(
            [['25-27'], ['14-16']],
            [['30-32'], ['17-19']],
            [AIR, AIR]
        ), is_linked=(2, 'Exploding Arrow')),
        Spell('Poisoned Arrow', [35, 102, 169], Effects(
            [['10-12', '13-15', '17-18']],
            [['12-14', '16-18', '20-21']],
            [NEUTRAL]
        ), is_linked=(1, 'Paralysing Arrow')),
        Spell('Paralysing Arrow', [145], Effects(
            [['37-39']],
            [['44-47']],
            [WATER]
        ), is_linked=(2, 'Poisoned Arrow')),
        Spell('Powerful Shots', [40, 107, 174], Effects(
            [['150', '200', '250']],
            [['170', '230', '290']],
            ['buff_pow_spell']
        )),
        Spell('Concentration Arrow', [45, 112, 179], Effects(
            [['14-16', '19-22', '23-26']],
            [['17-20', '23-26', '28-31']],
            [AIR]
        ), is_linked=(1, 'Destructive Bolts')),
        Spell('Destructive Bolts', [155], Effects(
            [['36-38']],
            [['43-46']],
            [EARTH]
        ), is_linked=(2, 'Concentration Arrow')),
        Spell("Bat's Eye", [50, 117, 184], Effects(
            [['13-15', '18-20', '21-24']],
            [['16-18', '21-24', '25-29']],
            [WATER], steals=[True]
        ), is_linked=(1, 'Crushing Arrow')),
        Spell('Crushing Arrow', [160], Effects(
            [['30-34']],
            [['36-41']],
            [FIRE]
        ), is_linked=(2, "Bat's Eye")),
        #TODO: figure out how to modify uppder limit to 12 (crash if I put higher value than 10)
        Spell('Piercing Shot', [60, 127, 194], Effects(
            create_stacking_values(((25, 28), (30, 34), (34, 38),), 4, 10),
            create_stacking_values(((30, 33), (36, 41), (41, 46),), 4, 10),
            [AIR]*10,
        ), aggregates=[(CHARGED_LABELS[n], [n]) for n in range(10)],
        is_linked=(1, 'Devouring Arrow')), 
        Spell('Devouring Arrow', [170], Effects(
            [['11-13'],
             ['23-27'],
             ['34-38'],
             ['34-38'],
             ['52-56'],
             ['70-74']],
            [['13-15'],
             ['26-30'],
             ['39-43'],
             ['39-43'],
             ['60-64'],
             ['81-85']],
            [AIR, AIR, AIR, AIR, AIR, AIR], steals=[False, False, False, True, True, True]
        ), aggregates=[('Not charged', [0]),
                        ('Charged once', [1]),
                        ('Charged twice', [2]),
                        ('Shock Not charged', [3]),
                        ('Shock Charged once', [4]),
                        ('Shock Charged twice', [5])],
        is_linked=(2, 'Piercing Shot')),
        Spell('Punitive Arrow', [65, 131, 198], Effects(
            create_level_based_stacking_values(((21, 23), (26, 28), (29, 31)), 
                                               (23, 29, 36), 3),
            create_level_based_stacking_values(((26, 28), (31, 33), (35, 37)), 
                                               (23, 29, 36), 3),
            [EARTH, EARTH, EARTH]
        ), aggregates=[(CHARGED_LABELS[n], [n]) for n in range(3)],
        is_linked=(1, 'Arrow of Judgement')),
        Spell('Arrow of Judgement', [175], Effects(
            [['14-15'], ['31-35']],
            [['16-18'], ['37-42']],
            [EARTH, EARTH], steals=[True, False]
        ), is_linked=(2, 'Punitive Arrow')),
        Spell('Atonement Arrow', [75, 142], Effects(
            create_level_based_stacking_values(((28, 30), (35, 37)), 
                                               (35, 43), 3),
            create_level_based_stacking_values(((34, 36), (42, 44)), 
                                               (35, 43), 3),
            [WATER, WATER, WATER],
        ), aggregates=[(CHARGED_LABELS[n], [n]) for n in range(3)],
        is_linked=(1, 'Redemption Arrow')),
        Spell('Redemption Arrow', [185], Effects(
            create_stacking_values(((23, 26),), 7, 9),
            create_stacking_values(((28, 31),), 7, 9),
            [WATER]*9,
        ), aggregates=[(CHARGED_LABELS[n], [n]) for n in range(9)],
        is_linked=(2, 'Atonement Arrow')),
        Spell('Explosive Arrow', [80, 147], Effects(
            [['24-27', '30-34']],
            [['29-33', '36-41']],
            [FIRE]
        ), is_linked=(1, 'Fulminating Arrow')),
        Spell('Fulminating Arrow', [190], Effects(
            create_stacking_values(((38, 42),), 10, 10),
            None,
            [FIRE] * 10,
        ), aggregates=[(CHARGED_LABELS[n], [n]) for n in range(10)], 
        is_linked=(2, 'Explosive Arrow')),
        Spell('Tormenting Arrow 2', [85, 152], Effects(
            [['10-12', '13-15'], ['10-12', '13-15']],
            [['13-15', '16-18'], ['13-15', '16-18']],
            [EARTH, WATER]
        ), is_linked=(1, 'Tyrannical Arrow')),
        Spell('Tyrannical Arrow', [195], Effects(
            [['13-15'], ['13-15'], ['7-10'], ['7-10']],
            [['16-18'], ['16-18'], ['7-10'], ['7-10']],
            [FIRE, AIR, FIRE, AIR]
        ), aggregates=[('', [0]),
                        ('', [1]),
                        ('After pushback damage', [2]),
                        ('If pushed or attracted', [3])], 
        is_linked=(2, 'Tormenting Arrow 2')),
    ],
    'Ecaflip': [
        Spell('Heads or Tails', [1, 66, 132], Effects(
            [['15-17', '20-23', '26-29'],
             ['10-12', '14-16', '18-20']],
            [['19-21', '24-27', '31-35'],
             ['13-15', '17-19', '22-24']],
            [EARTH, EARTH],
        ), aggregates=[('This turn', [0]),
                       ('Next turn', [1])], 
        is_linked=(1, 'Tails or Heads')),
        Spell('Tails or Heads', [95, 162], Effects(
            [['27-30', '33-37']],
            [['32-36', '40-44']],
            [EARTH],
        ), is_linked=(2, 'Heads or Tails')),
        Spell('Balling Up', [1, 67, 133], Effects(
            [['17-19', '23-25', '29-32']],
            [['21-23', '27-30', '35-38']],
            [AIR],
        ), is_linked=(1, 'Meowch')),
        Spell('Meowch', [100, 167], Effects(
            [['27-31','34-38']],
            [['33-37', '41-46']],
            [FIRE],
        ), is_linked=(2, 'Balling Up')),        
        Spell('Bluff', [3, 69, 136], Effects(
            [['15-17', '20-23', '26-29']],
            [['19-21', '24-27', '31-35']],
            [WATER],
        ), is_linked=(1, 'Nerve')),
        Spell('Nerve', [110, 177], Effects(
            [['28-31','35-39']],
            [['34-38', '42-47']],
            [AIR],
        ), is_linked=(2, 'Bluff')),
        Spell('Topkaj', [10, 77, 144], Effects(
            [['16-18', '22-24', '27-30']],
            [['19-21', '26-29', '32-36']],
            [FIRE]
        ), is_linked=(1, 'Yowling')),
        Spell('Yowling', [120, 187], Effects(
            [['26-30','30-34'],
             ['26-30','30-34']],
            [['31-36','36-41'],
             ['31-36','36-41']],
            [FIRE, FIRE],
            heals=[False, True],
        ), aggregates=[('Enemies', [0]),
                       ('Allies', [1])], is_linked=(2, 'Topkaj')),
        Spell('Roar', [130, 197], Effects(
            [['50', '70']],
            None,
            ['buff_pow']
        )),
        Spell('All or Nothing', [25, 92, 159], Effects(
            [['27-29', '34-37', '42-46']] * 4,
            [['32-35', '40-44', '50-55']] * 4,
            [WATER, FIRE, FIRE, WATER],
            heals=[False, True, True, False],
        ), aggregates=[('Enemies (imediately)', [0]),
                       ('Enemies (next turn)', [1]),
                       ('Allies (imediately)', [2]),
                       ('Allies (next turn)', [3])],
        is_linked=(1, 'Peril')),
        Spell('Peril', [135], Effects(
            [['37-41'],
             ['32-36']],
            [['44-49'],
             ['38-43']],
            [WATER, FIRE],
            heals=[False, True],
        ), aggregates=[('Summons', [0]),
                       ('Others', [1])], 
        is_linked=(2, 'All or Nothing')),
        Spell('Rough Tongue', [40, 107, 174], Effects(
            [['19-21', '24-27', '30-33']],
            [['23-25', '29-32', '36-40']],
            [FIRE]
        ), is_linked=(1, 'Lapping Up')),
        Spell('Lapping Up', [150], Effects(
            [['32-36']],
            [['38-43']],
            [EARTH],
        ), is_linked=(2, 'Rough Tongue')),
        Spell('Wheel of Fortune', [45, 112, 179], Effects(
            [['100', '175', '250']],
            [['140', '245', '350']],
            ['buff_pow_spell']
        )),
        Spell('Feline Spirit', [50, 117, 184], Effects(
            [['19-21', '26-29', '31-34']],
            [['23-26', '32-35', '37-41']],
            [EARTH]
        ), is_linked=(1, 'Pawpads')),
        Spell('Pawpads', [160], Effects(
            [['25-28']],
            [['30-34']],
            [FIRE],
        ), is_linked=(2, 'Feline Spirit')),
        Spell('Reflex', [65, 131, 198], Effects(
            [['23-26', '28-31', '31-35']],
            [['28-31', '33-38', '37-42']],
            [AIR]
        ), is_linked=(1, 'Bravado')),
        Spell('Bravado', [175], Effects(
            [['46-50']],
            [['55-60']],
            [AIR],
        ), is_linked=(2, 'Reflex')),
        Spell('Playful Claw', [70, 137], Effects(
            [['27-30', '35-39']],
            [['37-41', '47-53']],
            [WATER],
        ), is_linked=(1, 'Misadventure')),
        Spell('Misadventure', [180], Effects(
            [['37-41']] * 3,
            [['44-49']] * 3,
            [EARTH, EARTH, EARTH],
            steals=[False, False, True]
        ), aggregates=[('', [0]),
                        ('If previous casting was a critical hit', [1]),
                        ('', [2])],
        is_linked=(2, 'Playful Claw')),
        Spell('Felintion', [75, 142], Effects(
            [['27-29', '33-36']],
            [['32-35', '40-43']],
            [WATER],
            steals=[True]
        ), is_linked=(1, 'Kraps')),
        Spell('Kraps', [185], Effects(
            [['42-46']],
            [['50-55']],
            [WATER],
        ), is_linked=(2, 'Felintion')),
        Spell('Claw of Ceangal', [80, 147], Effects(
            [['13-15', '17-19']],
            [['16-18', '20-23']],
            [AIR]
        ), is_linked=(1, 'Misfortune')),
        Spell('Misfortune', [190], Effects(
            [['27-30']],
            [['32-36']],
            [WATER],
        ), is_linked=(2, 'Claw of Ceangal')),
        Spell('Rekop', [85, 152], Effects(
            [['13-15', '17-19'], ['20-22', '26-28'], ['26-30', '34-38']] * 4,
            None,
            [FIRE, EARTH, AIR, WATER] * 4,
        ), aggregates=[('1 turn', list(range(0, 4))),
                        ('2 turns', list(range(4, 8))),
                        ('3 turns', list(range(8, 12)))],
        is_linked=(1, 'Trickery')),
        Spell('Trickery', [195], Effects(
            [['58-62'],
             ['46-50'],
             ['34-38'],
             ['23-25']],
            [['70-74'],
             ['55-60'],
             ['41-46'],
             ['28-30']],
            [EARTH, AIR, WATER, FIRE],
        ), aggregates=[('5 AP', [0]),
                       ('4 AP', [1]),
                       ('3 AP', [2]),
                       ('2 AP', [3])],
        is_linked=(2, 'Rekop')),
        Spell('Fate of Ecaflip', [90, 157], Effects(
            [['31-34', '38-42']],
            [['37-40', '46-50']],
            [EARTH]
        ), is_linked=(1, "Ecaflip's Audacity")),
        Spell("Ecaflip's Audacity", [200], Effects(
            [['27-30'],
             ['150']],
            [['32-36'],
             ['180']],
            [EARTH, 'buff_pow'],
        ), aggregates=[('', [0]),
                       ('If the target is pushed', [1])], 
        is_linked=(2, 'Fate of Ecaflip')),
    ],
    'Eniripsa': [
        Spell('Raucous Word', [1, 67, 133], Effects(
            [['14-16', '19-21', '24-27'],
             ['14-16', '19-21', '24-27']],
            [['17-19', '22-25', '29-32'],
             ['17-19', '22-25', '29-32']],
            [FIRE, FIRE], heals=[True, False],
        ), aggregates=[('Allies', [0]),
                       ('Enemies', [1])], 
        is_linked=(1, 'Deafening Cry')),
        Spell('Deafening Cry', [100, 167], Effects(
            [['21-24', '26-30']],
            [['25-29', '32-36']],
            [FIRE]
        ), is_linked=(2, 'Raucous Word')),
        Spell('Mischievous Word', [1, 66, 132], Effects(
            [['12-14', '16-19', '21-24']],
            [['15-17', '20-22', '25-29']],
            [AIR]
        ), is_linked=(1, 'Malicious Word')),
        Spell('Malicious Word', [95, 162], Effects(
            [['24-27', '30-34']],
            [['29-33', '36-41']],
            [AIR]
        ), is_linked=(2, 'Mischievous Word')),
        Spell('Vampiric Word', [3, 69, 136], Effects(
            [['16-18', '21-23', '27-30']],
            [['19-21', '25-28', '32-36']],
            [WATER]
        ), is_linked=(1, 'Sobs')),
        Spell('Sobs', [110, 177], Effects(
            [['19-21', '23-26'],
             ['19-21', '23-26']],
            [['22-24', '28-31'],
             ['22-24', '28-31']],
            [WATER, WATER]
        ), aggregates=[('Target', [0]),
                       ('Allies around target are healed by 100% of damage', [1])],
        is_linked=(2, 'Vampiric Word')),
        Spell('Profanity', [6, 71, 138], Effects(
            [['14-16', '18-20', '22-25']],
            [['17-19', '21-24', '26-30']],
            [EARTH]
        ), is_linked=(1, 'Ancestral Ointment')),
        Spell('Ancestral Ointment', [115, 182], Effects(
            [['31-33', '35-38'],
             ['31-33', '35-38']],
            [['34-37', '40-44'],
             ['34-37', '40-44']],
            [EARTH, EARTH], heals=[False, True]
        ), aggregates=[('Enemies', [0]),
                       ('Allies', [1])],
        is_linked=(2, 'Profanity')),
        Spell('Scalpel', [125, 192], Effects(
            [['52', '60'],
             ['47-52', '54-60']] * 5,
            [['63', '72'],
             ['57-63', '65-72']] * 5,
            [NEUTRAL, NEUTRAL, EARTH, EARTH, FIRE, FIRE, WATER, WATER, AIR, AIR], heals=[False, True, False, True, False, True, False, True, False, True],
        ), aggregates=[("On ennemy, hit in best element", [0]),
                    ('', [2]),
                    ('', [4]),
                    ('', [6]),
                    ('', [8]),
                    ('On ally, heals in best element', [1]),
                    ('', [3]),
                    ('', [5]),
                    ('', [7]),
                    ('', [9])],),
        Spell('Lamentations', [20, 87, 154], Effects(
            [['18-20', '23-26', '29-32'],
             ['18-20', '23-26', '29-32']],
            [['22-24', '28-31', '35-38'],
             ['22-24', '28-31', '35-38']],
            [WATER, WATER], steals=[True, False],
        ), aggregates=[('Enemies', [0]),
                       ('Allies are healed by 50% of the damage inflicted on each enemies', [1])],
        is_linked=(1, 'Commotion')),
        Spell('Commotion', [130, 197], Effects(
            [['30-33', '33-37'],
             ['30-33', '33-37']],
            [['35-39', '40-44'],
             ['35-39', '40-44']],
            [FIRE, FIRE], heals=[True, False]
        ), aggregates=[('Allies', [0]),
                       ('Enemies', [1])],
        is_linked=(2, 'Lamentations')),
        Spell('Turbulent Word', [25, 92, 159], Effects(
            [['23-26', '29-33', '36-41'],
             ['23-26', '29-33', '36-41']],
            [['27-31', '35-39', '43-49'],
             ['27-31', '35-39', '43-49']],
            [FIRE, FIRE], heals=[True, False]
        ), aggregates=[('Allies', [0]),
                       ('Enemies', [1])],
        is_linked=(1, 'Furious Word')),
        Spell('Furious Word', [135], Effects(
            [['32-36']],
            [['38-43']],
            [EARTH]
        ), is_linked=(2, 'Turbulent Word')),
        Spell('Galvanising Word', [140], Effects(
            [['200']],
            None,
            ['buff_pow']
        )),
        Spell("Prankster's Word", [35, 102, 169], Effects(
            [['15-17', '18-20', '22-24'],
             ['15-17', '18-20', '22-24']],
            [['17-19', '21-23', '26-28'],
             ['17-19', '21-23', '26-28']],
            [AIR, AIR], heals=[False, True]
        ), aggregates=[('Enemies', [0]),
                       ('Allies', [1])],
        is_linked=(1, 'Defensive Word')),
        Spell('Defensive Word', [145], Effects(
            [['28-31']],
            [['34-37']],
            [WATER], steals=[True]
        ), is_linked=(2, "Prankster's Word")),
        Spell('Warpaint', [40, 107, 174], Effects(
            [['6-7', '7-9', '9-11'],
             ['6-7', '7-9', '9-11'],
             ['6-7', '7-9', '9-11']],
            [['6-7', '7-9', '9-11'],
             ['8-9', '10-12', '12-14'],
             ['8-9', '10-12', '12-14']],
            [EARTH, EARTH, EARTH], heals=[True, False, True]
        ), aggregates=[('Allies', [0]),
                       ('Enemies', [1]),
                       ('Allies at the start of their turn', [2])],
        is_linked=(1, 'Secret Word')),
        Spell('Secret Word', [150], Effects(
            [['28-32'], ['28-32'], ['58-62'], ['58-62']],
            [['34-38'], ['34-38'], ['64-68'], ['64-68']],
            [AIR] * 4, heals=[True, False, True, False]
        ), aggregates=[('Allies, not charged', [0]),
                       ('Enemies, not charged', [1]),
                       ('Allies, charged once', [2]),
                       ('Enemies, charged once', [3])],
        is_linked=(2, 'Warpaint')),
        Spell('War Cry', [50, 117, 184], Effects(
            [['23-26', '31-35', '37-41']],
            [['28-31', '38-42', '44-49']],
            [EARTH]
        ), is_linked=(1, 'Ritual Word')),
        Spell('Ritual Word', [160], Effects(
            [['28-32']] * 2,
            [['34-38']] * 2,
            [EARTH] * 2, heals=[False, True]
        ), aggregates=[('Enemies', [0]),
                       ('Allies', [1])],
        is_linked=(2, 'War Cry')),
        Spell('Forbidden Word', [55, 122, 189], Effects(
            [['30-33', '40-44', '46-50']],
            [['36-39', '48-52', '55-60']],
            [WATER]
        ), is_linked=(1, 'Bloodless Word')),
        Spell('Bloodless Word', [165], Effects(
            [['37-40']] * 2,
            [['41-45']] * 2,
            [WATER] * 2, heals=[False, True]
        ), aggregates=[('Enemies', [0]),
                       ('Allies', [1])],
        is_linked=(2, 'Forbidden Word')),
        Spell('Pilfering', [65, 131, 198], Effects(
            [['14-16', '17-19', '19-21']],
            [['17-19', '20-22', '22-25']],
            [FIRE], steals=[True]
        ), is_linked=(1, 'Distracting Word')),
        Spell('Distracting Word', [175], Effects(
            [['23-27']] * 2,
            [['28-32']] * 2,
            [FIRE] * 2, heals=[True, False]
        ), aggregates=[('Allies', [0]),
                       ('Enemies', [1])],
        is_linked=(2, 'Pilfering')),
        Spell('Flowery Word', [70, 137], Effects(
            [['26-29', '33-37']] * 2,
            [['31-35', '40-44']] * 2,
            [AIR] * 2, heals=[False, True]
        ), aggregates=[('Enemies', [0]),
                       ('Allies around enemies are healed at the end of enemies turns', [1])],
        is_linked=(1, 'Enchanted Thicket')),
        Spell('Enchanted Thicket', [180], Effects(
            [['39-43']] * 2,
            [['45-50']] * 2,
            [AIR] * 2, heals=[True, False]
        ), aggregates=[('Allies', [0]),
                       ('Enemies', [1])],
        is_linked=(2, 'Flowery Word')),
        Spell('Tribal Paintbrush', [80, 147], Effects(
            [['15-18', '19-22']] * 2 +
            create_stacking_values(((15, 18), (19, 22)), 10, 10),
            [['19-22', '23-26']] * 2 +
            create_stacking_values(((19, 22), (23, 26)), 10, 10),
            [EARTH] * 12, heals=[True, False] + [False] * 10
        ), aggregates=[('Allies', [0]),
                    ('Enemies', [1])] + [(CHARGED_LABELS[n], [n+2]) for n in range(10)],
        is_linked=(1, 'Shrill Choir')),
        Spell('Shrill Choir', [190], Effects(
            create_stacking_values(((40, 44),), 7, 10),
            create_stacking_values(((48, 53),), 7, 10),
            [FIRE] * 10
        ), aggregates=[(CHARGED_LABELS[n], [n]) for n in range(10)],
        is_linked=(2, 'Tribal Paintbrush')),
        Spell('Cryotherapy', [85, 152], Effects(
            [['11-13', '14-16']] * 3,
            [['13-15', '17-19']] * 3,
            [WATER] * 3, heals=[False, True, False]
        ), aggregates=[('Target', [0]),
                       ('After target loses state:<br>Allies around the target', [1]),
                       ('Enemies around the target', [2])],
        is_linked=(1, 'Murmur')),
        Spell('Murmur', [195], Effects(
            [['16-18']] * 2,
            [['19-22']] * 2,
            [AIR] * 2, heals=[False, True]
        ), aggregates=[('Enemies', [0]),
                       ('Allies', [1])],
        is_linked=(2, 'Cryotherapy')),
    ],
    'Enutrof': [
        Spell('Coin Throwing', [1, 66, 132], Effects(
            [['7-9', '10-12', '13-15']],
            [['9-11', '12-14', '16-18']],
            [WATER],
        ), is_linked=(1, 'Placer Mining')), 
        Spell('Placer Mining', [95, 162], Effects(
            [['8', '10'], 
             ['8', '10'], 
             ['6-9', '8-11'], 
             ['2-10', '4-13']],
            None,
            [WATER] * 4,
        ), aggregates=[('', [0]),
                       ('For 2 turns when target suffers an attempted MP reduction:<br>Not charged', [1]),
                       ('Charged once', [2]),
                       ('Charged twice', [3])],
        is_linked=(2, 'Coin Throwing')),
        Spell('Prime of Life', [1, 67, 133], Effects(
            [['17-19', '22-25', '28-32']],
            [['20-23', '26-30', '34-38']],
            [EARTH],
        ), is_linked=(1, 'Collapse')),
        Spell('Collapse', [100, 167], Effects(
            [['10', '12'], 
             ['10', '12'], 
             ['8-11', '10-13'], 
             ['4-13', '6-15']],
            None,
            [EARTH] * 4,
        ), aggregates=[('', [0]),
                       ('For 2 turns when target suffers a Range reduction:<br>Not charged', [1]),
                       ('Charged once', [2]),
                       ('Charged twice', [3])],
        is_linked=(2, 'Prime of Life')),
        Spell('Shovel Kiss', [3, 69, 136], Effects(
            [['11-14', '15-18', '19-23']],
            [['14-16', '18-21', '23-28']],
            [FIRE],
        ), is_linked=(1, 'Deposit')),
        Spell('Deposit', [110, 177], Effects(
            [['23-26', '29-32']] * 2,
            [['28-31', '35-38']] * 2,
            [FIRE] * 2, heals=[False, True]
        ), aggregates=[('Ennemies at the end of their turns', [0]),
                       ('Allies at the end of their turns', [1])],
        is_linked=(2, 'Shovel Kiss')),
        Spell('Opportuneness', [6, 71, 138], Effects(
            [['8-10', '11-13', '14-16'], ['50', '60', '75']],
            [['10-12', '13-15', '17-19'], ['55', '65', '85']],
            [AIR, 'buff_pow']
        ), is_linked=(1, 'Hard Cash')),
        Spell('Hard Cash', [115, 182], Effects(
            [['9', '11'], 
             ['9', '11'], 
             ['7-10', '9-12'], 
             ['3-12', '5-14']],
            None,
            [AIR] * 4,
        ), aggregates=[('', [0]),
                       ('For 2 turns when target suffers an attempted AP reduction:<br>Not charged', [1]),
                       ('Charged once', [2]),
                       ('Charged twice', [3])],
        is_linked=(2, 'Opportuneness')),
        Spell('Mound', [20, 87, 154], Effects(
            [['12-14', '16-18', '20-22']],
            [['15-17', '19-21', '24-26']],
            [EARTH],
        ), is_linked=(1, 'Mine Fire')),
        Spell('Mine Fire', [130, 197], Effects(
            [['27-30', '30-34']],
            [['32-36', '35-39']],
            [FIRE]
        ), is_linked=(2, 'Mound')),
        Spell('Auriferous Shovel', [30, 97, 164], Effects(
            [['20-23', '26-29', '32-36']],
            [['24-27', '31-35', '38-43']],
            [WATER],
        ), is_linked=(1, 'Shovel Throwing')),
        Spell('Shovel Throwing', [140], Effects(
            [['32-35']],
            [['38-42']],
            [EARTH],
        ), is_linked=(2, 'Auriferous Shovel')),
        Spell('Greed', [40, 107, 174], Effects(
            [['10', '25', '40']],
            [['15', '30', '45']],
            ['buff_pow'],
        ), stacks=15,),
        Spell('Loafylactic', [45, 112, 179], Effects(
            [['12-14', '16-18', '19-21']],
            [['14-16', '19-21', '23-25']],
            [AIR],
        ), is_linked=(1, 'Peat Bog')),
        Spell('Peat Bog', [155], Effects(
            create_stacking_values(((22, 25),), 5, 11),
            create_stacking_values(((26, 30),), 5, 11),
            [EARTH] * 11,
        ), aggregates=[(str(n) + " MP used this turn", [n]) for n in range(11)],
        is_linked=(2, 'Loafylactic')),
        Spell('Golden Age', [160], Effects(
            [['200']],
            None,
            ['buff_pow']
        )),
        Spell('Ghostly Shovel', [55, 122, 189], Effects(
            [['17-19', '23-25', '26-28']],
            [['20-22', '27-29', '31-34']],
            [FIRE],
        ), is_linked=(1, 'Spade of the Ancients')),
        Spell('Spade of the Ancients', [165], Effects(
            [['32-36']],
            [['38-43']],
            [AIR],
        ), is_linked=(2, 'Ghostly Shovel')),
        Spell('Bankruptcy', [60, 127, 194], Effects(
            [['26-29', '32-36', '36-40']],
            [['31-35', '39-44', '43-48']],
            [AIR],
        ), is_linked=(1, 'Obsolescence')),
        Spell('Obsolescence', [170], Effects(
            [['26-30']],
            [['31-36']],
            [WATER],
        ), is_linked=(2, 'Bankruptcy')),
        Spell('Shovel of the Ancients', [70, 137], Effects(
            [['30-33', '38-42']],
            [['36-39', '46-50']],
            [WATER],
        ), is_linked=(1, 'Sieving')),
        Spell('Sieving', [180], Effects(
            [['25-29']],
            [['30-35']],
            [WATER],
        ), is_linked=(2, 'Shovel of the Ancients')),
        Spell('Lucky Shovel', [185], Effects(
            [['20']] * 5,
            None,
            [NEUTRAL, EARTH, FIRE, WATER, AIR],
        ), aggregates=[('Hit in best element on enemy that kills Lucky Shovel', [0]),
                        ('', [1]),
                        ('', [2]),
                        ('', [3]),
                        ('', [4])],),
        Spell('Unsummoning', [85, 152], Effects(
            [['31-34', '39-42', '16-18']] * 3,
            [['38-40', '47-50', '19-21']] * 3,
            [FIRE] * 3,
        ), aggregates=[('', [0]),
                        ('On summons', list([1, 2]))],
        is_linked=(1, 'Firedamp Explosion')),
        Spell('Firedamp Explosion', [195], Effects(
            [['14'], 
             ['14'], 
             ['12-15'], 
             ['8-17']],
            None,
            [FIRE] * 4,
        ), aggregates=[('', [0]),
                       ('For 2 turns when target is healed:<br>Not charged', [1]),
                       ('Charged once', [2]),
                       ('Charged twice', [3])],
        is_linked=(2, 'Unsummoning')),
    ],
    'Feca': [
        Spell('Natural Attack', [1, 67, 133], Effects(
            [['10-12', '14-16', '18-20'],
             ['20', '40', '60']],
            [['13-15', '17-19', '22-24'],
             ['30', '50', '70']],
            [FIRE, 'buff_int'],
        ), stacks=3,
        is_linked=(1, 'Natural Attraction')), 
        Spell('Natural Attraction', [100, 167], Effects(
            [['19-22', '24-27']],
            [['23-26', '29-32']],
            [FIRE],
        ), is_linked=(2, 'Natural Attack')), 
        Spell('Blindness', [1, 68, 134], Effects(
            [['12-14', '15-17', '20-22']],
            [['14-16', '19-21', '24-26']],
            [NEUTRAL],
        ), is_linked=(1, 'Dazzling')), 
        Spell('Dazzling', [105, 172], Effects(
            [['34-39', '42-48']],
            [['40-46', '50-58']],
            [EARTH],
        ), is_linked=(2, 'Blindness')), 
        Spell('Typhoon', [3, 69, 136], Effects(
            [['13-15', '17-19', '22-24'],
             ['20', '40', '60']],
            [['15-17', '20-22', '26-29'],
             ['30', '50', '70']],
            [AIR, 'buff_agi'],
        ), stacks=3, is_linked=(1, 'Gust')), 
        Spell('Gust', [110, 177], Effects(
            [['21-23', '26-28']],
            [['25-27', '31-34']],
            [AIR],
        ), is_linked=(2, 'Typhoon')), 
        Spell('Bubble', [6, 71, 138], Effects(
            [['9-11', '12-14', '15-17']],
            [['10-12', '14-16', '18-20']],
            [WATER],
        ), is_linked=(1, 'Swelling')), 
        Spell('Swelling', [115, 182], Effects(
            [['32-36', '38-42']],
            [['39-43', '46-50']],
            [AIR],
        ), is_linked=(2, 'Bubble')),
        Spell('Aggressive Glyph', [15, 82, 149], Effects(
            [['20-22', '26-28', '32-34']],
            None,
            [AIR],
        ), special='glyph', is_linked=(1, 'Fulminating Glyph')), 
        Spell('Fulminating Glyph', [125, 192], Effects(
            [['27-31', '31-35']],
            [['32-37', '37-42']],
            [AIR],
        ), special='glyph', is_linked=(2, 'Aggressive Glyph')), 
        Spell('Lethargy', [20, 87, 154], Effects(
            [['23-25', '29-32', '36-40']],
            [['27-30', '35-39', '43-48']],
            [FIRE],
        ), is_linked=(1, 'Lifelessness')), 
        Spell('Lifelessness', [130, 197], Effects(
            [['34-38', '38-42'],
             ['120', '150']],
            [['41-45', '46-50'],
             ['140', '170']],
            [FIRE, 'buff_int'],
        ), stacks=2, is_linked=(2, 'Lethargy')),
        Spell('Cloudy Attack', [25, 92, 159], Effects(
            [['19-21', '25-27', '31-33'],
             ['40', '60', '80']],
            [['23-25', '30-32', '37-40'],
             ['60', '80', '100']],
            [WATER, 'buff_cha'],
        ), stacks=2, is_linked=(1, 'Stormy Attack')),
        Spell('Stormy Attack', [135], Effects(
            [['38-42']],
            [['46-50']],
            [WATER],
        ), is_linked=(2, 'Cloudy Attack')),
        Spell('Bastion', [30, 97, 164], Effects(
            [['80', '120', '150']],
            None,
            ['buff_pow'],
        ), stacks=2),
        Spell('Backlash', [35, 102, 169], Effects(
            [['18-21', '23-27', '29-33'],
             ['40', '60', '80']],
            [['22-25', '28-32', '35-40'],
             ['60', '80', '100']],
            [EARTH, 'buff_str'],
        ), stacks=2, is_linked=(1, 'Tetany')),
        Spell('Tetany', [145], Effects(
            [['34-38']],
            [['41-46']],
            [NEUTRAL],
        ), is_linked=(2, 'Backlash')),
        Spell('Repulsion Glyph', [45, 112, 179], Effects(
            [['13-14', '17-18', '21-22']] * 4,
            None,
            [FIRE, WATER, EARTH, AIR],
        ), aggregates=[('', [0, 1, 2, 3])], special='glyph',
        is_linked=(1, 'Barrier')),
        Spell('Barrier', [155], Effects(
            [['21-22']] * 4,
            None,
            [FIRE, WATER, EARTH, AIR],
        ), aggregates=[('', [0, 1, 2, 3])], special='glyph',
        is_linked=(2, 'Repulsion Glyph')),
        Spell('Blinding Glyph', [55, 122, 189], Effects(
            [['20-22', '27-30', '31-34']],
            None,
            [EARTH],
        ), special='glyph', is_linked=(1, 'Protective Glyph')),
        Spell('Protective Glyph', [165], Effects(
            [['31-35']],
            [['37-42']],
            [EARTH],
        ), special='glyph', is_linked=(2, 'Blinding Glyph')),
        Spell('Shiver', [60, 127, 194], Effects(
            [['22-25', '27-30', '30-34']],
            [['26-30', '32-36', '36-41']],
            [AIR],
        ), is_linked=(1, 'Tension')),
        Spell('Tension', [170], Effects(
            [['38-42']],
            [['46-50']],
            [WATER],
        ), is_linked=(2, 'Shiver')),
        #TODO: find out Paralysing Glyph's damages
        Spell('Paralysing Glyph', [65, 131, 198], Effects(
            [['22-25', '27-30', '30-34']],
            None,
            [WATER],
        ), special='glyph', is_linked=(1, 'Roaming Glyph')),
        Spell('Roaming Glyph', [175], Effects(
            [['30-34']],
            [['36-41']],
            [WATER],
        ), special='glyph', is_linked=(2, 'Paralysing Glyph')),
        Spell('Torpor', [70, 137], Effects(
            [['21-23', '27-30']],
            [['25-28', '32-36']],
            [EARTH],
        ), is_linked=(1, 'Lateral Flame')),
        Spell('Lateral Flame', [180], Effects(
            [['31-35']],
            [['37-42']],
            [FIRE],
        ), is_linked=(2, 'Torpor')),
        Spell('Reinforced Protection', [75, 142], Effects(
            [['120', '200'],
             ['160', '250']],
            None,
            ['buff_pow_nonglyph', 'buff_pow_glyph'],
        )),
        Spell('Burning Glyph', [85, 152], Effects(
            [['27-30', '33-37']],
            None,
            [FIRE],
        ), special='glyph', is_linked=(1, 'Perception Glyph')),
        Spell('Perception Glyph', [195], Effects(
            [['30-34']],
            [['36-41']],
            [FIRE],
        ), special='glyph', is_linked=(2, 'Burning Glyph')),
    ],
    'Foggernaut': [
        Spell('Anchor', [1, 67, 133], Effects(
            [['14-16', '19-21', '24-27']],
            [['17-19', '22-25', '29-32']],
            [EARTH],
        ), is_linked=(1, 'Mooring')),
        Spell('Mooring', [100, 167], Effects(
            [['14-16', '17-20']],
            [['17-20', '21-25']],
            [EARTH],
        ), is_linked=(2, 'Anchor')),
        Spell('Pilfer', [1, 66, 132], Effects(
            [['13-15', '17-20', '22-25']],
            [['16-18', '21-24', '26-30']],
            [FIRE],
            steals=[True],
        ), is_linked=(1, 'Scuttle')),
        Spell('Scuttle', [95, 162], Effects(
            [['38-43', '47-54']],
            [['46-52', '57-65']],
            [FIRE],
        ), is_linked=(2, 'Pilfer')),
        Spell('Torrent', [6, 71, 138], Effects(
            [['15-19', '20-23', '25-28']],
            [['19-22', '24-27', '29-33']],
            [WATER],
        ), is_linked=(1, 'Harmattan')),
        Spell('Harmattan', [115, 182], Effects(
            [['24-27', '28-32']],
            [['29-33', '34-38']],
            [AIR],
        ), is_linked=(2, 'Torrent')),
        Spell('Scaphander', [15, 82, 149], Effects(
            [['12', '19', '25'],
             ['25', '35', '40']],
            [['16', '23', '30'],
             ['30', '40', '50']],
            ['buff_dam', 'buff_pshdam']
        )),
        Spell('Backwash', [25, 92, 159], Effects(
            [['12-15', '17-20', '22-26']],
            [['16-20', '21-25', '27-32']],
            [EARTH],
        ), is_linked=(1, 'Surge')),
        Spell('Surge', [135], Effects(
            [['30-34']],
            [['36-41']],
            [FIRE],
        ), is_linked=(2, 'Backwash')),
        Spell('Tide', [30, 97, 164], Effects(
            [['18-20', '23-26', '28-32']],
            [['21-24', '27-31', '34-38']],
            [AIR],
        ), is_linked=(1, 'Corrosion')),
        Spell('Corrosion', [140], Effects(
            [['34-38']],
            [['41-46']],
            [AIR],
        ), is_linked=(2, 'Tide')),
        Spell('Vapour', [35, 102, 169], Effects(
            [['16-18', '22-25', '28-32']],
            [['20-22', '27-31', '34-39']],
            [FIRE],
        ), is_linked=(1, 'Valve')),
        Spell('Valve', [145], Effects(
            [['18-21'],
             ['30']],
            [['22-25'],
             ['30']],
            [FIRE, 'buff_heals'],
        ), is_linked=(2, 'Vapour')),
        Spell('Spyglass', [50, 117, 184], Effects(
            [['20-22', '26-30', '31-35']],
            [['23-27', '32-36', '37-42']],
            [WATER],
        ), is_linked=(1, 'Periscope')),
        Spell('Periscope 2', [160], Effects(
            [['30-34']],
            [['36-41']],
            [WATER],
        ), is_linked=(2, 'Periscope 1')),
        Spell('First Aid', [55, 122, 189], Effects(
            [['18-21', '22-26', '25-29']],
            [['22-25', '27-31', '30-35']],
            [FIRE],
            heals=[True]
        ), is_linked=(1, 'Rescue')),
        Spell('Rescue', [165], Effects(
            [['23-25']],
            [['27-30']],
            [FIRE],
            heals=[True]
        ), is_linked=(2, 'First Aid')),
        Spell('Torpedo', [60, 127, 194], Effects(
            [['18-21', '22-26', '25-29']],
            [['22-25', '27-31', '30-35']],
            [AIR],
        ), is_linked=(1, 'Short-Circuit')),
        Spell('Short-Circuit', [170], Effects(
            [['38-42']],
            [['44-49']],
            [AIR],
        ), is_linked=(2, 'Torpedo')),
        Spell('Ambush ', [65, 131, 198], Effects(
            [['7-9', '9-11', '10-12']] * 4,
            [['9-11', '11-13', '12-14']] * 4,
            [FIRE, WATER, EARTH, AIR],
         ), aggregates=[('', [0, 1, 2, 3])]),
        Spell('Froth', [80, 147], Effects(
            [['30-34', '38-43']],
            [['36-40', '45-51']],
            [WATER],
        ), is_linked=(1, 'Nautilus')),
        Spell('Nautilus', [190], Effects(
            [['23-27']],
            [['28-32']],
            [WATER],
        ), is_linked=(2, 'Froth')),
        Spell('Trident', [85, 152], Effects(
            [['25-28', '31-35'],
             ['9-11', '13-15']],
            [['30-34', '37-42'],
             ['9-11', '13-15']],
            [EARTH, EARTH],
         ), aggregates=[('Hit', [0]),
                        ('Pushback Poison', [1])],
        is_linked=(1, 'Seizing')),
        Spell('Seizing', [195], Effects(
            [['32-36']],
            [['38-43']],
            [EARTH],
        ), is_linked=(2, 'Trident')),
    ],
    'Iop': [
        Spell('Pressure', [1, 66, 132], Effects(
            [['16-18', '20-23', '26-30']],
            [['19-21', '24-28', '31-36']],
            [EARTH],
        ), is_linked=(1, 'Fracture')),
        Spell('Fracture', [95, 162], Effects(
            [['26-29', '32-36']],
            [['31-35', '38-43']],
            [AIR],
        ), is_linked=(2, 'Pressure')),
        Spell('Outpouring', [1, 68, 134], Effects(
            [['23-25', '30-33', '38-42']],
            [['27-30', '36-39', '46-50']],
            [WATER],
        ), is_linked=(1, 'Destructive Ring')),
        Spell('Destructive Ring', [105, 172], Effects(
            [['19-23', '24-28']],
            [['23-27', '29-34']],
            [AIR],
        ), is_linked=(2, 'Outpouring')),
        Spell('Divine Sword', [3, 69, 136], Effects(
            [['16-18', '20-23', '26-30'],
             ['10', '20', '30']],
            [['19-21', '24-28', '31-36'],
             ['10', '20', '30']],
            [AIR, 'buff_dam'],
        ), is_linked=(1, 'Chopper')),
        Spell('Chopper', [110, 177], Effects(
            [['19-22', '23-27']],
            [['22-26', '28-32']],
            [FIRE],
        ), is_linked=(2, 'Divine Sword')),
        Spell('Destructive Sword', [6, 71, 138], Effects(
            [['19-22', '26-29', '32-36']],
            [['23-26', '31-35', '38-43']],
            [FIRE],
        ), is_linked=(1, 'Accumulation')),
        Spell('Accumulation', [115, 182], Effects(
            create_level_based_stacking_values(((19, 22), (22, 26),), (20, 24), 2),
            create_level_based_stacking_values(((22, 27), (26, 31),), (24, 24), 2),
            [EARTH]*2,
        ), aggregates=[(CHARGED_LABELS[n], [n]) for n in range(2)],
        is_linked=(2, 'Destructive Sword')),
        Spell('Intimidation', [10, 77, 144], Effects(
            [['6', '8', '10']] * 5,
            [['7', '10', '12']] * 5,
            [NEUTRAL, EARTH, FIRE, WATER, AIR],
        ), aggregates=[('Hit in best element', [0]),
                        ('', [1]),
                        ('', [2]),
                        ('', [3]),
                        ('', [4])],),
        Spell('Violence', [125, 192], Effects(
            [['40', '50']],
            None,
            ['buff_pshdam'],
        ), stacks=4,),        
        Spell('Concentration', [25, 92, 159], Effects(
            [['19-21', '24-27', '30-34'],
             ['13-15', '16-19', '20-24']],
            [['23-26', '29-33', '36-41'],
             ['15-18', '19-23', '24-29']],
            [EARTH, EARTH],
        ), aggregates=[('Summons', [0]),
                        ('Others', [1])],
        is_linked=(1, 'Sword of Judgement')),
        Spell('Sword of Judgement', [135], Effects(
            [['31-35'],
             ['48-52']],
            [['37-42'],
             ['58-62']],
            [WATER, WATER],
        ), aggregates=[('', [0]),
                       ('In 2 turns', [1])],
        is_linked=(2, 'Concentration')),
        Spell('Fervour', [30, 97, 164], Effects(
            [['15-17', '19-22','24-27']],
            [['18-20', '23-26','29-32']],
            [WATER],
        ), is_linked=(1, 'Threat')),
        Spell('Threat', [140], Effects(
            [['26-28']],
            [['31-34']],
            [WATER],
        ), is_linked=(2, 'Fervour')),
        Spell('Strengthstorm', [45, 112, 179], Effects(
            [['17-20', '22-26', '27-31'],
             ['17-20', '22-26', '27-31'],
             ['17-20', '22-26', '27-31'],
             ['17-20', '22-26', '27-31'],
             ['21-25', '31-35', '41-45']],
            [['20-23', '27-31', '32-37'],
             ['20-23', '27-31', '32-37'],
             ['20-23', '27-31', '32-37'],
             ['20-23', '27-31', '32-37'],
             ['21-25', '31-35', '41-45']],
            [FIRE] * 5,
        ), aggregates=[('First target', [0]),
                       ('Second target not charged', [1, 2]),
                       ('Second target charged', [3, 4])],
        is_linked=(1, 'Tumult')),
        Spell('Tumult', [155], Effects(
            create_stacking_values(((19, 21),), 20, 5),
            create_stacking_values(((23, 25),), 20, 5),
            [FIRE] * 5,
        ), aggregates=[(str(n+1) + " targets", [n]) for n in range(5)],
        is_linked=(2, 'Strengthstorm')),
        Spell('Celestial Sword', [50, 117, 184], Effects(
            [['28-31', '31-35', '36-40']],
            [['34-37', '38-42', '43-48']],
            [AIR],
        ), is_linked=(1, 'Zenith')),
        Spell('Zenith', [160], Effects(
            [['27-29'], 
             ['52-58']],
            [['31-35'],
             ['64-70']],
            [AIR] * 2,
        ), aggregates=[('', [0, 1])],
        is_linked=(2, 'Celestial Sword')),
        Spell('Power', [55, 122, 189], Effects(
            [['100', '200', '300']],
            [['120', '240', '350']],
            ['buff_pow']
        ),),
        Spell('Endurance', [65, 131, 198], Effects(
            [['22-25', '27-30', '30-34']],
            [['27-30', '32-36', '36-41']],
            [WATER],
        ), is_linked=(1, 'Castigation')),
        Spell('Castigation', [175], Effects(
            [['34-38']],
            [['41-46']],
            [WATER],
        ), is_linked=(2, 'Endurance')),
        Spell('Sword of Iop', [70, 137], Effects(
            [['30-33', '37-41']],
            [['36-39', '44-49']],
            [EARTH],
        ), is_linked=(1, 'Pygmachia')),
        Spell('Pygmachia', [180], Effects(
            create_stacking_values(((9, 11),), 18, 4),
            create_stacking_values(((11, 13),), 18, 4),
            [EARTH]*4,
        ), aggregates=[(CHARGED_LABELS[n], [n]) for n in range(4)],
        is_linked=(2, 'Sword of Iop')),
        Spell('Sword of Fate', [80, 147], Effects(
            [['31-34', '38-42'],
             ['61-64', '78-82']],
            [['37-40', '46-50'],
             ['67-70', '86-90']],
            [FIRE, FIRE],
         ), aggregates=[('Not Charged', [0]),
                        ('Charged', [1])],
        is_linked=(1, 'Pounding')),
        Spell('Pounding', [190], Effects(
            [['30-34']],
            [['36-41']],
            [AIR],
        ), is_linked=(2, 'Sword of Fate')),
        Spell('Cleaver', [85, 152], Effects(
            [['40-45', '47-53']],
            [['48-54', '56-64']],
            [WATER],
        ), is_linked=(1, 'Sentence')),
        Spell('Sentence', [195], Effects(
            [['13-16'],
             ['26-30']],
            [['16-19'],
             ['32-36']],
            [FIRE, FIRE],
        ), aggregates=[('Target', [0]),
                        ('Enemies near target', [1])]
        , is_linked=(2, 'Cleaver')),
        Spell('Fit of Rage', [90, 157], Effects(
            create_stacking_values(((23, 25), (28, 32),), 20, 3),
            create_stacking_values(((27, 29), (34, 38),), 20, 3),
            [EARTH] * 3,
        ), aggregates=[(CHARGED_LABELS[n], [n]) for n in range(3)],
        is_linked=(1, 'Iop\'s Wrath')),
        Spell('Iop\'s Wrath', [200], Effects(
            [['81-100'],
             ['191-210']],
            [['97-120'],
             ['207-230']],
            [EARTH] * 2,
        ), aggregates=[('Not Charged', [0]),
                        ('Charged', [1])],
        is_linked=(2, 'Fit of Rage')), 
    ],
    'Masqueraider': [
        Spell('Brincaderia', [1, 67, 133], Effects(
            [['7-9', '10-12', '13-15']],
            [['10-12', '13-15', '16-18']],
            [FIRE],
        ), is_linked=(1, 'Picada')),
        Spell('Picada', [100, 167], Effects(
            [['20-22', '25-28']],
            [['23-26', '30-33']],
            [AIR],
        ), is_linked=(2, 'Brincaderia')),
        Spell('Catalepsy', [3, 69, 136], Effects(
            [['13-15', '18-20', '23-25']],
            [['16-18', '22-24', '28-30']],
            [EARTH],
            steals=[True],
        ), is_linked=(1, 'Decoy')),
        Spell('Decoy', [110, 177], Effects(
            [['20-23', '24-28']],
            [['24-28', '29-33']],
            [FIRE],
            steals=[True],
        ), is_linked=(2, 'Catalepsy')),
        Spell('Capering', [10, 77, 144], Effects(
            [['18-20', '23-26', '28-32']],
            [['21-24', '27-31', '34-38']],
            [AIR],
        ), is_linked=(1, 'Purgatorio')),
        Spell('Purgatorio', [120, 187], Effects(
            [['29-32', '32-36']],
            [['34-39', '38-43']],
            [FIRE],
        ), is_linked=(2, 'Capering')),
        Spell('Shove Off', [15, 82, 149], Effects(
            [['6-7', '7-8', '8-9']] * 4,
            [['8-9', '9-10', '10-11']] * 4,
            [AIR, WATER, EARTH, FIRE],
         ), aggregates=[('', [0, 1, 2, 3])]),
         Spell('Parafuso', [20, 87, 154], Effects(
            [['13-15', '17-19', '21-24']],
            [['16-18', '20-23', '25-29']],
            [WATER],
            steals=[True],
        ), is_linked=(1, 'Martelo')),
         Spell('Martelo', [130, 197], Effects(
            [['20-22', '22-25']],
            [['24-27', '26-30']],
            [EARTH]
        ), is_linked=(2, 'Parafuso')),
        Spell('Inferno', [35, 102, 169], Effects(
            [['24-27', '31-34', '38-42'],
             ['100', '150', '200']],
            [['29-32', '37-40', '46-50'],
             ['100', '150', '200']],
            [FIRE, 'buff_pow'],
        ), is_linked=(1, 'Distance')),
        Spell('Distance', [145], Effects(
            [['24-26']],
            [['29-31']],
            [WATER],
        ), is_linked=(2, 'Inferno')),
        Spell('Furia', [50, 117, 184], Effects(
            [['21-23', '28-31', '35-39'],
             ['20', '30', '40']],
            [['25-28', '34-38', '42-47'],
             ['20', '30', '40']],
            [EARTH, 'buff_dam'],
        ), is_linked=(1, 'Bocciara')),
        Spell('Bocciara', [160], Effects(
            [['16-19'],
             ['80']],
            [['20-24'],
             ['80']],
            [WATER, 'buff_pshdam'],
        ), is_linked=(2, 'Furia')),
        Spell('Ponteira', [60, 127, 194], Effects(
            [['12-15', '15-18', '20-23']],
            [['16-19', '19-22', '24-28']],
            [WATER],
        ), is_linked=(1, 'Agular')),
        Spell('Agular', [170], Effects(
            [['30-34']],
            [['36-41']],
            [AIR],
        ), is_linked=(2, 'Picada')),
        Spell('Neurosis', [175], Effects(
            [['200']],
            None,
            ['buff_pow'],
        )),
        Spell('Cavalcade', [70, 137], Effects(
            [['31-34', '38-42']],
            [['37-40', '46-50']],
            [AIR],
        ), is_linked=(1, 'Apostasy')),
        Spell('Apostasy', [180], Effects(
            [['25-28']],
            [['30-34']],
            [FIRE],
        ), is_linked=(2, 'Cavalcade')),
        Spell('Apathy', [80, 147], Effects(
            [['23-26', '28-32']],
            [['27-31', '34-38']],
            [EARTH],
        ), is_linked=(1, 'Retention')),
        Spell('Retention', [190], Effects(
            [['27-31']],
            [['33-37']],
            [AIR],
            steals=[True],
        ), is_linked=(1, 'Estrelia')),
        Spell('Boliche', [85, 152], Effects(
            [['21-23', '26-28']],
            [['25-27', '31-34']],
            [WATER],
        ), is_linked=(1, 'Ronda')),
        Spell('Ronda', [195], Effects(
            [['38-42']],
            [['46-50']],
            [EARTH],
        ), is_linked=(2, 'Boliche')),   
    ],
    'Osamodas': [
        Spell('Dragonic', [1, 66, 132], Effects(
            [['13-15', '17-20', '22-25']] * 2,
            [['16-18', '21-24', '27-30']] * 2,
            [FIRE] * 2, heals=[True, False],
        ), aggregates=[('Allies', [0]),
                       ('Enemies', [1])],
        is_linked=(1, 'Sparkmeleon')),
        Spell('Sparkmeleon', [95, 162], Effects(
            [['21-23', '26-29']] * 2,
            [['25-28', '31-35']] * 2,
            [FIRE] * 2, heals=[False, True],
        ), aggregates=[('Enemies', [0]), 
                       ('Allies', [1])],
        is_linked=(2, 'Dragonic')),
        Spell('Geyser', [1, 67, 133], Effects(
            [['15-17', '20-22', '25-28']],
            [['18-20', '23-26', '30-33']],
            [WATER]
        ), is_linked=(1, 'Aquaculture')),
        Spell('Aquaculture', [100, 167], Effects(
            [['25-28', '28-31'],
             ['100', '150']],
            [['30-34', '33-37'],
             ['100', '150']],
            [WATER, 'buff_pow'],
        ), is_linked=(2, 'Geyser')),
        Spell('Canine', [3, 69, 136], Effects(
            [['12-14', '16-19', '21-24']],
            [['15-17', '20-22', '25-29']],
            [AIR],
        ), is_linked=(1, 'Gambol')),
        Spell('Gambol', [110, 177], Effects(
            [['15-17', '19-21']],
            [['18-20', '23-25']],
            [AIR],
        ), is_linked=(2, 'Canine')),
        Spell('Fossil', [6, 71, 138], Effects(
            [['13-15', '18-20', '23-25']],
            [['16-18', '22-24', '28-30']],
            [EARTH],
        ), is_linked=(1, 'Sedimentation')),
        Spell('Sedimentation', [115, 182], Effects(
            [['32-36', '38-42']],
            [['39-43', '46-50']],
            [EARTH],
        ), is_linked=(2, 'Aquatic Wave')),
        Spell('Scalding Poison', [20, 87, 154], Effects(
            [['11-13', '13-15', '15-17']],
            None,
            [WATER],
        ), is_linked=(1, 'Aquatic Wave')),
        Spell('Aquatic Wave', [130, 197], Effects(
            [['19-22', '25-29']],
            [['24-27', '31-35']],
            [WATER],
        ), is_linked=(2, 'Scalding Poison')),
        Spell('Flaming Crow', [25, 92, 159], Effects(
            [['4-6', '6-8', '8-10'],
            ['4-6', '6-8', '8-10'],
            ['7-15', '11-19', '15-23'],
            ['7-15', '11-19', '15-23'],
            ['10-24', '16-30', '22-36'],
            ['10-24', '16-30', '22-36']],
            [['7-9', '9-11', '11-13'],
             ['7-9', '9-11', '11-13'],
            ['12-20', '16-24', '20-28'],
            ['12-20', '16-24', '20-28'],
            ['17-31', '23-37', '29-41'],
            ['17-31', '23-37', '29-41']],
            [FIRE] * 6, heals=[False, True, False, True, False, True],
        ), aggregates=[('Not charged:<br>Enemies', [0]),
                    ('Allies', [1]),
                    ('Charged once:<br>Enemies', [2]),
                    ('Allies', [3]),
                    ('Charged twice:<br>Enemies', [4]),
                    ('Allies', [5])],
        is_linked=(1, 'Cross Scale')),
        Spell('Cross Scale', [135], Effects(
            [['33-36']] * 2,
            [['38-42']] * 2,
            [FIRE] * 2,
        ), aggregates=[('Allies', [0]),
                       ('Enemies', [1])],
        is_linked=(2, 'Flaming Crow')),
        Spell('Repulsive Fang', [35, 102, 169], Effects(
            [['11-13', '13-15', '15-17']],
            [['14-16', '16-18', '18-21']],
            [AIR],
        ), is_linked=(1, 'Takeoff')),
        Spell('Takeoff', [145], Effects(
            [['33-37']],
            [['38-43']],
            [AIR],
        ), is_linked=(2, 'Repulsive Fang')),
        Spell('Woolly Sledgehammer', [40, 107, 174], Effects(
            [['13-15', '16-18', '18-20']],
            [['16-18', '19-21', '21-23']],
            [EARTH],
        ), is_linked=(1, 'Gobball Fleece')),
        Spell('Gobball Fleece', [150], Effects(
            [['32-36']],
            [['38-43']],
            [EARTH],
        ), is_linked=(2, 'Woolly Sledgehammer')),
        Spell('Duster', [50, 117, 184], Effects(
            create_level_based_stacking_values(((21, 24), (24, 27), (29, 33)), (3, 4, 5), 6),
            create_level_based_stacking_values(((25, 28), (29, 32), (35, 40)), (3, 4, 5), 6),
            [AIR, AIR, AIR, AIR, AIR, AIR]
        ), aggregates=[('No Tofus', [0]),
                       ('One Tofu', [1]),
                       ('Two Tofus', [2]),
                       ('Three Tofus', [3]),
                       ('Four Tofus', [4]),
                       ('Five Tofus', [5])],
        is_linked=(1, 'Dragon Heart')),
        Spell('Dragon Heart', [160], Effects(
            [['22-24'],
             ['11-12'],
             ['22-24']],
            None,
            [FIRE] * 3, heals=[True, True, False],
        ), aggregates=[('Allies', [0]),
                       ('Caster', [1]),
                       ('Enemies', [2])],
        is_linked=(2, 'Duster')),
        Spell('Dragon\'s Breath', [55, 122, 189], Effects(
            [['20-23', '27-31', '31-35']] * 2,
            [['24-27', '32-37', '37-42']] * 2,
            [FIRE] * 2, heals=[False, True],
        ), aggregates=[('Enemies', [0]),
                       ('Allies', [1])],
        is_linked=(1, 'Constriction')),
        Spell('Constriction', [165], Effects(
            [['25-28']],
            [['30-33']],
            [EARTH],
            steals=[True],
        ), is_linked=(2, 'Dragon\'s Breath')),
        Spell('Crackler Punch', [65, 131, 198], Effects(
            [['24-27', '31-35', '39-44']],
            [['29-32', '37-41', '47-52']],
            [EARTH],
        ), is_linked=(1, 'Batra')),
        Spell('Batra', [175], Effects(
            [['27-30'],
             ['9-10']],
            [['32-35'],
             ['11-12']],
            [WATER] * 2,
        ), aggregates=[('', [0, 1])],
        is_linked=(2, 'Crackler Punch')),
        Spell('Whirlwind', [70, 134], Effects(
            [['23-26', '29-32']],
            [['28-31', '35-38']],
            [WATER],
        ), is_linked=(1, 'Plucking')),
        Spell('Plucking', [180], Effects(
            [['23-26']],
            [['28-31']],
            [AIR],
        ), is_linked=(2, 'Duster')),
        Spell('Animal Tandem', [80, 147], Effects(
            [['110', '150']],
            None,
            ['buff_pow'],
        )),    
    ],
    'Pandawa': [
        Spell('Explosive Palm', [1, 68, 134], Effects(
            create_level_based_stacking_values(((12, 14), (15, 17), (20, 22)), (6, 8, 12), 2),
            create_level_based_stacking_values(((14, 16), (19, 21), (24, 26)), (6, 8, 12), 2),
            [FIRE] * 2,
        ), aggregates=[(CHARGED_LABELS[n], [n]) for n in range(2)],
        is_linked=(1, 'Distillation')),
        Spell('Distillation', [105, 172], Effects(
            [['8-10', '10-12'],
             ['10-13', '13-16'],
             ['14-17', '17-21'],
             ['26-29', '32-36']],
            [['10-12', '12-14'],
             ['12-15', '16-19'],
             ['16-20', '20-25'],
             ['31-35', '38-43']],
            [WATER] * 4,
        ), aggregates=[('Sober', [0, 1, 2]),
                       ('Drunk', [3])],
        is_linked=(2, 'Explosive Palm')),
        Spell('Hangover', [1, 67, 133], Effects(
            create_level_based_stacking_values(((14, 16), (19, 22), (24, 27)), (4, 6, 10), 2),
            create_level_based_stacking_values(((17, 19), (22, 25), (29, 32)), (4, 6, 10), 2),
            [EARTH]*2,
        ), aggregates=[(CHARGED_LABELS[n], [n]) for n in range(2)],
        is_linked=(1, 'Fiery Breath')),
        Spell('Fiery Breath', [100, 167], Effects(
            [['31-34', '38-42']],
            [['37-40', '46-50']],
            [FIRE],
        ), is_linked=(2, 'Hangover')),
        Spell('Schnaps', [6, 71, 138], Effects(
            [['12-14', '17-19', '21-24']],
            [['15-17', '20-23', '25-29']],
            [AIR],
        ), is_linked=(1, 'Debauchery')),
        Spell('Debauchery', [115, 182], Effects(
            [['17-19', '20-22']],
            [['20-22', '24-26']],
            [EARTH],
        ), is_linked=(2, 'Schnaps')),
        Spell('Tipple', [10, 77, 144], Effects(
            [['15-17', '20-23', '25-28']],
            [['18-22', '24-27', '30-34']],
            [WATER],
        ), is_linked=(1, 'Numbness')),
        Spell('Numbness', [120, 187], Effects(
            [['31-34', '36-40']],
            [['37-41', '43-48']],
            [AIR],
        ), is_linked=(2, 'Tipple')),
        Spell('Stretcher', [20, 87, 154], Effects(
            [['18-20', '23-26', '28-32']],
            [['21-24', '27-31', '34-38']],
            [EARTH],
        ), is_linked=(1, 'Alcoshu')),
        Spell('Alcoshu', [130, 197], Effects(
            [['10-12', '11-13']],
            [['12-14', '13-16']],
            [WATER], steals=[True],
        ), is_linked=(2, 'Stretcher')),
        Spell('Pandilongation', [25, 92, 159], Effects(
            [['18-20', '23-25', '28-31']],
            [['21-23', '27-30', '34-37']],
            [FIRE],
        ), is_linked=(1, 'Liqueur')),
        Spell('Liqueur', [135], Effects(
            [['22-25']],
            [['26-30']],
            [AIR],
            steals=[True],
        ), is_linked=(2, 'Pandilongation')),
        Spell('Inebriation', [30, 97, 164], Effects(
            [['50', '50', '50']] + [['8', '10', '12']] * 5,
            None,
            ['buff_pow', NEUTRAL, EARTH, FIRE, WATER, AIR],
        ), aggregates=[('', [0]),
                        ('Hit in best element', [1]),
                        ('', [2]),
                        ('', [3]),
                        ('', [4]),
                        ('', [5])]),
        Spell('Propulsion', [40, 107, 174], Effects(
            [['21-23', '27-30', '33-37']],
            [['25-28', '32-36', '40-44']],
            [AIR],
        ), is_linked=(1, 'Absinthe')),
        Spell('Absinthe', [150], Effects(
            [['12-15']],
            [['14-18']],
            [FIRE], steals=[True],
        ), is_linked=(2, 'Propulsion')),
        Spell('Brandy', [45, 112, 179], Effects(
            [['16-18', '22-24', '26-29']],
            [['20-22', '26-28', '31-35']],
            [WATER],
        ), is_linked=(1, 'Filthipint')),
        Spell('Filthipint', [155], Effects(
            [['34-38']],
            [['41-46']],
            [EARTH],
            steals=[True],
        ), is_linked=(2, 'Brandy')),
        Spell('Eviction', [60, 127, 194], Effects(
            [['11-13', '13-15', '15-17']],
            [['13-15', '16-18', '18-20']],
            [EARTH],
        ), is_linked=(1, 'Nausea')),
        Spell('Nausea', [170], Effects(
            [['15-17'],
             ['19-21']],
            [['18-20'],
             ['22-24']],
            [AIR] * 2,
        ), aggregates=[('Sober', [0]),
                       ('Drunk', [1])], 
        is_linked=(2, 'Eviction')),
        Spell('Explosive Flask', [65, 131, 198], Effects(
            [['13-15', '16-18', '18-20'],
             ['16-19', '20-22', '22-25']],
            [['16-18', '19-21', '22-24'],
             ['20-22', '24-27', '26-30']],
            [FIRE] * 2,
        ), aggregates=[('Sober', [0]),
                        ('Drunk', [1])],
        is_linked=(1, 'Pandatak')),
        Spell('Pandatak', [175], Effects(
            [['38-42'],
             ['46-50']],
            [['46-50'],
             ['54-58']],
            [EARTH] * 2,
        ), aggregates=[('Sober', [0]),
                        ('Drunk', [1])],
        is_linked=(2, 'Explosive Flask')),
        Spell('Alcoholic Breath', [75, 142], Effects(
            [['23-26', '28-32']],
            [['27-31', '34-38']],
            [AIR],
        ), is_linked=(1, 'Waterfall')),
        Spell('Waterfall', [185], Effects(
            [['24-28']],
            [['29-34']],
            [WATER],
        ), is_linked=(2, 'Alcoholic Breath')),
        Spell('Melancholy', [80, 147], Effects(
            [['29-32', '36-40'],
             ['35-38', '41-45']],
            [['35-39', '43-48'],
             ['44-48', '51-556']],
            [WATER] * 2,
        ), aggregates=[('Sober', [0]),
                       ('Drunk', [1])],
        is_linked=(1, 'Pandjiu')),
        Spell('Pandjiu', [190], Effects(
            [['28-32']],
            [['34-38']],
            [FIRE],
        ), is_linked=(2, 'Melancholy')),
        Spell('Pandawa\'s Hand', [200], Effects(
            [['50']] * 5 + [['5']] * 5,
            [['100']] * 5 + [['10']] * 5,
            [NEUTRAL, EARTH, FIRE, WATER, AIR] * 2,
        ), aggregates=[('Sober:<br>Hit in best element', [0]),
                        ('', [1]),
                        ('', [2]),
                        ('', [3]),
                        ('', [4]),
                        ('Drunk', [5, 6, 7, 8, 9])]), 
    ],
    'Rogue': [
        Spell('Explobomb', [1, 67, 133], Effects(
            [['9-10', '13-14', '17-19'],
             ['21-24', '24-27', '30-33'],
             ['11-12', '12-14', '15-17']],
            None,
            [FIRE] * 3,
        ), aggregates=[('Explosion', [0]),
                        ('Wall during caster turn', [1]),
                        ('Wall after caster turn', [2])],
        is_linked=(1, 'Resilient Explobomb')),
        Spell('Resilient Explobomb', [100, 167], Effects(
            [['13-14', '17-19'],
             ['24-27', '30-33'],
             ['12-14', '15-17']],
            None,
            [FIRE] * 3,
        ), aggregates=[('Explosion', [0]),
                        ('Wall during caster turn', [1]),
                        ('Wall after caster turn', [2])],
        is_linked=(2, 'Explobomb')),
        Spell('Grenado', [1, 68, 134], Effects(
            [['9-10', '13-14', '17-19'],
             ['15-18', '18-21', '24-27'],
             ['8-9', '9-10', '12-14']],
            None,
            [AIR] * 3,
        ), aggregates=[('Explosion', [0]),
                        ('Wall during caster turn', [1]),
                        ('Wall after caster turn', [2])],
        is_linked=(1, 'Resilient Grenado')),
        Spell('Resilient Grenado', [105, 172], Effects(
            [['13-14', '17-19'],
             ['18-21', '24-27'],
             ['9-10', '12-14']],
            None,
            [AIR] * 3,
        ), aggregates=[('Explosion', [0]),
                        ('Wall during caster turn', [1]),
                        ('Wall after caster turn', [2])],
        is_linked=(2, 'Grenado')),
        Spell('Pulsar', [6, 71, 138], Effects(
            [['13-15', '18-20', '23-25']],
            [['16-18', '22-24', '28-30']],
            [FIRE],
        ), is_linked=(1, 'Shrapnel')),
        Spell('Shrapnel', [115, 182], Effects(
            [['14-16', '17-19']],
            [['17-19', '20-23']],
            [WATER],
        ), is_linked=(2, 'Pulsar')),
        Spell('Carbine', [15, 82, 149], Effects(
            [['14-16', '18-20', '23-25']],
            [['17-19', '22-24', '28-30']],
            [AIR],
        ), is_linked=(1, 'Obliteration')),
        Spell('Obliteration', [125, 192], Effects(
            create_level_based_stacking_values(((29, 32), (33, 37)), (7, 10), 6),
            create_level_based_stacking_values(((35, 39), (40, 44)), (7, 10), 6),
            [EARTH] * 6,
        ), aggregates=[(BOMB_LABELS[n], [n]) for n in range(6)],
        is_linked=(2, 'Carbine')),
        Spell('Seismobomb', [25, 92, 159], Effects(
            [['12-13', '16-17', '20-22'],
             ['15-18', '18-21', '24-27'],
             ['8-9', '9-10', '12-14']],
            None,
            [EARTH] * 3,
        ), aggregates=[('Explosion', [0]),
                        ('Wall during caster turn', [1]),
                        ('Wall after caster turn', [2])],
        is_linked=(1, 'Resilient Seismobomb')),
        Spell('Resilient Seismobomb', [135], Effects(
            [['20-22'],
             ['24-27'],
             ['12-14']],
            None,
            [EARTH] * 3,
        ), aggregates=[('Explosion', [0]),
                        ('Wall during caster turn', [1]),
                        ('Wall after caster turn', [2])],
        is_linked=(2, 'Seismobomb')),
        Spell('Water Bomb', [30, 97, 164], Effects(
            [['9-10', '13-14', '17-19'],
             ['15-18', '18-21', '24-27'],
             ['8-9', '9-10', '12-14']],
            None,
            [WATER] * 3,
        ), aggregates=[('Explosion', [0]),
                        ('Wall during caster turn', [1]),
                        ('Wall after caster turn', [2])],
        is_linked=(1, 'Resilient Water Bomb')),
        Spell('Resilient Water Bomb', [140], Effects(
            [['17-19'],
             ['24-27'],
             ['12-14']],
            None,
            [WATER] * 3,
        ), aggregates=[('Explosion', [0]),
                        ('Wall during caster turn', [1]),
                        ('Wall after caster turn', [2])],
        is_linked=(2, 'Water Bomb')),
        Spell('Bombard', [40, 107, 174], Effects(
            [['14-16', '18-20', '23-25']],
            [['17-19', '22-24', '28-30']],
            [EARTH],
        ), is_linked=(1, 'Machine Gun')),
        Spell('Machine Gun', [150], Effects(
            [['34-38']],
            [['41-46']],
            [AIR],
        ), is_linked=(2, 'Bombard')),
        Spell('Stolen Goods', [45, 112, 179], Effects(
            [['17-19', '23-25', '28-30']],
            [['21-23', '28-30', '34-36']],
            [WATER],
        ), is_linked=(1, 'Weigh Down')),
        Spell('Weigh Down', [155], Effects(
            [['30-34']],
            [['37-42']],
            [FIRE],
        ), is_linked=(2, 'Stolen Goods')),
        Spell('Extraction', [55, 122, 184], Effects(
            [['16-18', '22-24', '28-30'],
             ['8-9', '11-12', '14-15']],
            [['20-22', '26-28', '32-36'],
             ['10-11', '13-14', '16-18']],
            [FIRE] * 2,
            steals=[True, True],
        ), aggregates=[('Enemies', [0]),
                        ('Allies', [1])],
        is_linked=(1, 'Cadence')),
        Spell('Cadence', [165], Effects(
            [['26-28']],
            [['31-34']],
            [AIR],
        ), is_linked=(2, 'Extraction')),
        Spell('Boomerang Daggers', [65, 131, 198], Effects(
            [['12-14', '14-16', '16-18']] * 2,
            [['14-16', '17-19', '19-21']] * 2,
            [AIR, AIR],
        ), aggregates=[('', [0, 1])],
        is_linked=(1, 'Blunderbuss')),
        Spell('Blunderbuss', [175], Effects(
            [['35-39']],
            [['42-47']],
            [WATER],
        ), is_linked=(2, 'Boomerang Daggers')),
        Spell('Sticky Bomb', [180], Effects(
            [['19']] * 4,
            None,
            [EARTH, FIRE, WATER, AIR],
        ), aggregates=[('Hit in best element', [0]),
                        ('', [1]),
                        ('', [2]),
                        ('', [3])]),
        Spell('Musket', [75, 142], Effects(
            [['15-17', '19-21']],
            [['18-20', '23-25']],
            [EARTH],
        ), is_linked=(1, 'Shot Pellets')),
        Spell('Shot Pellets', [185], Effects(
            [['30-34'],
             ['15-17']],
            [['34-40'],
             ['18-20']],
            [FIRE] * 2, steals=[True, True],
        ), aggregates=[('Enemies', [0]),
                        ('Allies', [1])],
        is_linked=(2, 'Musket')),
        Spell('Deception', [85, 152], Effects(
            [['27-30', '33-37']],
            [['32-36', '40-44']],
            [WATER],
        ), is_linked=(1, 'Arquebus')),
        Spell('Arquebus', [190], Effects(
            [['35-39']],
            [['42-47']],
            [EARTH],
        ), is_linked=(2, 'Deception')),  
    ],
    'Sacrier': [
        Spell('Hemorrhage', [1, 66, 132], Effects(
            [['13-16', '17-20', '22-26']],
            [['16-19', '21-24', '26-31']],
            [AIR],
            steals=[True],
        ), is_linked=(1, 'Desolation')),
        Spell('Desolation', [95, 162], Effects(
            [['21-24', '26-30']],
            [['25-29', '31-36']],
            [AIR],
            steals=[True],
        ), is_linked=(2, 'Hemorrhage')), 
        Spell('Nervousness', [1, 67, 133], Effects(
            [['13-14', '16-18', '21-23'],
             ['21-23', '27-30', '35-39']],
            [['15-17', '20-22', '25-28'],
             ['25-28', '33-36', '42-47']],
            [[WATER]] * 2
        ), aggregates=[('Suffering 1', [0]),
                       ('Suffering 10', [1])],
        is_linked=(1, 'Immolation')),
        Spell('Immolation', [100, 167], Effects(
            [['34-37', '40-44']],
            [['41-45', '48-53']],
            [[FIRE]],
        ), is_linked=(2, 'Nervousness')),
        Spell('Torture', [3, 69, 136], Effects(
            [['13-16', '17-20', '22-26']],
            [['16-19', '21-24', '26-31']],
            [EARTH],
            steals=[True],
        ), is_linked=(1, 'Blood Bath')),
        Spell('Blood Bath', [110, 177], Effects(
            [['21-24', '27-31']],
            [['25-29', '32-37']],
            [EARTH],
            steals=[True],
        ), is_linked=(2, 'Torture')),
        Spell('Excruciating Pain', [6, 71, 138], Effects(
            [['12-14', '16-18', '20-23'],
             ['20-23', '27-31', '34-38']],
            [['15-16', '20-22', '24-27'],
             ['24-27', '33-37', '41-46']],
            [FIRE] * 2,
        ), aggregates=[('Suffering 1', [0]),
                        ('Suffering 10', [1])],
        is_linked=(1, 'Clobbering')),
        Spell('Clobbering', [115, 182], Effects(
            [['31-35', '39-43']],
            [['38-41', '47-52']],
            [WATER],
        ), is_linked=(2, 'Excruciating Pain')),
        Spell('Mutilation', [10, 77, 144], Effects(
            [['50', '100', '150']],
            None,
            ['buff_pow']
        )),
        Spell('Ravages', [20, 87, 154], Effects(
            [['17-20', '22-26', '28-32']],
            [['21-24', '27-31', '34-38']],
            [EARTH]
        ), is_linked=(1, 'Light Speed')),
        Spell('Light Speed', [130, 197], Effects(
            [['20-23', '22-26']],
            [['24-28', '26-31']],
            [AIR],
        ), is_linked=(2, 'Ravages')),
        Spell('Assault', [25, 92, 159], Effects(
            [['9-11', '11-14', '14-17']],
            [['11-13', '13-16', '17-20']],
            [AIR]
        ), is_linked=(1, 'Aversion')),
        Spell('Aversion', [135], Effects(
            [['12-15']],
            [['15-18']],
            [FIRE],
        ), is_linked=(2, 'Assault')),
        Spell('Condensation', [32, 102, 169], Effects(
            [['13-16', '17-20', '21-25']],
            [['16-19', '20-24', '25-30']],
            [WATER]
        ), is_linked=(1, 'Influx')),
        Spell('Influx', [145], Effects(
            [['12-15']],
            [['15-18']],
            [EARTH],
        ), is_linked=(2, 'Condensation')),
        Spell('Hostility', [40, 107, 174], Effects(
            [['9-11', '12-14', '15-18']],
            [['11-14', '14-17', '18-22']],
            [FIRE]
        ), is_linked=(1, 'Projection')),
        Spell('Projection', [150], Effects(
            [['14-17']],
            [['17-20']],
            [WATER],
        ), is_linked=(2, 'Hostility')),
        Spell('Absorption', [55, 122, 189], Effects(
            [['13-16', '17-20', '20-24']],
            [['16-19', '20-24', '24-29']],
            [FIRE],
        ), is_linked=(1, 'Slaughter')),
        Spell('Slaughter', [165], Effects(
            [['26-30']],
            [['31-36']],
            [FIRE],
            steals=[True],
        ), is_linked=(2, 'Absorption')),
        Spell('Decimation', [60, 127, 194], Effects(
            [['16-17', '19-22', '22-24'],
             ['26-29', '32-36', '36-40']],
            [['19-21', '22-26', '26-29'],
             ['31-35', '39-43', '43-48']],
            [EARTH] * 2,
        ), aggregates=[('Suffering 1', [0]),
                        ('Suffering 10', [1])],
        is_linked=(1, 'Carnage')),
        Spell('Carnage', [170], Effects(
            [['44-48']],
            [['53-58']],
            [AIR],
            steals=[True],
        ), is_linked=(2, 'Decimation')),
        Spell('Fury', [70, 137], Effects(
            [['18-20', '23-26'],
             ['30-34', '39-43']],
            [['22-24', '28-31'],
             ['36-40', '47-52']],
            [AIR] * 2,
        ), aggregates=[('Suffering 1', [0]),
                        ('Suffering 10', [1])],
        is_linked=(1, 'Gash')),
        Spell('Gash', [180], Effects(
            [['47-51']],
            [['56-61']],
            [EARTH],
        ), is_linked=(2, 'Fury')),
        Spell('Stase', [75, 142], Effects(
            [['16-19', '20-24']],
            [['19-23', '24-29']],
            [WATER],
            steals=[True]
        ), is_linked=(1, 'Dissolution')),
        Spell('Dissolution', [185], Effects(
            [['25-29']],
            [['30-35']],
            [WATER],
            steals=[True]
        ), is_linked=(2, 'Stase')),
        Spell('Retribution', [90, 157], Effects(
            [['28', '35']] * 4,
            [['34', '42']] * 4,
            [EARTH, FIRE, WATER, AIR],
        ), aggregates=[('Hit in best element', [0]), 
                       ('', [1]),
                       ('', [2]),
                       ('', [3])],
        is_linked=(1, 'Bloodthirsty Madness')),
        Spell('Bloodthirsty Madness', [200], Effects(
            [['24-28']] * 4 + [['48-56']] * 4,
            None,
            [EARTH, FIRE, WATER, AIR] * 2, steals=[True] * 8,
        ), aggregates=[('Steals in best element', [0]),
                          ('', [1]),
                          ('', [2]),
                          ('', [3]),
                        ('Steals in best element on caster\'s Swords', [4]),
                          ('', [5]),
                          ('', [6]),
                          ('', [7])],
        is_linked=(2, 'Retribution')), 
    ],
    'Sadida': [
        Spell('Bramble', [1, 67, 133], Effects(
            [['14-16', '19-21', '24-27']],
            [['17-19', '22-25', '29-32']],
            [EARTH],
        ), is_linked=(1, 'Poisoned Undergrowth')),
        Spell('Poisoned Undergrowth', [100, 167], Effects(
            [['20-23', '24-28']],
            None,
            [EARTH],
        ), is_linked=(2, 'Bramble')),
        Spell('Prickly Embers', [3, 69, 136], Effects(
            [['14-16', '19-21', '24-27']],
            [['17-19', '22-25', '29-32']],
            [FIRE],
        ), is_linked=(1, 'Mangrove')),
        Spell('Mangrove', [110, 177], Effects(
            [['19-21', '23-26'],
             ['26-28', '32-35']],
            [['23-25', '28-31'],
             ['30-32', '37-40']],
            [FIRE] * 2,
        ), aggregates=[('', [0]),
                        ('Leafy Tree', [1])],
        is_linked=(2, 'Prickly Embers')),
        Spell('Tear', [10, 77, 144], Effects(
            [['13-15', '18-20', '22-25']],
            [['16-18', '21-24', '26-30']],
            [WATER],
        ), is_linked=(1, 'Rise of Sap')),
        Spell('Rise of Sap', [120, 187], Effects(
            [['24-38', '28-32']],
            [['29-33', '34-38']],
            [WATER],
            steals=[True],
        ), is_linked=(2, 'Tear')),
        Spell('Paralysing Poison', [15, 82, 149], Effects(
            [['13-15', '18-20', '21-23']],
            None,
            [FIRE],
        ), is_linked=(1, 'Contamination')),
        Spell('Contamination', [125, 192], Effects(
            [['9-11', '11-13']],
            None,
            [AIR],
        ), is_linked=(2, 'Paralysing Poison')),
        Spell('Soothing Bramble', [20, 87, 154], Effects(
            [['46-50', '61-65', '76-80']],
            None,
            [FIRE],
            heals=[True],
         )),
         Spell('Earthquake', [35, 102, 169], Effects(
            [['22-25', '28-31', '34-38']],
            None,
            [EARTH],
        ), is_linked=(1, 'Shake')),
        Spell('Shake', [145], Effects(
            [['32-35']],
            None,
            [AIR],
        ), is_linked=(2, 'Earthquake')),
        Spell('Natural Gift', [40, 107, 174], Effects(
            [['30', '40', '50']],
            None,
            [FIRE],
            heals=[True],
        ), is_linked=(1, 'Inoculation')),
        Spell('Inoculation', [150], Effects(
            [['38-42'],
             ['29-33']],
            [['43-47'],
             ['34-38']],
            [AIR] * 2,
        ), aggregates=[('Leafy Tree', [0]),
                       ('Infected enemy', [1])],
        is_linked=(2, 'Natural Gift')),
        Spell('Manifold Bramble', [45, 112, 179], Effects(
            [['17-19', '22-25', '27-30']],
            [['20-23', '27-30', '32-36']],
            [EARTH],
        ), is_linked=(1, 'Bane')),
        Spell('Bane', [155], Effects(
            [['27-30']],
            [['31-35']],
            [WATER], steals=[True],
        ), is_linked=(2, 'Manifold Bramble')),
        Spell('Dolly Sacrifice', [50, 117, 184], Effects(
            [['27-30', '37-41', '43-48']] * 2,
            [['33-36', '44-49', '52-58']] * 2,
            [WATER, WATER],
            steals=[False, True],
        ), aggregates=[('Enemies', [0]),
                       ('Allies/Summons', [1])],
        is_linked=(1, 'Force of Nature')),
        Spell('Force of Nature', [160], Effects(
            create_stacking_values(((21, 27),), 15, 6),
            create_stacking_values(((29, 36),), 15, 6),
            [EARTH] * 6,
        ), aggregates=[(TREE_LABELS[n], [n]) for n in range(6)],
        is_linked=(2, 'Dolly Sacrifice')),
        Spell('Aggressive Bramble', [65, 131, 198], Effects(
            [['34-37', '40-45', '45-50']],
            [['40-45', '48-54', '54-60']],
            [EARTH],
        ), is_linked=(1, 'Plaguing Bramble')),
        Spell('Plaguing Bramble', [175], Effects(
            [['23-26']],
            None,
            [FIRE],
        ), is_linked=(2, 'Aggressive Bramble')),
        Spell('Wild Grass', [70, 137], Effects(
            [['20-23', '26-29']],
            [['24-27', '31-35']],
            [FIRE],
        ), is_linked=(1, 'Contagion')),
        Spell('Contagion', [180], Effects(
            [['39-43']],
            [['45-50']],
            [AIR],
        ), is_linked=(2, 'Wild Grass')),
        Spell('Bush Fire', [80, 147], Effects(
            [['9-11', '13-15']] * 2,
            [['11-13', '16-18']] * 2,
            [FIRE, WATER],
        ), aggregates=[('', [0, 1])],
        is_linked=(1, 'Voodoo Curse')),
        Spell('Voodoo Curse', [190], Effects(
            [['11-13'],
            ['11-13']] * 2,
            None,
            [FIRE, WATER] * 2,
        ), aggregates=[('', [0, 1]),
                       ('If the target loses MP', [2]),
                       ('If the target loses AP', [3])],
        is_linked=(2, 'Bush Fire')),
        Spell('Paralysing Bramble', [195], Effects(
            [['20-23']],
            [['24-28']],
            [AIR],
         )),  
    ],
    'Sram': [
        Spell('Gangsterdom', [1, 66, 132], Effects(
            [['15-17', '21-23', '26-29'],
             ['50', '100', '200']],
            [['19-21', '25-28', '31-35'],
             ['50', '100', '200']],
            [EARTH, 'buff_pow_traps'],
        ), is_linked=(1, 'Pitfall')),
        Spell('Pitfall', [95, 162], Effects(
            create_stacking_values(((24, 27), (30, 34)), 8, 6),
            create_stacking_values(((29, 33), (34, 38)), 8, 6),
            [EARTH] * 6,
        ), aggregates=[(TRAP_LABELS[n], [n]) for n in range(6)],
        is_linked=(2, 'Gangsterdom')),
        Spell('Deviousness', [1, 67, 133], Effects(
            [['18-21', '22-25', '26-29']],
            [['22-25', '26-29', '31-34']],
            [FIRE],
        ), is_linked=(1, 'Cut-Throat')),
        Spell('Cut-Throat', [100, 167], Effects(
            [['30-33', '34-38'],
             ['100', '100']],
            [['46-40', '40-44'],
             ['150', '150']],
            [FIRE, 'buff_pow'],
        ), aggregates=[('', [0,]),
                       ('', [1])], stacks=1, 
        is_linked=(2, 'Deviousness')),
        Spell('Arsenic', [3, 69, 136], Effects(
            [['8-10', '11-13', '14-16']],
            [['10-12', '13-15', '17-19']],
            [AIR],
        ), is_linked=(1, 'Toxines')),
        Spell('Toxines', [110, 177], Effects(
            create_level_based_stacking_values(((5, 7), (7, 9)), (5, 6), 6),
            None,
            [AIR] * 6,
        ), aggregates=[(TRAP_LABELS[n], [n]) for n in range(6)],
        is_linked=(2, 'Arsenic')),
        Spell('Cruelty', [6, 71, 138], Effects(
            [['13-15', '18-20', '22-25']],
            [['16-18', '21-24', '26-30']],
            [WATER],
        ), is_linked=(1, 'Jinx')),
        Spell('Jinx', [115, 182], Effects(
            [['29-32', '34-38']],
            [['35-39', '41-46']],
            [WATER], steals=[True],
        ), is_linked=(2, 'Cruelty')),
        Spell('Tricky Trap', [15, 82, 149], Effects(
            [['18-20', '22-24', '26-28']],
            None,
            [FIRE],
        ), special='trap',
        is_linked=(1, 'Waylaying')),
        Spell('Waylaying', [125, 192], Effects(
            [['19-22', '22-25']],
            [['23-26', '27-30']],
            [WATER], steals=[True],
        ), is_linked=(2, 'Tricky Trap')),
        Spell('Miry Trap', [20, 87, 154], Effects(
            [['21-25', '27-31', '33-37']],
            None,
            [WATER],
        ), is_linked=(1, 'Epidemic'),
        special='trap'),
        Spell('Epidemic', [130, 197], Effects(
            [['32-36', '36-40']],
            None,
            [AIR],
        ), is_linked=(2, 'Miry Trap')),
        Spell('Malevolent Trap', [25, 92, 159], Effects(
            create_level_based_stacking_values(((18, 20), (23, 26), (28, 32)), (10, 15, 20), 13),
            None,
            [EARTH] * 13,
        ), aggregates=[(CHARGED_LABELS[n], [n]) for n in range(13)],
        is_linked=(1, 'Break-In'),
        special='trap'),
        Spell('Break-In', [135], Effects(
            [['15-17']],
            [['19-21']],
            [FIRE],
        ), is_linked=(2, 'Malevolent Trap')),
        Spell('Repelling Trap', [30, 97, 164], Effects(
            [['12-14', '15-17', '19-21']],
            None,
            [AIR],
        ), special='trap',
        is_linked=(1, 'Frightful Trap')),
        Spell('Frightful Trap', [140], Effects(
            [['20-22']],
            None,
            [EARTH],
        ), special='trap',
        is_linked=(2, 'Repelling Trap')),
        Spell('Shakedown', [40, 107, 174], Effects(
            [['21-24', '26-29', '31-34'],
             ['40', '60', '100']],
            [['26-29', '31-34', '37-41'],
             ['60', '80', '120']],
            [EARTH, 'buff_str'],
        ), aggregates=[('', [0]),
                       ('', [1])], stacks=2,
        is_linked=(1, 'Perquisition')),
        Spell('Perquisition', [150], Effects(
            [['24-27']],
            [['29-32']],
            [FIRE],
        ), is_linked=(2, 'Shakedown')),
        Spell('Con', [45, 112, 179], Effects(
            [['18-20', '24-26', '29-32'],
             ['40', '60', '100']],
            [['22-24', '29-32', '35-38'],
             ['60', '80', '120']],
            [AIR, 'buff_agi'],
        ), aggregates=[('', [0]),
                       ('', [1])], stacks=2,
        is_linked=(1, 'Raiding')),
        Spell('Raiding', [155], Effects(
            [['29-34']],
            [['35-41']],
            [WATER],
        ), is_linked=(2, 'Con')),
        Spell('Larceny', [50, 117, 184], Effects(
            [['34-38', '38-42', '38-42'],
             ['20', '40', '80']],
            [['41-45', '46-50', '46-50'],
             ['40', '60', '100']],
            [WATER, 'buff_cha'],
        ), aggregates=[('', [0]),
                       ('', [1])], stacks=2, 
        is_linked=(1, 'Lethal Attack')),
        Spell('Lethal Attack', [160], Effects(
            [['43-48'],
             ['54-60']],
            [['52-58'],
             ['65-72']],
            [EARTH] * 2,
        ), aggregates=[('', [0]),
                       ('On target with less than 25% HP', [1])],
        is_linked=(2, 'Larceny')),
        Spell('Furrow', [55, 122, 189], Effects(
            [['24-26', '31-35', '36-40'],
             ['20', '40', '80']],
            [['28-31', '38-42', '43-48'],
             ['40', '60', '100']],
            [FIRE, 'buff_int'],
        ), aggregates=[('', [0]),
                       ('', [1])], stacks=2,
        is_linked=(1, 'Toxic Injection')),
        Spell('Toxic Injection', [165], Effects(
            [['28-32']],
            [['34-38']],
            [AIR],
        ), is_linked=(2, 'Furrow')),
        Spell('Drift Trap', [65, 131, 198], Effects(
            [['12-14', '15-17', '17-19']],
            None,
            [FIRE],
        ), special='trap',
        is_linked=(1, 'Insidious Trap')),
        Spell('Insidious Trap', [175], Effects(
            [['8-9']],
            None,
            [AIR],
        ), is_linked=(2, 'Drift Trap'),
        special='trap'),
        Spell('Sickrat Trap', [70, 137], Effects(
            [['13-15', '17-19']],
            None,
            [WATER],
        ), special='trap',
        is_linked=(1, 'Fragmentation Trap')),
        Spell('Fragmentation Trap', [180], Effects(
            [['13-17'],
             ['27-31'],
             ['37-41'],
             ['47-51']],
            None,
            [FIRE, FIRE, FIRE, FIRE],
        ), aggregates=[('At the center', [0]),
                       ('One tile away from the center', [1]),
                       ('Two tiles away from the center', [2]),
                       ('Three tiles away from the center', [3])],
        is_linked=(2, 'Sickrat Trap'),
        special='trap'),
        Spell('Chakra Concentration', [75, 142], Effects(
            [['13', '15']],
            None,
            [FIRE],
            steals=[True],
        )),
        Spell('Lethal Trap', [80, 147], Effects(
            [['31-35', '39-43'],
             ['39-44', '49-54']],
            None,
            [EARTH] * 2,
        ), aggregates=[('', [0]),
                       ('On target with less than 25% HP', [1])], 
        is_linked=(1, 'Calamity'),
        special='trap'),
        Spell('Calamity', [190], Effects(
            [['40-44']],
            None,
            [WATER],
        ), is_linked=(2, 'Lethal Trap'),
        special='trap'),
        Spell('Mistake', [85, 152], Effects(
            [['27-31', '32-36']],
            [['33-37', '38-43']],
            [AIR],
        ), is_linked=(1, 'Perfidy')),
        Spell('Perfidy', [195], Effects(
            [['56-60']],
            [['62-66']],
            [EARTH],
        ), is_linked=(2, 'Mistake')),
    ],
    'Xelor': [
        Spell('Slow Down', [1, 66, 132], Effects(
            [['6-8', '8-10', '11-13']],
            [['8-10', '10-12', '13-16']],
            [WATER],
        ), is_linked=(1, 'Souvenir')),
        Spell('Souvenir', [95, 162], Effects(
            [['23-26', '28-32']],
            [['27-31', '34-38']],
            [EARTH],
        ), is_linked=(2, 'Slow Down')),
        Spell('Hand', [1, 67, 133], Effects(
            [['11-14', '15-18', '19-23'],
             ['14', '18', '23']],
            [['14-16', '18-21', '23-28'],
             ['16', '21', '28']],
            [FIRE] * 2,
        ), aggregates=[('', [0]),
                       ('Leaving Telegraf state', [1])],
        is_linked=(1, 'Cog')),
        Spell('Cog', [100, 167], Effects(
            [['14-16', '17-20']],
            [['16-19', '20-24']],
            [WATER],
        ), is_linked=(2, 'Hand')),
        Spell('Shriveling', [3, 69, 136], Effects(
            [['14-16', '19-22', '25-28'],
             ['20-22', '26-29', '33-36']],
            [['18-20', '23-26', '30-34'],
             ['24-26', '31-35', '40-43']],
            [AIR] * 2,
        ), aggregates=[('', [0]),
                       ('Telegraf state', [1])],
        is_linked=(1, 'Drying Up')),
        Spell('Drying Up', [110, 177], Effects(
            create_level_based_stacking_values(((27, 31), (34, 38)), (7, 10), 6),
            None,
            [AIR] * 6,
        ), aggregates=[(REBOUND_LABELS[n], [n]) for n in range(6)], 
        is_linked=(2, 'Shriveling')),
        Spell("Xelor's Punch", [10, 77, 144], Effects(
            [['14-16', '19-22', '23-27']],
            [['16-19', '22-26', '28-32']],
            [EARTH],
        ), is_linked=(1, 'Gear')),
        Spell('Gear', [120, 187], Effects(
            [['24-27', '27-31']],
            [['28-32', '33-37']],
            [EARTH],
        ), is_linked=(2, "Xelor's Punch")),
        Spell('Frostbite', [20, 87, 154], Effects(
            [['7-9', '9-11', '11-13']],
            [['8-10', '10-12', '13-16']],
            [AIR],
        ), is_linked=(1, 'Disruption')),
        Spell('Disruption', [130, 197], Effects(
            [['15-17', '17-19']],
            [['18-20', '20-23']],
            [FIRE],
        ), is_linked=(2, 'Frostbite')),
        Spell("Xelor's Sandglass", [25, 92, 159], Effects(
            [['17-19', '20-22', '23-26']],
            [['20-22', '23-26', '27-30']],
            [FIRE],
        ), is_linked=(1, 'Temporal Distortion')),
        Spell('Temporal Distortion', [135], Effects(
            [['34-38']],
            [['41-46']],
            [AIR],
        ), is_linked=(2, "Xelor's Sandglass")),
        Spell('Time Theft', [30, 97, 164], Effects(
            [['19-21', '24-27', '30-34']],
            [['23-26', '29-33', '36-41']],
            [WATER],
        ), is_linked=(1, 'Petrification')),
        Spell('Petrification', [140], Effects(
            [['34-38']],
            [['41-46']],
            [WATER],
        ), is_linked=(2, 'Time Theft')),
        Spell('Temporal Dust', [40, 107, 174], Effects(
            [['20-22', '26-28', '32-35']],
            [['24-27', '31-34', '38-42']],
            [FIRE],
        ), is_linked=(1, 'Temporal Suspension')),
        Spell('Temporal Suspension', [150], Effects(
            [['25-29']],
            [['30-35']],
            [FIRE],
        ), is_linked=(2, 'Temporal Dust')),
        Spell('Loss of Motivation', [50, 117, 184], Effects(
            [['14-16', '20-22', '23-26']],
            [['17-20', '23-27', '28-31']],
            [EARTH],
        ), is_linked=(1, 'Pendulum')),
        Spell('Pendulum', [160], Effects(
            [['38-42']],
            [['46-50']],
            [AIR],
        ), is_linked=(2, 'Loss of Motivation')),
        Spell('Clock', [75, 142], Effects(
            [['29-31', '36-39']],
            [['35-38', '43-47']],
            [WATER], steals=[True],
        ), is_linked=(1, 'Water Clock')),
        Spell('Water Clock', [185], Effects(
            [['32-36']],
            [['38-43']],
            [WATER],
        ), is_linked=(2, 'Clock')),
        Spell('Dark Ray', [80, 147], Effects(
            [['34-37', '40-44'],
             ['47-53', '59-67']],
            [['39-43', '47-51'],
             ['57-65', '73-81']],
            [EARTH] * 2,
        ), aggregates=[('', [0]),
                       ('Telegraf state', [1])],
        is_linked=(1, 'Shadowy Beam')),
        Spell('Shadowy Beam', [190], Effects(
            [['20-22']],
            [['24-26']],
            [EARTH],
        ), is_linked=(2, 'Dark Ray')),
        Spell('Knell', [200], Effects(
            [['6']] * 4,
            None,
            [AIR, WATER, EARTH, FIRE],
        ), aggregates=[('', [0, 1, 2, 3])]),
    ],
    'Eliotrope': [
        Spell('Insult', [1, 67, 133], Effects(
            [['15-17', '20-22', '26-28']],
            [['18-20', '24-26', '31-34']],
            [AIR],
        ), is_linked=(1, 'Contempt')),
        Spell('Contempt', [100, 167], Effects(
            [['19-22', '24-27']],
            [['23-26', '29-32']],
            [AIR],
        ), is_linked=(2, 'Insult')),
        Spell('Audacious', [1, 68, 134], Effects(
            [['15-17', '20-23', '26-29']],
            [['19-21', '24-27', '31-35']],
            [WATER],
        ), is_linked=(1, 'Tribulation')),
        Spell('Tribulation', [105, 172], Effects(
            [['17-19', '21-24']],
            [['20-23', '25-29']],
            [WATER],
        ), is_linked=(2, 'Affliction')),
        Spell('Shock', [3, 69, 136], Effects(
            [['11-13', '15-17', '19-21']],
            [['14-16', '18-20', '22-25']],
            [EARTH],
        ), is_linked=(1, 'Convulsion')),
        Spell('Convulsion', [110, 177], Effects(
            [['16-18', '20-22']],
            [['19-21', '24-26']],
            [EARTH],
        ), is_linked=(2, 'Shock')),
        Spell('Wakfu Ray', [6, 71, 138], Effects(
            [['15-17', '21-23', '26-28']] * 2,
            [['18-20', '25-27', '31-34']] * 2,
            [FIRE, FIRE],
            heals=[False, True],
        ), aggregates=[('Enemies', [0]),
                       ('Allies', [1])],
        is_linked=(1, 'Lazybeam')),
        Spell('Lazybeam', [115, 182], Effects(
            [['23-26', '27-31']] * 2,
            [['27-32', '32-37']] * 2,
            [FIRE, FIRE],
            steals=[False, True],
        ), aggregates=[('Directly', [0]),
                       ('Through a portal', [1])],
        is_linked=(2, 'Wakfu Ray')),
        Spell('Offence', [13, 82, 149], Effects(
            [['20-23', '25-29', '31-36']],
            [['23-27', '30-35', '37-43']],
            [FIRE],
        ), is_linked=(1, 'Composure')),
        Spell('Composure', [125, 192], Effects(
            [['28-31', '32-36']],
            [['33-37', '39-43']],
            [WATER],
        ), is_linked=(2, 'Offence')),
        Spell('Therapy', [25, 92, 159], Effects(
            [['12-14', '16-18', '21-23']],
            [['15-17', '20-22', '26-28']],
            [EARTH],
        ), is_linked=(1, 'Snub')),
        Spell('Snub', [135], Effects(
            [['23-26']],
            [['28-31']],
            [EARTH],
        ), is_linked=(2, 'Therapy')),
        Spell('Bullying', [40, 107, 174], Effects(
            [['14-16', '18-20', '23-25']],
            [['17-19', '22-24', '28-30']],
            [AIR],
        ), is_linked=(1, 'Sermon')),
        Spell('Sermon', [150], Effects(
            [['34-38']],
            [['41-46']],
            [AIR],
        ), is_linked=(2, 'Bullying')),
        Spell('Affliction', [50, 117, 184], Effects(
            [['16-18', '20-23', '25-28']] * 3,
            [['19-21', '24-27', '30-34']] * 3,
            [WATER] * 3,
        ), aggregates=[('Directly', [0]),
                       ('Through a portal', [1, 2])],
        is_linked=(1, 'Affront')),
        Spell('Affront', [160], Effects(
            [['20-23']] * 2,
            [['24-28']] * 2,
            [FIRE] * 2, steals=[False, True],
        ), aggregates=[('Directly', [0]),
                       ('Through a portal', [1])],
        is_linked=(2, 'Affliction')),
        Spell('Lightning Fist', [65, 131, 198], Effects(
            [['14-16', '19-21', '23-25']],
            [['17-19', '23-25', '28-30']],
            [WATER],
        ), is_linked=(1, 'Insolence')),
        Spell('Insolence', [175], Effects(
            [['25-28']],
            [['30-34']],
            [WATER],
        ), is_linked=(2, 'Lightning Fist')),
        Spell('Focus', [70, 137], Effects(
            [['75', '100'],
             ['150', '200']],
            None,
            ['buff_pow', 'buff_pow'],
        ), aggregates=[('Directly', [0]),
                       ('Through a portal', [1])]),
        Spell('Parasite', [75, 142], Effects(
            [['27-30', '33-37']] * 3,
            [['32-36', '40-44']] * 3,
            [FIRE] * 3,
        ), aggregates=[('Directly', [0]),
                       ('Through a portal', [1, 2])],
        is_linked=(1, 'Virus')),
        Spell('Virus', [185], Effects(
            [['34-38']],
            [['41-46']],
            [FIRE],
        ), is_linked=(2, 'Parasite')),
        Spell('Sinecure', [80, 147], Effects(
            [['9-11', '12-14']],
            [['12-14', '15-17']],
            [AIR],
        ), is_linked=(1, 'Persiflage')),
        Spell('Persiflage', [190], Effects(
            [['25-29']],
            [['30-35']],
            [EARTH],
        ), is_linked=(2, 'Sinecure')),
        Spell('Sarcasm', [85, 152], Effects(
            [['26-29', '32-36']],
            [['31-35', '38-43']],
            [EARTH],
        ), is_linked=(1, 'Ridicule ')),
        Spell('Ridicule', [195], Effects(
            [['30-34']],
            [['36-41']],
            [AIR],
        ), is_linked=(2, 'Sarcasme')), 
    ],
    'Huppermage': [
        Spell('Telluric Wave', [1, 67, 133], Effects(
            [['15-19', '20-24', '25-29']],
            [['20-24', '25-29', '30-34']],
            [EARTH],
        ), is_linked=(1, 'Cataract')),
        Spell('Cataract', [100, 167], Effects(
            [['15-17', '18-20']] * 2,
            [['18-20', '21-23']] * 2,
            [WATER, FIRE],
        ), aggregates=[('', [0, 1])],
        is_linked=(2, 'Telluric Wave')),
        Spell('Ether', [1, 66, 132], Effects(
            [['12-14', '16-18', '20-22']],
            [['15-17', '19-21', '23-25']],
            [AIR],
        ), is_linked=(1, 'Stinger')),
        Spell('Stinger', [95, 162], Effects(
            [['13-15', '16-18']] * 2,
            [['16-18', '19-21']] * 2,
            [EARTH, WATER],
        ), aggregates=[('', [0, 1])], 
        is_linked=(2, 'Ether')),
        Spell('Runification', [1, 68, 134], Effects(
            [['9', '12', '15']] * 4,
            None,
            [EARTH, FIRE, WATER, AIR],
        ), aggregates=[('Target in earth state', [0]),
                       ('Target in fire state', [1]),
                       ('Target in water state', [2]),
                       ('Target in air state', [3])],
        is_linked=(1, 'Manifestation')),
        Spell('Manifestation', [105, 172], Effects(
            [['15', '15']] * 4,
            None,
            [EARTH, FIRE, WATER, AIR],
        ), aggregates=[('Target in earth state', [0]),
                       ('Target in fire state', [1]),
                       ('Target in water state', [2]),
                       ('Target in air state', [3])],
        is_linked=(2, 'Runification')),
        Spell('Flamethrower', [3, 69, 136], Effects(
            [['12-14', '16-18', '20-22']],
            [['16-18', '20-22', '24-26']],
            [FIRE],
        ), is_linked=(1, 'Celestial Wave')),
        Spell('Celestial Wave', [110, 177], Effects(
            [['11-13', '14-16']] * 2,
            [['14-16', '17-19']] * 2,
            [AIR, EARTH],
        ), aggregates=[('', [0, 1])],
        is_linked=(2, 'Flamethrower')),
        Spell('Stalagmite', [6, 71, 138], Effects(
            [['18-21', '23-26', '28-31']],
            [['24-27', '29-32', '34-37']],
            [WATER],
        ), is_linked=(1, 'Ember')),
        Spell('Ember', [115, 182], Effects(
            [['15-17', '18-20']] * 2,
            [['18-20', '21-23']] * 2,
            [FIRE, AIR],
        ), aggregates=[('', [0, 1])], 
        is_linked=(2, 'Stalagmite')),
        Spell('Elemental Drain', [9, 47, 87], Effects(
            [['15-19', '19-23', '23-27']] * 4
            + [['50', '100', '180']] * 4,
            [['19-23', '23-27', '27-31']] * 4
            + [['60', '120', '200']] * 4,
            [EARTH, FIRE, WATER, AIR,
             'buff_str', 'buff_int', 'buff_cha', 'buff_agi'], 
        ), aggregates=[('Target in earth state', [0]),
                       ('', [4]),
                       ('Target in fire state', [1]),
                       ('', [5]),
                       ('Target in water state', [2]),
                       ('', [6]),
                       ('Target in air state', [3]),
                       ('', [7])],
        is_linked=(1, 'Morph')),
        Spell('Morph', [120, 187], Effects(
            [['24-27', '28-32']] * 4,
            [['29-33', '34-38']] * 4,
            [WATER, EARTH, AIR, FIRE], 
        ), aggregates=[('Target in water state', [0]),
                       ('Target in earth state', [1]),
                       ('Target in air state', [2]),
                       ('Target in fire state', [3])],
        is_linked=(2, 'Elemental Drain')),
        Spell('Storm', [15, 82, 149], Effects(
            [['24-28', '29-33', '34-38']],
            [['29-33', '34-38', '39-43']],
            [EARTH],
            steals=[True]
        ), is_linked=(1, 'Stalactite')),
        Spell('Stalactite', [125, 192], Effects(
            [['20-22', '23-25']],
            [['24-26', '26-28']],
            [WATER],
        ), is_linked=(2, 'Glacier')),
        Spell('Transfixing Gust', [20, 87, 154], Effects(
            [['20-22', '25-28', '31-35']],
            [['23-26', '30-34', '35-39']],
            [AIR],
            steals=[True]
        ), is_linked=(1, 'Tectonic Breach')),
        Spell('Tectonic Breach', [130, 197], Effects(
            [['12-14', '14-16']],
            [['15-17', '17-19']],
            [EARTH],
        ), is_linked=(2, 'Transfixing Gust')),
        Spell('Burning Stroke', [30, 97, 164], Effects(
            [['23-27', '28-32', '33-37']],
            [['28-32', '33-37', '38-42']],
            [FIRE],
            steals=[True]
        ), is_linked=(1, 'Hurricane')),
        Spell('Hurricane', [140], Effects(
            [['17-19']],
            [['20-22']],
            [AIR]
        ), is_linked=(2, 'Burning Stroke')),
        Spell('Glacier', [32, 102, 169], Effects(
            [['22-26', '28-32', '34-38']],
            [['26-30', '32-36', '38-42']],
            [WATER],
            steals=[True]
        ), is_linked=(1, 'Volcano')),
        Spell('Volcano', [145], Effects(
            [['19-21']],
            [['22-24']],
            [FIRE]
        ), is_linked=(2, 'Glacier')),
        Spell('Journey', [40, 107, 174], Effects(
            [['15-24', '23-32', '31-40']] * 4,
            [['25-34', '33-42', '41-50']] * 4,
            [EARTH, FIRE, WATER, AIR], 
        ), aggregates=[('Target in earth state', [0]),
                       ('Target in fire state', [1]),
                       ('Target in water state', [2]),
                       ('Target in air state', [3])]),
        Spell('Deflagration', [50, 117, 184], Effects(
            [['22-26', '26-30', '30-34']],
            [['26-30', '30-34', '34-38']],
            [FIRE],
        ), is_linked=(1, 'Comet')),
        Spell('Comet', [160], Effects(
            [['28-32']],
            [['32-36']],
            [AIR],
        ), is_linked=(2, 'Deflagration')),
        Spell('Contribution', [55, 122, 189], Effects(
            [['150'] * 3],
            None,
            ['buff_pow']
        ), aggregates=[('Target in water state', [0])], stacks=2),
        Spell('Icy Shards', [60, 127, 194], Effects(
            [['24-28', '29-33', '34-38']],
            [['28-32', '33-37', '38-42']],
            [WATER],
        ), is_linked=(1, 'Sun Lance')),
        Spell('Sun Lance', [170], Effects(
            [['34-38']],
            [['39-43']],
            [FIRE],
        ), is_linked=(2, 'Icy Shards')),
        Spell('Runic Overcharge', [175], Effects(
            [['10']] * 4,
            None,
            [WATER, FIRE, AIR, EARTH],
        ), aggregates=[('For each of the caster\'s runes', [0, 1, 2 , 3])]),
        Spell('Astral Blade', [75, 142], Effects(
            [['26-28', '32-35']],
            [['31-34', '36-39']],
            [AIR],
        ), is_linked=(1, 'Telluric Blade')),
        Spell('Telluric Blade', [185], Effects(
            [['34-38']],
            [['41-46']],
            [EARTH],
        ), is_linked=(2, 'Astral Blade')),
        Spell('Striking Meteor', [80, 147], Effects(
            [['20-24', '30-34']],
            [['24-27', '34-37']],
            [EARTH],
        ), is_linked=(1, 'Flood')),
        Spell('Flood', [190], Effects(
            [['31-35']],
            [['37-42']],
            [WATER],
        ), is_linked=(2, 'Striking Meteor')),
        Spell('Tribute', [90, 157], Effects(
            [['150', '150']],
            None,
            ['buff_pow'],
        ), is_linked=(1, 'Arcane Torrent')),
        Spell('Arcane Torrent', [200], Effects(
            [['6']] * 4 + [['9']] * 4 + [['12']] * 4 + [['15']] * 4 + [['18']] * 4 + [['21']] * 4,
            [['8']] * 4 + [['11']] * 4 + [['14']] * 4 + [['17']] * 4 + [['20']] * 4 + [['23']] * 4,
            [AIR, EARTH, FIRE, WATER] * 6,
        ), aggregates=[('1 combination', [0, 1, 2, 3]),
                        ('2 combinations', [4, 5, 6, 7]),
                        ('3 combinations', [8, 9, 10, 11]),
                        ('4 combinations', [12, 13, 14, 15]),
                        ('5 combinations', [16, 17, 18, 19]),
                        ('6 combinations', [20, 21, 22, 23])],
        is_linked=(2, 'Tribute')),
    ],
    'Ouginak': [
        Spell('Watchdog', [1, 67, 133], Effects(
            [['18-20', '24-27', '31-34']],
            [['22-24', '29-32', '37-41']],
            [EARTH],
        ), is_linked=(1, 'Jaw')),
        Spell('Jaw', [100, 167], Effects(
            [['23-35', '28-31']],
            [['27-30', '34-37']],
            [FIRE],
        ), is_linked=(2, 'Watchdog')),
        Spell('Marrow Bone', [1, 68, 134], Effects(
            create_level_based_stacking_values(((12, 14), (16, 19), (21, 24)), 
                                               (6, 7, 8), 5),
            create_level_based_stacking_values(((15, 17), (20, 22), (25, 29)), 
                                               (6, 7, 8), 5),
            [[WATER]] * 5,
        ), aggregates=[('', [0]),
                       ('After hitting a Prey once', [1]),
                       ('After hitting a Prey twice', [2]),
                       ('After hitting a Prey 3x', [3]),
                       ('After hitting a Prey 4x', [4])],
        is_linked=(1, 'Muzzle')),
        Spell('Muzzle', [105, 172], Effects(
            create_level_based_stacking_values(((30, 33), (37, 41)),
                                                  (18, 22), 5),
            create_level_based_stacking_values(((30, 33), (36, 39)),
                                                  (18, 22), 5),
            [EARTH] * 5,
        ), aggregates=[('', [0]),
                       ('1 ennemy adjacent to a Prey', [1]),
                        ('2 enemies adjacent to a Prey', [2]),
                        ('3 enemies adjacent to a Prey', [3]),
                        ('4 enemies adjacent to a Prey', [4])],
        is_linked=(2, 'Marrow Bone')),
        Spell('Carrion', [3, 69, 136], Effects(
            [['18-20', '25-27', '29-32']],
            [['22-24', '30-33', '35-38']],
            [AIR],
        ), is_linked=(1, 'Radius')),
        Spell('Radius', [110, 177], Effects(
            [['26-29', '32-36']],
            [['31-35', '38-43']],
            [WATER],
        ), is_linked=(2, 'Carrion')),
        Spell('Tracking', [6, 71, 138], Effects(
            [['19-21', '25-28', '31-35']],
            [['22-25', '30-34', '37-42']],
            [FIRE],
        ), is_linked=(1, 'Carving Up')),
        Spell('Carving Up', [115, 182], Effects(
            [['34-38', '40-45']],
            [['41-46', '48-54']],
            [AIR],
        ), is_linked=(2, 'Tracking')),
        Spell('Mastiff', [20, 87, 154], Effects(
            [['10-11', '13-15', '17-19']] * 2,
            [['13-15', '16-18', '20-23']] * 2,
            [EARTH,EARTH],
            steals=(False, True)
        ), aggregates=[('', [0]),
                       ('If the target is Prey', [1])],
        is_linked=(1, 'Stripping')),
        Spell('Stripping', [130, 197], Effects(
            create_level_based_stacking_values(((31, 35), (35, 39)),
                                                  (16, 20), 5),
            create_level_based_stacking_values(((38, 42), (42, 47)),
                                                  (16, 20), 5),
            [AIR] * 5,
        ), aggregates=[('', [0]),
                        ('1 ally adjacent to a Prey', [1]),
                        ('2 allies adjacent to a Prey', [2]),
                        ('3 allies adjacent to a Prey', [3]),
                        ('4 allies adjacent to a Prey', [4])],
        is_linked=(2, 'Mastiff')),
        Spell('Tibia', [25, 92, 159], Effects(
            [['25-28', '32-36', '40-45']],
            [['30-34', '39-43', '48-54']],
            [WATER],
        ), is_linked=(1, 'Humerous')),
        Spell('Humerous', [135], Effects(
            [['41-46']],
            [['49-55']],
            [EARTH],
        ), is_linked=(2, 'Tibia')),
        Spell('R-Canine', [30, 97, 164], Effects(
            [['50', '70', '100']],
            None,
            ['buff_pow'],
        ), stacks=2),
        Spell('Tally Ho', [35, 102, 169], Effects(
            [['18-20', '23-26', '29-31']],
            [['22-24', '28-30', '35-37']],
            [FIRE],
        ), is_linked=(1, 'Hunt')),
        Spell('Hunt', [145], Effects(
            [['39-44']],
            [['47-53']],
            [FIRE],
        ), is_linked=(2, 'Tally Ho')),
        Spell('Carcass', [40, 107, 174], Effects(
            create_level_based_stacking_values(((5, 7), (7, 9), (9, 11)), 
                                               (4, 5, 6), 5),
            create_level_based_stacking_values(((3, 8), (9, 11), (11, 13)), 
                                               (4, 5, 6), 5),
            [[AIR]] * 6,
        ), aggregates=[('', [0]),
                       ('After hitting a Prey once', [1]),
                       ('After hitting a Prey twice', [2]),
                       ('After hitting a Prey 3x', [3]),
                       ('After hitting a Prey 4x', [4])],
        is_linked=(1, 'Beaten')),
        Spell('Beaten', [150], Effects(
            [['27-30'],
             ['75']],
            [['32-36'],
             ['75']],
            [AIR, 'buff_pow'],
        ), aggregates=[('If the target is Prey, stack x2', [0]),
                       ('', [1])], stacks=2,
        is_linked=(2, 'Carcass')),
        Spell('Woof', [50, 117, 184], Effects(
            [['12-14', '17-19', '20-22']] * 2,
            [['15-17', '20-22', '24-26']] * 2,
            [FIRE] * 2,
            steals=[False, True],
        ), aggregates=[('', [0]),
                       ('If the target is Prey', [1])],
        is_linked=(1, 'Vertebra')),
        Spell('Vertebra', [160], Effects(
            [['32-36']],
            [['38-43']],
            [WATER],
        ), is_linked=(2, 'Woof')),
        Spell('Ulna', [55, 122, 189], Effects(
            [['10-12', '14-16', '16-18']],
            [['12-14', '16-18', '19-22']],
            [WATER],
        ), is_linked=(1, 'Calcaneus')),
        Spell('Calcaneus', [165], Effects(
            [['14-16']],
            [['17-19']],
            [WATER],
        ), is_linked=(2, 'Ulna')),
        Spell('Amarok', [65, 131, 198], Effects(
            [['21-23', '25-28', '28-31']],
            [['25-28', '30-33', '34-37']],
            [EARTH],
        ), is_linked=(1, 'Cerberus')),
        Spell('Cerberus', [175], Effects(
            [['15-18'],
             ['21-25'],
             ['15-18'],
             ['15-18'],
             ['13-14'],
             ['13-14'],
             ['13-14']],
            [['19-23'],
             ['26-30'],
             ['19-22'],
             ['19-22'],
             ['15-16'],
             ['15-16'],
             ['15-16']],
            [EARTH] * 7,
        ), aggregates=[('No Rage', [0]),
                        ('Rage', [1]),
                        ('Raage', [2, 3]),
                        ('Animal Form', [4, 5, 6])],
        is_linked=(2, 'Amarok')),
        Spell('Gnaw', [185], Effects(
            [['80']],
            None,
            ['buff_pow'],
        ), stacks=3),
        Spell('Bloodhound', [80, 147], Effects(
            [['23-25', '28-31']],
            [['27-30', '34-37']],
            [AIR],
        ), is_linked=(1, 'Tetanisation')),
        Spell('Tetanisation', [190], Effects(
            [['41-46']],
            [['49-55']],
            [FIRE],
        ), is_linked=(2, 'Bloodhound')),   
    ],
    'Forgelance': [
        Spell('Lance of the Lake', [1, 66, 132], Effects(
            [['13-15', '17-20', '22-25']],
            [['16-18', '21-23', '26-30']],
            [WATER],
        ), is_linked=(1, 'Seismic Pike')),
        Spell('Seismic Pike', [95, 162], Effects(
            [['21-24', '26-29']],
            [['25-29', '31-36']],
            [EARTH],
        ), is_linked=(2, 'Lance of the Lake')),
        Spell('Slingshot', [1, 67, 133], Effects(
            [['15-17', '19-21', '25-28']],
            [['18-20', '22-25', '30-34']],
            [EARTH],
        ), is_linked=(1, 'Lightning-Javelin')),
        Spell('Lightning-Javelin', [100, 167], Effects(
            [['23-26', '28-32']],
            [['28-31', '35-39']],
            [WATER],
        ), is_linked=(2, 'Slingshot')),
        Spell('Parry', [105, 172], Effects(
            [['24', '30']] * 4,
            None,
            [EARTH, FIRE, WATER, AIR],
        ), aggregates=[('Hit in best element', [0]), 
                       ('', [1]),
                       ('', [2]),
                       ('', [3])]),
        Spell('Fire Lance', [3, 69, 136], Effects(
            [['12-13', '16-19', '21-24']],
            [['15-17', '20-22', '25-29']],
            [FIRE],
        ), is_linked=(1, 'Disengaging')),
        Spell('Disengaging', [110, 177], Effects(
            [['23-26', '29-32']],
            [['28-31', '35-38']],
            [AIR],
        ), is_linked=(2, 'Fire Lance')),
        Spell('No Myr Javelin', [6, 71, 138], Effects(
            [['16-18', '21-24', '26-30']],
            [['19-21', '25-29', '31-36']],
            [AIR],
        ), is_linked=(1, 'Hot Iron')),
        Spell('Hot Iron', [115, 182], Effects(
            [['17-20', '20-23']],
            [['20-23', '24-28']],
            [FIRE],
        ), is_linked=(2, 'No Myr Javelin')),
        Spell('Heroic Charge', [10, 77, 144], Effects(
            [['20', '27', '33']] * 4,
            [['24', '32', '40']] * 4,
            [EARTH, FIRE, WATER, AIR],
        ), aggregates=[('Hit in best element', [0]),
                        ('', [1]),
                        ('', [2]),
                        ('', [3])],),
        Spell('Collapse', [15, 82, 149], Effects(
            [['13-15', '16-18', '20-22']],
            [['15-17', '19-21', '24-26']],
            [EARTH],
        ), is_linked=(1, 'Brass Rain')),
        Spell('Brass Rain', [125, 192], Effects(
            [['16-18', '19-21']],
            [['20-22', '23-25']],
            [AIR],
        ), is_linked=(2, 'Collapse')),
        Spell('Biting Trident', [20, 87, 154], Effects(
            [['13-15', '17-19', '21-24']],
            [['16-18', '20-23', '25-29']],
            [WATER],
        ), is_linked=(1, 'Spicy Mill')),
        Spell('Spicy Mill', [130, 197], Effects(
            [['25-29', '28-32']],
            [['30-34', '34-38']],
            [FIRE],
        ), is_linked=(2, 'Biting Trident')),
        Spell('Burning Estoc', [30, 97, 164], Effects(
            [['14-16', '19-21', '23-26']],
            [['17-20', '22-25', '28-31']],
            [FIRE],
        ), is_linked=(1, 'Octave')),
        Spell('Octave', [140], Effects(
            [['16-18']],
            [['19-22']],
            [WATER],
        ), is_linked=(2, 'Burning Estoc')),
        Spell('Brass Volley', [35, 102, 169], Effects(
            [['14-16', '18-20', '22-25']],
            [['17-19', '21-24', '26-30']],
            [AIR],
        ), is_linked=(1, 'Upheaval')),
        Spell('Upheaval', [145], Effects(
            [['29-33']],
            [['35-40']],
            [EARTH],
        ), is_linked=(2, 'Brass Volley')),
        Spell('Balestra', [40, 107, 174], Effects(
            [['18-20', '23-25', '28-31']],
            [['21-23', '27-30', '34-37']],
            [WATER],
        ), is_linked=(1, 'Windmill')),
        Spell('Windmill', [150], Effects(
            [['29-33']],
            [['35-40']],
            [AIR],
        ), is_linked=(2, 'Balestra')),
        Spell('Earthen Weakness', [45, 112, 179], Effects(
            [['8-10', '11-13', '14-16']],
            [['10-12', '13-15', '17-19']],
            [EARTH],
        ), is_linked=(1, 'Lunge')),
        Spell('Lunge', [155], Effects(
            [['12-14']],
            [['14-17']],
            [FIRE],
        ), is_linked=(2, 'Earthen Weakness')),
        Spell('Kyrja', [50, 117, 184], Effects(
            [['18-20', '24-27', '28-32']] * 4,
            [['21-24', '29-33', '34-38']] * 4,
            [EARTH, FIRE, WATER, AIR], steals=[True, True, True, True],
        ), aggregates=[('Steals in best element', [0]),
                        ('', [1]),
                        ('', [2]),
                        ('', [3])],
        is_linked=(1, 'Vajra')),
        Spell('Vajra', [160], Effects(
            [['39-44']] * 4,
            [['47-53']] * 4,
            [EARTH, FIRE, WATER, AIR], steals=[True, True, True, True],
        ), aggregates=[('Steals in best element', [0]),
                        ('', [1]),
                        ('', [2]),
                        ('', [3])],
        is_linked=(2, 'Kyrja')),
        Spell('Maelstrom', [55, 122, 189], Effects(
            [['11-13', '16-18', '18-20']],
            [['14-16', '19-21', '22-24']],
            [FIRE],
        ), is_linked=(1, 'Ydra')),
        Spell('Ydra', [165], Effects(
            [['25-28']],
            [['30-34']],
            [EARTH],
        ), is_linked=(2, 'Maelstrom')),
        Spell('Iron Prelude', [60, 127, 194], Effects(
            [['100', '150', '200']],
            None,
            ['buff_pow'],
        )),
        Spell('Cyclone Lancer', [65, 131, 198], Effects(
            [['23-25', '28-30', '31-33']],
            [['28-30', '33-35', '37-40']],
            [AIR],
        ), is_linked=(1, 'Elding')),
        Spell('Elding', [175], Effects(
            [['32-36']],
            [['38-43']],
            [WATER],
        ), is_linked=(2, 'Cyclone Lancer')),
        Spell('Jormun', [75, 142], Effects(
            [['24-27', '30-34'], ['21-24', '26-30']],
            [['29-33', '36-41'], ['25-29', '31-36']],
            [WATER, WATER],
        ), aggregates=[('On ennemy', [0]),
                       ('On caster', [1]),],
        is_linked=(1, 'Muspel')),
        Spell('Muspel', [185], Effects(
            [['32-36']],
            [['38-42']],
            [FIRE],
        ), is_linked=(2, 'Jormun')),
        Spell('Middle Earth', [85, 152], Effects(
            [['24-27', '30-34'], ['30', '50']],
            [['29-33', '36-41'], ['30', '50']],
            [EARTH, 'buff_pow'],
        ), is_linked=(1, 'Noa')),
        Spell('Noa', [195], Effects(
            [['20-23'], ['23-26']],
            [['24-28'], ['28-31']],
            [AIR, AIR],
        ), aggregates=[('', [0]),
                       ('Noa state', [1])], 
        is_linked=(2, 'Middle Earth')),
        #TODO figure out effects of Eclipse, Helmgang and Surtr Spark
    ]
}

DEFAULT_SOFT_CAPS = {
    'vit': [0, None, 0, 0, 0, 0],
    'wis': [0, 0, 0, None, 0, 0],
    'str': [0, 100, 200, 300, None, 0],
    'int': [0, 100, 200, 300, None, 0],
    'cha': [0, 100, 200, 300, None, 0],
    'agi': [0, 100, 200, 300, None, 0]
}
SOFT_CAPS = {'Cra' : DEFAULT_SOFT_CAPS,
             'Ecaflip' : DEFAULT_SOFT_CAPS,
             'Eniripsa' : DEFAULT_SOFT_CAPS,
             'Enutrof' : DEFAULT_SOFT_CAPS,
             'Feca' : DEFAULT_SOFT_CAPS,
             'Iop' : DEFAULT_SOFT_CAPS,
             'Osamodas' : DEFAULT_SOFT_CAPS,
             'Pandawa' : DEFAULT_SOFT_CAPS,
             'Foggernaut' : DEFAULT_SOFT_CAPS,
             'Rogue' : DEFAULT_SOFT_CAPS,
             'Sacrier' : DEFAULT_SOFT_CAPS,
             'Sadida' : DEFAULT_SOFT_CAPS,
             'Sram' : DEFAULT_SOFT_CAPS,
             'Xelor' : DEFAULT_SOFT_CAPS,
             'Eliotrope' : DEFAULT_SOFT_CAPS,
             'Masqueraider' : DEFAULT_SOFT_CAPS,
             'Huppermage' : DEFAULT_SOFT_CAPS,
             'Ouginak' : DEFAULT_SOFT_CAPS,
             'Forgelance' : DEFAULT_SOFT_CAPS}

ATTRIBUTE_TO_ELEMENT = {
    'int': 'fire',
    'cha': 'water',
    'agi': 'air',
    'str': 'earth'
}

def get_best_element(char_stats):
    best_element = 'str'
    best_element_val = char_stats['str']
    for element in ['int', 'cha', 'agi']:
        if char_stats[element] > best_element_val:
            best_element = element
            best_element_val = char_stats[element]
    return best_element

def get_equiped_weapon(char_stats):
    weapon = None
    for item in char_stats['items']:
        if item.slot == 'weapon':
            weapon = item
            break
    return weapon

def calculate_damage(base_damage, char_stats, critical_hit, is_spell):
    damage_instances = []
    for dam in base_damage:
        if dam.element == 'best':
            dam.element = get_best_element(char_stats)
            dam.element = ATTRIBUTE_TO_ELEMENT[dam.element]
        element_val = max(char_stats[DAMAGE_TYPE_TO_MAIN_STAT[dam.element]], 0)
        if not dam.heals:
            element_val = element_val + max(char_stats['pow'], 0)
            element_dam = char_stats[dam.element.lower() + "dam"]
            element_dam = element_dam + char_stats['dam']
            if critical_hit:
                element_dam += char_stats['cridam']
        else:
            element_dam = char_stats['heals']
        minimum_damage = (max(int((1 + element_val / 100.0) * dam.min_dam)
                                               + element_dam, 0))
        maximum_damage = (max(int((1 + element_val / 100.0) * dam.max_dam)
                                               + element_dam, 0))
        if is_spell:
            minimum_damage = minimum_damage * (100 + char_stats['perspedam'])/100
            maximum_damage = maximum_damage * (100 + char_stats['perspedam'])/100
        else:
            minimum_damage = minimum_damage * (100 + char_stats['perweadam'])/100
            maximum_damage = maximum_damage * (100 + char_stats['perweadam'])/100
        damage = CalculatedDamage(min_dam=minimum_damage,
                                  max_dam=maximum_damage,
                                  element=dam.element,
                                  steals=dam.steals,
                                  heals=dam.heals)
        
        damage_instances.append(damage)
    return damage_instances

class CalculatedDamage(BaseDamage):
    pass

class BuffEffect(BaseDamage):
    pass