#!/usr/bin/env python

import yaml
import string
import sys

if __name__ == "__main__":

    print "--Gear List\n"

    with open("gear.yaml", 'r') as stream:
        gear = yaml.load(stream)

    categories = ['pack', 'shelter', 'sleep system', 'cooking', 'rain gear', 'clothes', 'electronics', 'miscellaneous', 'dog gear', 'food']

    all_gear = []
    base_gear = []
    nonbase_gear = []
    worn_gear = []

    for key in gear.keys():
        item = gear[key]
        if item['category'] not in categories:
            print "\n**** Error, bad category:", item['category']
            print "**** Valid categories:", categories, "\n"
            sys.exit(1)
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
        if num_worn > 0:
            worn_gear.append(key)
        if num_base + num_nonbase + num_worn > 0:
            all_gear.append(key)

    base_weight = 0.0
    for key in base_gear:
        base_weight += float(gear[key]['weight'])
    base_weight *= 0.00220462

    nonbase_weight = 0.0
    for key in nonbase_gear:
        nonbase_weight += float(gear[key]['weight'])
    nonbase_weight *= 0.00220462

    worn_weight = 0.0
    for key in worn_gear:
        worn_weight += float(gear[key]['weight'])
    worn_weight *= 0.00220462

    print "Categories", categories

    print "\nBase weight:", base_weight, "lb."
    print "Non-base weight:", nonbase_weight, "lb."
    print "Total pack weight:", base_weight + nonbase_weight, "lb."
    print "Worn weight:", worn_weight, "lb.\n"

    tex =  "\documentclass[letterpaper, 12pt]{article}\n"
    tex += "\usepackage{fullpage}\n"
    tex += "\\title{Backpacking Gear List}\n"
    tex += "\\author{}\n"
    tex += "\\begin{document}\n"
    tex += "\maketitle\n"
    tex += "\\thispagestyle{empty}\n"

    notes = []

    base_weight_string = "{0:0.1f}".format(base_weight)
    total_weight_string = "{0:0.1f}".format(base_weight + nonbase_weight)
    
    tex += "\n\centerline{Base weight: " + base_weight_string + " lb.}"
    #tex += "\n\centerline{Total weight: " + total_weight_string + "}"

    for category in categories:
        tex += "\n\\vspace{0.2in}{\large \\textbf{" + category + "}}\n"
        for key in gear.keys():
            item = gear[key]
            if item['category'] == category:
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
                    if 'note' in item.keys():
                        notes.append(item['note'])

    for note in notes:
        print note
        tex += "\n\\vspace{0.2in}" + note + "\n"
                
    tex += "\end{document}\n"

    tex_file = open("gear_list.tex", 'w')
    tex_file.write(tex)
    tex_file.close()
    print "LaTex written to gear_list.tex\n"

