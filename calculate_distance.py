import json, sys, numpy, os
from geopy.distance import geodesic

def compare_position_result(json_p1, json_p2):
    json_1 = json.load(open(json_p1))
    json_2 = json.load(open(json_p2))

    latlon_1 = numpy.array(json_1['trajectory'])
    latlon_2 = numpy.array(json_2['trajectory'])
    
    limit = latlon_1.shape[1]
    if latlon_1.shape[1] > latlon_2.shape[1]:
        limit = latlon_2.shape[1]
    result = [None] * limit
    for i in range(limit):
        tmp_1 = (latlon_1[0][i], latlon_1[1][i])
        tmp_2 = (latlon_2[0][i], latlon_2[1][i])
        dist = geodesic(tmp_1, tmp_2).m
        result[i] = dist
    
    print(numpy.mean(result))
    data_json = {}
    data_json['Moyenne'] = numpy.mean(result)
    data_json['Distances'] = result
    return data_json


def dump_to_json(filename, json_d):
        with open(filename, 'w') as f:
                json.dump(json_d, f, ensure_ascii=False, indent=1)

if __name__ == "__main__":
    json_d = compare_position_result(sys.argv[1], sys.argv[2])
    path = os.path.join(os.getcwd(), "distance_result.json")
    dump_to_json(path, json_d)