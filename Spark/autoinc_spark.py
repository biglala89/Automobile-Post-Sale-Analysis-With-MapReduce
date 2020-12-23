from pyspark import SparkContext
import os


def load_data():
    sc = SparkContext()
    data = sc.textFile('../source_data/data.csv')
    return data


def map_vin_pair():
    """
    Map raw daa to (vin, make, year) tuples.
    """
    raw_rdd = load_data()
    raw_rdd = raw_rdd.map(lambda x: x.split(','))
    vin_kv = raw_rdd.map(lambda x: (x[1], [x[0], x[2], x[4]]))
    return vin_kv


def cache_rdd(vin_kv):
    """
    Cache read dataset for faster future readings.
    """
    vin_kv.cache()


def extract_group_master_info(vin_kv):
    """
    Extract make, year information from initial sale record per vin group.
    """
    group_lvl_info = {}
    for kv in vin_kv.collect():
        if kv[1][0] == 'I':
            group_lvl_info[kv[0]] = kv[1][1:]
    return group_lvl_info


def populate_make(group, group_lvl_info):
    """
    Propagate group info to records with missing make and year 
    and create new tuples.
    """
    new_group = []
    vin = group[0]
    make_year_pair = list(group[1])
    for make_year in make_year_pair:
        make_year[1], make_year[2] = group_lvl_info[vin][0], group_lvl_info[vin][1]
        new_group.append((vin, (make_year[0], make_year[1], make_year[2])))
    return new_group


def populate_make_year(group_lvl_info, vin_kv):
    """
    Populate records for each vin group.
    """
    enhance_make = vin_kv.groupByKey().flatMap(
        lambda x: populate_make(x, group_lvl_info))
    return enhance_make


def extract_make_key_value(pair):
    return ('-'.join(pair[1][1:]), 1)


def count_incidents(enhance_make):
    """
    Count the number of incidents per make and year combination.
    """
    make_kv = enhance_make.map(
        lambda x: extract_make_key_value(x))
    incident_rdd = make_kv.reduceByKey(lambda a, b: a + b).sortByKey()
    incident_count = incident_rdd.collect()
    print(incident_count)
    return incident_count


def save_output(incident_count):
    with open('reports.txt', 'w') as f:
        for item in incident_count:
            f.write("{},{}\n".format(item[0], str(item[1])))


def main():
    vin_kv = map_vin_pair()
    cache_rdd(vin_kv)
    group_lvl_info = extract_group_master_info(vin_kv)
    enhance_make = populate_make_year(group_lvl_info, vin_kv)
    incident_count = count_incidents(enhance_make)
    save_output(incident_count)


if __name__ == '__main__':
    main()
