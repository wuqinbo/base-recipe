# -*- coding:utf8 -*-

from .exts import db


class UserList(db.Document):
    username = db.StringField()
    password = db.StringField()

# 菜谱数据模型layer01
class NutritionHealthLayer01(db.Document):
    recipeId = db.IntField()
    name = db.StringField()
    health_light = db.IntField()
    weight = db.IntField()
    thumb_image_url = db.StringField()
    code = db.StringField()
    calory = db.StringField()
    calory_unit = db.IntField()
    caloryInt = db.IntField()
    unit_id = db.IntField()
    is_liquid = db.BooleanField()
    recipeType = db.StringField()
    materials = db.DictField()
    large_image_url = db.StringField()
    uploader = db.StringField()
    appraise = db.StringField()
    protein = db.StringField()
    fat = db.StringField()
    fiber_dietary = db.StringField()
    carbohydrate = db.StringField()
    gi = db.StringField()
    gl = db.StringField()
    compare = db.DictField()
    recipe = db.BooleanField()
    units = db.ListField()
    ingredient = db.DictField()
    lights = db.DictField()
    comments_ct = db.IntField()
    health_appraise = db.ListField()
    stepsStrLen = db.IntField()
    seasoningCount = db.IntField()
    minor_materialsCount = db.IntField()
    major_materialsCount = db.IntField()
    carbsRatio = db.FloatField()
    fatRatio = db.FloatField()
    proteinRatio = db.FloatField()
    is_soup = db.BooleanField()
    recipeTotalWeight = db.FloatField()  # 食材总重量
    oilWeight = db.FloatField()  # oil重量
    sugarWeight = db.FloatField()  # 糖重量
    oilRatio = db.FloatField()
    sugarRatio = db.FloatField()
    materialsType = db.IntField()  # 0 荤菜 1 素菜 2 大荤 3 小荤
    materialsTypeName = db.StringField()  # 0 荤菜 1 素菜 2 大荤 3 小荤
    isHot = db.BooleanField()
    isSweet = db.BooleanField()
    isSour = db.BooleanField()
    tasteLabel = db.StringField()
    ingredientList = db.ListField()
    ingredientStr = db.StringField()
    recipesKinds = db.ListField()  # 菜谱主食材分类--叶菜类，根茎类，菌菇类，豆制品，鸡蛋

    hotRatio = db.FloatField()  # 辣
    sweetRatio = db.FloatField()  # 甜
    fragranceRatio = db.FloatField()  # 香
    freshRatio = db.FloatField()  # 鲜
    lightRatio = db.FloatField()  # 淡
    sourRatio = db.FloatField()  # 酸
    bitterRatio = db.FloatField()  # 苦
    greasyRatio = db.FloatField()  # 腻
    saltyRatio = db.FloatField()
    fishyRatio = db.FloatField()
    numbRatio = db.FloatField()
    curryRatio = db.FloatField()
    mustardRatio = db.FloatField()
    cookingMethod = db.StringField()
    cookingMethodIndex = db.IntField()
    cookingMethodList = db.ListField()
    hasCookingStep = db.BooleanField()

    def setAttrs(self, entries):
        for k, v in entries.items():
            if k == 'id':
                setattr(self, 'unit_id', v)
            elif k == 'recipe_type':
                setattr(self, 'recipeType', v)
            else:
                setattr(self, k, v)
