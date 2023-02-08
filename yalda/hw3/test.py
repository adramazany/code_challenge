import numpy as np

st="1,2,3"
ar= [float(v) for v in st.split(",")]
nar = np.array(ar)
print(nar)
N=10
vol = N/nar
print(vol)
Lx,Ly,Lz = np.cbrt(vol)
print(Lx,Ly,Lz)
