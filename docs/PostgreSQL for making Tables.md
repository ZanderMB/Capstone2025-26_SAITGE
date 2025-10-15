-- General Notes
-- For the **Img columns, make sure to put in the link/path to the image when inserting data otherwise you break shit

-- Survivor Notes
-- 

```sql
CREATE TABLE Survivor (
    SurvID SERIAL PRIMARY KEY,
    SurvImg TEXT,
    SurvName VARCHAR(100) NOTNULL,
    SurvDesc TEXT NOTNULL,
    SurvHP DECIMAL NOTNULL,
    SurvDMG DECIMAL NOTNULL,
    SurvRegen DECIMAL NOTNULL,
    SurvArmour DECIMAL NOTNULL,
    SurvSpd DECIMAL NOTNULL,
    SurvMass DECIMAL NOTNULL,
)
```

--Items Notes
-- ActPass = Active or Passive those are the ONLY two values that should be in that.
-- Item Stack can be one of a few things, Linear, Exponential, Hyperbolic, Reciprocal, Special, or a combination of two types.
-- Item Tier is what you think it is, Common, Uncommon, Legendary, Boss, Lunar, Void, or Untiered. BUT active items can only be one of three, Equipment, Lunar, or Elite.

```sql
CREATE TABLE Items (
    ItemID SERIAL PRIMARY KEY,
    ItemImg TEXT,
    ItemName VARCHAR(100) NOTNULL,
    ItemDesc TEXT NOTNULL,
    ItemStack VARCHAR(32)
    ItemTier VARCHAR(24)
    ItemActPass VARCHAR(12) NOTNULL,
)
```
-- Monsters Notes
-- Classes are; Regular, Special, Boss, Special Boss, or Other (Only 6 type of Other and they are all Ally types)

```sql
CREATE TABLE Monsters (
    MonsID SERIAL PRIMARY KEY,
    MonsImg TEXT,
    MonsName VARCHAR(100) NOTNULL,
    MonsHP DECIMAL NOTNULL,
    MonsRegen DECIMAL NOTNULL,
    MonsArmour DECIMAL NOTNULL,
    MonsSpd DECIMAL NOTNULL,
    MonsClass VARCHAR(32) NOTNULL,
    MonsType VARCHAR(32) NOTNULL,
)
```


-- Python-SQLALCHEMY VERSION BELOW
-- When using SQLALCHEMY make sure to import properstuff
```python
import sqlalchemy
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Text,
    Numeric
)
from sqlalchemy.orm import declarative_base

# delcaritive_base returns a new base class
# all mapped classes should include it
Base = declaritive_base()
```


-- Survivors

```python
class Survivor(base):
    __tablename__ = 'survivor'
    
    # Indicating an Interger column as PRIMARY_KEY does the same thing as SERIAL in SQL
    surv_id = Column('SurvID', Integer, primary_key=True)

    surv_img = Column('SurvImg', Text)
    surv_name = Column('SurvName', String(100), nullable=False)
    surv_desc = Column('SurvDesc', Text, nullable=False)

    # For DECIMAL columns, SQLAlchemy's Numeric type is the same thing
    surv_hp = Column('SurvHP', Numeric, nullable=False)
    surv_dmg = Column('SurvDMG', Numeric, nullable=False)
    surv_regen = Column('SurvRegen', Numeric, nullable=False)
    surv_armour = Column('SurvArmour', Numeric, nullable=False)
    surv_spd = Column('SurvSpd', Numeric, nullable=False)
    surv_mass = Column('SurvMass', Numeric, nullable=False)

    def __repr__(self):
        return f"<Survivor(name='{self.surv_name}')>"

if __name__ == '__main__':
    # Replace with your actual database connection string
    # The example uses an in-memory SQLite database for demonstration.
    engine = create_engine('sqlite:///:memory:')

    # This issues the CREATE TABLE statement to the database
    # for all tables that inherit from Base.
    print("Creating table...")
    Base.metadata.create_all(engine)
    print("Table 'survivor' created successfully.")
```

-- Items
```python

```

-- Monsters
```python

```