# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class PlayerInfo(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    player = models.TextField(db_column='Player', blank=True, null=True)  # Field name made lowercase.
    pos = models.TextField(db_column='Pos', blank=True, null=True)  # Field name made lowercase.
    ht = models.TextField(db_column='Ht', blank=True, null=True)  # Field name made lowercase.
    wt = models.TextField(db_column='Wt', blank=True, null=True)  # Field name made lowercase.
    birth_date = models.DateTimeField(db_column='Birth Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase.
    exp = models.TextField(db_column='Exp', blank=True, null=True)  # Field name made lowercase.
    college = models.TextField(db_column='College', blank=True, null=True)  # Field name made lowercase.
    url = models.TextField(db_column='URL', blank=True, null=True)  # Field name made lowercase.
    year = models.BigIntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Player Info'


class SummaryStats(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    player = models.TextField(db_column='Player', blank=True, null=True)  # Field name made lowercase.
    tm = models.TextField(db_column='Tm', blank=True, null=True)  # Field name made lowercase.
    g = models.TextField(db_column='G', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    gs = models.TextField(db_column='GS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mp = models.TextField(db_column='MP', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fg = models.TextField(db_column='FG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fga = models.TextField(db_column='FGA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fg_field = models.TextField(db_column='FG%', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    number_3p = models.TextField(db_column='3P', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    number_3pa = models.TextField(db_column='3PA', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    number_3p_field = models.TextField(db_column='3P%', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    number_2p = models.TextField(db_column='2P', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    number_2pa = models.TextField(db_column='2PA', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    number_2p_field = models.TextField(db_column='2P%', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    efg_field = models.TextField(db_column='eFG%', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    ft = models.TextField(db_column='FT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fta = models.TextField(db_column='FTA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ft_field = models.TextField(db_column='FT%', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    orb = models.TextField(db_column='ORB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    drb = models.TextField(db_column='DRB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    trb = models.TextField(db_column='TRB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ast = models.TextField(db_column='AST', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    stl = models.TextField(db_column='STL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    blk = models.TextField(db_column='BLK', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tov = models.TextField(db_column='TOV', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pf = models.TextField(db_column='PF', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pts = models.TextField(db_column='PTS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    year = models.BigIntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Summary Stats'
