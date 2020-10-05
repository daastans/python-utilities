import csv
import pandas

""" Reads the file from path and removes duplicated rows"""
def main():
  path="path/to/file.csv"
  df=pandas.read_csv(path,error_bad_lines=False)

  dup=df.duplicated(subset=['OriginalVerse'],keep='first')
  df[[not i for i in dup]].to_csv(path,quoting=csv.QUOTE_ALL,index=False)

if __name__=='__main__':
    main()
