#Grafica de un evento sismico

import matplotlib.pyplot as plt
import numpy as np
from obspy.clients.fdsn import Client
from obspy import UTCDateTime
from obspy.signal import freqattributes

#Datos de  IRIS

Network = "EC"  ; Station = "TULM" ; Location = '--'; Channel ="HHE"

t1 = UTCDateTime("2024-12-14T18:05:16.000")
client=Client("IRIS")
st = client.get_waveforms(Network,Station,Location,Channel,t1,t1+150)

#Traza
tr = st[0]; df=tr.stats.sampling_rate; dD=tr.stats.delta

#Filtrado

fMin=1.5 ; fMax=2.5
tr_filt = tr.copy()
tr_filt.filter('bandpass',freqmin=fMin,freqmax=fMax,corners=3,zerophase=True)
tr_spec = freqattributes.spectrum(tr_filt.data,df,18001)

#Grafico de los datos filtrados

t = np.arange(0,tr.stats.npts / tr.stats.sampling_rate , tr.stats.delta)
plt.subplot(211); plt.plot(t,tr.data,'k'); plt.ylabel("Datos en crudo")
plt.subplot(212);plt.plot(t, tr_filt.data,'k')
plt.ylabel('Datos filtrados');plt.xlabel("Segundos")

plt.show()