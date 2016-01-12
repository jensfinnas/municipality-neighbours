# encoding: utf-8
import csvkit as csv

class RegionList(object):
    def __init__(self, in_file, key):
        self.key = key
        self.data = self._open_data(in_file)

    def _open_data(self, in_file):
        _regions = {}
        with open(in_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                _regions[row[self.key]] = row
            
            return _regions

    def _translate_neighbour(self, field="all"):
        _data = []
        for name_short, row in self.data.iteritems():
            row = dict(row)
            neighbours = row["neighbours"].split(",")
            if field == "all":
                row["neighbours"] = [self.data[x] for x in neighbours if x != ""]
            else:
                neighbours = [self.data[x][field] for x in neighbours if x != ""]
                row["neighbours"] = ",".join(neighbours)

            _data.append(row)

        return _data

    def _transpose(self, data, fields):
        _data = []
        for row in data:
            _row = {}
            for neighbour in row["neighbours"]:
                for field in fields:
                    _row["a_%s" %field ] = row[field]
                    _row["b_%s" %field ] = neighbour[field]
                _data.append(_row)


        return _data

    def write_csv(self, data, out_file):
        with open(out_file, 'w') as csvfile:
            print "Write to %s" % out_file
            fieldnames = data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)

    def as_csv(self, out_file, field):
        data = self._translate_neighbour(field=field)
        self.write_csv(data, out_file)

    def as_transposed_csv(self, out_file, fields):
        data = self._transpose(self._translate_neighbour(), fields)
        self.write_csv(data, out_file)
