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

    tex =  "\documentclass[letterpaper, 12pt]{article}\n"
    tex += "\usepackage{fullpage}\n"
    tex += "\\title{Backpacking Gear List}\n"
    tex += "\\author{}\n"
    tex += "\date{}\n"
    tex += "\\begin{document}\n"
    tex += "\maketitle\n"
    tex += "\\thispagestyle{empty}\n"

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
        num_total = num_base + num_nonbase + num_worn
        if num_total > 0:
            entry = "\n" + item['type'] + ": " + key
            if num_total > 1:
                entry += " (x" + str(num_total) + ")"
            entry += "\n"
            tex += entry

    tex += "\end{document}\n"

    tex_file = open("gear_list.tex", 'w')
    tex_file.write(tex)
    tex_file.close()
    print "LaTex written to gear_list.tex\n"
