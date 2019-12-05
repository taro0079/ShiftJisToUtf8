## フォルダ内のdatファイルの文字コードをshift_jisからutf-8に変換する

import codecs
import sys
import os
import glob


def main():
#    args = sys.argv
#    filename = args[1]
    path = "*.dat" # datファイル全て
    filename2 = "test" # 仮のファイル名
    flist = glob.glob(path) 
    print(flist)

    for file in flist:
        fin = codecs.open(file, "r", "shift_jis")
        fout = codecs.open(filename2, "w", "utf-8")
        for row in fin:
            fout.write(row)
        fin.close()
        fout.close()
        os.rename(filename2, file)
#    fin = codecs.open(filename, "r", "shift_jis")
#    fout = codecs.open(filename2, "w", "utf-8")
#    for row in fin:
#        fout.write(row)
#    fin.close
#    fout.close
#    os.rename(filename2, filename)

if __name__=='__main__':
    main()
