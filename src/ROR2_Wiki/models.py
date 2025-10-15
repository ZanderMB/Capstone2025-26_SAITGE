from django.db import models

# Create your models here.

#==============================
# Survivor Model
#==============================
class Survivor(models.Model):
    # Django makes the Primary Key auto-incrementing like SERIAL in SQL

    # Make sure to use db_column to match column names
    surv_img = models.ImageField(upload_to='survivors/', db_column='SurvImg', blank=True, null=True)
    surv_name = models.CharField(max_length=100, db_column='SurvName')
    surv_desc = models.TextField(db_column='SurvDesc')
    surv_hp = models.DecimalField(max_digits=10, decimal_places=2, db_column='SurvHP')
    surv_dmg = models.DecimalField(max_digits=10, decimal_places=2, db_column='SurvDMG')
    surv_regen = models.DecimalField(max_digits=10, decimal_places=2, db_column='SurvRegen')
    surv_armour = models.DecimalField(max_digits=10, decimal_places=2, db_column='SurvArmour')
    surv_spd = models.DecimalField(max_digits=10, decimal_places=2, db_column='SurvSpd')
    surv_mass = models.DecimalField(max_digits=10, decimal_places=2, db_column='SurvMass')

    #make sure Django uses survivor name in the database
    class Meta:
        db_table = 'survivor'

    def __str__(self):
        return self.surv_name
    
#==============================
# Items Model
#==============================
class Item(models.Model):
    # Make sure to check notes in doc/PostgreSQL_for_making_Tables.md

    class ActivationType(models.TextChoices):
        ACTIVE = 'Acive', 'Active'
        PASSIVE = 'Passive', 'Passive'

    class StackType(models.TextChoices):
        LINEAR = 'Linear', 'Linear'
        EXPONENTIAL = 'Exponential', 'Exponential'
        HYPERBOLIC = 'Hyperbolic', 'Hyperbolic'
        RECIPROCAL = 'Reciprocal', 'Reciprocal'
        SPECIAL = 'Special', 'Special'
        # Will add combination types later (Linear-Exponential, Exponential-Hyperbolic, etc)

    class ItemTier(models.TextChoices):
        # Active Items can ONLY use the ones specificed by comments and in the notes
        COMMON = 'Common', 'Common'
        UNCOMMON = 'Uncommon', 'Uncommon'
        LEGENDARY = 'Legendary', 'Legendary'
        BOSS = 'Boss', 'Boss'
        LUNAR = 'Lunar', 'Lunar' # For Active Items and Passive
        VOID = 'Void', 'Void'
        UNTIERED = 'Untiered', 'Untiered'
        EQUIPMENT = 'Equipment', 'Equipment' # For Actives Items ONLY
        ELITE = 'Elite', 'Elite' # For Active Items ONLY

    item_img = models.ImageField(upload_to='items/',db_column='ItemImg', blank=True, null=True)
    item_name = models.CharField(max_length=100, db_column='ItemName')
    item_desc = models.TextField(db_column='ItemDesc')
    item_stack = models.CharField(max_length=32, db_column='ItemStack', choices=StackType.choices, blank=True)
    item_tier = models.CharField(max_length=24, db_column='ItemTier', choices=ItemTier.choices, blank=True)
    item_act_pass = models.CharField(max_length=12, db_column='ItemActPass', choices=ActivationType.choices)

    class Meta:
        db_table = 'Items'
    
    def __str__(self):
        return self.item_name
    


#==============================
# Monster Model
#==============================
class Monster(models.Model):
    
    # Check notes for monster types if new ones added
    class MonsterClass(models.TextChoices):
        REGULAR = 'Regular', 'Regular'
        SPECIAL = 'Special', 'Special'
        BOSS = 'Boss', 'Boss'
        SPECIAL_BOSS = 'Special_Boss', 'Special_Boss'
        OTHER = 'Other', 'Other'

    mons_img = models.ImageField(upload_to='monsters/',db_column='MonsImg', blank=True, null=True)
    mons_name = models.CharField(max_length=100, db_column='MonsName')
    mons_hp = models.DecimalField(max_digits=10, decimal_places=2, db_column='MonsHP')
    mons_regen = models.DecimalField(max_digits=10, decimal_places=2, db_column='MonsRegen')
    mons_armour = models.DecimalField(max_digits=10, decimal_places=2, db_column='MonsArmour')
    mons_spd = models.DecimalField(max_digits=10, decimal_places=2, db_column='MonsSpd')
    mons_class = models.CharField(max_length=32, db_column='MonsClass', choices=MonsterClass.choices)
    mons_type = models.CharField(max_length=32, db_column='MonsType')

    class Meta:
        db_table = 'Monsters'

    def __str__(self):
        return self.mons_name