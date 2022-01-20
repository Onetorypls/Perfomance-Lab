import json
def recording(id1, values):
    for value in values.keys():
        for i in range(len(values[value])):
            if values[value][i]['id'] == id1:
                return values[value][i]['value']

tests = json.load(open(input()))
values = json.load(open(input()))
report = tests.copy()

for test in tests.keys():
    for i in range(len(tests[test])):
        if 'values' not in tests[test][i].keys():
            id1 = tests[test][i]['id']
            report[test][i]['value'] = recording(id1, values)
        if 'values' in tests[test][i].keys():
            id1 = tests[test][i]['id']
            report[test][i]['value'] = recording(id1, values)
            for j in range(len(tests[test][i]['values'])):
                if 'values' not in tests[test][i]['values'][j].keys():
                    id1 = tests[test][i]['values'][j]['id']
                    report[test][i]['values'][j]['value'] = recording(id1, values)
                if 'values' in tests[test][i]['values'][j].keys():
                    id1 = tests[test][i]['values'][j]['id']
                    report[test][i]['values'][j]['value'] = recording(id1, values)
                    for k in range(len(tests[test][i]['values'][j]['values'])):
                        if 'values' not in tests[test][i]['values'][j]['values'][k].keys():
                            id1 = tests[test][i]['values'][j]['values'][k]['id']
                            report[test][i]['values'][j]['values'][k]['value'] = recording(id1, values)
                        if 'values' in tests[test][i]['values'][j]['values'][k].keys():
                            id1 = tests[test][i]['values'][j]['values'][k]['id']
                            report[test][i]['values'][j]['values'][k]['value'] = recording(id1, values)
                            for l in range(len(tests[test][i]['values'][j]['values'][k]['values'])):
                                id1 = tests[test][i]['values'][j]['values'][k]['values'][l]['id']
                                report[test][i]['values'][j]['values'][k]['values'][l]['value'] = recording(id1, values)

with open(input(), 'w') as f:
    json.dump(report, f)