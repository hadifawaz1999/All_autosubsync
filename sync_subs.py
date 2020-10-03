import autosubsync as ass
import os

vids_path = '/media/hadi/torrents/saved/Two and a half men/Two and a Half Men Season 3 720p MaRS/'
subs_path = '/media/hadi/torrents/subs/twoandahalfmen_s03/'
outs_path = '/media/hadi/torrents/saved/Two and a half men/Two and a Half Men Season 3 720p MaRS/'

for rootv, dirsv, vids in os.walk(vids_path):
    vids.sort()

    for roots, dirss, subs in os.walk(subs_path):
        subs.sort()
        for i in range(len(vids)):
            vid_path = vids_path+vids[i]
            sub_path=subs_path+subs[i]
            out_path=outs_path+vids[i][:-3]+'srt'
            print(vid_path,sub_path,out_path,sep='\n')
            ass.synchronize(vid_path,sub_path,out_path,verbose=True)