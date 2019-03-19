import random
class Character:
	"""Stores and edits character data"""
	# Page 1
	name = "default"
	cla = [["default", 0]]
	background = ""
	race = "default"
	align = "default"
	xp = 0
	
	armor_class = 0
	initiative = 0
	speed = 0

	personality_traits = ["none"]
	ideals = ["none"]
	bonds = ["none"]
	flaws = ["none"]

	max_hp = 0
	current_hp = 0
	temp_hp = 0
	hit_dice = [0, "D6"]
	death_saves_success = 0
	death_saves_failure = 0

	attacks = [["none", 0, "D6"], ["none", 0, "D6"], ["none", 0, "D6"]]

	proficiency_bonus = 0
	inspiration = 0

	stre = 0
	dex = 0
	const = 0
	intel = 0
	wisdom = 0
	char = 0

	sav_stre = 0
	sav_dex = 0
	sav_const = 0
	sav_intel = 0
	sav_wis = 0
	sav_char = 0

	acrobatics = 0
	animal_handle = 0
	arcana = 0
	athletics = 0
	deception = 0
	history = 0
	insight = 0
	intimidation = 0
	investigation = 0
	medicine = 0
	nature = 0
	perception = 0
	performance = 0
	persuasion = 0
	religion = 0
	sleight_of_hand = 0
	stealth = 0
	survival = 0
	passive_wisdom = 0

	other_proficiences_languages = ["none"]
	cp = 0
	sp = 0
	ep = 0
	gp = 0
	pp = 0
	equipment = [["filler", "notes"]]
	features_traits = [""]

	# Page 2
	allies_organizations = ["none"]
	age = 0
	height = 0
	weight = 0
	hair = ""
	skin = ""
	eyes = ""
	character_appearance = ""
	character_backstory = ""
	additional_features_traits = ["none"]
	treasure = ["none"]

	# Page 3
	spellcasting_class = ""
	spellcasting_ability = ""
	spell_save_DC = 0
	spell_attack_bonus = 0
	spell_slots = 0
	spell_slots_used = 0
	cantrips = [["none", "notes"]]
	spellbook = [[["name", "note"]]]

	def __init__(self):
		"""init default variables"""

	def roll(self, num):
		"""picks a number between 1 and num"""
		print(random.randint(1,num+1))

	def print_basic_stats(self):
		"""Name, Class, Alignment, Background, XP, Armor Class, HP"""
		print("{}, {}xp".format(self.name,self.xp))
		print("HP: {}(max) + {}(temp)/{}".format(self.current_hp, self.temp_hp, self.max_hp))
		print("Armor Class: {}".format(self.armor_class))
		print("~~CLASSES~~")
		print("{} alignment".format(self.align))
		
		print("")

	
	def add_class(self):
		"""Add a class to cla"""
	
	def del_class(self):
		"""delete a class from cla"""

	def disp_money(self):
		"""prints balance"""
		print("Platinum: {}".format(self.pp))
		print("Gold: {}".format(self.gp))
		print("Electrum: {}".format(self.ep))
		print("Silver: {}".format(self.sp))
		print("Copper: {}".format(self.cp))
		
	def edit_money(self, plat, gold, elec, silv, copp):
		"""edits balance (handle negatives)"""

	def print_attacks(self):
		"""Prints Attacks"""
	
	def edit_attacks(self, slot, name, bonus, damage):
		"""Edit Attacks"""

	def print_spellbook(self):
		"""prints spellbook, cantrips, spell_slots (page 3)"""

	def del_spell(self, num):
		"""removes spell from spellbook"""
	
	def add_spell(self, lvl, name, notes):
		"""adds spell to spellbook"""

	def del_cantrip(self, num):
		"""removes cantrip from cantrips"""
	
	def add_cantrip(self, name, notes):
		"""adds cantrip to cantrips"""

	def update_variables(self):
		"""make sure skill atributes are updated with proficiency bonus"""
	
	def change_temp_hp(self, num):
		"""changes temporary hp"""