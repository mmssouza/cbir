
@set curv_fname="curvatura_sig.pkl"
@set cd_fname="cd_sig.pkl"
@set angle_fname="angle_sig.pkl"
gera_curvatura_sig.py %1 20 155 -16000 16000 %curv_fname%
gera_cd_sig.py %1 10 0 1 100 %cd_fname%
gera_angle_sig.py %1 25 10 0.1 3.141592 145 %angle_fname%

rank40.py %curv_fname% %cd_fname% %angle_fname%
rank.py  %curv_fname% %cd_fname% %angle_fname% 
