"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter(Model.name=='Corvette', Model.brand_name=='Chevrolet').all()
# Get all models that are older than 1960.
Model.query.filter(Model.year > 1960).all()
# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()
# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()
# Get all brands that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()
# Get all brands that are either 1) discontinued (at any time) or 2) founded 
# before 1950.
Brand.query.filter((Brand.discontinued != None) | (Brand.founded < 1950)).all()
# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != 'Chevrolet').all()
# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models_for_year = Model.query.filter(Model.year == year).all()

    for model in models_for_year:
        print "name: %s, brand_name: %s, headquarters: %s \n" % (model.name, model.brand_name, model.brands.headquarters)

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    #[<brand id=1...>, <brand id=2...>]
    all_brands = Brand.query.options(db.joinedload('models')).all()

    for brand in all_brands:
        if brand.models is not None:
            print "brand name: %s, model name: %s" % (brand.name, brand.models.name)
        else:
            pass

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
# object

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
#a table that links two other tables and has no meaningful fields. Manages many to
#many relationships

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    brands_list = Brand.query.filter((Brand.name == mystr) | (Brand.name.like('%' + mystr + '%'))).all()
    return brands_list


def get_models_between(start_year, end_year):
    models_list = Model.query.filter( (Model.year >= start_year) & (Model.year < end_year) ).all()
    return models_list
