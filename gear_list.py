#!/usr/bin/env python

import yaml
import string

if __name__ == "__main__":

    print "--Gear List\n"

    with open("gear.yaml", 'r') as stream:
        gear = yaml.load(stream)

    base_gear = []
    nonbase_gear = []
    worn_gear = []

    for key in gear.keys():
        item = gear[key]
        num_base = 0
        if 'base' in item.keys():
            num_base = int(item['base'])
        num_nonbase = 0
        if 'nonbase' in item.keys():
            num_nonbase = int(item['nonbase'])
        num_worn = 0
        if 'num_worn' in item.keys():
            num_worn = int(item['worn'])
        if num_base > 0:
            base_gear.append(key)
        if num_nonbase > 0:
            nonbase_gear.append(key)
        if num_worn:
            worn_gear.appen(key)

    base_weight = 0.0
    for key in base_gear:
        print gear[key]['type'] + ": " + key
        base_weight += float(gear[key]['weight'])

    base_weight *= 0.00220462

    print "\nBase weight:", base_weight, "lb.\n"
