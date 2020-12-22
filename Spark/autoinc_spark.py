from pyspark import SparkContext
import os

sc = SparkContext()

# Read the input data CSV file
raw_rdd = sc.textFile(
    '/Users/chowli/Documents/Springboard_DE/Projects/mini-projects/Post_Sale_Automobile_Report/source_data/data.csv')
raw_rdd = raw_rdd.map(lambda x: x.split(','))

vin_kv = raw_rdd.map(lambda x: (x[1], [x[0], x[2], x[4]]))
vin_kv.cache()

group_lvl_info = {}
for kv in vin_kv.collect():
    if kv[1][0] == 'I':
        group_lvl_info[kv[0]] = kv[1][1:]


def populate_make(group, group_lvl_info):
    new_group = []
    vin = group[0]
    make_year_pair = list(group[1])
    for make_year in make_year_pair:
        make_year[1], make_year[2] = group_lvl_info[vin][0], group_lvl_info[vin][1]
        new_group.append((vin, (make_year[0], make_year[1], make_year[2])))
    return new_group


enhance_make = vin_kv.groupByKey().flatMap(
    lambda x: populate_make(x, group_lvl_info))


def extract_make_key_value(pair):
    return ('-'.join(pair[1][1:]), 1)


make_kv = enhance_make.map(lambda x: extract_make_key_value(x))
incident_rdd = make_kv.reduceByKey(lambda a, b: a + b).sortByKey()
incident_count = incident_rdd.collect()
print(incident_count)

with open('reports.txt', 'w') as f:
    for item in incident_count:
        f.write("{},{}\n".format(item[0], str(item[1])))
