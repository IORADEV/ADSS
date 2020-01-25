# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class AeZoneType4326(models.Model):
    gid = models.AutoField(primary_key=True)
    objectid = models.IntegerField(blank=True, null=True)
    aezonecode = models.SmallIntegerField(blank=True, null=True)
    area_ha = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ae_zones = models.CharField(max_length=25, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ae_zone_type_4326'


class BasinThiruv02012020(models.Model):
    gid = models.AutoField(primary_key=True)
    id = models.BigIntegerField(blank=True, null=True)
    gridcode = models.BigIntegerField(blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'basin_thiruv_02_01_2020'


class KeralaState(models.Model):
    gid = models.AutoField(primary_key=True)
    st_nm = models.CharField(max_length=24, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kerala_state'


class SoilTexture21012020(models.Model):
    gid = models.AutoField(primary_key=True)
    objectid_1 = models.BigIntegerField(blank=True, null=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    depth_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    drainage_i = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    texture_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    slope_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    erosion_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    flooding_i = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    taxonomy_i = models.CharField(max_length=50, blank=True, null=True)
    particlesi = models.BigIntegerField(blank=True, null=True)
    soiltemp_i = models.BigIntegerField(blank=True, null=True)
    pmat = models.BigIntegerField(blank=True, null=True)
    surfacefor = models.BigIntegerField(blank=True, null=True)
    stoniness_field = models.BigIntegerField(db_column='stoniness_', blank=True, null=True)  # Field renamed because it ended with '_'.
    oc = models.BigIntegerField(blank=True, null=True)
    cec = models.BigIntegerField(blank=True, null=True)
    ph_id = models.BigIntegerField(blank=True, null=True)
    calcareous = models.BigIntegerField(blank=True, null=True)
    salinity_i = models.BigIntegerField(blank=True, null=True)
    sodicity = models.BigIntegerField(blank=True, null=True)
    minerology = models.BigIntegerField(blank=True, null=True)
    shape_leng = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    soil_id = models.BigIntegerField(blank=True, null=True)
    shape_le_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    text = models.CharField(max_length=50, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'soil_texture_21_01_2020'


class ThiruvSacredgroves16012020(models.Model):
    gid = models.AutoField(primary_key=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    x = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    y = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    name_of_ka = models.CharField(max_length=254, blank=True, null=True)
    village = models.CharField(max_length=254, blank=True, null=True)
    location = models.CharField(max_length=254, blank=True, null=True)
    kavu_no_field = models.CharField(db_column='kavu_no_', max_length=254, blank=True, null=True)  # Field renamed because it ended with '_'.
    f7 = models.CharField(max_length=254, blank=True, null=True)
    f8 = models.CharField(max_length=254, blank=True, null=True)
    f9 = models.CharField(max_length=254, blank=True, null=True)
    f10 = models.CharField(max_length=254, blank=True, null=True)
    f11 = models.CharField(max_length=254, blank=True, null=True)
    f12 = models.CharField(max_length=254, blank=True, null=True)
    f13 = models.CharField(max_length=254, blank=True, null=True)
    f14 = models.CharField(max_length=254, blank=True, null=True)
    f15 = models.CharField(max_length=254, blank=True, null=True)
    f16 = models.CharField(max_length=254, blank=True, null=True)
    f17 = models.CharField(max_length=254, blank=True, null=True)
    f18 = models.CharField(max_length=254, blank=True, null=True)
    f19 = models.CharField(max_length=254, blank=True, null=True)
    f20 = models.CharField(max_length=254, blank=True, null=True)
    f21 = models.CharField(max_length=254, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'thiruv_sacredgroves_16_01_2020'


class TvmDivision(models.Model):
    gid = models.AutoField(primary_key=True)
    area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    perimeter = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    division_field = models.IntegerField(db_column='division_', blank=True, null=True)  # Field renamed because it ended with '_'.
    division_i = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    office_cod = models.CharField(max_length=7, blank=True, null=True)
    area_1 = models.FloatField(blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tvm_division'


class TvmDrainage4326(models.Model):
    gid = models.AutoField(primary_key=True)
    arcid = models.IntegerField(blank=True, null=True)
    grid_code = models.IntegerField(blank=True, null=True)
    from_node = models.IntegerField(blank=True, null=True)
    to_node = models.IntegerField(blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tvm_drainage_4326'


class TvmRange4326(models.Model):
    gid = models.AutoField(primary_key=True)
    area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    perimeter = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    range_field = models.IntegerField(db_column='range_', blank=True, null=True)  # Field renamed because it ended with '_'.
    range_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    range_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    beat_nos = models.IntegerField(blank=True, null=True)
    section_no = models.IntegerField(blank=True, null=True)
    district = models.CharField(max_length=30, blank=True, null=True)
    hq = models.CharField(max_length=20, blank=True, null=True)
    remarks = models.CharField(max_length=50, blank=True, null=True)
    office_cod = models.CharField(max_length=7, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tvm_range_4326'


class TvmSection4326(models.Model):
    gid = models.AutoField(primary_key=True)
    area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    perimeter = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sectionp_field = models.DecimalField(db_column='sectionp_', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it ended with '_'.
    sectionp_i = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    hq_name = models.CharField(max_length=20, blank=True, null=True)
    beats = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    buildings = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    enclosures = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    plantation = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    settlement = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    estates = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    leases = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    remarks = models.CharField(max_length=80, blank=True, null=True)
    office_cod = models.CharField(max_length=7, blank=True, null=True)
    name_small = models.CharField(max_length=50, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tvm_section_4326'


class TvmSoil4326(models.Model):
    gid = models.AutoField(primary_key=True)
    objectid_1 = models.BigIntegerField(blank=True, null=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    depth_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    drainage_i = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    texture_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    slope_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    erosion_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    flooding_i = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    taxonomy_i = models.CharField(max_length=50, blank=True, null=True)
    particlesi = models.BigIntegerField(blank=True, null=True)
    soiltemp_i = models.BigIntegerField(blank=True, null=True)
    pmat = models.BigIntegerField(blank=True, null=True)
    surfacefor = models.BigIntegerField(blank=True, null=True)
    stoniness_field = models.BigIntegerField(db_column='stoniness_', blank=True, null=True)  # Field renamed because it ended with '_'.
    oc = models.BigIntegerField(blank=True, null=True)
    cec = models.BigIntegerField(blank=True, null=True)
    ph_id = models.BigIntegerField(blank=True, null=True)
    calcareous = models.BigIntegerField(blank=True, null=True)
    salinity_i = models.BigIntegerField(blank=True, null=True)
    sodicity = models.BigIntegerField(blank=True, null=True)
    minerology = models.BigIntegerField(blank=True, null=True)
    shape_leng = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    soil_id = models.BigIntegerField(blank=True, null=True)
    shape_le_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tvm_soil_4326'


class TvmWatershed4326(models.Model):
    gid = models.AutoField(primary_key=True)
    id = models.BigIntegerField(blank=True, null=True)
    gridcode = models.BigIntegerField(blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tvm_watershed_4326'
