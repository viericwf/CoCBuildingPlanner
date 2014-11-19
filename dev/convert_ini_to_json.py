import os, json, re

## display time (3d, 5h) in minutes
def convert_to_hr(time_str):
    import re
    t, measure = re.findall(r'^([0-9\.]+)([a-z])$', time_str)[0]
    if measure == 'd': return float(t) * 24 * 60
    elif measure == 'h': return float(t) * 60
    elif measure == 'm': return float(t)

def name_decorator(name):
    return name.replace('_', ' ').title()

def convert_ini_to_json(input_folder, output):

    ## check output folder
    if not os.path.exists(os.path.dirname(output)):
        os.makedirs(os.path.dirname(output))

    ini_files = filter(lambda x:x.endswith('.ini'), os.listdir(input_folder))

    buildings = {}
    for ini_file in ini_files:

        print 'process', ini_file

        # read .ini file
        doc = open(os.path.join(input_folder, ini_file)).read()
        # filter out data
        data = [line for line in  doc.strip().split('\n') if not line.startswith('#') and len(line.strip())]

        name = name_decorator(ini_file.split('.ini')[0])
        properties = [ { x:y for (x,y) in entry } for entry in [re.findall(r'([a-z]+)=([a-z0-9\._]+);', line) for line in data]]
        
        buildings[name] = properties

    
    for building, properties in buildings.items():
        for entry in properties:
            entry['cost'] = int(entry['cost'])
            entry['name'] = name
            entry['lv'] = int(entry['lv'])
            entry['time_str'] = entry['time']
            entry['time'] = convert_to_hr( entry['time_str'] )

    json.dump(buildings, open(output, 'w'))

if __name__ == '__main__':

    convert_ini_to_json(input_folder='../ini/', output='../static/data/buildings.json')