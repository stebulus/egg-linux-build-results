import os
import os.path
import sys

def first_line(path):
  with open(path) as f:
    return f.readline().rstrip()

def contents(path):
  for f in os.listdir(path):
    if not f.startswith('.'):
      yield f

def as_dict(path):
  result = {}
  for f in contents(path):
    ff = os.path.join(path, f)
    if os.path.isdir(ff):
      result[f] = as_dict(ff)
    else:
      result[f] = first_line(ff)
  return result

def read_reports(root):
  reports = []
  for d in contents(root):
    dd = os.path.join(root, d)
    if os.path.isdir(dd):
      reports.append(as_dict(dd))
  return reports

if __name__ == '__main__':
  reports = read_reports(sys.argv[1])
  for r in reports:
    if r["result-checksum"] == "fb074dbb34a531f1e6cf9d14e4edc6e970bfe04b19e92bd9ce0c6740a95cc667":
      print r["date"], r["build-machine"]["lsb-release"]
